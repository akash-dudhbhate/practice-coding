"""
Auto-Check System — Lesson 02 (Strings & String Methods)
=========================================================
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
    if not hasattr(module, 'count_vowels'):
        return False, "Function 'count_vowels' not found"
    if module.count_vowels("hello") != 2:
        return False, "count_vowels('hello') should be 2"
    if module.count_vowels("AEIOU") != 5:
        return False, "count_vowels('AEIOU') should be 5"
    if module.count_vowels("rhythm") != 0:
        return False, "count_vowels('rhythm') should be 0"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'reverse_string'):
        return False, "Function 'reverse_string' not found"
    if module.reverse_string("hello") != "olleh":
        return False, "reverse_string('hello') should be 'olleh'"
    if module.reverse_string("abc") != "cba":
        return False, "reverse_string('abc') should be 'cba'"
    if module.reverse_string("") != "":
        return False, "reverse_string('') should be ''"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'is_palindrome'):
        return False, "Function 'is_palindrome' not found"
    if module.is_palindrome("racecar") != True:
        return False, "is_palindrome('racecar') should be True"
    if module.is_palindrome("hello") != False:
        return False, "is_palindrome('hello') should be False"
    if module.is_palindrome("A Santa at NASA") != True:
        return False, "is_palindrome('A Santa at NASA') should be True"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'get_initials'):
        return False, "Function 'get_initials' not found"
    if module.get_initials("John Doe") != "JD":
        return False, "get_initials('John Doe') should be 'JD'"
    if module.get_initials("Akash  Dev") != "AD":
        return False, "get_initials('Akash  Dev') should be 'AD'"
    if module.get_initials("single") != "S":
        return False, "get_initials('single') should be 'S'"
    if module.get_initials("") != "":
        return False, "get_initials('') should be ''"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'count_words'):
        return False, "Function 'count_words' not found"
    if module.count_words("Hello world") != 2:
        return False, "count_words('Hello world') should be 2"
    if module.count_words("  one  two  three  ") != 3:
        return False, "count_words('  one  two  three  ') should be 3"
    if module.count_words("") != 0:
        return False, "count_words('') should be 0"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'replace_spaces'):
        return False, "Function 'replace_spaces' not found"
    if module.replace_spaces("  hello world  ") != "hello_world":
        return False, "replace_spaces('  hello world  ') should be 'hello_world'"
    if module.replace_spaces("no spaces") != "no_spaces":
        return False, "replace_spaces('no spaces') should be 'no_spaces'"
    if module.replace_spaces("  single  ") != "single":
        return False, "replace_spaces('  single  ') should be 'single'"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'is_anagram'):
        return False, "Function 'is_anagram' not found"
    if module.is_anagram("listen", "silent") != True:
        return False, "is_anagram('listen','silent') should be True"
    if module.is_anagram("hello", "world") != False:
        return False, "is_anagram('hello','world') should be False"
    if module.is_anagram("Dormitory", "Dirty room") != True:
        return False, "is_anagram('Dormitory','Dirty room') should be True"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'run_length_encode'):
        return False, "Function 'run_length_encode' not found"
    if module.run_length_encode("aaabbc") != "a3b2c1":
        return False, "run_length_encode('aaabbc') should be 'a3b2c1'"
    if module.run_length_encode("abc") != "a1b1c1":
        return False, "run_length_encode('abc') should be 'a1b1c1'"
    if module.run_length_encode("aaaa") != "a4":
        return False, "run_length_encode('aaaa') should be 'a4'"
    if module.run_length_encode("") != "":
        return False, "run_length_encode('') should be ''"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'extract_domain'):
        return False, "Function 'extract_domain' not found"
    if module.extract_domain("user@gmail.com") != "gmail.com":
        return False, "extract_domain('user@gmail.com') should be 'gmail.com'"
    if module.extract_domain("test@company.co.uk") != "company.co.uk":
        return False, "extract_domain('test@company.co.uk') should be 'company.co.uk'"
    if module.extract_domain("noatsign") != "":
        return False, "extract_domain('noatsign') should be ''"
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
        print("  LESSON 02 — AUTO-CHECK ALL")
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
