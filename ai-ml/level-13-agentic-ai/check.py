"""
Auto-Check System — Level 13 (Agentic AI)
===========================================
Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import os
import sys
import glob
import importlib.util


def load_module(filepath):
    spec = importlib.util.spec_from_file_location("solution", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _find_file(level_dir, level, num):
    num_clean = num.lstrip("p")
    filepath = os.path.join(level_dir, level, f"p{num_clean}-solve.py")
    if not os.path.exists(filepath):
        pattern = os.path.join(level_dir, level, f"p{num_clean}-*.py")
        matches = [f for f in glob.glob(pattern) if "solutions" not in f]
        if matches:
            filepath = matches[0]
    return filepath


def check_easy_p01(module):
    if not hasattr(module, 'agent_decide'):
        return False, "Function 'agent_decide' not found"
    cases = [
        ("calculate 6*7", "calculator"),
        ("search for news", "search"),
        ("write a report", "writer"),
        ("cook dinner", "unknown"),
    ]
    for goal, expected in cases:
        r = module.agent_decide(goal)
        if expected not in r.lower():
            return False, f"'{goal}': expected '{expected}', got '{r}'"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'build_tools'):
        return False, "Function 'build_tools' not found"
    tools = module.build_tools()
    if tools["add"](3, 5) != 8:
        return False, f"add(3,5) should be 8"
    if tools["multiply"](4, 7) != 28:
        return False, f"multiply(4,7) should be 28"
    if "Mumbai" not in tools["weather"]("Mumbai"):
        return False, "weather should include city name"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'react_loop'):
        return False, "Function 'react_loop' not found"
    result = module.react_loop("calculate 6 * 7")
    if result != 42:
        return False, f"Expected 42, got {result}"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'run_agent'):
        return False, "Function 'run_agent' not found"
    r1 = module.run_agent("add 2 and 3")
    if r1 != ("add", 5):
        return False, f"Expected ('add', 5), got {r1}"
    r2 = module.run_agent("multiply 4 and 7")
    if r2 != ("multiply", 28):
        return False, f"Expected ('multiply', 28), got {r2}"
    r3 = module.run_agent("weather Mumbai")
    if "Mumbai" not in r3[1]:
        return False, f"Expected weather for Mumbai, got {r3}"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'plan'):
        return False, "Function 'plan' not found"
    r = module.plan("research AI trends")
    if len(r) != 3:
        return False, f"Expected 3 steps, got {len(r)}"
    if 'search' not in r[0].lower():
        return False, f"First step should involve search, got '{r[0]}'"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'AgentMemory'):
        return False, "Class 'AgentMemory' not found"
    m = module.AgentMemory()
    m.add("User likes Python")
    m.add("User is learning ML")
    r = m.respond("What should I learn next?")
    if "Python" not in r or "ML" not in r:
        return False, f"Response should include memory facts, got '{r}'"
    if "What should I learn next?" not in r:
        return False, "Response should include the question"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'multi_agent'):
        return False, "Function 'multi_agent' not found"
    r = module.multi_agent("Write a blog post")
    if len(r) != 3:
        return False, f"Expected 3 agents, got {len(r)}"
    for role in ['researcher', 'writer', 'reviewer']:
        if role not in r:
            return False, f"Missing role: {role}"
        if 'blog post' not in r[role]:
            return False, f"{role} should reference the task"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'evaluate_agent'):
        return False, "Function 'evaluate_agent' not found"
    r = module.evaluate_agent("42", "42", 3, 3, 2, 3)
    if r['correctness'] != 1.0:
        return False, f"Expected correctness=1.0, got {r['correctness']}"
    if r['efficiency'] != 1.0:
        return False, f"Expected efficiency=1.0, got {r['efficiency']}"
    if abs(r['completeness'] - 0.6667) > 0.01:
        return False, f"Expected completeness~0.67, got {r['completeness']}"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'autonomous_agent'):
        return False, "Function 'autonomous_agent' not found"
    actions = module.autonomous_agent("research a topic and write a summary")
    if len(actions) != 3:
        return False, f"Expected 3 actions, got {len(actions)}"
    if 'search' not in actions[0].lower():
        return False, f"First action should be search, got '{actions[0]}'"
    return True, "All tests passed!"


CHECKS = {
    "easy/p01": check_easy_p01,
    "easy/p02": check_easy_p02,
    "easy/p03": check_easy_p03,
    "medium/p01": check_medium_p01,
    "medium/p02": check_medium_p02,
    "medium/p03": check_medium_p03,
    "hard/p01": check_hard_p01,
    "hard/p02": check_hard_p02,
    "hard/p03": check_hard_p03,
}


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 check.py <level>/<problem>")
        sys.exit(1)

    target = sys.argv[1]
    level_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(level_dir)

    if target == "all":
        print("=" * 60)
        print("  LEVEL 13 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id, check_func in CHECKS.items():
            level, num = check_id.split("/")
            filepath = _find_file(level_dir, level, num)
            if not os.path.exists(filepath):
                print(f"  {check_id}: FILE NOT FOUND")
                continue
            try:
                module = load_module(filepath)
                passed, msg = check_func(module)
                status = "PASS" if passed else "FAIL"
                print(f"  {check_id}: {status} — {msg}")
            except Exception as e:
                print(f"  {check_id}: ERROR — {e}")
        print("=" * 60)
        return

    level, num = target.split("/")
    check_id = f"{level}/{num}"
    if check_id not in CHECKS:
        print(f"Error: unknown problem '{check_id}'")
        sys.exit(1)

    filepath = _find_file(level_dir, level, num)
    if not os.path.exists(filepath):
        print(f"Error: file not found: {filepath}")
        sys.exit(1)

    try:
        module = load_module(filepath)
        passed, msg = CHECKS[check_id](module)
        if passed:
            print(f"PASS — {msg}")
            print(f"  Add '# DONE' to the first line of {filepath}")
        else:
            print(f"FAIL — {msg}")
    except Exception as e:
        print(f"ERROR — {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
