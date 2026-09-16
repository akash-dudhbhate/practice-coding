"""Level 13 Agentic Ai — Easy P01 Solution"""

def solve():
    class SimpleAgent:
        def __init__(self):
            self.tools = {
                'calculator': lambda x: eval(x),
                'greeter': lambda name: f"Hello, {name}!"
            }
        def use_tool(self, tool_name, *args):
            if tool_name in self.tools:
                return self.tools[tool_name](*args)
            return "Tool not found"
    agent = SimpleAgent()
    print(agent.use_tool('calculator', '2 + 2'))
    print(agent.use_tool('greeter', 'World'))
    return agent

if __name__ == "__main__":
    solve()