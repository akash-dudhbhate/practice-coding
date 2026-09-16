"""Level 13 Agentic Ai — Easy P02 Solution"""

def solve():
    tools = {
        'add': {'description': 'Add two numbers', 'params': ['a', 'b']},
        'multiply': {'description': 'Multiply two numbers', 'params': ['a', 'b']},
        'get_weather': {'description': 'Get weather for a city', 'params': ['city']}
    }
    def call_tool(tool_name, **kwargs):
        if tool_name == 'add':
            return kwargs['a'] + kwargs['b']
        elif tool_name == 'multiply':
            return kwargs['a'] * kwargs['b']
        elif tool_name == 'get_weather':
            return f"Weather in {kwargs['city']}: sunny"
        return "Unknown tool"
    print(call_tool('add', a=5, b=3))
    print(call_tool('multiply', a=4, b=7))
    print(call_tool('get_weather', city='Mumbai'))
    return tools

if __name__ == "__main__":
    solve()