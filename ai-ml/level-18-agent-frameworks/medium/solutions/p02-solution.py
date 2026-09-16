"""Level 18 — Agent Frameworks — Medium P02 Solution"""

def conditional_router(state):
    """Look at the state, return the NAME of the next node.
    Error beats done — a crashed tool shouldn't 'finish' silently."""
    if state.get("error"):
        return "handle_error"
    if state.get("done"):
        return "finish"
    return "continue"

if __name__ == "__main__":
    print(conditional_router({"error": "tool crashed"}))   # handle_error
    print(conditional_router({"done": True}))              # finish
    print(conditional_router({"done": False, "step": 2}))  # continue
    print(conditional_router({}))                          # continue
    print(conditional_router({"error": "x", "done": True}))# handle_error
