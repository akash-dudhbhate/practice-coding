# Level 13 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept explains:
What it is · Why it exists · Where it's used · What goes wrong without it ·
worked example · code · expected output.

**Vocabulary for this level:**
- **Agent** — a program where an LLM (or simple logic) *decides what
  to do next*, not just what to say. A chatbot answers; an agent
  acts.
- **Tool** — a function the agent can call: calculator, web search,
  database query. The agent doesn't know facts; it knows how to
  *fetch* them.
- **Loop** — agents repeat think → act → observe until the goal is
  done. That's what makes them "agentic" instead of one-shot.

The progression of this level: `decide → use tools → loop →
plan → remember → collaborate → evaluate → go autonomous`.

---

## Easy

### 1. The Agent Decision — `p01`

**What it is:** At its core, an agent is a function that maps
`goal → action`. Given a text goal, decide WHICH capability to
invoke. The simplest possible version is if/elif on keywords — real
agents replace this with an LLM, but the shape is identical.

**Why it exists:** A chatbot only produces text — to *act* on the
world, something must translate "what the user wants" into "which
capability runs." The routing decision exists as the minimal first
piece of every agent: without it, tools can't be chosen at all.

**Where it's used:** This routing decision is the first thing
every agent framework implements. With a real LLM, the model reads
the goal plus a list of tool descriptions and outputs the tool
name — the if/elif you're writing is the "compiler's view" of
that.

**What goes wrong without it:** No decision layer → the agent
either hardcodes one tool (wrong tool on mismatched goals) or
guesses randomly. And notice the last line of the example: a good
agent KNOWS when it can't help — without an "unknown goal" path,
"cook dinner" gets force-matched to some tool and produces
nonsense. An "I don't know" path is a required feature, not a bug.
Also: decision is not execution — returning a STRING naming the
tool vs. actually calling it are separate steps (medium/p01);
mixing them makes agents impossible to debug.

**Worked example:**
```python
agent_decide("calculate 6 * 7")     → "use calculator"
agent_decide("search for AI news")  → "use search"
agent_decide("write a report")      → "use writer"
agent_decide("cook dinner")         → "unknown goal"   # no tool fits
```

**Code:**
```python
def agent_decide(goal):
    g = goal.lower()
    if "calculate" in g: return "use calculator"
    if "search" in g:    return "use search"
    if "write" in g:     return "use writer"
    return "unknown goal"
```

**Expected output:**
```
agent_decide("calculate 6 * 7")    → "use calculator"
agent_decide("search for AI news") → "use search"
agent_decide("write a report")     → "use writer"
agent_decide("cook dinner")        → "unknown goal"
```

---

### 2. Tool Registry — `p02`

**What it is:** A dict mapping `name → function`. The agent's
"toolbox." It picks a tool by name (a string from the decision
step), looks it up in the registry, and calls it. This is how an
LLM's text output becomes real code execution.

**Why it exists:** An LLM can only output *text* — it can say
"add" but can't run `add`. The registry exists as the bridge: a
lookup table from the name string the model produced to the
callable your code executes.

**Where it's used:** This is literally how OpenAI/Anthropic
"function calling" works: you send the API a list of tool names +
signatures, the model replies `{"name": "add", "args": [3, 5]}`,
YOUR code does `tools["add"](3, 5)`. The registry is the bridge.

**What goes wrong without it:** Hardcode tool logic inside the
agent → adding a tool means editing agent code, and the agent
bloats into a god-function. The classic trap: store the FUNCTION,
not its result — `{"add": add}` (callable) vs `{"add": add(2,3)}`
(already-run result 5). Store the result and
`tools["add"](4, 7)` crashes with `TypeError: 'int' object is not
callable`.

**Worked example:**
```python
tools = {
    "add":      lambda a, b: a + b,
    "multiply": lambda a, b: a * b,
    "weather":  lambda city: f"Weather in {city}: sunny",
}

tools["add"](3, 5)          # 8
tools["multiply"](4, 7)     # 28
tools["weather"]("Mumbai")  # "Weather in Mumbai: sunny"
```
The agent never contains tool logic itself — it just holds names
and looks them up.

**Code:**
```python
def build_tools():
    return {
        "add":      lambda a, b: a + b,
        "multiply": lambda a, b: a * b,
        "weather":  lambda city: f"Weather in {city}: sunny",
    }
```

**Expected output:**
```
tools["add"](3, 5)         → 8
tools["multiply"](4, 7)    → 28
tools["weather"]("Mumbai") → "Weather in Mumbai: sunny"
```

---

### 3. The ReAct Loop — `p03`

**What it is:** ReAct = **Rea**soning + **Act**ing. Instead of
answering in one shot, the agent cycles through three phases:
- **THINK** — reason about what to do next
- **ACT** — call a tool
- **OBSERVE** — read the tool's result

...then loop back to THINK with the new information until done.

**Why it exists:** One-shot answering can't use tool results —
the model would have to guess what the tool returned. The loop
exists so each iteration knows more than the last: the OBSERVE
result becomes part of the next THINK's context, which is what
lets an agent correct itself mid-task instead of blindly
continuing.

**Where it's used:** ReAct is the canonical agent pattern (from a
2022 paper). AutoGPT, LangChain agents, Claude Code, and Devin all
run this loop — if OBSERVE shows an error, the next THINK plans
around it.

**What goes wrong without it:** No loop → the agent calls a tool
once and can't react to the result — a failed search ends the
task with no retry. ReAct is a LOOP, not a fixed script: real
versions repeat until a "done" condition. And without a max-
iterations cap, a stuck agent loops forever burning API calls.
A single THINK→ACT is just tool calling; the *cycling* is what
makes it ReAct.

**Worked example:** goal = "calculate 6 * 7"
```
loop 1:
  THINK:   I need to calculate 6 * 7
  ACT:     Use calculator tool
  OBSERVE: Result is 42

loop 2:
  THINK:   I have the answer
  ACT:     Return 42
```

**Code:**
```python
def react_loop(goal):
    expr = goal.replace("calculate", "").strip()   # "6 * 7"
    print(f"THINK: I need to calculate {expr}")
    print("ACT: Use calculator tool")
    result = eval(expr)
    print(f"OBSERVE: Result is {result}")
    print("THINK: I have the answer")
    print(f"ACT: Return {result}")
    return result
```

**Expected output:** `react_loop("calculate 6 * 7")` prints
```
THINK: I need to calculate 6 * 7
ACT: Use calculator tool
OBSERVE: Result is 42
THINK: I have the answer
ACT: Return 42
```
and returns `42`.

---

## Medium

### 4. Tool-Calling Agent — `p01`

**What it is:** Combine the previous two concepts into one working
agent: parse the task → pick the tool → extract the arguments →
call it → return `(tool_name, result)`. This is the complete
"one-shot agent" — decide AND execute.

**Why it exists:** A decision without execution does nothing — the
registry and the router are useless until something parses a task
into `(tool, args)` and runs it. This layer exists as the
execution half of function calling.

**Where it's used:** When a real LLM outputs
`{"tool": "multiply", "args": {"a": 4, "b": 7}}`, production code
does EXACTLY this: validate the name, extract args, call, return.

**What goes wrong without it:** `tools[parts[0]]` on an unknown
tool name → `KeyError` crash — validate first. And return
`(name, result)`, not just `result`: callers need to know WHICH
tool ran for logging, debugging, and the observe step. Silent
execution hides errors — when the answer is wrong you can't tell
whether the tool or the parsing failed.

**Worked example:**
```python
run_agent("add 2 and 3")
  # parse: tool="add", args=[2, 3]
  # → ("add", 5)

run_agent("multiply 4 and 7")
  # parse: tool="multiply", args=[4, 7]
  # → ("multiply", 28)

run_agent("weather Mumbai")
  # parse: tool="weather", args=["Mumbai"]
  # → ("weather", "Weather in Mumbai: sunny")
```
Three pieces of parsing: the tool keyword, the numbers/city, and
filtering filler words like "and".

**Code:**
```python
def run_agent(task):
    tools = build_tools()
    parts = task.split()
    if parts[0] == "weather":
        return ("weather", tools["weather"](parts[1]))
    nums = [int(w) for w in parts if w.isdigit()]
    return (parts[0], tools[parts[0]](*nums))
```

**Expected output:**
```
run_agent("add 2 and 3")      → ("add", 5)
run_agent("multiply 4 and 7") → ("multiply", 28)
run_agent("weather Mumbai")   → ("weather", "Weather in Mumbai: sunny")
```

---

### 5. Multi-Step Planner — `p02`

**What it is:** Complex goals can't be done in one tool call. A
**planner** takes the goal and outputs an *ordered list of steps*
before executing anything. Plan first, act second — like writing
an outline before the essay.

**Why it exists:** LLMs are bad at "do 10 things at once" but good
at "do the next one thing." Planning exists to decompose a fuzzy
big goal into a checklist the agent can grind through — it's why
agents can handle hour-long tasks without losing the thread.

**Where it's used:** Frameworks call this "task decomposition" —
it's the front-end of every long-running agent system.

**What goes wrong without it:** No plan → the agent attacks a big
goal in one shot → half-finishes, loses track of what it already
did, misses required parts (the completeness axis in hard/p02
catches exactly this). And a plan is NOT executed code — it's a
list of *intentions*. The planner says WHAT to do in order; a
separate executor decides HOW. Try to run the plan inside `plan()`
and you've mixed the two layers.

**Worked example:**
```python
plan("research AI trends") →
    ["Search for information",
     "Read and summarize",
     "Write report"]

plan("solve this math problem") →
    ["Break down the problem",
     "Solve each part",
     "Combine answers"]
```
Each step in the list becomes its own ReAct loop or tool call when
executed.

**Code:**
```python
def plan(goal):
    g = goal.lower()
    if "research" in g:
        return ["Search for information", "Read and summarize",
                "Write report"]
    if "solve" in g:
        return ["Break down the problem", "Solve each part",
                "Combine answers"]
    return ["Clarify the goal"]
```

**Expected output:**
```
plan("research AI trends")       → ["Search for information", "Read and summarize", "Write report"]
plan("solve this math problem")  → ["Break down the problem", "Solve each part", "Combine answers"]
plan("anything else")            → ["Clarify the goal"]
```

---

### 6. Agent Memory — `p03`

**What it is:** LLMs are stateless — every call forgets everything.
**Memory** = a store of facts the agent keeps and re-injects into
every prompt/response so it behaves as if it "remembers" the user.

**Why it exists:** Statelessness is an LLM feature (no hidden
state, reproducible) but a product bug — users expect continuity.
Memory exists as the external store that gets pasted into context
each call, giving the *illusion* of a model that remembers.

**Where it's used:** This is how ChatGPT's memory and every
"remember me" feature works — a store outside the model injected
into context. Agents also use it for working memory (results from
earlier steps) and long-term memory (user prefs).

**What goes wrong without it:** No memory → the agent asks your
name every session and re-derives step results it already
computed. The key misconception: memory is not magic persistence
inside the model — it's just data you re-send each time. If you
don't include a fact in the next call, the model truly does not
know it. And unbounded memory → the context window overflows, so
real systems summarize or retrieve relevant memories (level-12
RAG!).

**Worked example:**
```python
memory.add("User likes Python")
memory.add("User is learning ML")

respond("What should I learn next?")
→ "Based on [User likes Python | User is learning ML],
   here's my response to: What should I learn next?"
```
With a real LLM, those facts get pasted into the system prompt:
`"Facts about the user: likes Python, learning ML. Now answer: ..."`

**Code:**
```python
class AgentMemory:
    def __init__(self):
        self.facts = []

    def add(self, fact):
        self.facts.append(fact)

    def get_all(self):
        return self.facts

    def respond(self, question):
        joined = " | ".join(self.facts)
        return (f"Based on [{joined}], here's my response to: "
                f"{question}")
```

**Expected output:** After the two `add` calls,
`respond("What should I learn next?")` →
`"Based on [User likes Python | User is learning ML], here's my
response to: What should I learn next?"` and `get_all()` →
`["User likes Python", "User is learning ML"]`.

---

## Hard

### 7. Multi-Agent Systems — `p01`

**What it is:** Instead of one agent doing everything, build
several *specialized* agents — researcher, writer, reviewer — and
pass work between them. Each has a narrow role (and often its own
system prompt/persona), which makes each one's job easier.

**Why it exists:** One agent doing everything needs a bloated
prompt and produces shallow work in every area — the same reason
persona prompts help (level-11). Specialization exists because a
narrow role produces more focused, higher-quality output than "do
everything."

**Where it's used:** The pattern behind CrewAI, AutoGen, and
dev-team-style agents — a pipeline where researcher's notes feed
the writer, the writer's draft feeds the reviewer.

**What goes wrong without it:** Single mega-agent → role
confusion and generic output. But the opposite is also a trap:
multi-agent isn't automatically better — it multiplies cost,
latency, and failure points (each handoff can lose context). Use
it when tasks genuinely need different expertise, not as a default
architecture.

**Worked example:** task = "Write a blog post"
```
researcher(task) → "Working on Write a blog post"  # gathers info
writer(task)     → "Working on Write a blog post"  # drafts
reviewer(task)   → "Working on Write a blog post"  # checks quality

result = {"researcher": ..., "writer": ..., "reviewer": ...}
```
In a real pipeline the output CHAINS: researcher's notes feed the
writer, the writer's draft feeds the reviewer.

**Code:**
```python
def multi_agent(task):
    researcher = lambda t: f"Working on {t}"
    writer     = lambda t: f"Working on {t}"
    reviewer   = lambda t: f"Working on {t}"
    return {"researcher": researcher(task),
            "writer":     writer(task),
            "reviewer":   reviewer(task)}
```

**Expected output:** `multi_agent("Write a blog post")` →
```
{"researcher": "Working on Write a blog post",
 "writer":     "Working on Write a blog post",
 "reviewer":   "Working on Write a blog post"}
```

---

### 8. Agent Evaluation — `p02`

**What it is:** Score an agent on three axes, each 0-1:
- **Correctness** — did it produce the right output?
- **Efficiency** — did it use the minimum number of steps?
  (`min_steps / steps_used`, capped at 1.0)
- **Completeness** — did it cover all parts of the goal?
  (`covered_parts / total_parts`)

**Why it exists:** "The agent worked" is meaningless — agents can
be right-but-slow (burning money on 20 loops) or fast-but-half-
done. Separate axes exist so you know WHAT to fix: an agent
averaging 0.8 could be "great at everything" or "perfect but does
3× too many steps" — one number hides the difference.

**Where it's used:** Agent benchmarking and regression testing —
optimize the weakest axis, not the average.

**What goes wrong without it:** One overall score (or no score)
→ you ship agents that silently waste tokens or skip half the
task. An agent that's right but takes 20 loops burns money —
efficiency catches that. An agent that's fast but half-finishes is
useless — completeness catches that. Keep the three scores
separate.

**Worked example:**
```python
evaluate_agent("42", "42", steps_used=3, min_steps=3,
               covered_parts=2, total_parts=3)

correctness  = 1.0           # "42" == "42"
efficiency   = 3/3 = 1.0     # used exactly the minimum
completeness = 2/3 ≈ 0.67    # covered 2 of 3 required parts

→ {'correctness': 1.0, 'efficiency': 1.0, 'completeness': 0.67}
```
The agent got the right answer efficiently but MISSED a part of
the goal — the completeness score exposes that.

**Code:**
```python
def evaluate_agent(agent_output, expected, steps_used, min_steps,
                   covered_parts, total_parts):
    return {
        "correctness":  1.0 if agent_output == expected else 0.5,
        "efficiency":   min(1.0, min_steps / steps_used),
        "completeness": covered_parts / total_parts,
    }
```

**Expected output:** `evaluate_agent("42", "42", 3, 3, 2, 3)` →
`{"correctness": 1.0, "efficiency": 1.0, "completeness":
0.6666666666666666}`.

---

### 9. Autonomous Goal Decomposition — `p03`

**What it is:** The highest-level agent pattern: you give a vague
high-level goal ("build a website"), and the agent itself decides
WHAT steps to take — not just how to do a step you handed it.
Goal → agent-generated action list → then the planner/ReAct pieces
execute each action.

**Why it exists:** A hand-written planner only covers goals you
anticipated — novel goals hit a dead end. Decomposition exists so
the agent derives actions from the goal *type* itself: the model
is prompted "given this goal, list the next actions" and keeps
re-planning as observations come in. It's one step closer to true
autonomy.

**Where it's used:** This is the "A" in AutoGPT-style agents.
Everything in this level is a hand-rolled version of one stage of
that loop.

**What goes wrong without it:** Only-match-known-plans → an
unseen goal type returns "Clarify the goal" forever — the agent
can't start work on anything new. And keep the layers straight:
decomposition ≠ execution. The output is a list of action STRINGS
— actually doing them is the tool-calling agent (medium/p01)
running inside a ReAct loop (easy/p03). These three pieces stack:
decompose → per action, loop think/act/observe → call tools.
Skip the wiring and your "autonomous agent" just prints a todo
list.

**Worked example:**
```python
autonomous_agent("research a topic and write a summary")
→ ["search for information", "analyze results", "summarize findings"]

autonomous_agent("build an app")
→ ["plan structure", "write code", "test it"]

autonomous_agent("analyze sales data")
→ ["collect data", "run analysis", "report results"]
```
Notice the difference from medium/p02: the planner matched a
*known* goal to a *known* plan. Here the agent derives actions from
the goal type itself — one step closer to true autonomy.

**Code:**
```python
def autonomous_agent(goal):
    g = goal.lower()
    if "research" in g:
        return ["search for information", "analyze results",
                "summarize findings"]
    if "build" in g:
        return ["plan structure", "write code", "test it"]
    if "analyze" in g:
        return ["collect data", "run analysis", "report results"]
    return ["break goal into sub-goals"]
```

**Expected output:**
```
autonomous_agent("research a topic and write a summary")
    → ["search for information", "analyze results", "summarize findings"]
autonomous_agent("build an app")
    → ["plan structure", "write code", "test it"]
autonomous_agent("analyze sales data")
    → ["collect data", "run analysis", "report results"]
autonomous_agent("something novel")
    → ["break goal into sub-goals"]
```

---

## Done with concepts? → Try `easy/p01-agent-decision.py`
