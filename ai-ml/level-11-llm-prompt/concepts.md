# Level 11 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept has:
what it is in plain words → a worked example with real numbers →
why ML cares → the code → what confuses beginners.

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
Rule of thumb: **every extra constraint you add removes a guess the
model has to make.**

**Why ML cares:** Production AI features (auto-summaries, ticket
tagging, email drafting) are all built on prompts like this. The
structured version is what lets an LLM plug into normal software —
a JSON answer can be stored in a database or shown in a UI.

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

**Common confusion:** Beginners think a *longer* prompt is better.
It's not length — it's *constraints*. "Please be very thorough and
write a great summary" is long but still vague.

---

### 2. Few-Shot Prompting — `p02`

**What it is:** Instead of *explaining* a task, you *show* a few
input→output examples inside the prompt. The model sees the pattern
and continues it for your new input. "Few-shot" = a few examples.
("Zero-shot" = no examples, just instructions.)

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

**Why ML cares:** This is how you get a general LLM to do YOUR
specific task without fine-tuning. 3-10 examples in the prompt can
match a small fine-tuned model for many classification jobs. It's
also how structured formats get enforced — examples of the format
are stronger than descriptions of the format.

**Code:**
```python
def few_shot_prompt(examples, query):
    lines = ["Classify the sentiment:", ""]
    for text, label in examples:
        lines.append(f'Text: "{text}" → {label}')
    lines.append(f'Text: "{query}" →')   # trailing arrow invites the answer
    return "\n".join(lines)
```

**Common confusion:** The examples must be *consistent*. If one
example says "Positive" and a similar one says "Good", the model
learns an inconsistent pattern and outputs garbage labels.

---

### 3. Temperature — `p03`

**What it is:** A number (usually 0.0-2.0) that controls how random
the model's word choices are. An LLM doesn't pick "the" next word —
it computes a probability for EVERY possible next word, then samples
from those probabilities. Temperature reshapes those probabilities.

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

**Why ML cares:** Use temp ≈ 0 for anything deterministic:
extraction, classification, code generation, JSON output (you want
valid JSON *every time*). Use higher temp for brainstorming,
writing, or when you want diverse answers to choose from.

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

**Common confusion:** Temperature does NOT make the model "smarter"
or "know more." temp=1.5 doesn't unlock hidden knowledge — it just
rolls the dice more often, including on wrong answers.

---

## Medium

### 4. Chain-of-Thought Prompting — `p01`

**What it is:** For reasoning problems (math, logic, multi-step),
add "solve this step by step" to the prompt. The model then writes
out intermediate reasoning *before* the final answer — and because
it can use its own earlier reasoning as context, the final answer
gets much better.

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
The written steps act like scratch paper — each line is context for
the next line, so errors get caught mid-way.

**Why ML cares:** CoT is one of the cheapest accuracy boosts in
existence — zero training, one phrase, big gains on reasoning.
It's also the ancestor of "agent reasoning" (level-13): agents
think → act → observe in loops for the same reason.

**Code:**
```python
def chain_of_thought(problem):
    return (f"Solve this step by step:\n\n"
            f"Problem: {problem}")
```

**Common confusion:** CoT helps for *reasoning* tasks, not factual
recall. "What year was Python created?" gains nothing from step-
by-step — there's no reasoning to do, just a fact to recall.

---

### 5. Persona + Format + Context — `p02`

**What it is:** The three-part professional prompt structure:
- **Persona** — who the model should be ("You are a data scientist")
- **Format** — how to structure the output ("3 bullet points")
- **Context** — the domain/background to use ("machine learning basics")

Plus the actual question at the end.

**Worked example:**
```
You are a data scientist. Your task is to explain a concept.

Context: machine learning basics

Format your response as:
3 bullet points

Input: What is overfitting?
```
Each piece controls a different axis: persona controls *vocabulary
and depth*, format controls *shape*, context controls *which facts
are relevant*.

**Why ML cares:** This is the template behind most production
prompts. Customer-support bots, code reviewers, and writing
assistants are all "persona + format + context + question" under
the hood. If an answer is wrong, you now know which knob to turn:
wrong tone → fix persona; wrong shape → fix format; wrong facts →
fix context.

**Code:**
```python
def structured_prompt(persona, context, format, question):
    return (f"You are a {persona}. Your task is to explain a concept.\n\n"
            f"Context: {context}\n\n"
            f"Format your response as:\n{format}\n\n"
            f"Input: {question}")
```

**Common confusion:** Persona does NOT change what the model knows.
"You are a doctor" doesn't add medical knowledge — it just shifts
the model toward the style/depth doctors write in.

---

### 6. Parsing Structured LLM Output — `p03`

**What it is:** LLMs return plain text. If you asked for JSON, the
answer often arrives wrapped in extra chatter. To use it in code,
find the `{...}` part and run `json.loads()` on it.

**Worked example:**
```python
raw = 'The sentiment is: {"score": 0.95, "category": "positive"}'
#                     ^ not JSON here    ^ ...but this part is
start = raw.index("{")          # index of first {
end   = raw.rindex("}") + 1     # index AFTER last }
data  = json.loads(raw[start:end])
# → {'score': 0.95, 'category': 'positive'}
```

**Why ML cares:** This is the bridge between "LLM as chatbot" and
"LLM as a function in your program." Every structured-extraction
pipeline (résumé parsing, ticket tagging, data cleanup) does exactly
this: prompt for JSON → extract braces → `json.loads` → use the dict.

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

**Common confusion:** `json.loads` fails on the whole string — the
words around the JSON aren't valid JSON. You MUST slice out just
the `{...}` first. (Also watch for `invalid` JSON like trailing
commas or single quotes — models produce those sometimes.)

---

## Hard

### 7. Prompt Iteration & Scoring — `p01`

**What it is:** Prompts are code — you version them and improve them.
The loop: write v1 → test → identify what's missing → write v2 →
repeat. "Scoring" means putting a number on prompt quality (e.g.,
counting how many specificity features it has) so improvement is
measurable, not vibes.

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

**Why ML cares:** This is the real workflow at AI companies. Nobody
writes the perfect prompt on try one. Teams keep prompt version
history, and a "prompt score" is the cheap proxy you check BEFORE
spending money on full evaluation.

**Code:**
```python
def iterate_prompts(task):
    v1 = f"Do this: {task}."
    v2 = f"Do this in 3 bullet points: {task}."
    v3 = f"Do this in 3 bullet points with key metrics: {task}."
    return [(v1, score(v1)), (v2, score(v2)), (v3, score(v3))]
```

**Common confusion:** A higher-scoring *prompt* doesn't guarantee a
better *response* — prompt specificity is a proxy metric. You still
need to evaluate actual outputs (next concept).

---

### 8. Prompt Evaluation Framework — `p02`

**What it is:** Before shipping a prompt, automatically check its
outputs against criteria: Is it short enough? In the right format?
Does it contain required content? Each check returns True/False so
you can score responses objectively across many test inputs.

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

**Why ML cares:** This is "unit testing for prompts." Change one
word in a production prompt and 10 test cases might regress — an
evaluator catches that instantly. Companies run hundreds of these
checks on every prompt change, same as CI for normal code.

**Code:**
```python
def evaluate_response(response, criteria):
    return {
        "length":   len(response) <= criteria["max_length"],
        "format":   all(l.startswith("- ") for l in response.splitlines()),
        "accuracy": criteria["contains"].lower() in response.lower(),
    }
```

**Common confusion:** These checks test *form*, not *truth*. A
response can pass length+format+keyword checks and still be factually
wrong. Automated checks are a first filter, not a proof of quality.

---

### 9. System Prompts — `p03`

**What it is:** Most chat APIs split input into two message types:
a **system prompt** (invisible to the end user, sets the model's
role/rules/personality once) and **user messages** (the actual
questions). The system prompt affects every response in the
conversation.

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

**Why ML cares:** This is where product behavior lives. The guard
rails ("never give medical advice"), the voice ("be concise"), the
output rules ("always JSON") — all in the system prompt. Changing
it is the cheapest way to change an entire app's personality.

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

**Common confusion:** The system prompt is not a magic cage — it's
still just text the model continues. Determined users can sometimes
talk it out of its rules ("prompt injection"). For truly critical
rules, enforce them in code, not just in the prompt.

---

## Done with concepts? → Try `easy/p01-prompt-styles.py`
