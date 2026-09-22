# Level 11 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept explains:
What it is · Why it exists · Where it's used · What goes wrong without it ·
worked example · code · expected output.

**Vocabulary for this level:**
- **LLM** (Large Language Model) — a neural network trained on huge
  amounts of text. You give it a string, it continues the string.
- **Prompt** — the input text you send to the LLM. You don't "code"
  the model; you *write* instructions for it.
- **Completion / response** — the text the LLM generates back.

The mental model for the whole level: an LLM is a very good
*pattern continuer*. Whatever format, tone, and reasoning style your
prompt demonstrates is what it will continue. Prompt engineering is
the art of setting up that pattern.

---

## Easy

### 1. Three Prompt Styles — `p01`

**What it is:** The same task can be asked three ways, from vague to
precise. A vague prompt leaves everything to the model's guess. A
detailed prompt pins down what you want. A structured prompt pins
down the exact output *format* so another program can parse it.

**Why it exists:** You can't change an LLM's weights — the prompt
is your ONLY control surface. Since the model continues whatever
pattern you set up, constraint styles were developed to remove
guesses: every requirement you state is one the model doesn't have
to invent.

**Where it's used:** Production AI features (auto-summaries,
ticket tagging, email drafting) are all built on prompts like
this. The structured version is what lets an LLM plug into normal
software — a JSON answer can be stored in a database or shown in a
UI.

**What goes wrong without it:** Vague prompt → unpredictable
length, style, and format → your downstream parser breaks on a
whim. And longer is NOT better: "Please be very thorough and write
a great summary" is long but still vague — it's *constraints* that
help, not word count. Rule of thumb: **every extra constraint you
add removes a guess the model has to make.**

**Worked example:** Task = "summarize an article."
```
Vague:      "Summarize this text."
            → model guesses length, style, format. Unpredictable.

Detailed:   "Summarize this text in 3 bullet points."
            → you get exactly 3 bullets. Predictable.

Structured: "Summarize this text as JSON with keys: main_point, key_details."
            → {"main_point": "...", "key_details": "..."}
            → Python code can now read the answer automatically.
```

**Code:**
```python
def make_prompts(text):
    return {
        "simple":     f"Summarize this text. {text}",
        "detailed":   f"Summarize this text in 3 bullet points. {text}",
        "structured": f"Summarize this text as JSON with keys: "
                      f"main_point, key_details. {text}",
    }
```

**Expected output:** `make_prompts("ARTICLE")` returns
```
{"simple":     "Summarize this text. ARTICLE",
 "detailed":   "Summarize this text in 3 bullet points. ARTICLE",
 "structured": "Summarize this text as JSON with keys: main_point, key_details. ARTICLE"}
```

---

### 2. Few-Shot Prompting — `p02`

**What it is:** Instead of *explaining* a task, you *show* a few
input→output examples inside the prompt. The model sees the pattern
and continues it for your new input. "Few-shot" = a few examples.
("Zero-shot" = no examples, just instructions.)

**Why it exists:** A general LLM doesn't know YOUR task, YOUR
labels, or YOUR format — and fine-tuning is expensive. Few-shot
was discovered because examples inside the prompt teach the task
without touching a single weight: the prompt itself becomes the
training data.

**Where it's used:** Getting a general LLM to do your specific
task without fine-tuning — 3-10 examples can match a small
fine-tuned model on many classification jobs. It's also how
structured formats get enforced: examples of the format are
stronger than descriptions of the format.

**What goes wrong without it:** Zero-shot on a custom label scheme
→ the model invents its own labels ("Good", "Nice", "Positive")
and downstream code can't match them. Inconsistent examples are
just as bad — if one says "Positive" and a similar one says
"Good", the model learns an inconsistent pattern and outputs
garbage labels.

**Worked example:**
```
Classify the sentiment:

Text: "I love it" → Positive
Text: "Terrible" → Negative
Text: "Meh" → Neutral
Text: "This is amazing!" →
```
The model's job is trivial now: the pattern screams "Positive."
No training, no weights updated — the *prompt itself* taught it
the task.

**Code:**
```python
def few_shot_prompt(examples, query):
    lines = ["Classify the sentiment:", ""]
    for text, label in examples:
        lines.append(f'Text: "{text}" → {label}')
    lines.append(f'Text: "{query}" →')   # trailing arrow invites the answer
    return "\n".join(lines)
```

**Expected output:** With the three worked-example pairs and
`query="This is amazing!"`, the function returns the prompt block
shown above — ending in `Text: "This is amazing!" →` (trailing
arrow, no label).

---

### 3. Temperature — `p03`

**What it is:** A number (usually 0.0-2.0) that controls how random
the model's word choices are. An LLM doesn't pick "the" next word —
it computes a probability for EVERY possible next word, then samples
from those probabilities. Temperature reshapes those probabilities.

**Why it exists:** Different tasks need different amounts of
randomness — extraction wants the same answer every time,
brainstorming wants variety. Temperature exists as the single dial
that reshapes the sampling distribution: lower sharpens it toward
the top choice, higher flattens it toward uniform.

**Where it's used:** temp ≈ 0 for anything deterministic:
extraction, classification, code generation, JSON output (you want
valid JSON *every time*). Higher temp for brainstorming, writing,
or when you want diverse answers to choose from.

**What goes wrong without it:** Run a JSON-extraction pipeline at
temp 1.0 → occasionally malformed output → `json.loads` crashes
mid-pipeline on a random Tuesday. The reverse also hurts:
temp=0 on a brainstorming feature → identical suggestions on every
call. And temperature does NOT make the model "smarter" or "know
more" — temp=1.5 doesn't unlock hidden knowledge, it just rolls
the dice more often, including on wrong answers.

**Worked example:** Say the model's next-word probabilities are:
```
"cat"    → 0.70
"dog"    → 0.20
"zebra"  → 0.10
```
- **temp = 0.0** → always picks "cat" (argmax). Same prompt, same
  answer, every time.
- **temp = 0.5** → still favors "cat" but occasionally picks "dog".
- **temp = 1.0** → samples fairly from the raw probabilities.
- **temp = 1.5** → flattens them, so "zebra" becomes almost as
  likely as "cat" — creative but can go incoherent.

**Code:**
```python
def explain_temperature(temp):
    if temp <= 0.2:
        return "Deterministic — same output every time"
    elif temp <= 0.7:
        return "Balanced — some variety but coherent"
    elif temp <= 1.2:
        return "Creative — more random, diverse outputs"
    return "Very creative — may be incoherent"
```

**Expected output:**
```
explain_temperature(0.0) → "Deterministic — same output every time"
explain_temperature(0.5) → "Balanced — some variety but coherent"
explain_temperature(1.0) → "Creative — more random, diverse outputs"
explain_temperature(1.5) → "Very creative — may be incoherent"
```

---

## Medium

### 4. Chain-of-Thought Prompting — `p01`

**What it is:** For reasoning problems (math, logic, multi-step),
add "solve this step by step" to the prompt. The model then writes
out intermediate reasoning *before* the final answer — and because
it can use its own earlier reasoning as context, the final answer
gets much better.

**Why it exists:** An LLM answers by pattern-matching — for
multi-step problems it blurts a plausible-looking answer without
doing the math. CoT was discovered because written steps act like
scratch paper: each line becomes context for the next line, so the
model literally computes its way to the answer instead of guessing
it.

**Where it's used:** One of the cheapest accuracy boosts in
existence — zero training, one phrase, big gains on reasoning.
It's also the ancestor of "agent reasoning" (level-13): agents
think → act → observe in loops for the same reason.

**What goes wrong without it:** On arithmetic/word problems the
model blurts a plausible-but-wrong answer ("$4" instead of "$8")
because nothing forced it to compute. The opposite misuse: CoT
helps for *reasoning* tasks, not factual recall — "What year was
Python created?" gains nothing from step-by-step, there's no
reasoning to do, just a fact to recall.

**Worked example:**
```
Without CoT:
  "If 3 apples cost $2, how much do 12 cost?"
  → model might blurt "$4" (pattern-matches, no math done)

With CoT:
  "Solve this step by step: If 3 apples cost $2, how much do 12 cost?"
  → Step 1: cost per apple = $2 / 3 ≈ $0.67
    Step 2: $0.67 × 12 ≈ $8.00
    Answer: $8.00
```

**Code:**
```python
def chain_of_thought(problem):
    return (f"Solve this step by step:\n\n"
            f"Problem: {problem}")
```

**Expected output:** `chain_of_thought("If 3 apples cost $2, how
much do 12 cost?")` returns
```
Solve this step by step:

Problem: If 3 apples cost $2, how much do 12 cost?
```

---

### 5. Persona + Format + Context — `p02`

**What it is:** The three-part professional prompt structure:
- **Persona** — who the model should be ("You are a data scientist")
- **Format** — how to structure the output ("3 bullet points")
- **Context** — the domain/background to use ("machine learning basics")

Plus the actual question at the end.

**Why it exists:** A single blob prompt mixes every concern —
when the output is wrong you can't tell which knob to turn.
Splitting into persona/format/context exists because each piece
controls a different axis: persona controls *vocabulary and
depth*, format controls *shape*, context controls *which facts are
relevant*. Wrong tone → fix persona; wrong shape → fix format;
wrong facts → fix context.

**Where it's used:** The template behind most production prompts.
Customer-support bots, code reviewers, and writing assistants are
all "persona + format + context + question" under the hood.

**What goes wrong without it:** One undifferentiated prompt → bad
output means rewriting the whole thing blindly. And persona does
NOT change what the model knows — "You are a doctor" doesn't add
medical knowledge, it just shifts the model toward the
style/depth doctors write in. Expecting knowledge from a persona
gets you confident, well-styled wrong answers.

**Worked example:**
```
You are a data scientist. Your task is to explain a concept.

Context: machine learning basics

Format your response as:
3 bullet points

Input: What is overfitting?
```

**Code:**
```python
def structured_prompt(persona, context, format, question):
    return (f"You are a {persona}. Your task is to explain a concept.\n\n"
            f"Context: {context}\n\n"
            f"Format your response as:\n{format}\n\n"
            f"Input: {question}")
```

**Expected output:** `structured_prompt("data scientist",
"machine learning basics", "3 bullet points", "What is
overfitting?")` returns exactly the prompt block shown above.

---

### 6. Parsing Structured LLM Output — `p03`

**What it is:** LLMs return plain text. If you asked for JSON, the
answer often arrives wrapped in extra chatter. To use it in code,
find the `{...}` part and run `json.loads()` on it.

**Why it exists:** Models don't guarantee clean output — they add
preambles like "The sentiment is:" even when asked for raw JSON.
The extract-braces-then-parse technique exists as the bridge
between "LLM as chatbot" and "LLM as a function in your program."

**Where it's used:** Every structured-extraction pipeline —
résumé parsing, ticket tagging, data cleanup — does exactly this:
prompt for JSON → extract braces → `json.loads` → use the dict.

**What goes wrong without it:** `json.loads` on the whole string →
`JSONDecodeError` crash — the words around the JSON aren't valid
JSON; you MUST slice out just the `{...}` first. Also watch for
invalid JSON like trailing commas or single quotes — models
produce those sometimes. And on total failure, return `None`
rather than letting the exception kill your pipeline.

**Worked example:**
```python
raw = 'The sentiment is: {"score": 0.95, "category": "positive"}'
#                     ^ not JSON here    ^ ...but this part is
start = raw.index("{")          # index of first {
end   = raw.rindex("}") + 1     # index AFTER last }
data  = json.loads(raw[start:end])
# → {'score': 0.95, 'category': 'positive'}
```

**Code:**
```python
import json

def parse_llm_output(text):
    try:
        start = text.index("{")
        end = text.rindex("}") + 1
        return json.loads(text[start:end])
    except (ValueError, json.JSONDecodeError):
        return None
```

**Expected output:**
```
parse_llm_output('The sentiment is: {"score": 0.95, "category": "positive"}')
    → {'score': 0.95, 'category': 'positive'}
parse_llm_output('no json here') → None
```

---

## Hard

### 7. Prompt Iteration & Scoring — `p01`

**What it is:** Prompts are code — you version them and improve them.
The loop: write v1 → test → identify what's missing → write v2 →
repeat. "Scoring" means putting a number on prompt quality (e.g.,
counting how many specificity features it has) so improvement is
measurable, not vibes.

**Why it exists:** Nobody writes the perfect prompt on try one,
and "it feels better" doesn't survive a code review. Iteration +
scoring exist so prompt improvement is a measurable process with
history — the cheap proxy you check BEFORE spending money on full
evaluation.

**Where it's used:** The real workflow at AI companies — teams
keep prompt version history and score candidates before running
expensive output evaluation.

**What goes wrong without it:** Tweak prompts by vibes →
regressions go unnoticed and you can't tell which change helped.
But don't over-trust the metric: a higher-scoring *prompt* doesn't
guarantee a better *response* — specificity is a proxy. You still
need to evaluate actual outputs (next concept).

**Worked example:**
```
v1: "Summarize this."                              score 0.60
    → has a task, but no format, no constraints

v2: "Summarize in 3 bullet points."                score 0.75
    → + format constraint

v3: "Summarize in 3 bullet points with key metrics." score 0.85
    → + content constraint (what belongs in the bullets)
```
A simple scorer: start at 0.5, add points for each feature found
(mentions a count? a format word like "bullet"/"JSON"? a content
requirement?).

**Code:**
```python
def iterate_prompts(task):
    v1 = f"Do this: {task}."
    v2 = f"Do this in 3 bullet points: {task}."
    v3 = f"Do this in 3 bullet points with key metrics: {task}."
    return [(v1, score(v1)), (v2, score(v2)), (v3, score(v3))]
```

**Expected output:** Returns a list like
```
[("Do this: summarize.", 0.60),
 ("Do this in 3 bullet points: summarize.", 0.75),
 ("Do this in 3 bullet points with key metrics: summarize.", 0.85)]
```
— scores climbing as constraints are added.

---

### 8. Prompt Evaluation Framework — `p02`

**What it is:** Before shipping a prompt, automatically check its
outputs against criteria: Is it short enough? In the right format?
Does it contain required content? Each check returns True/False so
you can score responses objectively across many test inputs.

**Why it exists:** Prompt edits silently regress — change one word
and 10 test cases might break. An evaluation framework exists as
"unit testing for prompts": it catches regressions instantly
instead of after users complain.

**Where it's used:** Companies run hundreds of these checks on
every prompt change — same role as CI for normal code.

**What goes wrong without it:** No eval → a prompt change ships
broken outputs to production unnoticed. But know the limit: these
checks test *form*, not *truth* — a response can pass
length+format+keyword checks and still be factually wrong.
Automated checks are a first filter, not a proof of quality.

**Worked example:**
```python
response = "- Point one\n- Point two\n- Point three"
criteria = {"max_length": 100, "format": "bullet", "contains": "point"}

checks:
  length   → len(response) <= 100        → True
  format   → every line starts with "-"  → True
  accuracy → "point" in response.lower() → True

result = {"length": True, "format": True, "accuracy": True}
```
One False anywhere = the response fails review.

**Code:**
```python
def evaluate_response(response, criteria):
    return {
        "length":   len(response) <= criteria["max_length"],
        "format":   all(l.startswith("- ") for l in response.splitlines()),
        "accuracy": criteria["contains"].lower() in response.lower(),
    }
```

**Expected output:** With the worked-example response and
criteria → `{"length": True, "format": True, "accuracy": True}`.
Change the response to plain prose → `"format": False`.

---

### 9. System Prompts — `p03`

**What it is:** Most chat APIs split input into two message types:
a **system prompt** (invisible to the end user, sets the model's
role/rules/personality once) and **user messages** (the actual
questions). The system prompt affects every response in the
conversation.

**Why it exists:** Mixing product rules into every user message is
fragile — users could see, override, or forget them. The system
prompt exists as a separate, privileged channel that shapes every
response without cluttering the conversation.

**Where it's used:** This is where product behavior lives. The
guardrails ("never give medical advice"), the voice ("be
concise"), the output rules ("always JSON") — all in the system
prompt. Changing it is the cheapest way to change an entire app's
personality.

**What goes wrong without it:** Rules only in user prompts →
inconsistent behavior and user-visible instructions. But don't
over-trust it either: the system prompt is not a magic cage —
it's still just text the model continues. Determined users can
sometimes talk it out of its rules ("prompt injection"). For truly
critical rules, enforce them in code, not just in the prompt.

**Worked example:** Same question, different system prompts:
```
System: "You are a helpful assistant."
  "What is overfitting?" → friendly, general explanation

System: "You are an expert data scientist."
  same question → technical terms, math, assumes expertise

System: "You are a critical reviewer."
  same question → pokes holes, warns about misuse
```
One line of setup, three completely different products.

**Code:**
```python
def get_personas():
    return {
        "helpful":  "You are a helpful assistant. Be clear and friendly.",
        "expert":   "You are an expert data scientist. Provide detailed "
                    "technical explanations.",
        "creative": "You are a creative writer. Be vivid and original.",
        "critical": "You are a critical reviewer. Find flaws and risks.",
    }
```

**Expected output:** `get_personas()` returns a dict with 4 keys
(`helpful`, `expert`, `creative`, `critical`), each mapping to a
system-prompt string like `"You are a helpful assistant. Be clear
and friendly."`

---

## Done with concepts? → Try `easy/p01-prompt-styles.py`
