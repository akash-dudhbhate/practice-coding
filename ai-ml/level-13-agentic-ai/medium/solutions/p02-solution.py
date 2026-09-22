"""Level 13 — Agentic AI — Medium P02 Solution"""

def plan(goal):
    g = goal.lower()
    if "research" in g:
        return ["Search for information", "Read and summarize", "Write report"]
    elif "solve" in g:
        return ["Break down the problem", "Solve each part", "Combine answers"]
    return ["No plan found"]

if __name__ == "__main__":
    for s in plan("research AI trends"):
        print(f"Executing: {s}")
