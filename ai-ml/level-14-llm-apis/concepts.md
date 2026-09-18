# Level 14 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept explains:
What it is · Why it exists · Where it's used · What goes wrong without
it · worked example · code · expected output.

**How this level works:** levels 11-13 *simulated* LLMs. Here you
call a real one through ONE shared function in `llm.py`:

```python
from llm import chat
chat(prompt, system="", temperature=0.0) → str
```

One env var picks the backend: `LLM_BACKEND=simulated` (default,
offline), `ollama` (local model), or `openai` (needs an API key).
Your code NEVER changes — the backend is configuration, not code.

**Vocabulary:**
- **API** (Application Programming Interface) — a function/service
  you call over the network instead of running locally.
- **Token** — the billing/processing unit of LLMs: roughly
  4 characters of English ≈ 1 token.

---

## Easy

### 1. The chat() Abstraction — `p01`

**What it is:** One function — `chat(prompt) → str` — that hides
WHICH LLM is behind it. Simulated mock, local Ollama, or OpenAI:
the caller sees identical behavior. Inside, `chat()` reads the
`LLM_BACKEND` env var and routes to the right HTTP call.

**Why it exists:** Every vendor's SDK call looks different, and code
that calls a paid API can't be unit-tested offline. A single wrapper
function was invented to create a seam: swap backends via config,
develop against the free mock, and bolt on retries, logging, and
cost tracking (hard/p03) in exactly one place.

**Where it's used:** Every production LLM app — chatbots, extraction
pipelines, agent loops — wraps the API behind an internal function
or client object. It's the reason "switch from OpenAI to a local
model" is a config change instead of a rewrite.

**What goes wrong without it:**
- Sprinkling `openai.chat.completions.create()` across 20 files =
  vendor lock-in: one breaking SDK change means 20 edits, and every
  test needs a live API key and a network call.
- No mock backend → you can't develop offline, can't run CI without
  a key, and every test run costs real money.
- The `sys.path.insert` dance at the top of each problem file isn't
  boilerplate to ignore — delete it and `from llm import chat` can't
  find `level-14-llm-apis/llm.py` from inside the subfolders.

**Worked example:**
```python
from llm import chat

reply = chat("What is 2+2?")
# simulated backend → "[simulated-llm] Response to: What is 2+2?"
# openai backend    → "2 + 2 equals 4."
# your code: IDENTICAL either way
```

**Code:**
```python
def ask_llm(question):
    return chat(question)      # one line — the abstraction does the work
```

**Expected output:**
```python
ask_llm("What is 2+2?")
# simulated backend → "[simulated-llm] Response to: What is 2+2?"
# openai backend    → "2 + 2 equals 4."
```

---

### 2. System Prompts via API — `p02`

**What it is:** In a real API call, the message list has roles:
`{"role": "system", ...}` sets behavior/persona once, then
`{"role": "user", ...}` is the actual question. Our `chat()` takes
it as `system=` and builds that message list for you.

**Why it exists:** Chatbots need persistent behavior — a persona,
guard rails, output rules — that applies to EVERY reply without
repeating it in every user message. The system role was invented as
that channel: a separate, higher-priority instruction the model is
trained to follow even when a user message conflicts.

**Where it's used:** Every chatbot persona, every guard rail
("never give medical advice"), every output rule ("always answer in
JSON"). This is the cheapest "fine-tuning" that exists — sent once,
affects every reply.

**What goes wrong without it:**
- Without a system role you'd paste behavior instructions into every
  user message — wasting tokens on every call AND letting users
  override your rules (the whole point is that the system role
  outranks them).
- Treating the system prompt as "just the first user message" —
  it's a separate role with higher priority, not a suggestion the
  user can argue with.
- (Level-11 hard/p03 covered the persona idea; here you use the real
  API parameter.)

**Worked example:**
```python
chat("Explain recursion",
     system="You explain things to a 5-year-old")
# → "...like a box with a smaller box inside..."

chat("Explain recursion",
     system="You are a senior systems engineer")
# → "...a function invoking itself with a reduced input,
#    bounded by a base case to prevent stack overflow..."
```
Same question. The system prompt alone changes vocabulary, depth,
and tone.

**Code:**
```python
def ask_with_persona(question, persona):
    return chat(question, system=persona)
```

**Expected output:**
```python
ask_with_persona("Explain recursion",
                 "You explain things to a 5-year-old")
# → a simple, child-friendly explanation string
ask_with_persona("Explain recursion",
                 "You are a senior systems engineer")
# → a technical explanation (base case, stack, reduced input)
```

---

### 3. Temperature in API Calls — `p03`

**What it is:** The same randomness dial from level-11, now a real
API parameter. `temperature=0.0` → deterministic (same prompt, same
reply); `temperature=0.9` → creative (varied replies).

**Why it exists:** Sampling randomness is built into how LLMs
generate — you can't remove it, but you can tune it per task.
Temperature was invented so one model serves both "always produce
valid JSON" tasks and "give me ten different taglines" tasks without
retraining.

**Where it's used:** Pick by task, not taste:
- **temp ≈ 0** — extraction, classification, JSON output, code.
  You need *repeatable, valid* output.
- **temp ≈ 0.8-1.0** — brainstorming, marketing copy, varied answers.
It's a real parameter on every LLM API (level-15 shows the math
underneath).

**What goes wrong without it:**
- High temperature on a JSON-extraction task → occasional malformed
  output that crashes `json.loads` — the failure medium/p02 exists
  to handle.
- temp=0 doesn't guarantee *correct* output — it guarantees
  *repeatable* output. A model can be deterministically wrong.
  Temperature controls dice-rolling, not knowledge.
- No temperature control → every task gets the same compromise
  setting: too random for parsing, too boring for brainstorming.

**Worked example:**
```python
prompt = "Write a tagline for a coffee shop"

chat(prompt, temperature=0.0)
# run 1: "Your daily brew, perfected."
# run 2: "Your daily brew, perfected."   ← identical

chat(prompt, temperature=0.9)
# run 1: "Sip happens — espresso yourself."
# run 2: "Where every cup tells a story." ← different every time
```

**Code:**
```python
def creative_vs_precise(prompt):
    precise  = chat(prompt, temperature=0.0)
    creative = chat(prompt, temperature=0.9)
    return precise, creative
```

**Expected output:**
```python
creative_vs_precise("Write a tagline for a coffee shop")
# → ("Your daily brew, perfected.",      # same every run
#    "Sip happens — espresso yourself.") # different every run
```

---

## Medium

### 4. Structured Output (JSON Extraction) — `p01`

**What it is:** Ask the model to reply in JSON so your code can use
the answer as data: prompt with "Return ONLY valid JSON" →
`json.loads(reply)` → a Python dict.

**Why it exists:** LLMs return text; downstream code needs data.
Structured-output prompting was invented to turn the LLM from a
"chatbot" into "a function that returns structured data" — the
bridge from generated prose into databases, UIs, and other code.

**Where it's used:** Résumé parsers, ticket routers, data-extraction
pipelines — all are "prompt for JSON → parse → use" loops. It's how
LLM output feeds any system that isn't a human reading a chat.

**What goes wrong without it:**
- `json.loads` wants PURE JSON — if the model replies `Here's the
  JSON: {"name": ...}` or wraps it in ```` ```json ```` fences,
  parsing crashes. That's not rare; it's common enough that the next
  concept (retry) exists.
- Without structured output you'd parse free-text answers with
  regexes — brittle code that breaks every time the model rephrases.
- Forgetting `temperature=0.0` → the format varies run to run and
  your parser meets a new edge case each call.

**Worked example:**
```python
text   = "My name is Alice, I'm 30, from Paris"
prompt = (f"Extract name, age, city from: {text}. "
          f"Return ONLY valid JSON.")
reply  = chat(prompt, temperature=0.0)   # temp=0 for reliability
# reply = '{"name": "Alice", "age": 30, "city": "Paris"}'
data   = json.loads(reply)
# → {'name': 'Alice', 'age': 30, 'city': 'Paris'}
```
The LLM went from "chatbot" to "function that returns structured
data."

**Code:**
```python
import json

def extract(text):
    prompt = (f"Extract name, age, city from: {text}. "
              f"Return ONLY valid JSON.")
    return json.loads(chat(prompt, temperature=0.0))
```

**Expected output:**
```python
extract("My name is Alice, I'm 30, from Paris")
# → {'name': 'Alice', 'age': 30, 'city': 'Paris'}
```

---

### 5. Retry on Parse Failure — `p02`

**What it is:** LLM output is unreliable — sometimes it adds a
preamble or breaks JSON syntax. Instead of crashing, catch the
parse error and retry ONCE with a stronger, more explicit prompt.
If that fails too, return an error value instead of raising.

**Why it exists:** Even at temp=0, edge-case inputs produce
malformed replies. The retry pattern was invented because crashing
on the 1-in-1000 weird reply kills a pipeline processing thousands
of items — while a stricter second prompt fixes ~90% of failures
(the model usually "understands" the correction immediately).

**Where it's used:** Production LLM code is always
`try → validate → retry → graceful failure`. Every structured-output
pipeline, agent tool-call parser, and extraction job runs this
pattern.

**What goes wrong without it:**
- One malformed reply → `JSONDecodeError` → the whole batch job
  dies on item 4,837 of 10,000. Unhandled, a single weird model
  response is a production outage.
- Retry the CALL, not just the parse — parsing the same bad string
  twice gives the same failure. The point is a *new, stricter
  prompt* that produces a cleaner reply.
- No graceful fallback → your function raises instead of returning
  an error value, so the caller can't decide how to handle it.

**Worked example:**
```
attempt 1: "Extract ... Return ONLY valid JSON."
  reply → 'Here is the JSON: {"name": "Alice"}'   ← json.loads fails

attempt 2: "Your previous reply was not valid JSON. Return ONLY
            the raw JSON object, no markdown, no preamble."
  reply → '{"name": "Alice"}'                     ← parses ✓

if both fail → return {"error": "unparseable"}
```

**Code:**
```python
def parse_or_retry(text):
    prompt = f"Extract name, age, city from: {text}. Return ONLY valid JSON."
    try:
        return json.loads(chat(prompt, temperature=0.0))
    except json.JSONDecodeError:
        stronger = ("Your previous reply was not valid JSON. "
                    "Return ONLY the raw JSON object, no markdown, "
                    "no preamble. Extract from: " + text)
        try:
            return json.loads(chat(stronger, temperature=0.0))
        except json.JSONDecodeError:
            return {"error": "unparseable"}
```

**Expected output:**
```python
parse_or_retry("Alice, 30, Paris")
# → {'name': 'Alice', 'age': 30, 'city': 'Paris'}   (possibly after
#    one retry)
# → {"error": "unparseable"}                        (if both fail)
```

---

### 6. Batch Calls — `p03`

**What it is:** Instead of one API call per item, put MANY items in
ONE prompt and ask for a JSON array back, in order. 100 texts →
1 call, not 100.

**Why it exists:** Each API call carries fixed overhead — latency,
HTTP round-trip, and per-call token costs. Batching was invented to
amortize that overhead: 100 items in one call is dramatically
cheaper and faster than 100 calls.

**Where it's used:** Every production labeling/classification
pipeline — bulk sentiment tagging, content moderation queues,
enrichment jobs. Anywhere you process items in bulk through an LLM.

**What goes wrong without it:**
- One call per item → 100× the latency and per-call overhead. On a
  paid API, a nightly 10k-item job becomes a real bill.
- "In order" is doing heavy lifting — if the model returns labels
  in a different order or wrong count, every label gets assigned to
  the wrong text. Always sanity-check `len(labels) == len(texts)`
  after parsing.

**Worked example:**
```python
classify_batch(["I love this", "terrible product", "it's ok"],
               ["positive", "negative", "neutral"])

prompt sent:
  "Classify each text into one of ['positive','negative','neutral'].
   Return a JSON array of labels, in order.
   1. I love this
   2. terrible product
   3. it's ok"

reply → '["positive", "negative", "neutral"]'
json.loads → ['positive', 'negative', 'neutral']   # same length!
```

**Code:**
```python
def classify_batch(texts, categories):
    numbered = "\n".join(f"{i+1}. {t}" for i, t in enumerate(texts))
    prompt = (f"Classify each text into one of {categories}. "
              f"Return a JSON array of labels, in order.\n{numbered}")
    return json.loads(chat(prompt, temperature=0.0))
```

**Expected output:**
```python
classify_batch(["I love this", "terrible product", "it's ok"],
               ["positive", "negative", "neutral"])
# → ['positive', 'negative', 'neutral']
```

---

## Hard

### 7. Streaming Tokens — `p01`

**What it is:** Real APIs can send the reply piece-by-piece as it's
generated (a *stream*) instead of one big string at the end. In
Python you consume it as a **generator** — a function using `yield`
that produces values one at a time inside a for-loop.

**Why it exists:** LLM generation takes seconds — a full answer
arrives all at once only after it's completely done. Streaming was
invented so the user reads the first words while the rest are still
generating: it's *perceived* speed, and for long answers it feels
10× faster even though total time is identical.

**Where it's used:** ChatGPT "typing" character-by-character is this
exact mechanism — every chat UI, live transcription, and
incremental display of LLM output.

**What goes wrong without it:**
- Without streaming, users stare at a spinner for the full
  generation time — a 20-second answer feels broken and gets
  abandoned.
- A generator is NOT a string — `stream("hi")` gives a generator
  object, not text. You must loop over it (or `list()` it) to get
  the chunks. Calling `print(stream(...))` prints
  `<generator object ...>`.

**Worked example:**
```python
def stream(prompt):
    reply = chat(prompt)                # full reply (simulated)
    for word in reply.split():
        yield word + " "                # emit one chunk at a time

for chunk in stream("Tell me a joke"):
    print(chunk, end="", flush=True)    # appears word by word
# "Why did the chicken cross the road? ..."
```

**Code:**
```python
def stream(prompt):          # generator — note `yield`, not `return`
    for word in chat(prompt).split():
        yield word + " "
```

**Expected output:**
```python
stream("Tell me a joke")          # → <generator object ...>
list(stream("Tell me a joke"))    # → ['Why ', 'did ', 'the ', ...]

for chunk in stream("Tell me a joke"):
    print(chunk, end="", flush=True)
# Why did the chicken cross the road? ...   (printed word by word)
```

---

### 8. Tool Calling via JSON — `p02`

**What it is:** The LLM can't DO things — it decides WHAT to do,
you execute. The pattern: list your tools in the prompt → model
replies `{"tool": "name", "args": {...}}` → your code validates and
calls `tools[name](**args)`. This is level-13's registry + agent,
now driven by a real model.

**Why it exists:** A language model has no side effects — it can
describe an action but never perform one. Tool calling was invented
to split the work: the model decides WHAT to do (emits JSON naming
a function and arguments), and trusted code executes it. Validation
is the safety boundary between "model said" and "code did."

**Where it's used:** This is LITERALLY OpenAI/Anthropic function
calling under the hood — the model emits JSON, your code runs it,
and (in full agent loops) the result goes back to the model as an
observation. Every agent framework and chat-with-tools product runs
this loop.

**What goes wrong without it:**
- NEVER call `tools[d["tool"]]` without checking `d["tool"] in
  tools` first. The model can hallucinate tool names — unvalidated,
  that's an instant KeyError or worse (running a function it
  invented).
- Without the JSON contract you'd parse "please calculate six times
  seven" back into a function call with regexes — fragile and
  un-auditable.
- No `unknown` fallback → every unparseable reply crashes instead of
  degrading gracefully.

**Worked example:**
```python
TOOLS = {
    "calc":    "Math: args = {a: num, b: num, op: '+|-|*|/'}",
    "search":  "Web search: args = {query: str}",
    "weather": "Weather: args = {city: str}",
}

agent_decide("what is 6 * 7?")
  → prompt lists the 3 tools + asks for JSON
  → model replies '{"tool": "calc", "args": {"a": 6, "b": 7, "op": "*"}}'
  → parse + validate → {"tool": "calc", "args": {...}}

agent_decide("sing me a song")
  → no tool fits → validate fails → {"tool": "unknown", "args": {}}
```

**Code:**
```python
def agent_decide(task):
    prompt = (f"Tools: {TOOLS}\nWhich tool handles: {task}? "
              f'Return ONLY JSON: {{"tool": "name", "args": {{}}}}')
    try:
        d = json.loads(chat(prompt, temperature=0.0))
        if d.get("tool") in TOOLS:
            return d
    except json.JSONDecodeError:
        pass
    return {"tool": "unknown", "args": {}}
```

**Expected output:**
```python
agent_decide("what is 6 * 7?")
# → {"tool": "calc", "args": {"a": 6, "b": 7, "op": "*"}}
agent_decide("sing me a song")
# → {"tool": "unknown", "args": {}}
```

---

### 9. Cost Tracking — `p03`

**What it is:** LLM APIs bill per token (~4 chars ≈ 1 token). A
cost tracker wraps `chat()` to count calls, estimate tokens from
character length, and keep a history — so spending is visible, not
a surprise bill.

**Why it exists:** Metered APIs mean code can literally spend money
— a runaway agent loop (level-13) or a bug that calls `chat()`
10,000× is a real incident teams have paid for. Tracking was
invented to make spend visible and enforceable: it's the foundation
of rate limiting and per-user budgets — you can't cap what you
can't count.

**Where it's used:** Usage dashboards, per-user budget enforcement,
rate limiting, and billing reconciliation in every product built on
metered LLM APIs.

**What goes wrong without it:**
- Without tracking, the first sign of a looped `chat()` bug is the
  invoice at month's end — discovered by finance, not engineering.
- `chars / 4` is an ESTIMATE of *prompt* tokens only. Real billing
  also counts the reply tokens, and true token counts come from a
  tokenizer (level-15), not character math. This tracker is a floor,
  not an invoice — treat it as exact and you'll under-budget.

**Worked example:**
```python
llm = TrackedLLM()
llm.call("hello")            # 5 chars  → ~1 token
llm.call("what is AI?")      # 12 chars → ~3 tokens

llm.stats()
# {"calls": 2, "est_tokens": 4,
#  "est_cost_usd": 4 × $0.00015/1K ≈ $0.0000006}
llm.history   # [{"prompt": "hello", "reply": ..., "tokens": 1}, ...]
```

**Code:**
```python
class TrackedLLM:
    def __init__(self):
        self.calls = 0
        self.est_tokens = 0
        self.history = []

    def call(self, prompt):
        reply = chat(prompt)
        tokens = len(prompt) // 4
        self.calls += 1
        self.est_tokens += tokens
        self.history.append({"prompt": prompt, "reply": reply,
                             "tokens": tokens})
        return reply

    def stats(self):
        return {"calls": self.calls, "est_tokens": self.est_tokens,
                "est_cost_usd": self.est_tokens * 0.00015 / 1000}
```

**Expected output:**
```python
llm = TrackedLLM()
llm.call("hello"); llm.call("what is AI?")
llm.stats()
# → {"calls": 2, "est_tokens": ~4,
#    "est_cost_usd": ~6e-07}    # ≈ $0.0000006
len(llm.history)   # → 2
```

---

## Done with concepts? → Try `easy/p01-first-call.py`
