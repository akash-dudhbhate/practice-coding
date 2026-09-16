"""Level 13 Agentic Ai — Hard P01 Solution"""

def solve():
    class Agent:
        def __init__(self, name, role):
            self.name = name
            self.role = role
        def work(self, task):
            return f"{self.name} ({self.role}): Working on {task}"
    class MultiAgentSystem:
        def __init__(self):
            self.agents = [
                Agent("Researcher", "gather info"),
                Agent("Writer", "create content"),
                Agent("Reviewer", "check quality")
            ]
        def collaborate(self, task):
            results = []
            for agent in self.agents:
                results.append(agent.work(task))
            return results
    system = MultiAgentSystem()
    results = system.collaborate("Write a blog post")
    for r in results:
        print(r)
    return system

if __name__ == "__main__":
    solve()