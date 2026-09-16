"""Level 13 Agentic Ai — Medium P01 Solution"""

def solve():
    class MultiToolAgent:
        def __init__(self):
            self.tools = {
                'search': lambda q: f"Results for: {q}",
                'calculator': lambda x: eval(x),
                'translator': lambda t, lang: f"Translated '{t}' to {lang}"
            }
        def plan(self, task):
            if 'calculate' in task.lower():
                return ['calculator']
            elif 'search' in task.lower():
                return ['search']
            elif 'translate' in task.lower():
                return ['translator']
            return []
        def execute(self, task):
            tools_needed = self.plan(task)
            results = []
            for tool in tools_needed:
                if tool == 'calculator':
                    results.append(self.tools[tool]('2 + 2'))
                elif tool == 'search':
                    results.append(self.tools[tool](task))
                elif tool == 'translator':
                    results.append(self.tools[tool](task, 'Spanish'))
            return results
    agent = MultiToolAgent()
    print(agent.execute("Calculate 5 * 5"))
    print(agent.execute("Search for AI news"))
    return agent

if __name__ == "__main__":
    solve()