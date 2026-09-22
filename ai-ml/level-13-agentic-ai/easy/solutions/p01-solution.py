"""Level 13 — Agentic AI — Easy P01 Solution"""

def agent_decide(goal):
    g = goal.lower()
    if "calculate" in g:
        return "use calculator"
    elif "search" in g:
        return "use search"
    elif "write" in g:
        return "use writer"
    return "unknown goal"

if __name__ == "__main__":
    print(agent_decide("calculate 6 * 7"))
    print(agent_decide("search for AI news"))
    print(agent_decide("write a report"))
    print(agent_decide("cook dinner"))
