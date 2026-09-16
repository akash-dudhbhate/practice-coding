"""Level 13 Agentic Ai — Medium P03 Solution"""

def solve():
    class MemoryAgent:
        def __init__(self):
            self.memory = []
            self.context_window = 5
        def remember(self, info):
            self.memory.append(info)
            if len(self.memory) > self.context_window:
                self.memory.pop(0)
        def recall(self):
            return self.memory
        def respond(self, query):
            context = ' | '.join(self.memory[-3:])
            return f"Based on [{context}], here's my response to: {query}"
    agent = MemoryAgent()
    agent.remember("User likes Python")
    agent.remember("User is learning ML")
    agent.remember("User prefers examples")
    print(agent.respond("What should I learn next?"))
    return agent

if __name__ == "__main__":
    solve()