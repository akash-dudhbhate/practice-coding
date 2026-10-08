"""
Auto-Check System — DSA Lesson 07 (Linked Lists)
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


def _stub_check(filepath):
    """Reject unwritten stubs before running any function checks."""
    with open(filepath, "r") as f:
        content = f.read()
    if "TODO" in content:
        return False, "stub still contains TODO — write your solution!"
    return True, ""


# ---- checker's own linked-list plumbing -----------------------------
# The checker feeds YOUR functions nodes built from this class; your
# functions only need to read/write .val and .next on whatever they get.

class _Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def _build(values):
    dummy = _Node()
    tail = dummy
    for v in values:
        tail.next = _Node(v)
        tail = tail.next
    return dummy.next


def _to_pylist(head, cap=10000):
    """Walk a chain into a Python list. Cap guards against cyclic output."""
    out = []
    while head is not None and len(out) < cap:
        out.append(head.val)
        head = head.next
    return out


def _build_cycle(values, pos):
    """Build a list whose tail points at index `pos` (-1 = no cycle)."""
    nodes = [_Node(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if nodes and 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None


# ---- problem checks --------------------------------------------------

def check_easy_p01(module):
    if not hasattr(module, 'build_list'):
        return False, "Function 'build_list' not found"
    if _to_pylist(module.build_list([1, 2, 3])) != [1, 2, 3]:
        return False, "build_list([1,2,3]) should produce 1->2->3 (in order!)"
    if module.build_list([]) is not None:
        return False, "build_list([]) should return None"
    if _to_pylist(module.build_list([7])) != [7]:
        return False, "build_list([7]) should produce a single node"
    if _to_pylist(module.build_list([1, 2, 3, 4, 5])) != [1, 2, 3, 4, 5]:
        return False, "build_list([1..5]) should produce 1->2->3->4->5"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'to_list'):
        return False, "Function 'to_list' not found"
    if module.to_list(_build([1, 2, 3, 4])) != [1, 2, 3, 4]:
        return False, "to_list(1->2->3->4) should be [1,2,3,4]"
    if module.to_list(None) != []:
        return False, "to_list(None) should be []"
    if module.to_list(_build([9])) != [9]:
        return False, "to_list(9) should be [9]"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'find_middle'):
        return False, "Function 'find_middle' not found"
    if module.find_middle(_build([1, 2, 3, 4, 5])) != 3:
        return False, "find_middle(1->2->3->4->5) should be 3"
    if module.find_middle(_build([1, 2, 3, 4])) != 3:
        return False, "find_middle(1->2->3->4) should be 3 (second middle)"
    if module.find_middle(_build([1])) != 1:
        return False, "find_middle(1) should be 1"
    if module.find_middle(_build([1, 2])) != 2:
        return False, "find_middle(1->2) should be 2"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'reverse_list'):
        return False, "Function 'reverse_list' not found"
    if _to_pylist(module.reverse_list(_build([1, 2, 3, 4, 5]))) != [5, 4, 3, 2, 1]:
        return False, "reverse_list(1->2->3->4->5) should be 5->4->3->2->1"
    if module.reverse_list(None) is not None:
        return False, "reverse_list(None) should return None"
    if _to_pylist(module.reverse_list(_build([1]))) != [1]:
        return False, "reverse_list(1) should be 1"
    if _to_pylist(module.reverse_list(_build([1, 2]))) != [2, 1]:
        return False, "reverse_list(1->2) should be 2->1"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'has_cycle'):
        return False, "Function 'has_cycle' not found"
    if module.has_cycle(_build_cycle([1, 2, 3, 4], 1)) is not True:
        return False, "tail->node1 on 1->2->3->4 should be True"
    if module.has_cycle(_build_cycle([1, 2], 0)) is not True:
        return False, "tail->head on 1->2 should be True"
    if module.has_cycle(_build_cycle([1, 2, 3], -1)) is not False:
        return False, "normal 1->2->3->None should be False"
    if module.has_cycle(None) is not False:
        return False, "has_cycle(None) should be False"
    if module.has_cycle(_build_cycle([1], -1)) is not False:
        return False, "single node no-cycle should be False"
    if module.has_cycle(_build_cycle([1], 0)) is not True:
        return False, "self-loop should be True"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'merge_two'):
        return False, "Function 'merge_two' not found"
    if _to_pylist(module.merge_two(_build([1, 2, 4]), _build([1, 3, 4]))) != [1, 1, 2, 3, 4, 4]:
        return False, "merge_two(1->2->4, 1->3->4) should be 1->1->2->3->4->4"
    if _to_pylist(module.merge_two(None, _build([1, 2]))) != [1, 2]:
        return False, "merge_two(None, 1->2) should be 1->2"
    if module.merge_two(None, None) is not None:
        return False, "merge_two(None, None) should return None"
    if _to_pylist(module.merge_two(_build([5, 6]), _build([1, 2, 3, 4]))) != [1, 2, 3, 4, 5, 6]:
        return False, "merge_two(5->6, 1->2->3->4) should be 1->2->3->4->5->6"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'remove_nth'):
        return False, "Function 'remove_nth' not found"
    if _to_pylist(module.remove_nth(_build([1, 2, 3, 4, 5]), 2)) != [1, 2, 3, 5]:
        return False, "remove_nth(1->2->3->4->5, 2) should be 1->2->3->5"
    if module.remove_nth(_build([1]), 1) is not None:
        return False, "remove_nth(1, 1) should return None"
    if _to_pylist(module.remove_nth(_build([1, 2]), 1)) != [1]:
        return False, "remove_nth(1->2, 1) should be 1"
    if _to_pylist(module.remove_nth(_build([1, 2]), 2)) != [2]:
        return False, "remove_nth(1->2, 2) should be 2 (removing the head!)"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'reorder_list'):
        return False, "Function 'reorder_list' not found"
    h = _build([1, 2, 3, 4])
    module.reorder_list(h)
    if _to_pylist(h) != [1, 4, 2, 3]:
        return False, "reorder_list(1->2->3->4) should mutate to 1->4->2->3"
    h = _build([1, 2, 3, 4, 5])
    module.reorder_list(h)
    if _to_pylist(h) != [1, 5, 2, 4, 3]:
        return False, "reorder_list(1->2->3->4->5) should mutate to 1->5->2->4->3"
    h = _build([1, 2, 3])
    module.reorder_list(h)
    if _to_pylist(h) != [1, 3, 2]:
        return False, "reorder_list(1->2->3) should mutate to 1->3->2"
    h = _build([1])
    module.reorder_list(h)
    if _to_pylist(h) != [1]:
        return False, "reorder_list(1) should leave 1"
    module.reorder_list(None)  # must not crash
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'reverse_k_group'):
        return False, "Function 'reverse_k_group' not found"
    if _to_pylist(module.reverse_k_group(_build([1, 2, 3, 4, 5]), 2)) != [2, 1, 4, 3, 5]:
        return False, "reverse_k_group(1->2->3->4->5, 2) should be 2->1->4->3->5"
    if _to_pylist(module.reverse_k_group(_build([1, 2, 3, 4, 5]), 3)) != [3, 2, 1, 4, 5]:
        return False, "reverse_k_group(1->2->3->4->5, 3) should be 3->2->1->4->5"
    if _to_pylist(module.reverse_k_group(_build([1, 2, 3]), 5)) != [1, 2, 3]:
        return False, "k > length should leave the list unchanged"
    if _to_pylist(module.reverse_k_group(_build([1]), 1)) != [1]:
        return False, "reverse_k_group(1, 1) should be 1"
    if _to_pylist(module.reverse_k_group(_build([1, 2, 3, 4, 5, 6]), 3)) != [3, 2, 1, 6, 5, 4]:
        return False, "reverse_k_group(1->..->6, 3) should be 3->2->1->6->5->4"
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
        print("  DSA LESSON 07 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id, check_func in CHECKS.items():
            level, num = check_id.split("/")
            filepath = _find_file(level_dir, level, num)
            if not os.path.exists(filepath):
                print(f"  {check_id}: FILE NOT FOUND")
                continue
            ok, msg = _stub_check(filepath)
            if not ok:
                print(f"  {check_id}: FAIL — {msg}")
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

    ok, msg = _stub_check(filepath)
    if not ok:
        print(f"FAIL — {msg}")
        sys.exit(0)

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
