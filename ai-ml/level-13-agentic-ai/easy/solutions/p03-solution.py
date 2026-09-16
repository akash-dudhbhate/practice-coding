"""Level 13 Agentic Ai — Easy P03 Solution"""

def solve():
    class AgentLoop:
        def __init__(self):
            self.state = 'thinking'
            self.steps = []
        def run(self, task):
            self.steps.append(f"THINK: I need to {task}")
            self.steps.append(f"ACT: Use calculator tool")
            self.steps.append(f"OBSERVE: Result is 42")
            self.steps.append(f"THINK: I have the answer")
            self.steps.append(f"ACT: Return 42")
            return self.steps
    agent = AgentLoop()
    steps = agent.run("calculate 6 * 7")
    for step in steps:
        print(step)
    return steps

if __name__ == "__main__":
    solve()