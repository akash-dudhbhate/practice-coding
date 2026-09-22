# Level 13 — Agentic AI

> **Math level:** 10th grade is enough. See [MATH-YOU-NEED.md](../MATH-YOU-NEED.md) — it explains every symbol used here.

## What You'll Learn
- Agent decision-making — pick the right tool for the goal
- Tool registry — a dict of functions the agent can call
- ReAct pattern — Think → Act → Observe loop
- Tool-calling agent — decide → execute → return result
- Multi-step planning — decompose goals into ordered actions
- Agent memory — store facts across interactions
- Multi-agent systems — specialized roles working together
- Agent evaluation — correctness, efficiency, completeness
- Autonomous goal decomposition

## Prerequisites
- Level 11 (prompt patterns)
- Level 12 (tool-like function calling)

## Problems

### Easy
1. `easy/p01-agent-decision.py` — `agent_decide()` → goal → tool name
2. `easy/p02-tool-registry.py` — `build_tools()` → callable tool dict
3. `easy/p03-react-loop.py` — `react_loop()` → Think→Act→Observe

### Medium
4. `medium/p01-tool-calling.py` — `run_agent()` → decide + execute
5. `medium/p02-planner.py` — `plan()` → multi-step plan
6. `medium/p03-agent-memory.py` — `AgentMemory` → persistent context

### Hard
7. `hard/p01-multi-agent.py` — `multi_agent()` → 3 specialized roles
8. `hard/p02-agent-eval.py` — `evaluate_agent()` → 3-metric scoring
9. `hard/p03-autonomous.py` — `autonomous_agent()` → goal → action list

### Project
`project/` — Build a multi-tool agent that can plan and execute.

## Verify

```bash
python3 check.py easy/p01
python3 check.py all
```
