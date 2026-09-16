"""
Auto-Check System — Level 00A (What is AI?)
=============================================
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
    if not hasattr(module, 'spam_rules'):
        return False, "Function 'spam_rules' not found"
    if module.spam_rules("FREE prize for you") != "spam":
        return False, "spam_rules('FREE prize for you') should be 'spam'"
    if module.spam_rules("meet me at lunch") != "ham":
        return False, "spam_rules('meet me at lunch') should be 'ham'"
    if module.spam_rules("urgent winner click now") != "spam":
        return False, "spam_rules('urgent winner click now') should be 'spam'"
    if module.spam_rules("hello how are you") != "ham":
        return False, "spam_rules('hello how are you') should be 'ham'"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'predict'):
        return False, "Function 'predict' not found"
    if abs(module.predict(1000) - 200.0) > 0.01:
        return False, f"predict(1000) should be 200.0, got {module.predict(1000)}"
    if abs(module.predict(2000) - 400.0) > 0.01:
        return False, f"predict(2000) should be 400.0, got {module.predict(2000)}"
    if abs(module.predict(500) - 100.0) > 0.01:
        return False, f"predict(500) should be 100.0, got {module.predict(500)}"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'predict_with_weight'):
        return False, "Function 'predict_with_weight' not found"
    if abs(module.predict_with_weight(1000, 0.2) - 200.0) > 0.01:
        return False, "predict_with_weight(1000, 0.2) should be 200.0"
    if abs(module.predict_with_weight(1000, 0.5) - 500.0) > 0.01:
        return False, "predict_with_weight(1000, 0.5) should be 500.0"
    if abs(module.predict_with_weight(1000, 0.1) - 100.0) > 0.01:
        return False, "predict_with_weight(1000, 0.1) should be 100.0"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'train_one_step'):
        return False, "Function 'train_one_step' not found"
    w = module.train_one_step(0.1, 1000, 200.0, 0.5)
    if abs(w - 0.15) > 0.001:
        return False, f"After 1 step weight should be ~0.15, got {w}"
    w = module.train_one_step(w, 1000, 200.0, 0.5)
    if abs(w - 0.175) > 0.001:
        return False, f"After 2 steps weight should be ~0.175, got {w}"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'predict_price'):
        return False, "Function 'predict_price' not found"
    result = module.predict_price(1500, 3, 10)
    if abs(result - 245.0) > 0.01:
        return False, f"predict_price(1500,3,10) should be 245.0, got {result}"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'similarity'):
        return False, "Function 'similarity' not found"
    s = module.similarity("machine learning models", "machine learning code")
    if abs(s - 0.5) > 0.01:
        return False, f"similarity should be 0.5, got {s}"
    s = module.similarity("python data science", "cooking pasta recipe")
    if abs(s - 0.0) > 0.01:
        return False, f"similarity should be 0.0, got {s}"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'mini_rag'):
        return False, "Function 'mini_rag' not found"
    docs = [
        "Python is a programming language",
        "Cats sleep 16 hours a day",
        "Machine learning needs data",
    ]
    r = module.mini_rag("what is python?", docs)
    if r != docs[0]:
        return False, f"Expected '{docs[0]}', got '{r}'"
    r = module.mini_rag("how long do cats sleep?", docs)
    if r != docs[1]:
        return False, f"Expected '{docs[1]}', got '{r}'"
    r = module.mini_rag("quantum physics explained", docs)
    if r != "I don't know":
        return False, f"Expected \"I don't know\", got '{r}'"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'choose_action'):
        return False, "Function 'choose_action' not found"
    if module.choose_action("what's the weather in Tokyo?") != "get_weather":
        return False, "weather query should → 'get_weather'"
    if module.choose_action("search for pizza recipes") != "web_search":
        return False, "search query should → 'web_search'"
    if module.choose_action("send email to john") != "send_email":
        return False, "email query should → 'send_email'"
    if module.choose_action("calculate 5 + 3") != "calculator":
        return False, "calculate query should → 'calculator'"
    if module.choose_action("tell me a joke") != "chat":
        return False, "other query should → 'chat'"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'where_does_it_fit'):
        return False, "Function 'where_does_it_fit' not found"
    tests = [
        ("gradient descent", "training"),
        ("vector store", "rag"),
        ("docker", "deploy"),
        ("pizza", "unknown"),
        ("weights", "model"),
        ("inference", "prediction"),
        ("dataset", "data"),
        ("tool calling", "agent"),
    ]
    for inp, expected in tests:
        r = module.where_does_it_fit(inp)
        if r != expected:
            return False, f"'{inp}' → expected '{expected}', got '{r}'"
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

    if target == "all":
        print("=" * 60)
        print("  LEVEL 00A — AUTO-CHECK ALL")
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
