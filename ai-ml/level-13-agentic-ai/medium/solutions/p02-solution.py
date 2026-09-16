"""Level 13 Agentic Ai — Medium P02 Solution"""

def solve():
    class PlanningAgent:
        def plan(self, goal):
            if 'research' in goal.lower():
                return [
                    '1. Search for information',
                    '2. Read and summarize',
                    '3. Write report'
                ]
            elif 'build' in goal.lower():
                return [
                    '1. Design the system',
                    '2. Write code',
                    '3. Test and debug'
                ]
            return ['1. Analyze the task']
        def execute_plan(self, plan):
            for step in plan:
                print(f"Executing: {step}")
            return "Plan completed"
    agent = PlanningAgent()
    plan = agent.plan("Research AI trends")
    agent.execute_plan(plan)
    return agent

if __name__ == "__main__":
    solve()