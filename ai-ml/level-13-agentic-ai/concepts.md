# Level 13 — Concepts Reference

## Easy

### Agent Decision
- Agent = function that maps goal → action/tool
- Simplest form: if/elif on keywords

### Tool Registry
- Dict of name → function; agent picks by name, calls it
- This is the foundation of all agent frameworks

### ReAct
- Think (reason about next step) → Act (call tool) → Observe (see result) → repeat
- The core loop in AutoGPT, LangChain agents, etc.

## Medium

### Tool-Calling Agent
- Parse task → pick tool → call with args → return (name, result)
- Connects decision-making to actual execution

### Multi-Step Planner
- Break complex goals into ordered steps
- "research X" → search → read → write

### Agent Memory
- Store facts; include them in every response
- Gives the agent persistent context across interactions

## Hard

### Multi-Agent System
- Specialized agents (researcher, writer, reviewer) collaborate
- Each handles one aspect; results chain together

### Agent Evaluation
- correctness (right answer?), efficiency (min steps?), completeness (all parts?)
- Score each 0-1; optimize the weakest

### Autonomous Decomposition
- High-level goal → ordered action list
- The agent decides WHAT to do, not just HOW
