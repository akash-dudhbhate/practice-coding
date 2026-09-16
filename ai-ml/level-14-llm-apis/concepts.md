# Level 14 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept has:
what it is in plain words → a worked example with real numbers →
why ML cares → the code → what confuses beginners.

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

**Worked example:**
```python
from llm import chat

reply = chat("What is 2+2?")
# simulated backend → "[simulated-llm] Response to: What is 2+2?"
# openai backend    → "2 + 2 equals 4."
# your code: IDENTICAL either way
```

**Why ML cares:** Production apps always wrap the API behind one
function. Reasons: (1) you can test offline with the mock;
(2) swapping OpenAI → a local model is a config change, not a
rewrite; (3) retries, logging, and cost tracking (hard/p03) get
added in ONE place. Sprinkling `openai.chat.completions.create()`
across 20 files = vendor lock-in and untestable code.

**Code:**
```python
def ask_llm(question):
    return chat(question)      # one line — the abstraction does the work
```

**Common confusion:** The `sys.path.insert` dance at the top of each
problem file isn't boilerplate to ignore — it makes `from llm import
chat` find `level-14-llm-apis/llm.py` no matter which subfolder the
problem lives in.

---

### 2. System Prompts via API — `p02`

**What it is:** In a real API call, the message list has roles:
`{"role": "system", ...}` sets behavior/persona once, then
`{"role": "user", ...}` is the actual question. Our `chat()` takes
it as `system=` and builds that message list for you.

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

**Why ML cares:** This is the cheapest "fine-tuning" that exists.
Every chatbot persona, every guard rail ("never give medical
advice"), every output rule ("always answer in JSON") lives in the
system prompt — sent once, affects every reply.

**Code:**
```python
def ask_with_persona(question, persona):
    return chat(question, system=persona)
```

**Common confusion:** The system prompt is not "the first user
message" — it's a separate role with higher priority. Models are
trained to follow it even when the user message conflicts. (Level-11
hard/p03 covered the persona idea; here you use the real parameter.)

---

### 3. Temperature in API Calls — `p03`

**What it is:** The same randomness dial from level-11, now a real
API parameter. `temperature=0.0` → deterministic (same prompt, same
reply); `temperature=0.9` → creative (varied replies).

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

**Why ML cares:** Pick by task, not taste:
- **temp ≈ 0** — extraction, classification, JSON output, code.
  You need *repeatable, valid* output.
- **temp ≈ 0.8-1.0** — brainstorming, marketing copy, varied answers.

**Code:**
```python
def creative_vs_precise(prompt):
    precise  = chat(prompt, temperature=0.0)
    creative = chat(prompt, temperature=0.9)
    return precise, creative
```

**Common confusion:** temp=0 doesn't guarantee *correct* output —
it guarantees *repeatable* output. A model can be deterministically
wrong. Temperature controls dice-rolling, not knowledge.

---

## Medium

### 4. Structured Output (JSON Extraction) — `p01`

**What it is:** Ask the model to reply in JSON so your code can use
the answer as data: prompt with "Return ONLY valid JSON" →
`json.loads(reply)` → a Python dict.

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

**Why ML cares:** This is how LLM output feeds databases, UIs, and
other code. Résumé parsers, ticket routers, and data-extraction
pipelines are all "prompt for JSON → parse → use" loops.

**Code:**
```python
import json

def extract(text):
    prompt = (f"Extract name, age, city from: {text}. "
              f"Return ONLY valid JSON.")
    return json.loads(chat(prompt, temperature=0.0))
```

**Common confusion:** `json.loads` wants PURE JSON — if the model
replies `Here's the JSON: {"name": ...}` or wraps it in
```` ```json ```` fences, parsing crashes. That's not rare; it's
common enough that the next concept exists.

---

### 5. Retry on Parse Failure — `p02`

**What it is:** LLM output is unreliable — sometimes it adds a
preamble or breaks JSON syntax. Instead of crashing, catch the
parse error and retry ONCE with a stronger, more explicit prompt.
If that fails too, return an error value instead of raising.

**Worked example:**
```
attempt 1: "Extract ... Return ONLY valid JSON."
  reply → 'Here is the JSON: {"name": "Alice"}'   ← json.loads fails

attempt 2: "Your previous reply was not valid JSON. Return ONLY
            the raw JSON object, no markdown, no preamble."
  reply → '{"name": "Alice"}'                     ← parses ✓

if both fail → return {"error": "unparseable"}
```

**Why ML cares:** One retry fixes ~90% of malformed responses —
the model usually "understands" the correction immediately.
Production LLM code is always `try → validate → retry →
graceful failure`. Never crash on the 1-in-1000 weird reply.

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

**Common confusion:** Retry the CALL, not just the parse — parsing
the same bad string twice gives the same failure. The point is a
*new, stricter prompt* that produces a cleaner reply.

---

### 6. Batch Calls — `p03`

**What it is:** Instead of one API call per item, put MANY items in
ONE prompt and ask for a JSON array back, in order. 100 texts →
1 call, not 100.

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

**Why ML cares:** Each API call has fixed overhead — latency, HTTP
round-trip, and per-call token costs. Batching 100 items into one
call is dramatically cheaper and faster than 100 calls. Every
production labeling pipeline does this.

**Code:**
```python
def classify_batch(texts, categories):
    numbered = "\n".join(f"{i+1}. {t}" for i, t in enumerate(texts))
    prompt = (f"Classify each text into one of {categories}. "
              f"Return a JSON array of labels, in order.\n{numbered}")
    return json.loads(chat(prompt, temperature=0.0))
```

**Common confusion:** "In order" is doing heavy lifting — if the
model returns labels in a different order or wrong count, every
label gets assigned to the wrong text. Always sanity-check
`len(labels) == len(texts)` after parsing.

---

## Hard

### 7. Streaming Tokens — `p01`

**What it is:** Real APIs can send the reply piece-by-piece as it's
generated (a *stream*) instead of one big string at the end. In
Python you consume it as a **generator** — a function using `yield`
that produces values one at a time inside a for-loop.

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

**Why ML cares:** Streaming is *perceived* speed. ChatGPT "typing"
character-by-character is this exact mechanism — the user reads the
first words while the rest are still generating. For long answers
it feels 10× faster even though total time is identical.

**Code:**
```python
def stream(prompt):          # generator — note `yield`, not `return`
    for word in chat(prompt).split():
        yield word + " "
```

**Common confusion:** A generator is NOT a string —
`stream("hi")` gives a generator object, not text. You must loop
over it (or `list()` it) to get the chunks. Calling `print(stream(...))`
prints `<generator object ...>`.

---

### 8. Tool Calling via JSON — `p02`

**What it is:** The LLM can't DO things — it decides WHAT to do,
you execute. The pattern: list your tools in the prompt → model
replies `{"tool": "name", "args": {...}}` → your code validates and
calls `tools[name](**args)`. This is level-13's registry + agent,
now driven by a real model.

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

**Why ML cares:** This is LITERALLY OpenAI/Anthropic function
calling under the hood — the model emits JSON naming a function and
arguments, your code runs it, and (in full agent loops) the result
goes back to the model as an observation. Validation is the safety
boundary between "model said" and "code did."

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

**Common confusion:** NEVER call `tools[d["tool"]]` without checking
`d["tool"] in tools` first. The model can hallucinate tool names —
unvalidated, that's an instant KeyError or worse (running a
function it invented).

---

### 9. Cost Tracking — `p03`

**What it is:** LLM APIs bill per token (~4 chars ≈ 1 token). A
cost tracker wraps `chat()` to count calls, estimate tokens from
character length, and keep a history — so spending is visible, not
a surprise bill.

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

**Why ML cares:** Runaway agent loops (level-13) or chatty users
can burn real money — a bug that loops `chat()` 10,000× is a real
incident teams have paid for. Tracking is also the foundation of
rate limiting and per-user budgets: you can't cap what you can't
count.

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

**Common confusion:** `chars / 4` is an ESTIMATE of *prompt* tokens
only. Real billing also counts the reply tokens, and true token
counts come from a tokenizer (level-15), not character math. This
tracker is a floor, not an invoice.

---

## Done with concepts? → Try `easy/p01-first-call.py`
