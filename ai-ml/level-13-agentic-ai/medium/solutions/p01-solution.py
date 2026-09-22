"""Level 13 — Agentic AI — Medium P01 Solution"""

def run_agent(task):
    tools = {
        "add": lambda a, b: a + b,
        "multiply": lambda a, b: a * b,
        "weather": lambda city: f"Weather in {city}: sunny"
    }
    parts = task.split()
    if "add" in parts:
        a, b = int(parts[1]), int(parts[3])
        return ("add", tools["add"](a, b))
    elif "multiply" in parts:
        a, b = int(parts[1]), int(parts[3])
        return ("multiply", tools["multiply"](a, b))
    elif "weather" in parts:
        return ("weather", tools["weather"](parts[1]))
    return ("unknown", None)

if __name__ == "__main__":
    print(run_agent("add 2 and 3"))
    print(run_agent("multiply 4 and 7"))
    print(run_agent("weather Mumbai"))
