"""Level 13 — Agentic AI — Easy P03 Solution"""

def react_loop(goal):
    expr = goal.replace("calculate", "").strip()
    print(f"THINK: I need to {goal}")
    print(f"ACT: Use calculator tool")
    result = eval(expr)
    print(f"OBSERVE: Result is {result}")
    print(f"THINK: I have the answer")
    print(f"ACT: Return {result}")
    return result

if __name__ == "__main__":
    print(react_loop("calculate 6 * 7"))
