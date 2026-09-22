"""Level 13 — Agentic AI — Hard P03 Solution"""

def autonomous_agent(goal):
    g = goal.lower()
    if "research" in g:
        return ["search for information", "analyze results", "summarize findings"]
    elif "build" in g:
        return ["plan structure", "write code", "test it"]
    elif "analyze" in g:
        return ["collect data", "run analysis", "report results"]
    return ["no plan found"]

if __name__ == "__main__":
    goal = "Research a topic and write a summary"
    print(f"Goal: {goal}")
    for i, action in enumerate(autonomous_agent(goal)):
        print(f"Action {i+1}: {action}")
