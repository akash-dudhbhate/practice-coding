# Level 18 — Agent Frameworks (Graph-Based Agents)

> **Math level:** 10th grade is enough. See [MATH-YOU-NEED.md](../MATH-YOU-NEED.md) — it explains every symbol used here.

## What You'll Learn
- `State` — a dict-based container that tracks every write (`.history`)
- `Node` — a named function wrapper: `node(state) → new_state`
- `linear_graph()` — chain nodes in a fixed order
- `Graph` — nodes + edges + conditional edges = a real agent runtime
- `conditional_router()` — a function that picks the next node from state
- `build_agent_graph()` — assemble input → plan → execute → output
- `parallel_nodes()` — fan-out: run many nodes on the same state, merge results
- `self_correct_loop()` — retry-until-check-passes as a node
- `full_agent()` — parse → plan → tools → verify → respond in one graph

This is the LangGraph pattern: **nodes are actions, edges are decisions**,
state flows through the graph. Level 13 taught hand-rolled loops; here the
graph *is* the loop — you declare structure, the runtime walks it.

## Prerequisites
- Level 13 (agentic loops — ReAct, tools, memory)
- Level 11 (prompt patterns)

## Problems

### Easy
1. `easy/p01-state.py` — `State` → dict container with `.get`/`.set`/`.history`
2. `easy/p02-node.py` — `Node` → named callable: `node(state) → new_state`
3. `easy/p03-linear-graph.py` — `linear_graph(nodes)` → state→state pipeline

### Medium
4. `medium/p01-graph.py` — `Graph` → `.add_node`/`.add_edge`/`.add_conditional`/`.run`
5. `medium/p02-conditional-router.py` — `conditional_router(state)` → next node name
6. `medium/p03-build-agent-graph.py` — `build_agent_graph()` → 4-node Graph

### Hard
7. `hard/p01-parallel-nodes.py` — `parallel_nodes(nodes_dict)` → fan-out + merge
8. `hard/p02-self-correct-loop.py` — `self_correct_loop(check, fix, max)` → retry node
9. `hard/p03-full-agent.py` — `full_agent(task)` → parse→plan→tools→verify→respond

### Project
`project/` — Build a mini LangGraph: a router-driven agent graph with a
self-correction loop, all in pure Python.

## Verify

```bash
python3 check.py easy/p01
python3 check.py all
```
