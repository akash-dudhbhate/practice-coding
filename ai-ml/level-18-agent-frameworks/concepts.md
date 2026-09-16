# Level 18 — Concepts Reference

## The Big Idea
```
Level 13:  while True: think → act → observe      (loop is handwritten)
Level 18:  graph.run(state)                       (loop is declared as structure)
```
A graph agent = **nodes** (functions that transform state) + **edges**
(who runs next) + **conditional edges** (a function decides who runs next).
The runtime walks the graph until it hits a node with no outgoing edge.
This is exactly how LangGraph, CrewAI flows, and most agent frameworks work.

## Easy

### State
- A shared dict that flows through the graph; every node reads/writes it
- `.history` records every `set()` — this is how frameworks do "checkpointing"
- Keep it a plain container: nodes stay simple, state carries context

### Node
- `Node(name, fn)` — a named wrapper so the graph can log/trace "who ran"
- Contract: `fn(state_dict) → new_state_dict`
- Making it callable (`__call__`) means a Node *is* a state→state function

### Linear Graph
- The simplest graph: a list of nodes run in order
- `linear_graph(nodes)` returns a `state → state` function — a graph is
  just a bigger node. This composability is the core insight.

## Medium

### Graph
- `add_node(name, fn)` registers an action
- `add_edge(a, b)` = "after a, always run b"
- `add_conditional(a, router)` = "after a, run `router(state)` → next name"
- `run(state)` = walk from entry node until a dead end (terminal node)
- First node added = entry point (same convention as LangGraph's set_entry_point)

### Conditional Router
- A plain function `state → "node_name"` — the *only* mechanism for branching
- `if "error" in state → "handle_error"` is the entire trick behind
  retry loops, tool selection, and human-in-the-loop gates

### Agent Graph (input→plan→execute→output)
- The canonical agent shape: understand → decide steps → act → format answer
- Each node appends its name to `state["trace"]` — free observability

## Hard

### Parallel Nodes
- Fan-out: every branch gets a **copy** of the input state (no interference)
- Fan-in: merge each branch's dict of updates back into one state
- This is LangGraph's `Send`/`join` pattern — run searches/tools in parallel

### Self-Correct Loop
- `while not check(state) and iters < max: state = fix(state)`
- In graph terms: a `verify` node + conditional edge back to `fix` — a *cycle*
- Cycles are what make graphs more powerful than pipelines (DAGs can't loop)

### Full Agent (parse→plan→tools→verify→respond)
- `verify`'s conditional edge either exits to `respond` or loops back to
  `tools` for a retry — the whole "agentic" behavior is one router function
- Deterministic tools keep it testable: math eval, fake search, echo
