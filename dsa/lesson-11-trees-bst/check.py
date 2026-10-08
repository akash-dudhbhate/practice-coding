"""
Auto-Check System — Lesson 11 (Trees & BSTs)
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
from collections import deque


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


# --- shared tree helpers for tests (duck-typed: any TreeNode works) ---

class _TN:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _build(vals):
    """Level-order list -> tree. None marks a missing child."""
    if not vals:
        return None
    root = _TN(vals[0])
    q, i = deque([root]), 1
    while q and i < len(vals):
        node = q.popleft()
        if vals[i] is not None:
            node.left = _TN(vals[i]); q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = _TN(vals[i]); q.append(node.right)
        i += 1
    return root


def _to_list(root):
    """Tree -> level-order list, trailing Nones trimmed."""
    if root is None:
        return []
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def check_easy_p01(module):
    for fname in ("inorder", "preorder", "postorder"):
        if not hasattr(module, fname):
            return False, f"Function '{fname}' not found"
    t = _build([1, 2, 3, 4, None, 5, 6])
    if module.inorder(t) != [4, 2, 1, 5, 3, 6]:
        return False, "inorder([1,2,3,4,None,5,6]) should be [4,2,1,5,3,6]"
    t = _build([1, 2, 3, 4, None, 5, 6])
    if module.preorder(t) != [1, 2, 4, 3, 5, 6]:
        return False, "preorder(...) should be [1,2,4,3,5,6]"
    t = _build([1, 2, 3, 4, None, 5, 6])
    if module.postorder(t) != [4, 2, 5, 6, 3, 1]:
        return False, "postorder(...) should be [4,2,5,6,3,1]"
    if module.inorder(None) != [] or module.preorder(None) != [] or module.postorder(None) != []:
        return False, "empty tree should give []"
    vine = _build([1, None, 2, None, 3])
    if module.inorder(vine) != [1, 2, 3]:
        return False, "inorder on vine [1,None,2,None,3] should be [1,2,3]"
    vine = _build([1, None, 2, None, 3])
    if module.postorder(vine) != [3, 2, 1]:
        return False, "postorder on vine should be [3,2,1]"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'max_depth'):
        return False, "Function 'max_depth' not found"
    if module.max_depth(_build([3, 9, 20, None, None, 15, 7])) != 3:
        return False, "max_depth([3,9,20,None,None,15,7]) should be 3"
    if module.max_depth(None) != 0:
        return False, "max_depth(None) should be 0"
    if module.max_depth(_build([1])) != 1:
        return False, "max_depth([1]) should be 1"
    if module.max_depth(_build([1, 2, None, 3, None, 4])) != 4:
        return False, "max_depth on degenerate tree should be 4"
    if module.max_depth(_build([1, 2, 3, 4, 5, 6, 7])) != 3:
        return False, "max_depth on perfect tree of 7 should be 3"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'count_nodes'):
        return False, "Function 'count_nodes' not found"
    if module.count_nodes(_build([3, 9, 20, None, None, 15, 7])) != 5:
        return False, "count_nodes([3,9,20,None,None,15,7]) should be 5"
    if module.count_nodes(None) != 0:
        return False, "count_nodes(None) should be 0"
    if module.count_nodes(_build([1])) != 1:
        return False, "count_nodes([1]) should be 1"
    if module.count_nodes(_build([1, 2, 3, 4, 5, 6, 7])) != 7:
        return False, "count_nodes on perfect tree should be 7"
    if module.count_nodes(_build([1, None, 2, None, 3])) != 3:
        return False, "count_nodes on vine should be 3"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'level_order'):
        return False, "Function 'level_order' not found"
    if module.level_order(_build([3, 9, 20, None, None, 15, 7])) != [[3], [9, 20], [15, 7]]:
        return False, "level_order([3,9,20,None,None,15,7]) should be [[3],[9,20],[15,7]]"
    if module.level_order(None) != []:
        return False, "level_order(None) should be []"
    if module.level_order(_build([1])) != [[1]]:
        return False, "level_order([1]) should be [[1]]"
    if module.level_order(_build([1, 2, None, 3, None, 4])) != [[1], [2], [3], [4]]:
        return False, "level_order on vine should be [[1],[2],[3],[4]]"
    if module.level_order(_build([1, 2, 3, 4, 5, 6, 7])) != [[1], [2, 3], [4, 5, 6, 7]]:
        return False, "level_order on perfect tree should be [[1],[2,3],[4,5,6,7]]"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'insert_bst'):
        return False, "Function 'insert_bst' not found"
    if not hasattr(module, 'search_bst'):
        return False, "Function 'search_bst' not found"
    root = None
    for v in [5, 3, 7, 1, 4]:
        root = module.insert_bst(root, v)
    if _to_list(root) != [5, 3, 7, 1, 4]:
        return False, "insert 5,3,7,1,4 should build tree [5,3,7,1,4]"
    if module.search_bst(root, 4) is not True:
        return False, "search_bst(root, 4) should be True"
    if module.search_bst(root, 6) is not False:
        return False, "search_bst(root, 6) should be False"
    if module.search_bst(root, 5) is not True:
        return False, "search_bst(root, 5) should be True (root itself)"
    if module.search_bst(None, 1) is not False:
        return False, "search_bst(None, 1) should be False"
    root2 = module.insert_bst(root, 6)
    if _to_list(root2) != [5, 3, 7, 1, 4, 6]:
        return False, "after inserting 6, tree should be [5,3,7,1,4,6] (6 = left child of 7)"
    if module.search_bst(root2, 6) is not True:
        return False, "search_bst(root, 6) after insert should be True"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'is_valid_bst'):
        return False, "Function 'is_valid_bst' not found"
    if module.is_valid_bst(_build([2, 1, 3])) is not True:
        return False, "is_valid_bst([2,1,3]) should be True"
    if module.is_valid_bst(_build([5, 1, 4, None, None, 3, 6])) is not False:
        return False, "is_valid_bst([5,1,4,None,None,3,6]) should be False"
    if module.is_valid_bst(_build([5, 4, 6, None, None, 3, 7])) is not False:
        return False, "local checks pass but 3 < 5 sits in 5's right subtree — should be False"
    if module.is_valid_bst(None) is not True:
        return False, "empty tree should be True"
    if module.is_valid_bst(_build([2, 2, 2])) is not False:
        return False, "duplicates not allowed — [2,2,2] should be False"
    if module.is_valid_bst(_build([6, 2, 8, 0, 4, 7, 9])) is not True:
        return False, "is_valid_bst([6,2,8,0,4,7,9]) should be True"
    if module.is_valid_bst(_build([10, 5, 15, None, None, 6, 20])) is not False:
        return False, "[10,5,15,None,None,6,20] — 6 < 10 in right subtree — should be False"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'lca_bst'):
        return False, "Function 'lca_bst' not found"
    root = _build([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    cases = [((2, 8), 6), ((2, 4), 2), ((3, 5), 4), ((7, 9), 8),
             ((0, 5), 2), ((6, 9), 6), ((0, 9), 6)]
    for (p, q), expected in cases:
        node = module.lca_bst(root, p, q)
        if node is None or getattr(node, "val", None) != expected:
            got = getattr(node, "val", node)
            return False, f"lca_bst(root, {p}, {q}) should be node {expected}, got {got}"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'serialize'):
        return False, "Function 'serialize' not found"
    if not hasattr(module, 'deserialize'):
        return False, "Function 'deserialize' not found"
    t = _build([1, 2, 3, None, None, 4, 5])
    s = module.serialize(t)
    if not isinstance(s, str):
        return False, "serialize must return a str"
    rebuilt = module.deserialize(s)
    if _to_list(rebuilt) != [1, 2, 3, None, None, 4, 5]:
        return False, "round-trip failed for [1,2,3,None,None,4,5]"
    if module.deserialize(module.serialize(None)) is not None:
        return False, "empty tree must round-trip to None"
    single = module.deserialize(module.serialize(_build([42])))
    if _to_list(single) != [42]:
        return False, "single node [42] must round-trip"
    vine = _build([1, None, 2, None, 3])
    if _to_list(module.deserialize(module.serialize(vine))) != [1, None, 2, None, 3]:
        return False, "right vine [1,None,2,None,3] must round-trip — is your format losing structure?"
    big = _build([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    if _to_list(module.deserialize(module.serialize(big))) != _to_list(big):
        return False, "round-trip failed for [6,2,8,0,4,7,9,None,None,3,5]"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'diameter'):
        return False, "Function 'diameter' not found"
    if module.diameter(_build([1, 2, 3, 4, 5])) != 3:
        return False, "diameter([1,2,3,4,5]) should be 3 (path 4-2-1-3)"
    if module.diameter(_build([1, 2])) != 1:
        return False, "diameter([1,2]) should be 1"
    if module.diameter(None) != 0:
        return False, "diameter(None) should be 0"
    if module.diameter(_build([1])) != 0:
        return False, "diameter([1]) should be 0 edges"
    tricky = _build([1, 2, 3, 4, 5, None, None, 6, None, None, 7,
                     8, None, None, 9])
    if module.diameter(tricky) != 6:
        return False, "diameter should be 6 — path 8-6-4-2-5-7-9 avoids the root"
    if module.diameter(_build([1, 2, 3, 4, 5, 6, 7])) != 4:
        return False, "diameter on perfect tree of 7 should be 4"
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
        _run_batch(level_dir, solutions=False, title="LESSON 11 — CHECK YOUR FILES")
        return

    if target == "solutions":
        n = _run_batch(level_dir, solutions=True, title="LESSON 11 — REFERENCE SOLUTIONS")
        sys.exit(0 if n == len(CHECKS) else 1)

    if target == "verify":
        n_sol = _run_batch(level_dir, solutions=True, title="LESSON 11 — SOLUTIONS (must pass)")
        print()
        # stubs must NOT pass — they should be rejected
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
