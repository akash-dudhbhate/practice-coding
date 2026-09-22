"""
Auto-Check System — Level 18 (Agent Frameworks)
===========================================
Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import importlib.util, os, sys, glob


def load_mod(fp):
    spec = importlib.util.spec_from_file_location("work", fp)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def check_easy_p01(mod):
    if not hasattr(mod, "State"): return False, "class 'State' not found"
    s = mod.State({"task": "x"})
    s.set("a", 1); s.set("b", 2)
    if s.get("a") != 1: return False, f"get('a') should be 1, got {s.get('a')}"
    if s.get("missing", "d") != "d": return False, "get() should return default for missing key"
    if len(s.history) != 2: return False, f"history should have 2 writes, got {s.history}"
    if s.history[0] != ("a", 1) or s.history[1] != ("b", 2):
        return False, f"history should be [('a',1),('b',2)], got {s.history}"
    e = mod.State()
    if e.get("k") is not None: return False, "empty State get should return None"
    if e.history != []: return False, "fresh State history should be empty"
    return True, "State container works: get/set/history"


def check_easy_p02(mod):
    if not hasattr(mod, "Node"): return False, "class 'Node' not found"
    n = mod.Node("inc", lambda s: {**s, "x": s["x"] + 1})
    if n.name != "inc": return False, f"name should be 'inc', got {n.name!r}"
    if not callable(n): return False, "Node instance should be callable (define __call__)"
    r = n({"x": 4})
    if r.get("x") != 5: return False, f"node({{'x':4}}) should give x=5, got {r}"
    r2 = n.run({"x": 1})
    if r2.get("x") != 2: return False, f"node.run({{'x':1}}) should give x=2, got {r2}"
    return True, "Node wraps fn, keeps name, callable + .run()"


def check_easy_p03(mod):
    if not hasattr(mod, "linear_graph"): return False, "function 'linear_graph' not found"
    add_one = lambda s: {**s, "x": s["x"] + 1}
    times_3 = lambda s: {**s, "x": s["x"] * 3}
    minus_2 = lambda s: {**s, "x": s["x"] - 2}
    pipe = mod.linear_graph([add_one, times_3, minus_2])
    r = pipe({"x": 1})
    if r.get("x") != 4: return False, f"((1+1)*3)-2 should be 4, got {r}"
    r0 = pipe({"x": 0})
    if r0.get("x") != 1: return False, f"((0+1)*3)-2 should be 1, got {r0}"
    ident = mod.linear_graph([])
    ri = ident({"k": 9})
    if ri.get("k") != 9: return False, "empty node list should return state unchanged"
    return True, "linear_graph chains nodes in order"


def check_medium_p01(mod):
    if not hasattr(mod, "Graph"): return False, "class 'Graph' not found"
    # linear edges
    g = mod.Graph()
    g.add_node("a", lambda s: {**s, "log": s.get("log", []) + ["a"]})
    g.add_node("b", lambda s: {**s, "log": s.get("log", []) + ["b"]})
    g.add_edge("a", "b")
    r = g.run({})
    if r.get("log") != ["a", "b"]: return False, f"expected log ['a','b'], got {r.get('log')}"
    # conditional routing
    g2 = mod.Graph()
    g2.add_node("start", lambda s: {**s, "n": s["n"] + 1})
    g2.add_node("big",   lambda s: {**s, "label": "big"})
    g2.add_node("small", lambda s: {**s, "label": "small"})
    g2.add_conditional("start", lambda s: "big" if s["n"] > 5 else "small")
    rb = g2.run({"n": 10})
    if rb.get("label") != "big": return False, f"n=10 should route to big, got {rb}"
    rs = g2.run({"n": 1})
    if rs.get("label") != "small": return False, f"n=1 should route to small, got {rs}"
    # conditional must beat a plain edge on the same node
    g3 = mod.Graph()
    g3.add_node("s", lambda s: s)
    g3.add_node("via_edge", lambda s: {**s, "path": "edge"})
    g3.add_node("via_cond", lambda s: {**s, "path": "cond"})
    g3.add_edge("s", "via_edge")
    g3.add_conditional("s", lambda s: "via_cond")
    rc = g3.run({})
    if rc.get("path") != "cond": return False, "conditional edge should take priority over plain edge"
    # cycle protection
    g4 = mod.Graph()
    g4.add_node("x", lambda s: s)
    g4.add_node("y", lambda s: s)
    g4.add_edge("x", "y"); g4.add_edge("y", "x")
    try:
        g4.run({}, max_steps=10)
        return False, "cycle should raise RuntimeError after max_steps"
    except RuntimeError:
        pass
    return True, "Graph runs edges, conditionals, priority, loop-guard"


def check_medium_p02(mod):
    if not hasattr(mod, "conditional_router"): return False, "function 'conditional_router' not found"
    cases = [
        ({"error": "boom"}, "handle_error"),
        ({"error": "x", "done": True}, "handle_error"),   # error beats done
        ({"done": True}, "finish"),
        ({"done": False}, "continue"),
        ({}, "continue"),
    ]
    for state, expected in cases:
        r = mod.conditional_router(state)
        if r != expected: return False, f"router({state}) should be '{expected}', got '{r}'"
    return True, "Router picks next node from state"


def check_medium_p03(mod):
    if not hasattr(mod, "build_agent_graph"): return False, "function 'build_agent_graph' not found"
    if not hasattr(mod, "Graph"): return False, "class 'Graph' not found (include it in this file)"
    g = mod.build_agent_graph()
    if not isinstance(g, mod.Graph): return False, "build_agent_graph should return a Graph"
    if len(g.nodes) != 4: return False, f"expected 4 nodes, got {len(g.nodes)}"
    for name in ["input", "plan", "execute", "output"]:
        if name not in g.nodes: return False, f"missing node '{name}'"
    r = g.run({"task": "summarize notes"})
    if r.get("trace") != ["input", "plan", "execute", "output"]:
        return False, f"trace should be input→plan→execute→output, got {r.get('trace')}"
    if r.get("output") != "executed: summarize notes":
        return False, f"output should be 'executed: summarize notes', got {r.get('output')!r}"
    return True, "4-node agent graph runs end-to-end with trace"


def check_hard_p01(mod):
    if not hasattr(mod, "parallel_nodes"): return False, "function 'parallel_nodes' not found"
    p = mod.parallel_nodes({
        "a": lambda s: {"x": s["n"] + 1},
        "b": lambda s: {"y": s["n"] * 10, "saw_x": "x" in s},
    })
    out = p({"n": 5})
    if out.get("x") != 6 or out.get("y") != 50:
        return False, f"merged state should have x=6,y=50, got {out}"
    if out.get("n") != 5: return False, "input keys should survive the merge"
    if out.get("results", {}).get("a") != {"x": 6}:
        return False, f"results['a'] should be {{'x':6}}, got {out.get('results')}"
    if out.get("saw_x") is not False:
        return False, "branch b saw branch a's write — branches must get COPIES"
    if out.get("trace") != ["parallel"]:
        return False, f"trace should be ['parallel'], got {out.get('trace')}"
    return True, "Parallel fan-out: copies in, merged results out"


def check_hard_p02(mod):
    if not hasattr(mod, "self_correct_loop"): return False, "function 'self_correct_loop' not found"
    needs_3 = lambda s: s.get("x", 0) >= 3
    bump = lambda s: {**s, "x": s.get("x", 0) + 1}
    ok_node = mod.self_correct_loop(needs_3, bump, 10)
    r = ok_node({"x": 0})
    if r.get("x") != 3 or r.get("iterations") != 3 or r.get("ok") is not True:
        return False, f"should reach x=3 in 3 iters with ok=True, got {r}"
    weak = mod.self_correct_loop(needs_3, bump, 2)
    r2 = weak({"x": 0})
    if r2.get("x") != 2 or r2.get("iterations") != 2 or r2.get("ok") is not False:
        return False, f"should stop at max_iters=2 with ok=False, got {r2}"
    pre = ok_node({"x": 5})
    if pre.get("iterations") != 0 or pre.get("ok") is not True:
        return False, f"already-good state should need 0 fixes, got {pre}"
    return True, "Self-correct loop: retries until check passes or cap hit"


def check_hard_p03(mod):
    if not hasattr(mod, "full_agent"): return False, "function 'full_agent' not found"
    r = mod.full_agent("calculate 6 * 7")
    if "42" not in str(r.get("response")):
        return False, f"math task should give Result: 42, got {r.get('response')!r}"
    if r.get("verified") is not True:
        return False, "math result should verify True"
    if r.get("trace") != ["parse", "plan", "tools", "verify", "respond"]:
        return False, f"success trace should be parse→plan→tools→verify→respond, got {r.get('trace')}"
    r2 = mod.full_agent("search agent frameworks")
    if "agent frameworks" not in str(r2.get("tool_result", "")):
        return False, f"search should produce 'Results for: agent frameworks', got {r2.get('tool_result')!r}"
    r3 = mod.full_agent("fly to the moon")
    if r3.get("verified") is not False or r3.get("attempts") != 2:
        return False, f"unknown task should retry once then fail (attempts=2), got attempts={r3.get('attempts')}"
    if "Failed" not in str(r3.get("response")):
        return False, f"failed task should respond with 'Failed...', got {r3.get('response')!r}"
    if r3.get("trace") != ["parse", "plan", "tools", "verify", "tools", "verify", "respond"]:
        return False, f"retry trace should loop tools→verify once, got {r3.get('trace')}"
    return True, "Full agent: parse→plan→tools→verify→respond with retry cycle"


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
    if len(sys.argv) < 2: print("Usage: python3 check.py <difficulty/pXX> or 'all'"); return
    t = sys.argv[1]
    if t == "all": [run_one(c) for c in sorted(CHECKS)]; return
    run_one(t)


def run_one(cid):
    if cid not in CHECKS: print(f"Unknown: {cid}"); return
    diff, num = cid.split("/"); nc = num.lstrip("p")
    d = os.path.join(os.path.dirname(__file__), diff)
    ms = [f for f in glob.glob(os.path.join(d, f"p{nc}-*.py")) if "solutions" not in f]
    w = ms[0] if ms else None
    if not w: print(f"{cid}: FILE NOT FOUND"); return
    try:
        mod = load_mod(w); passed, msg = CHECKS[cid](mod)
        print(f"{cid}: {'PASS' if passed else 'FAIL'} — {msg}")
        if passed:
            with open(w) as f:
                if "DONE" not in f.readline().strip(): print("  → add '# DONE' to mark complete")
    except Exception as e:
        if "NoneType" in str(e):
            print(f"{cid}: FAIL — a function returned None — write the body!")
        else:
            print(f"{cid}: ERROR — {e}")


if __name__ == "__main__": main()
