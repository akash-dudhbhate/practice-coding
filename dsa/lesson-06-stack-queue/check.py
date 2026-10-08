"""
Auto-Check System — Lesson 06 (Stacks & Queues)
=========================================================
Usage:
    python3 check.py easy/p01        # check one of YOUR files
    python3 check.py all             # check all 9 of YOUR files
    python3 check.py solutions       # run all 9 reference solutions
    python3 check.py verify          # solutions must pass AND stubs must fail
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


def _find_file(level_dir, level, num, solutions=False):
    num_clean = num.lstrip("p")
    if solutions:
        filepath = os.path.join(level_dir, level, "solutions", f"p{num_clean}-solution.py")
        if os.path.exists(filepath):
            return filepath
        pattern = os.path.join(level_dir, level, "solutions", f"p{num_clean}-*.py")
        matches = glob.glob(pattern)
        return matches[0] if matches else filepath
    filepath = os.path.join(level_dir, level, f"p{num_clean}-solve.py")
    if not os.path.exists(filepath):
        pattern = os.path.join(level_dir, level, f"p{num_clean}-*.py")
        matches = [f for f in glob.glob(pattern) if "solutions" not in f]
        if matches:
            filepath = matches[0]
    return filepath


def _is_stub(filepath):
    """True if the learner file still has the TODO marker (unwritten)."""
    try:
        with open(filepath) as f:
            return "# TODO" in f.read()
    except OSError:
        return False


def check_easy_p01(module):
    if not hasattr(module, 'is_balanced'):
        return False, "Function 'is_balanced' not found"
    if module.is_balanced("{[()]}") != True:
        return False, "is_balanced('{[()]}') should be True"
    if module.is_balanced("([)]") != False:
        return False, "is_balanced('([)]') should be False"
    if module.is_balanced("()[]{}") != True:
        return False, "is_balanced('()[]{}') should be True"
    if module.is_balanced("(((") != False:
        return False, "is_balanced('(((') should be False"
    if module.is_balanced("") != True:
        return False, "is_balanced('') should be True"
    if module.is_balanced(")") != False:
        return False, "is_balanced(')') should be False"
    if module.is_balanced("a(b[c]d)e") != True:
        return False, "is_balanced('a(b[c]d)e') should be True"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'reverse_with_stack'):
        return False, "Function 'reverse_with_stack' not found"
    if module.reverse_with_stack("hello") != "olleh":
        return False, "reverse_with_stack('hello') should be 'olleh'"
    if module.reverse_with_stack("abc") != "cba":
        return False, "reverse_with_stack('abc') should be 'cba'"
    if module.reverse_with_stack("") != "":
        return False, "reverse_with_stack('') should be ''"
    if module.reverse_with_stack("racecar") != "racecar":
        return False, "reverse_with_stack('racecar') should be 'racecar'"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'SimpleQueue'):
        return False, "Class 'SimpleQueue' not found"
    q = module.SimpleQueue()
    if q.is_empty() != True:
        return False, "is_empty() on a fresh queue should be True"
    if q.dequeue() is not None:
        return False, "dequeue() on empty queue should return None"
    if q.peek() is not None:
        return False, "peek() on empty queue should return None"
    q.enqueue(1); q.enqueue(2); q.enqueue(3)
    if q.peek() != 1:
        return False, "peek() should return 1 (the front)"
    if q.dequeue() != 1 or q.dequeue() != 2:
        return False, "dequeue order should be 1 then 2 (FIFO)"
    if q.is_empty() != False:
        return False, "queue should not be empty — 3 remains"
    q.enqueue(4)
    if q.dequeue() != 3 or q.dequeue() != 4:
        return False, "interleaved enqueue must still dequeue FIFO: 3 then 4"
    if q.is_empty() != True:
        return False, "queue should be empty after all dequeues"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'next_greater'):
        return False, "Function 'next_greater' not found"
    if module.next_greater([2, 1, 2, 4, 3]) != [4, 2, 4, -1, -1]:
        return False, "next_greater([2,1,2,4,3]) should be [4,2,4,-1,-1]"
    if module.next_greater([1, 2, 3, 4]) != [2, 3, 4, -1]:
        return False, "next_greater([1,2,3,4]) should be [2,3,4,-1]"
    if module.next_greater([4, 3, 2, 1]) != [-1, -1, -1, -1]:
        return False, "next_greater([4,3,2,1]) should be [-1,-1,-1,-1]"
    if module.next_greater([5, 5, 5]) != [-1, -1, -1]:
        return False, "next_greater([5,5,5]) should be [-1,-1,-1]"
    if module.next_greater([]) != []:
        return False, "next_greater([]) should be []"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'daily_temperatures'):
        return False, "Function 'daily_temperatures' not found"
    if module.daily_temperatures([73,74,75,71,69,72,76,73]) != [1,1,4,2,1,1,0,0]:
        return False, "daily_temperatures([73,74,75,71,69,72,76,73]) should be [1,1,4,2,1,1,0,0]"
    if module.daily_temperatures([30,40,50,60]) != [1,1,1,0]:
        return False, "daily_temperatures([30,40,50,60]) should be [1,1,1,0]"
    if module.daily_temperatures([90,80,70]) != [0,0,0]:
        return False, "daily_temperatures([90,80,70]) should be [0,0,0]"
    if module.daily_temperatures([30,60,90]) != [1,1,0]:
        return False, "daily_temperatures([30,60,90]) should be [1,1,0]"
    if module.daily_temperatures([50,50,51]) != [2,1,0]:
        return False, "daily_temperatures([50,50,51]) should be [2,1,0]"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'eval_rpn'):
        return False, "Function 'eval_rpn' not found"
    if module.eval_rpn(["2", "1", "+", "3", "*"]) != 9:
        return False, "eval_rpn(['2','1','+','3','*']) should be 9"
    if module.eval_rpn(["4", "13", "5", "/", "+"]) != 6:
        return False, "eval_rpn(['4','13','5','/','+']) should be 6"
    if module.eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) != 22:
        return False, "eval_rpn(long list) should be 22"
    if module.eval_rpn(["5"]) != 5:
        return False, "eval_rpn(['5']) should be 5"
    if module.eval_rpn(["3", "4", "-"]) != -1:
        return False, "eval_rpn(['3','4','-']) should be -1 — operand order!"
    if module.eval_rpn(["-7", "2", "/"]) != -3:
        return False, "eval_rpn(['-7','2','/']) should be -3 — truncate toward zero"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'max_sliding_window'):
        return False, "Function 'max_sliding_window' not found"
    if module.max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) != [3, 3, 5, 5, 6, 7]:
        return False, "max_sliding_window([1,3,-1,-3,5,3,6,7], 3) should be [3,3,5,5,6,7]"
    if module.max_sliding_window([1], 1) != [1]:
        return False, "max_sliding_window([1], 1) should be [1]"
    if module.max_sliding_window([9, 11], 2) != [11]:
        return False, "max_sliding_window([9,11], 2) should be [11]"
    if module.max_sliding_window([4, 3, 2, 1], 2) != [4, 3, 2]:
        return False, "max_sliding_window([4,3,2,1], 2) should be [4,3,2]"
    if module.max_sliding_window([1, 2, 3], 1) != [1, 2, 3]:
        return False, "max_sliding_window([1,2,3], 1) should be [1,2,3]"
    if module.max_sliding_window([7, 7, 7], 2) != [7, 7]:
        return False, "max_sliding_window([7,7,7], 2) should be [7,7]"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'largest_rectangle_area'):
        return False, "Function 'largest_rectangle_area' not found"
    if module.largest_rectangle_area([2, 1, 5, 6, 2, 3]) != 10:
        return False, "largest_rectangle_area([2,1,5,6,2,3]) should be 10"
    if module.largest_rectangle_area([2, 4]) != 4:
        return False, "largest_rectangle_area([2,4]) should be 4"
    if module.largest_rectangle_area([1, 1, 1, 1]) != 4:
        return False, "largest_rectangle_area([1,1,1,1]) should be 4"
    if module.largest_rectangle_area([6, 2, 5, 4, 5, 1, 6]) != 12:
        return False, "largest_rectangle_area([6,2,5,4,5,1,6]) should be 12"
    if module.largest_rectangle_area([5]) != 5:
        return False, "largest_rectangle_area([5]) should be 5"
    if module.largest_rectangle_area([]) != 0:
        return False, "largest_rectangle_area([]) should be 0"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'TwoStackQueue'):
        return False, "Class 'TwoStackQueue' not found"
    q = module.TwoStackQueue()
    if q.empty() != True:
        return False, "empty() on fresh queue should be True"
    if q.dequeue() is not None:
        return False, "dequeue() on empty queue should return None"
    q.enqueue(1); q.enqueue(2); q.enqueue(3)
    if q.peek() != 1:
        return False, "peek() should return 1"
    if q.dequeue() != 1:
        return False, "first dequeue should be 1"
    q.enqueue(4)
    if q.dequeue() != 2 or q.dequeue() != 3 or q.dequeue() != 4:
        return False, "FIFO order must survive interleaved enqueue: 2,3,4"
    if q.empty() != True:
        return False, "queue should be empty now"
    if q.peek() is not None:
        return False, "peek() on empty queue should return None"
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


def _run_one(level_dir, check_id, solutions):
    level, num = check_id.split("/")
    filepath = _find_file(level_dir, level, num, solutions=solutions)
    if not os.path.exists(filepath):
        return check_id, "MISSING", "file not found", filepath
    module = load_module(filepath)
    passed, msg = CHECKS[check_id](module)
    return check_id, ("PASS" if passed else "FAIL"), msg, filepath


def _run_batch(level_dir, solutions, title):
    print("=" * 60)
    print(f"  {title}")
    print("=" * 60)
    n_pass = 0
    for check_id in CHECKS:
        try:
            cid, status, msg, fp = _run_one(level_dir, check_id, solutions)
        except Exception as e:
            cid, status, msg, fp = check_id, "ERROR", str(e), ""
            if "NoneType" in msg:
                msg = "a function returned None — write the body!"
        if status == "PASS":
            n_pass += 1
        if status == "FAIL" and not solutions and fp and _is_stub(fp):
            print(f"  {cid}: STUB — TODO still present, write your code first")
        else:
            print(f"  {cid}: {status} — {msg}")
    print("-" * 60)
    print(f"  {n_pass}/{len(CHECKS)} passed")
    print("=" * 60)
    return n_pass


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    target = sys.argv[1]
    level_dir = os.path.dirname(os.path.abspath(__file__))

    if target == "all":
        _run_batch(level_dir, solutions=False, title="LESSON 06 — CHECK YOUR FILES")
        return

    if target == "solutions":
        n = _run_batch(level_dir, solutions=True, title="LESSON 06 — REFERENCE SOLUTIONS")
        sys.exit(0 if n == len(CHECKS) else 1)

    if target == "verify":
        n_sol = _run_batch(level_dir, solutions=True, title="LESSON 06 — SOLUTIONS (must pass)")
        print()
        n_stub = 0
        for check_id in CHECKS:
            level, num = check_id.split("/")
            fp = _find_file(level_dir, level, num)
            if _is_stub(fp):
                n_stub += 1
                print(f"  {check_id}: STUB correctly rejected (TODO present)")
            else:
                print(f"  {check_id}: WARNING — stub file has no TODO marker")
        print("-" * 60)
        print(f"  solutions: {n_sol}/{len(CHECKS)} pass · stubs rejected: {n_stub}/{len(CHECKS)}")
        print("=" * 60)
        sys.exit(0 if (n_sol == len(CHECKS) and n_stub == len(CHECKS)) else 1)

    level, num = target.split("/")
    check_id = f"{level}/{num}"
    if check_id not in CHECKS:
        print(f"Error: unknown problem '{check_id}'")
        sys.exit(1)

    filepath = _find_file(level_dir, level, num)
    if not os.path.exists(filepath):
        print(f"Error: file not found: {filepath}")
        sys.exit(1)

    if _is_stub(filepath):
        print(f"STUB — {filepath} still has the TODO marker. Write your code first!")
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
