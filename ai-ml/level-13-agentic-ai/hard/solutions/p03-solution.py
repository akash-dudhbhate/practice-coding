"""Level 13 Agentic Ai — Hard P03 Solution"""

def solve():
    class AutonomousAgent:
        def __init__(self):
            self.steps_completed = 0
            self.max_steps = 10
        def think(self, state):
            if self.steps_completed == 0:
                return "search for information"
            elif self.steps_completed == 1:
                return "analyze results"
            elif self.steps_completed == 2:
                return "summarize findings"
            else:
                return "done"
        def act(self, action):
            self.steps_completed += 1
            return f"Action {self.steps_completed}: {action}"
        def run(self, goal):
            print(f"Goal: {goal}")
            state = "start"
            while self.steps_completed < self.max_steps:
                action = self.think(state)
                if action == "done":
                    break
                result = self.act(action)
                print(result)
            return f"Completed in {self.steps_completed} steps"
    agent = AutonomousAgent()
    agent.run("Research a topic and write a summary")
    return agent

if __name__ == "__main__":
    solve()