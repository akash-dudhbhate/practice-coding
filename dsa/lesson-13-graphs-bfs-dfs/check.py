"""
Auto-Check System — Lesson 13 (Graphs: BFS & DFS)
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


# ---- checker's own graph plumbing ------------------------------------
# clone_graph gets nodes built from this class; your function only needs
# to read .val / .neighbors and return NEW node objects with the same
# shape (any class works — the checker only reads them back).

class _GNode:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def _build_graph(adj):
    """adj = list of neighbor lists, 1-indexed vals: [[2,4],[1,3],...]."""
    nodes = [_GNode(i + 1) for i in range(len(adj))]
    for i, nbrs in enumerate(adj):
        nodes[i].neighbors = [nodes[j - 1] for j in nbrs]
    return nodes[0] if nodes else None


def _clone_valid(orig, clone):
    """True iff clone is a structurally identical graph of NEW objects."""
    if orig is None and clone is None:
        return True
    if orig is None or clone is None:
        return False
    if orig is clone:
        return False
    paired = {orig: clone}           # orig -> clone, doubles as visited
    stack = [orig]
    while stack:
        o = stack.pop()
        c = paired[o]
        if c is o or c.val != o.val:
            return False
        if len(o.neighbors) != len(c.neighbors):
            return False
        for on, cn in zip(o.neighbors, c.neighbors):
            if cn.val != on.val:
                return False
            if on in paired:
                if paired[on] is not cn:
                    return False
            else:
                paired[on] = cn
                stack.append(on)
    return True


def _copy(grid):
    return [row[:] for row in grid]


# ---- problem checks ---------------------------------------------------

def check_easy_p01(module):
    if not hasattr(module, 'build_adjacency'):
        return False, "Function 'build_adjacency' not found"
    if module.build_adjacency(4, [(0,1),(0,2),(1,3)]) != {0:[1,2], 1:[0,3], 2:[0], 3:[1]}:
        return False, "build_adjacency(4, [(0,1),(0,2),(1,3)]) should be {0:[1,2],1:[0,3],2:[0],3:[1]}"
    if module.build_adjacency(3, []) != {0:[], 1:[], 2:[]}:
        return False, "build_adjacency(3, []) should keep all vertices: {0:[],1:[],2:[]}"
    if module.build_adjacency(2, [(0,1)]) != {0:[1], 1:[0]}:
        return False, "build_adjacency(2, [(0,1)]) should be {0:[1],1:[0]}"
    if module.build_adjacency(5, [(1,2)]) != {0:[], 1:[2], 2:[1], 3:[], 4:[]}:
        return False, "isolated vertices must appear with empty lists"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'bfs_order'):
        return False, "Function 'bfs_order' not found"
    adj = {0:[1,2], 1:[0,3], 2:[0,4,5], 3:[1], 4:[2], 5:[2]}
    if module.bfs_order(adj, 0) != [0, 1, 2, 3, 4, 5]:
        return False, "bfs_order(adj, 0) should be [0,1,2,3,4,5] — rings, not a dive"
    if module.bfs_order({0:[]}, 0) != [0]:
        return False, "bfs_order({0:[]}, 0) should be [0]"
    if module.bfs_order({0:[1], 1:[0], 2:[]}, 0) != [0, 1]:
        return False, "disconnected vertex 2 must NOT be visited"
    if module.bfs_order({0:[1], 1:[0,2], 2:[1]}, 0) != [0, 1, 2]:
        return False, "bfs_order on a chain should be [0,1,2]"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'dfs_order'):
        return False, "Function 'dfs_order' not found"
    adj = {0:[1,2], 1:[0,3], 2:[0,4,5], 3:[1], 4:[2], 5:[2]}
    if module.dfs_order(adj, 0) != [0, 1, 3, 2, 4, 5]:
        return False, "dfs_order(adj, 0) should be preorder [0,1,3,2,4,5] — dive, not rings"
    if module.dfs_order({0:[]}, 0) != [0]:
        return False, "dfs_order({0:[]}, 0) should be [0]"
    if module.dfs_order({0:[1], 1:[0], 2:[]}, 0) != [0, 1]:
        return False, "disconnected vertex 2 must NOT be visited"
    if module.dfs_order({0:[1,2], 1:[0,3], 2:[0], 3:[1]}, 0) != [0, 1, 3, 2]:
        return False, "dfs_order should dive 0->1->3, backtrack, then 2: [0,1,3,2]"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'count_components'):
        return False, "Function 'count_components' not found"
    if module.count_components(5, [(0,1),(1,2),(3,4)]) != 2:
        return False, "count_components(5, [(0,1),(1,2),(3,4)]) should be 2"
    if module.count_components(4, []) != 4:
        return False, "count_components(4, []) should be 4 — isolated vertices count!"
    if module.count_components(4, [(0,1),(2,3)]) != 2:
        return False, "count_components(4, [(0,1),(2,3)]) should be 2"
    if module.count_components(3, [(0,1),(1,2),(0,2)]) != 1:
        return False, "a triangle is ONE component"
    if module.count_components(1, []) != 1:
        return False, "count_components(1, []) should be 1"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'num_islands'):
        return False, "Function 'num_islands' not found"
    if module.num_islands(_copy([[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]])) != 3:
        return False, "the 4x5 example should be 3 islands"
    if module.num_islands(_copy([[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]])) != 1:
        return False, "one big blob is 1 island"
    if module.num_islands(_copy([[0,0],[0,0]])) != 0:
        return False, "all water should be 0"
    if module.num_islands(_copy([[1]])) != 1:
        return False, "[[1]] should be 1"
    if module.num_islands(_copy([[1,0,1],[0,1,0],[1,0,1]])) != 5:
        return False, "diagonals don't connect — that grid is 5 islands"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'shortest_distance'):
        return False, "Function 'shortest_distance' not found"
    sq = {0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2]}
    if module.shortest_distance(sq, 0, 3) != 2:
        return False, "square 0->3 should be 2"
    if module.shortest_distance(sq, 0, 0) != 0:
        return False, "start == target should be 0"
    if module.shortest_distance({0:[1],1:[0],2:[]}, 0, 2) != -1:
        return False, "unreachable should be -1"
    if module.shortest_distance({0:[1],1:[0,2],2:[1,3],3:[2]}, 0, 3) != 3:
        return False, "chain 0->3 should be 3"
    if module.shortest_distance({0:[1,3],1:[0,2],2:[1,3],3:[0,2]}, 0, 3) != 1:
        return False, "0->3 is a direct edge: 1 (a stack/DFS would dive past it)"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'ladder_length'):
        return False, "Function 'ladder_length' not found"
    if module.ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"]) != 5:
        return False, "hit->hot->dot->dog->cog should be 5"
    if module.ladder_length("hit", "cog", ["hot","dot","dog","lot","log"]) != 0:
        return False, "end missing from word_list should be 0"
    if module.ladder_length("hit", "lot", ["hit","hot","lot"]) != 3:
        return False, "hit->hot->lot should be 3"
    if module.ladder_length("hot", "dog", ["hot","dog"]) != 0:
        return False, "hot and dog differ by 2 letters: 0"
    if module.ladder_length("talk", "tail", ["talk","tall","tail"]) != 3:
        return False, "talk->tall->tail should be 3"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'oranges_rotting'):
        return False, "Function 'oranges_rotting' not found"
    if module.oranges_rotting(_copy([[2,1,1],[1,1,0],[0,1,1]])) != 4:
        return False, "[[2,1,1],[1,1,0],[0,1,1]] should take 4 minutes"
    if module.oranges_rotting(_copy([[2,1,1],[0,1,1],[1,0,1]])) != -1:
        return False, "isolated fresh orange means -1"
    if module.oranges_rotting(_copy([[0,2]])) != 0:
        return False, "no fresh oranges should be 0"
    if module.oranges_rotting(_copy([[1]])) != -1:
        return False, "a lone fresh orange can never rot: -1"
    if module.oranges_rotting(_copy([[2]])) != 0:
        return False, "[[2]] should be 0"
    if module.oranges_rotting(_copy([[2,1,1],[1,1,1],[0,1,2]])) != 2:
        return False, "two rotten sources should finish in 2 minutes"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'clone_graph'):
        return False, "Function 'clone_graph' not found"
    if module.clone_graph(None) is not None:
        return False, "clone_graph(None) should return None"
    for adj in ([[2,4],[1,3],[2,4],[1,3]], [[]], [[2],[1]], [[2,3],[1,3],[1,2]]):
        orig = _build_graph(adj)
        clone = module.clone_graph(orig)
        if not _clone_valid(orig, clone):
            return False, f"clone of {adj} must be same shape, all NEW node objects"
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
        _run_batch(level_dir, solutions=False, title="LESSON 13 — CHECK YOUR FILES")
        return

    if target == "solutions":
        n = _run_batch(level_dir, solutions=True, title="LESSON 13 — REFERENCE SOLUTIONS")
        sys.exit(0 if n == len(CHECKS) else 1)

    if target == "verify":
        n_sol = _run_batch(level_dir, solutions=True, title="LESSON 13 — SOLUTIONS (must pass)")
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
