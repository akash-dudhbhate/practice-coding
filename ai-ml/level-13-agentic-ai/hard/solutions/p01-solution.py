"""Level 13 — Agentic AI — Hard P01 Solution"""

def multi_agent(task):
    return {
        "researcher": f"Working on {task}",
        "writer": f"Working on {task}",
        "reviewer": f"Working on {task}"
    }

if __name__ == "__main__":
    r = multi_agent("Write a blog post")
    for role, output in r.items():
        print(f"{role} ({role}): {output}")
