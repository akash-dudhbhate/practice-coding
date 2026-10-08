"""
Auto-Check System — Lesson 14 (Graph Algorithms)
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


def _valid_topo(order, n, edges):
    """True iff `order` is a permutation of range(n) with every edge
    a->b appearing as position[a] < position[b]."""
    if not isinstance(order, list) or sorted(order) != list(range(n)):
        return False
    pos = {v: i for i, v in enumerate(order)}
    return all(pos[a] < pos[b] for a, b in edges)


# ---- problem checks ---------------------------------------------------

def check_easy_p01(module):
    if not hasattr(module, 'has_directed_cycle'):
        return False, "Function 'has_directed_cycle' not found"
    if module.has_directed_cycle(3, [(0,1),(1,2),(2,0)]) is not True:
        return False, "triangle 0->1->2->0 is a cycle: True"
    if module.has_directed_cycle(3, [(0,1),(1,2)]) is not False:
        return False, "a chain has no cycle: False"
    if module.has_directed_cycle(4, [(0,1),(0,2),(1,3),(2,3)]) is not False:
        return False, "a diamond DAG has no cycle: False"
    if module.has_directed_cycle(2, [(0,1),(1,0)]) is not True:
        return False, "0->1->0 is a 2-cycle: True"
    if module.has_directed_cycle(1, [(0,0)]) is not True:
        return False, "self-loop is a cycle: True"
    if module.has_directed_cycle(4, [(0,1),(1,2),(2,3)]) is not False:
        return False, "path graph: False"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'topo_order'):
        return False, "Function 'topo_order' not found"
    e = [(0,1),(1,2),(2,3)]
    if module.topo_order(4, e) != [0, 1, 2, 3]:
        return False, "a chain forces exactly [0,1,2,3]"
    e = [(0,1),(0,2)]
    if not _valid_topo(module.topo_order(3, e), 3, e):
        return False, "0 must precede 1 and 2"
    if module.topo_order(3, [(0,1),(1,0)]) != []:
        return False, "cycle must return []"
    if not _valid_topo(module.topo_order(2, []), 2, []):
        return False, "no edges: any permutation of [0,1] is valid"
    e = [(0,1),(0,2),(1,3),(2,3)]
    if not _valid_topo(module.topo_order(4, e), 4, e):
        return False, "diamond: 0 first, 3 last, 1/2 in the middle"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'UnionFind'):
        return False, "Class 'UnionFind' not found"
    uf = module.UnionFind(5)
    if uf.count() != 5:
        return False, "UnionFind(5).count() should start at 5"
    if uf.same(0, 1) is not False:
        return False, "same(0,1) should be False before any union"
    if uf.union(0, 1) is not True:
        return False, "first union(0,1) should return True"
    if uf.same(0, 1) is not True or uf.same(0, 2) is not False:
        return False, "after union(0,1): same(0,1)=True, same(0,2)=False"
    if uf.count() != 4:
        return False, "one merge should drop count to 4"
    if uf.union(0, 1) is not False:
        return False, "union of already-connected vertices must return False"
    if uf.count() != 4:
        return False, "redundant union must NOT change count"
    uf.union(2, 3)
    uf.union(1, 3)
    if uf.same(0, 2) is not True:
        return False, "0 and 2 should be connected transitively: True"
    if uf.count() != 2:
        return False, "after unions (0,1)(2,3)(1,3): count should be 2"
    if uf.same(0, 4) is not False:
        return False, "vertex 4 was never merged: False"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'kahn_order'):
        return False, "Function 'kahn_order' not found"
    e = [(0,1),(0,2),(1,3),(2,3)]
    if not _valid_topo(module.kahn_order(4, e), 4, e):
        return False, "diamond DAG needs a valid order (0 first, 3 last)"
    if module.kahn_order(2, [(0,1),(1,0)]) != []:
        return False, "cycle must return [] — never a partial order"
    e = [(1,0),(2,0),(3,1),(3,2)]
    if not _valid_topo(module.kahn_order(4, e), 4, e):
        return False, "3 must precede 1 and 2; both precede 0"
    if not _valid_topo(module.kahn_order(3, []), 3, []):
        return False, "no edges: any permutation is valid"
    if module.kahn_order(3, [(0,1),(1,2),(2,0)]) != []:
        return False, "3-cycle must return []"
    e = [(0,1),(1,2),(2,3)]
    if module.kahn_order(4, e) != [0, 1, 2, 3]:
        return False, "a chain forces exactly [0,1,2,3]"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'can_finish'):
        return False, "Function 'can_finish' not found"
    if module.can_finish(2, [(1,0)]) is not True:
        return False, "course 1 needs 0 — take 0 first: True"
    if module.can_finish(2, [(1,0),(0,1)]) is not False:
        return False, "circular prereqs: False"
    if module.can_finish(4, [(1,0),(2,1),(3,2)]) is not True:
        return False, "a chain of prereqs is fine: True"
    if module.can_finish(1, []) is not True:
        return False, "one course, no prereqs: True"
    if module.can_finish(3, [(0,1),(1,2),(2,0)]) is not False:
        return False, "0->1->2->0 cycle: False"
    if module.can_finish(5, [(1,0),(2,0),(3,1),(4,3)]) is not True:
        return False, "this DAG should be finishable: True"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'components_after_unions'):
        return False, "Function 'components_after_unions' not found"
    if module.components_after_unions(6, [(0,1),(1,2),(3,4)]) != 3:
        return False, "{0,1,2} {3,4} {5} should be 3"
    if module.components_after_unions(5, []) != 5:
        return False, "no unions: 5 singletons"
    if module.components_after_unions(4, [(0,1),(2,3),(1,2)]) != 1:
        return False, "everything merges into one set: 1"
    if module.components_after_unions(3, [(0,1)]) != 2:
        return False, "one merge on n=3: 2 sets"
    if module.components_after_unions(1, []) != 1:
        return False, "single vertex: 1"
    if module.components_after_unions(4, [(0,1),(0,1)]) != 3:
        return False, "duplicate union is a no-op: still 3"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'dijkstra'):
        return False, "Function 'dijkstra' not found"
    INF = float("inf")
    edges = [(0,1,5),(0,2,1),(2,1,2),(1,3,1),(2,3,5)]
    if module.dijkstra(4, edges, 0) != [0, 3, 1, 4]:
        return False, "dijkstra(...) from 0 should be [0,3,1,4] — detour beats direct"
    if module.dijkstra(3, [(0,1,2)], 0) != [0, 2, INF]:
        return False, "unreachable vertex should be inf"
    if module.dijkstra(3, [(0,1,2),(0,2,5)], 1) != [INF, 0, INF]:
        return False, "directed edges: from 1 nothing is reachable"
    if module.dijkstra(1, [], 0) != [0]:
        return False, "single vertex: [0]"
    e = [(0,1,1),(1,2,1),(0,2,4),(2,3,1),(1,3,9),(3,4,1)]
    if module.dijkstra(5, e, 0) != [0, 1, 2, 3, 4]:
        return False, "expected [0,1,2,3,4]"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'network_delay_time'):
        return False, "Function 'network_delay_time' not found"
    if module.network_delay_time([(2,1,1),(2,3,1),(3,4,1)], 4, 2) != 2:
        return False, "signal from 2 reaches all in 2"
    if module.network_delay_time([(1,2,1)], 2, 1) != 1:
        return False, "single edge: 1"
    if module.network_delay_time([(1,2,1)], 2, 2) != -1:
        return False, "node 1 unreachable from 2: -1"
    if module.network_delay_time([(1,2,1),(2,3,2),(1,3,4)], 3, 1) != 3:
        return False, "max(1, 1+2, 4) should be 3 — detour beats direct"
    if module.network_delay_time([(1,2,5),(2,3,5),(1,3,100)], 3, 1) != 10:
        return False, "expected 10"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'find_redundant_connection'):
        return False, "Function 'find_redundant_connection' not found"
    if module.find_redundant_connection([(1,2),(1,3),(2,3)]) != [2, 3]:
        return False, "expected [2,3]"
    if module.find_redundant_connection([(1,2),(2,3),(3,4),(1,4),(1,5)]) != [1, 4]:
        return False, "expected [1,4] — the LAST cycle-closing edge"
    if module.find_redundant_connection([(1,2),(2,3),(3,1)]) != [3, 1]:
        return False, "expected [3,1] (wrap-around cycle)"
    if module.find_redundant_connection([(1,2),(2,3),(2,4),(3,4)]) != [3, 4]:
        return False, "expected [3,4]"
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
        _run_batch(level_dir, solutions=False, title="LESSON 14 — CHECK YOUR FILES")
        return

    if target == "solutions":
        n = _run_batch(level_dir, solutions=True, title="LESSON 14 — REFERENCE SOLUTIONS")
        sys.exit(0 if n == len(CHECKS) else 1)

    if target == "verify":
        n_sol = _run_batch(level_dir, solutions=True, title="LESSON 14 — SOLUTIONS (must pass)")
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
