"""Level 13 — Agentic AI — Medium P03 Solution"""

class AgentMemory:
    def __init__(self):
        self.facts = []

    def add(self, fact):
        self.facts.append(fact)

    def get_all(self):
        return self.facts

    def respond(self, question):
        mem = " | ".join(self.facts)
        return f"Based on [{mem}], here's my response to: {question}"

if __name__ == "__main__":
    m = AgentMemory()
    m.add("User likes Python")
    m.add("User is learning ML")
    m.add("User prefers examples")
    print(m.respond("What should I learn next?"))
