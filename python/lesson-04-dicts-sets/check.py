"""
Auto-Check System — Lesson 04 (Dictionaries & Sets)
====================================================
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
    if not hasattr(module, 'word_count'):
        return False, "Function 'word_count' not found"
    if module.word_count("the cat the dog") != {"the": 2, "cat": 1, "dog": 1}:
        return False, "word_count('the cat the dog') should be {'the': 2, 'cat': 1, 'dog': 1}"
    if module.word_count("") != {}:
        return False, "word_count('') should be {}"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'has_key'):
        return False, "Function 'has_key' not found"
    if module.has_key({"a": 1}, "a") != True:
        return False, "has_key({'a': 1}, 'a') should be True"
    if module.has_key({"a": 1}, "b") != False:
        return False, "has_key({'a': 1}, 'b') should be False"
    if module.has_key({}, "a") != False:
        return False, "has_key({}, 'a') should be False"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'unique_items'):
        return False, "Function 'unique_items' not found"
    if module.unique_items([1, 2, 2, 3, 3, 3]) != [1, 2, 3]:
        return False, "unique_items([1,2,2,3,3,3]) should be [1,2,3]"
    if module.unique_items([]) != []:
        return False, "unique_items([]) should be []"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'merge_dicts'):
        return False, "Function 'merge_dicts' not found"
    if module.merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) != {"a": 1, "b": 3, "c": 4}:
        return False, "merge_dicts should give {'a': 1, 'b': 3, 'c': 4}"
    if module.merge_dicts({}, {"a": 1}) != {"a": 1}:
        return False, "merge_dicts({}, {'a': 1}) should be {'a': 1}"
    d1 = {"a": 1}
    module.merge_dicts(d1, {"b": 2})
    if d1 != {"a": 1}:
        return False, "merge_dicts must NOT mutate the inputs"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'invert_dict'):
        return False, "Function 'invert_dict' not found"
    if module.invert_dict({"a": 1, "b": 2}) != {1: "a", 2: "b"}:
        return False, "invert_dict({'a':1,'b':2}) should be {1:'a',2:'b'}"
    if module.invert_dict({}) != {}:
        return False, "invert_dict({}) should be {}"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'common_elements'):
        return False, "Function 'common_elements' not found"
    if module.common_elements([1, 2, 3], [2, 3, 4]) != [2, 3]:
        return False, "common_elements([1,2,3],[2,3,4]) should be [2,3]"
    if module.common_elements([1], [2]) != []:
        return False, "common_elements([1],[2]) should be []"
    if module.common_elements([], []) != []:
        return False, "common_elements([],[]) should be []"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'group_by_parity'):
        return False, "Function 'group_by_parity' not found"
    if module.group_by_parity([1, 2, 3, 4]) != {"even": [2, 4], "odd": [1, 3]}:
        return False, "group_by_parity([1,2,3,4]) should be {'even': [2,4], 'odd': [1,3]}"
    if module.group_by_parity([]) != {"even": [], "odd": []}:
        return False, "group_by_parity([]) should be {'even': [], 'odd': []}"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'set_difference'):
        return False, "Function 'set_difference' not found"
    if module.set_difference([1, 2, 3], [2, 3, 4]) != {"only_a": [1], "only_b": [4]}:
        return False, "set_difference([1,2,3],[2,3,4]) should be {'only_a':[1],'only_b':[4]}"
    if module.set_difference([1, 2], [1, 2]) != {"only_a": [], "only_b": []}:
        return False, "Identical inputs should give empty lists"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'char_frequency'):
        return False, "Function 'char_frequency' not found"
    if module.char_frequency("aab bc") != [("a", 2), ("b", 2), ("c", 1)]:
        return False, "char_frequency('aab bc') should be [('a',2),('b',2),('c',1)]"
    if module.char_frequency("") != []:
        return False, "char_frequency('') should be []"
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
        print("  LESSON 04 — AUTO-CHECK ALL")
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
                if "NoneType" in str(e):
                    print(f"  {check_id}: FAIL — a function returned None — write the body!")
                else:
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
        if "NoneType" in str(e):
            print(f"FAIL — a function returned None — write the body!")
        else:
            print(f"ERROR — {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
