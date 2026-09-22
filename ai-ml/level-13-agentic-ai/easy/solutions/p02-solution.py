"""Level 13 — Agentic AI — Easy P02 Solution"""

def build_tools():
    return {
        "add": lambda a, b: a + b,
        "multiply": lambda a, b: a * b,
        "weather": lambda city: f"Weather in {city}: sunny"
    }

if __name__ == "__main__":
    tools = build_tools()
    print(tools["add"](3, 5))
    print(tools["multiply"](4, 7))
    print(tools["weather"]("Mumbai"))
