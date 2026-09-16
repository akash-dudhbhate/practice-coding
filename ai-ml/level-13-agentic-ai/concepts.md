# Level 13 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept has:
what it is in plain words → a worked example with real numbers →
why ML cares → the code → what confuses beginners.

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

**Worked example:**
```python
agent_decide("calculate 6 * 7")     → "use calculator"
agent_decide("search for AI news")  → "use search"
agent_decide("write a report")      → "use writer"
agent_decide("cook dinner")         → "unknown goal"   # no tool fits
```
Notice the last line: a good agent KNOWS when it can't help —
an "I don't know" path is a required feature, not a bug.

**Why ML cares:** This routing decision is the first thing every
agent framework implements. With a real LLM, the model reads the
goal plus a list of tool descriptions and outputs the tool name —
the if/elif you're writing is the "compiler's view" of that.

**Code:**
```python
def agent_decide(goal):
    g = goal.lower()
    if "calculate" in g: return "use calculator"
    if "search" in g:    return "use search"
    if "write" in g:     return "use writer"
    return "unknown goal"
```

**Common confusion:** Decision is not execution. This function
returns a STRING naming the tool — actually *calling* the tool is a
separate step (medium/p01). Mixing them makes agents impossible to
debug.

---

### 2. Tool Registry — `p02`

**What it is:** A dict mapping `name → function`. The agent's
"toolbox." It picks a tool by name (a string from the decision
step), looks it up in the registry, and calls it. This is how an
LLM's text output becomes real code execution.

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

**Why ML cares:** This is literally how OpenAI/Anthropic "function
calling" works: you send the API a list of tool names + signatures,
the model replies `{"name": "add", "args": [3, 5]}`, YOUR code does
`tools["add"](3, 5)`. The registry is the bridge.

**Code:**
```python
def build_tools():
    return {
        "add":      lambda a, b: a + b,
        "multiply": lambda a, b: a * b,
        "weather":  lambda city: f"Weather in {city}: sunny",
    }
```

**Common confusion:** Store the FUNCTION, not its result.
`{"add": add}` (callable) vs `{"add": add(2,3)}` (already-run
result 5). You want to call it later with whatever args the task
needs.

---

### 3. The ReAct Loop — `p03`

**What it is:** ReAct = **Rea**soning + **Act**ing. Instead of
answering in one shot, the agent cycles through three phases:
- **THINK** — reason about what to do next
- **ACT** — call a tool
- **OBSERVE** — read the tool's result

...then loop back to THINK with the new information until done.

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
The key trick: the OBSERVE result becomes part of the next THINK's
context — each loop iteration knows more than the last.

**Why ML cares:** ReAct is the canonical agent pattern (from a 2022
paper). AutoGPT, LangChain agents, Claude Code, and Devin all run
this loop. The reason it works: the model can correct itself —
if OBSERVE shows an error, the next THINK plans around it instead
of blindly continuing.

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

**Common confusion:** ReAct is a LOOP, not a fixed script — real
versions repeat until a "done" condition (max iterations or the
model says "final answer"). A single THINK→ACT is just tool calling;
the *cycling* is what makes it ReAct.

---

## Medium

### 4. Tool-Calling Agent — `p01`

**What it is:** Combine the previous two concepts into one working
agent: parse the task → pick the tool → extract the arguments →
call it → return `(tool_name, result)`. This is the complete
"one-shot agent" — decide AND execute.

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

**Why ML cares:** When a real LLM outputs
`{"tool": "multiply", "args": {"a": 4, "b": 7}}`, production code
does EXACTLY this: validate the name, extract args, call, return.
You're building the execution half of function calling.

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

**Common confusion:** Returning `(name, result)` not just `result`
matters — callers need to know WHICH tool ran (for logging,
debugging, and the observe step). Silent execution hides errors.

---

### 5. Multi-Step Planner — `p02`

**What it is:** Complex goals can't be done in one tool call. A
**planner** takes the goal and outputs an *ordered list of steps*
before executing anything. Plan first, act second — like writing
an outline before the essay.

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

**Why ML cares:** LLMs are bad at "do 10 things at once" but good
at "do the next one thing." Planning turns a fuzzy big goal into a
checklist the agent can grind through. Frameworks call this
"task decomposition" — it's why agents can handle hour-long tasks.

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

**Common confusion:** A plan is NOT executed code — it's a list of
*intentions*. The planner says WHAT to do in order; a separate
executor decides HOW each step happens. Don't try to run the plan
inside `plan()`.

---

### 6. Agent Memory — `p03`

**What it is:** LLMs are stateless — every call forgets everything.
**Memory** = a store of facts the agent keeps and re-injects into
every prompt/response so it behaves as if it "remembers" the user.

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

**Why ML cares:** This is how ChatGPT's memory, and every
"remember me" feature, works — a store outside the model that gets
injected into context. Agents also use it for working memory
(results from earlier steps) and long-term memory (user prefs).

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

**Common confusion:** Memory is not magic persistence inside the
model — it's just data you re-send each time. If you don't include
a fact in the next call, the model truly does not know it.

---

## Hard

### 7. Multi-Agent Systems — `p01`

**What it is:** Instead of one agent doing everything, build
several *specialized* agents — researcher, writer, reviewer — and
pass work between them. Each has a narrow role (and often its own
system prompt/persona), which makes each one's job easier.

**Worked example:** task = "Write a blog post"
```
researcher(task) → "Working on Write a blog post"  # gathers info
writer(task)     → "Working on Write a blog post"  # drafts
reviewer(task)   → "Working on Write a blog post"  # checks quality

result = {"researcher": ..., "writer": ..., "reviewer": ...}
```
In a real pipeline the output CHAINS: researcher's notes feed the
writer, the writer's draft feeds the reviewer.

**Why ML cares:** This is the pattern behind CrewAI, AutoGen, and
dev-team-style agents. Specialization helps for the same reason
persona prompts help (level-11): a narrow role produces more
focused, higher-quality output than "do everything."

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

**Common confusion:** Multi-agent isn't automatically better — it
multiplies cost, latency, and failure points. Use it when tasks
genuinely need different expertise, not as a default architecture.

---

### 8. Agent Evaluation — `p02`

**What it is:** Score an agent on three axes, each 0-1:
- **Correctness** — did it produce the right output?
- **Efficiency** — did it use the minimum number of steps?
  (`min_steps / steps_used`, capped at 1.0)
- **Completeness** — did it cover all parts of the goal?
  (`covered_parts / total_parts`)

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

**Why ML cares:** "The agent worked" is meaningless without these
axes. An agent that's right but takes 20 loops burns money;
efficiency catches that. An agent that's fast but half-finishes
is useless; completeness catches that.

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

**Common confusion:** One overall score hides problems. An agent
averaging 0.8 could be "great at everything" or "perfect but does
3× too many steps." Keep the three scores separate — optimize the
weakest one.

---

### 9. Autonomous Goal Decomposition — `p03`

**What it is:** The highest-level agent pattern: you give a vague
high-level goal ("build a website"), and the agent itself decides
WHAT steps to take — not just how to do a step you handed it.
Goal → agent-generated action list → then the planner/ReAct pieces
execute each action.

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

**Why ML cares:** This is the "A" in AutoGPT-style agents: the
model is prompted "given this goal, list the next actions" and
keeps re-planning as observations come in. Everything in this
level is a hand-rolled version of one stage of that loop.

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

**Common confusion:** Decomposition ≠ execution. The output is a
list of action STRINGS — actually doing them is the job of the
tool-calling agent (medium/p01) running inside a ReAct loop
(easy/p03). These three pieces stack: decompose → per action,
loop think/act/observe → call tools.

---

## Done with concepts? → Try `easy/p01-agent-decision.py`
