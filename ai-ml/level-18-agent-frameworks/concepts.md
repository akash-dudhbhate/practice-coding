# Level 18 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept explains:
What it is · Why it exists · Where it's used · What goes wrong without
it · worked example · code · expected output.

## The Big Idea

```
Level 13:  while True: think → act → observe   (loop is handwritten)
Level 18:  graph.run(state)                    (loop is a STRUCTURE)
```

A graph agent = **nodes** (functions that transform state) + **edges**
(who runs next) + **conditional edges** (a function that looks at the
state and picks who runs next). The runtime walks the graph until a
node has no outgoing edge. This is exactly how LangGraph works — we
build a tiny version from scratch.

---

## Easy

### 1. State (the shared scratchpad) — `p01`

**What it is:** One dictionary-like object that flows through every
node of the graph. Nodes never call each other — they read from the
state and write results back into it. The "plan" node and the "tools"
node communicate only through this shared object.

**Why it exists:** Nodes need to communicate without calling each
other directly — direct calls would hard-wire the pipeline's shape
into the nodes themselves. Shared state was invented to decouple
them: each node is a pure state→state function, and the graph
structure (not the nodes) decides who runs when. The `.history`
list is the seed of "checkpointing": if the agent crashes at step 7,
you replay the writes and resume instead of restarting — and you
can audit every decision afterward.

**Where it's used:** How real agent frameworks pass context between
steps — LangGraph's `StateGraph`, Airflow's XCom, Temporal's
workflow state. Any multi-step system that needs crash-recovery or
audit trails.

**What goes wrong without it:**
- Nodes calling each other directly → changing the pipeline means
  editing every node's internals; the graph structure disappears
  into function calls.
- The INITIAL dict is not recorded in `.history` — history only
  tracks `.set()` calls made after construction. Beginners often
  log the initial state too and then wonder why tests see an extra
  entry.
- No shared state → no audit trail and no crash recovery: a dead
  agent restarts from zero and nobody can see what it decided.

**Worked example:**
```python
s = State({"task": "build a graph"})   # initial dict (not a "write")
s.set("plan", ["step1", "step2"])
s.set("step", 1)

s.get("task")            → "build a graph"
s.get("missing", "nope") → "nope"      # default when key absent
s.history                → [('plan', ['step1','step2']), ('step', 1)]
# history records every .set() in order — the initial dict doesn't count
```

**Code:**
```python
class State:
    def __init__(self, initial=None):
        self.data = dict(initial or {})
        self.history = []

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
        self.history.append((key, value))
```

**Expected output:**
```python
s = State({"task": "build a graph"})
s.set("plan", ["step1", "step2"]); s.set("step", 1)
s.get("task")            → "build a graph"
s.get("missing", "nope") → "nope"
s.history                → [('plan', ['step1','step2']), ('step', 1)]
```

---

### 2. Node (a named action) — `p02`

**What it is:** A node is the unit of work: a function that takes the
state dict in and returns a state dict out. We wrap it in a class
mainly to give it a NAME — so the graph can record "plan ran, then
execute ran."

```
state_in ──► ┌ NODE("shout") ┐ ──► state_out
```

**Why it exists:** Naming turns a pile of lambdas into a system you
can observe. When your agent does something weird at 3am, the trace
"parse → plan → tools → verify" is how you find the broken step —
impossible if the steps are anonymous functions.

**Where it's used:** Every framework does this: LangGraph nodes are
named functions, Airflow tasks have task_ids, CI pipelines name
their steps. Named steps are the precondition for tracing,
dashboards, and targeted retries.

**What goes wrong without it:**
- Anonymous lambdas → the trace shows `<lambda>` five times and
  there's no way to tell which step failed.
- A node function returns a NEW dict — typically `{**state, "key":
  new_val}` — rather than mutating the input. Mutating in place
  makes debugging and replaying much harder (you can't diff
  before/after if the "before" was overwritten).

**Worked example:**
```python
def shout(state):                          # dict in
    return {**state, "text": state["text"].upper()}   # dict out

n = Node("shout", shout)
n.name             → "shout"
n.run({"text": "hi"})  → {'text': 'HI'}
n({"text": "go"})      → {'text': 'GO'}   # callable — same as .run()
```

**Code:**
```python
class Node:
    def __init__(self, name, fn):
        self.name = name
        self.fn = fn

    def run(self, state):
        return self.fn(state)

    __call__ = run        # or: def __call__(self, s): return self.run(s)
```

**Expected output:**
```python
n = Node("shout", lambda s: {**s, "text": s["text"].upper()})
n.name                → "shout"
n.run({"text": "hi"}) → {'text': 'HI'}
n({"text": "go"})     → {'text': 'GO'}
```

---

### 3. Linear Graph (the simplest graph) — `p03`

**What it is:** A chain: node1's output feeds node2, node2's feeds
node3. No branches, no loops. And the deep insight: `linear_graph`
RETURNS a function — a graph built from nodes is itself just a
`state → state` function.

**Why it exists:** You need a way to compose nodes into pipelines
without a framework — the chain is the simplest composition. The
deeper reason it matters: because a graph is itself a `state →
state` function, a whole graph can be a NODE inside a bigger graph.
Function composition, applied to agents.

**Where it's used:** Frameworks composing sub-agents: your
"research agent" (a 5-node graph) becomes one node in the
"assistant" graph. Any sequential pipeline — ETL, preprocessing
chains, middleware.

**What goes wrong without it:**
- `linear_graph` returns a FUNCTION, not a result. You build the
  pipeline once (`pipe = linear_graph(...)`), then call it on
  different starting states. Calling it on a state directly
  (`linear_graph(nodes)(state)`) works but rebuilds the pipeline
  every call.
- Without composition you'd hand-wire each step's output to the
  next — every pipeline becomes bespoke glue code.

**Worked example:**
```python
add_one  = lambda s: {**s, "x": s["x"] + 1}
times_3  = lambda s: {**s, "x": s["x"] * 3}
minus_2  = lambda s: {**s, "x": s["x"] - 2}

pipe = linear_graph([add_one, times_3, minus_2])
pipe({"x": 1})
  → add_one:  {"x": 2}
  → times_3:  {"x": 6}
  → minus_2:  {"x": 4}
  → {'x': 4}
```

**Code:**
```python
def linear_graph(nodes):
    def pipeline(state):
        for node in nodes:
            state = node(state)
        return state
    return pipeline
```

**Expected output:**
```python
pipe = linear_graph([add_one, times_3, minus_2])
pipe({"x": 1})    → {'x': 4}
pipe({"x": 10})   → {'x': 31}     # (10+1)*3-2
```

---

## Medium

### 4. The Graph Runtime — `p01`

**What it is:** A chain can't branch or loop. A Graph adds edges:
`add_edge(a, b)` = "after a, always run b"; `add_conditional(a, router)`
= "after a, ask router(state) who runs next." `run()` walks from the
first-registered node until it hits a node with no outgoing edge.

**Why it exists:** Real agent behavior isn't a straight line — it
branches on errors, loops on retries, exits early on success. Edges
and a walker were invented so the *shape* of the computation lives
in data (the graph) instead of being hard-coded in the nodes.
`max_steps` exists because a miswired conditional can loop forever —
a real risk once you add cycles (hard/p03).

**Where it's used:** This `run` loop IS an agent framework's engine.
LangGraph's `StateGraph.compile().invoke()` is the same walk:
execute node → consult conditional edges first → plain edges →
dead end means done.

**What goes wrong without it:**
- A miswired router pointing back to an earlier node → infinite
  loop → infinite API bill on a paid LLM. `max_steps` is the
  circuit breaker — never run a cyclic graph uncapped.
- Conditional edges take PRIORITY over plain edges from the same
  node — if you registered both, the router decides. Expecting the
  plain edge to fire anyway → the graph takes a path you didn't
  predict.
- "First node added = entry point" is a convention (LangGraph makes
  you call `set_entry_point` explicitly; we skip that step) — add
  nodes in a different order and a different node starts the walk.

**Worked example:**
```python
g = Graph()
g.add_node("start", lambda s: {**s, "n": s["n"] + 1})   # entry point
g.add_node("big",   lambda s: {**s, "label": "big"})
g.add_node("small", lambda s: {**s, "label": "small"})
g.add_conditional("start", lambda s: "big" if s["n"] > 5 else "small")

g.run({"n": 10}):
  "start" runs → {"n": 11}  → router sees n=11 → "big"
  "big" runs   → {"n": 11, "label": "big"}  → no outgoing edge → STOP

g.run({"n": 1}):
  "start" → {"n": 2} → router: 2 > 5? no → "small" → STOP
```

**Code:**
```python
def run(self, state, max_steps=100):
    current = self.entry               # first node added
    steps = 0
    while current is not None:
        steps += 1
        if steps > max_steps:
            raise RuntimeError("max steps exceeded")
        state = self.nodes[current](state)
        if current in self.conditionals:
            current = self.conditionals[current](state)  # router picks
        elif current in self.edges:
            current = self.edges[current]
        else:
            current = None             # terminal node
    return state
```

**Expected output:**
```python
g.run({"n": 10})   → {'n': 11, 'label': 'big'}
g.run({"n": 1})    → {'n': 2, 'label': 'small'}
```

---

### 5. Conditional Router (the decision function) — `p02`

**What it is:** A plain function `state → "node_name"`. It never
modifies the state — it just LOOKS at it and returns the name of the
next node. This one mechanism is how agents branch.

**Why it exists:** Routing decisions need a place to live — putting
"who runs next" inside nodes would hard-wire the pipeline again.
The router was invented as a read-only observer: it inspects state
and names the next node, keeping branching logic separate from the
work itself.

**Where it's used:** Almost every "agentic" behavior is one router:
```
  tool selection:   state["kind"] == "math"  → "calc_node"
  error handling:   "error" in state         → "handle_error"
  retry loops:      not state["verified"]    → "tools"   (back edge!)
  human gates:      state["needs_approval"]  → "ask_human"
```
The LLM in a real agent often just fills in the keys the router
reads.

**What goes wrong without it:**
- Check `state.get("error")` (truthy) not `"error" in state` — a
  key present but set to `None`/`""` shouldn't trigger error
  handling. Presence-vs-truthiness bugs route healthy runs to the
  error path.
- Order matters: error beats done. Checking `done` first → a
  crashed run that also set done=True exits "successfully" and
  swallows the failure.
- A router that WRITES state → invisible side-effects between
  nodes: the trace can't explain why state changed.

**Worked example:**
```python
conditional_router({"error": "tool crashed"}) → "handle_error"
conditional_router({"done": True})            → "finish"
conditional_router({"done": False, "step": 2}) → "continue"
conditional_router({})                        → "continue"

# "error" is checked FIRST — a crashed run that also set done=True
# must still route to handle_error.
```

**Code:**
```python
def conditional_router(state):
    if state.get("error"):
        return "handle_error"
    if state.get("done"):
        return "finish"
    return "continue"
```

**Expected output:**
```python
conditional_router({"error": "tool crashed"})     → "handle_error"
conditional_router({"done": True})                → "finish"
conditional_router({"done": False, "step": 2})    → "continue"
conditional_router({})                            → "continue"
```

---

### 6. The Canonical Agent Graph — `p03`

**What it is:** The standard four-node pipeline every agent framework
tutorial builds: `input → plan → execute → output`. Each node also
appends its name to `state["trace"]` — a free execution log.

**Why it exists:** Understand → decide → act → format is the
skeleton under every agent — the pipeline exists because that
sequence is universal. The `trace` list exists because debugging an
agent requires knowing which nodes actually ran — observability for
free.

**Where it's used:** From AutoGPT to LangGraph examples, this
skeleton recurs everywhere. Production frameworks ship whole
tracing dashboards (LangSmith, Langfuse) for exactly this data.

**What goes wrong without it:**
- Nodes read keys written by EARLIER nodes (`execute` reads
  `s["input"]` that `input` wrote). If the trace shows `execute`
  ran but you get `KeyError: 'input'`, you probably skipped the
  `input` node's write — check the trace, it tells you what ran.
- Without a trace, a wrong result is a mystery — you can't tell
  whether `plan` ran, was skipped, or produced garbage.

**Worked example:**
```python
g = build_agent_graph()
g.run({"task": "summarize notes"})

node-by-node:
  "input":   state["input"]  = "summarize notes"     trace=["input"]
  "plan":    state["plan"]   = ["step1", "step2"]    trace+=[ "plan"]
  "execute": state["result"] = "executed: summarize notes"  trace+=...
  "output":  state["output"] = state["result"]       trace+=["output"]

final state:
  trace  = ['input', 'plan', 'execute', 'output']
  output = 'executed: summarize notes'
```

**Code:**
```python
def build_agent_graph():
    g = Graph()
    def traced(name, fn):
        def node(s):
            s = dict(s)
            s["trace"] = s.get("trace", []) + [name]
            return fn(s)
        return node

    g.add_node("input", traced("input",
        lambda s: {**s, "input": s["task"]}))
    g.add_node("plan", traced("plan",
        lambda s: {**s, "plan": ["step1", "step2"]}))
    g.add_node("execute", traced("execute",
        lambda s: {**s, "result": f"executed: {s['input']}"}))
    g.add_node("output", traced("output",
        lambda s: {**s, "output": s["result"]}))
    g.add_edge("input", "plan")
    g.add_edge("plan", "execute")
    g.add_edge("execute", "output")
    return g
```

**Expected output:**
```python
g = build_agent_graph()
final = g.run({"task": "summarize notes"})
final["trace"]    → ['input', 'plan', 'execute', 'output']
final["output"]   → 'executed: summarize notes'
```

---

## Hard

### 7. Parallel Nodes (fan-out / fan-in) — `p01`

**What it is:** Run several nodes on the SAME input at once (fan-out),
then merge their outputs into one state (fan-in). Each branch gets a
COPY — branches can't see each other's writes, since conceptually
they run at the same time.

```
    ┌──► node_a ──┐
in ─┼──► node_b ──┼──► merged_state
    └──► node_c ──┘
```

**Why it exists:** Real agents call several tools at once — parallel
web searches, parallel code checks, map-reduce over subtasks.
Fan-out/fan-in was invented to express that concurrency. The copy
rule exists because parallel branches shouldn't see each other's
partial writes; merge order = dict order, later branches win on
conflict — that's how real frameworks resolve collisions
deterministically.

**Where it's used:** LangGraph's `Send`/join pattern, parallel tool
calls in agent APIs, map-reduce pipelines.

**What goes wrong without it:**
- Passing the SAME dict to every branch instead of `dict(state)`
  copies: then branch b sees branch a's writes, the "parallel"
  behavior depends on iteration order, and conflicts become
  nondeterministic — exactly what the copy rule prevents.
- Sequential-only execution → 3 API calls take 3× the latency for
  no benefit; fan-out is how you parallelize I/O-bound agent work.

**Worked example:**
```python
p = parallel_nodes({
    "a": lambda s: {"x": s["n"] + 1},
    "b": lambda s: {"y": s["n"] * 10},
})
out = p({"n": 5})

branch a on copy {"n":5} → {"x": 6}
branch b on copy {"n":5} → {"y": 50}     # b never saw a's "x"

merge: out = {"n": 5, "x": 6, "y": 50}
       out["results"] = {"a": {"x": 6}, "b": {"y": 50}}
       out["trace"]   = ["parallel"]
```

**Code:**
```python
def parallel_nodes(nodes_dict):
    def parallel(state):
        merged = dict(state)
        results = {}
        for name, fn in nodes_dict.items():
            out = fn(dict(state))        # each branch gets a COPY
            results[name] = out
            merged.update(out)           # fan-in merge
        merged["results"] = results
        merged["trace"] = merged.get("trace", []) + ["parallel"]
        return merged
    return parallel
```

**Expected output:**
```python
p = parallel_nodes({"a": lambda s: {"x": s["n"] + 1},
                    "b": lambda s: {"y": s["n"] * 10}})
p({"n": 5})
# → {"n": 5, "x": 6, "y": 50,
#    "results": {"a": {"x": 6}, "b": {"y": 50}},
#    "trace": ["parallel"]}
```

---

### 8. Self-Correct Loop (retry until good) — `p02`

**What it is:** Agents produce garbage sometimes. The fix pattern:
produce → verify → if bad, loop back and fix, up to a hard cap.
As a reusable node: keep calling `fix_fn` until `check_fn(state)`
passes or `max_iters` is hit.

**Why it exists:** One-shot generation is unreliable — the
verify-and-retry cycle was invented so imperfect outputs get a
bounded chance to improve. In graph terms this is a `verify` node
with a conditional edge back to `fix` — a CYCLE. Cycles are what
make agent graphs more powerful than pipelines (DAGs can't loop).
The cap exists because an uncapped retry loop on a paid LLM API is
an infinite bill.

**Where it's used:** Self-correction in every agent framework —
code-generation loops (write → run → fix errors), RAG
re-retrieval, LLM-judge verification loops.

**What goes wrong without it:**
- Check BEFORE the first fix (`while not check... and iters <
  max`), not fix-then-check. If the input already passes, zero
  fixes should run — `iterations: 0, ok: True`. Fix-first wastes a
  call and could break an already-good state.
- No cap → a permanently-failing check loops forever, burning API
  calls until someone kills the process.
- No verify step at all → garbage output ships downstream
  unchecked; the loop is what catches it.

**Worked example:**
```python
needs_3 = lambda s: s.get("x", 0) >= 3
bump    = lambda s: {**s, "x": s.get("x", 0) + 1}

self_correct_loop(needs_3, bump, max_iters=10)({"x": 0})
  check: x=0 <3 → fix → x=1 → fix → x=2 → fix → x=3 → check ✓
  → {'x': 3, 'iterations': 3, 'ok': True}

self_correct_loop(needs_3, bump, max_iters=2)({"x": 0})
  fix → x=1 → fix → x=2 → cap hit, stop even though check fails
  → {'x': 2, 'iterations': 2, 'ok': False}
```

**Code:**
```python
def self_correct_loop(check_fn, fix_fn, max_iters):
    def node(state):
        iters = 0
        while not check_fn(state) and iters < max_iters:
            state = fix_fn(state)
            iters += 1
        state["iterations"] = iters
        state["ok"] = bool(check_fn(state))
        return state
    return node
```

**Expected output:**
```python
self_correct_loop(needs_3, bump, max_iters=10)({"x": 0})
# → {'x': 3, 'iterations': 3, 'ok': True}
self_correct_loop(needs_3, bump, max_iters=2)({"x": 0})
# → {'x': 2, 'iterations': 2, 'ok': False}
self_correct_loop(needs_3, bump, max_iters=10)({"x": 5})
# → {'x': 5, 'iterations': 0, 'ok': True}   # already good, 0 fixes
```

---

### 9. Full Agent (parse → plan → tools → verify → respond, with a cycle) — `p03`

**What it is:** Everything assembled: a five-node graph where
`verify`'s conditional edge either exits to `respond` or loops BACK
to `tools` for a retry. That one router function IS the agent's
self-correction.

```
parse ──► plan ──► tools ──► verify ──► respond
                     ▲          │
                     └─ retry ──┘   (if not verified and attempts < 2)
```

**Why it exists:** This is the complete agentic loop that
production frameworks sell: deterministic tools + a verify gate +
bounded retry. It exists because one-shot agents fail too often to
ship — the retry back-edge plus the verify gate is what makes the
loop trustworthy. The math tool's char-whitelist + `eval` with
empty builtins is also the (tiny) version of real tool sandboxing —
never `eval` raw model output.

**Where it's used:** Production agent loops — the same structure
sits under LangGraph agents, AutoGPT-style loops, and
chat-with-tools products.

**What goes wrong without it:**
- The retry is a BACK-EDGE — a conditional edge pointing to an
  earlier node — which is why `max_steps` in `run()` matters:
  miswire it and the agent spins forever.
- Increment `attempts` inside the `tools` node, not in the router —
  routers should stay read-only observers of state; a counting
  router hides the retry bookkeeping from the trace.
- `eval` without the whitelist + empty builtins → a crafted
  expression like `__import__('os').system('rm -rf /')` runs raw —
  sandboxing is non-negotiable.
- No verify gate → tool failures pass straight to respond as if
  they succeeded.

**Worked example:**
```python
full_agent("calculate 6 * 7")
  parse:   "calculate" in task → kind="math", expr="6 * 7"
  plan:    plan = ["parse", "use math", "verify", "respond"]
  tools:   TOOLS["math"]("6 * 7") → 42, attempts=1, tool_result=42
  verify:  verified = (42 is not None) = True
  router:  verified → "respond"
  respond: response = "Result: 42"
  trace = ['parse','plan','tools','verify','respond']

full_agent("fly to the moon")
  parse:   no keyword → kind="unknown"
  tools:   no tool for unknown → tool_result=None, attempts=1
  verify:  verified=False → router: attempts<2 → back to "tools"
  tools:   attempts=2, still None
  verify:  still False → attempts==2 → "respond"
  respond: "Failed after 2 attempts"
```

**Code:**
```python
g.add_conditional("verify",
    lambda s: "tools" if (not s.get("verified")
                          and s.get("attempts", 0) < 2)
              else "respond")

def safe_eval(expr):
    if not all(c in "0123456789+-*/(). " for c in expr):
        return None
    try:
        return eval(expr, {"__builtins__": {}}, {})
    except Exception:
        return None
```

**Expected output:**
```python
full_agent("calculate 6 * 7")
# → "Result: 42"
#   trace: ['parse', 'plan', 'tools', 'verify', 'respond']

full_agent("fly to the moon")
# → "Failed after 2 attempts"
#   tools ran twice (the retry back-edge), then verify gave up

safe_eval("6 * 7")      → 42
safe_eval("open('x')")  → None   # non-whitelist chars rejected
```

---

## Done with concepts? → Try `easy/p01-state.py`
