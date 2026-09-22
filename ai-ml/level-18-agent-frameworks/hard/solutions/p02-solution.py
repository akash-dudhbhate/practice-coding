"""Level 18 — Agent Frameworks — Hard P02 Solution"""

def self_correct_loop(check_fn, fix_fn, max_iters):
    """Node factory: keep calling fix_fn(state) until check_fn passes
    or max_iters fixes have been applied — a graph cycle folded into
    one node. Reports work via state['iterations'] and state['ok']."""
    def node(state):
        state = dict(state)
        iters = 0
        while not check_fn(state) and iters < max_iters:
            state = fix_fn(state)
            iters += 1
        state["iterations"] = iters
        state["ok"] = bool(check_fn(state))
        return state
    return node

if __name__ == "__main__":
    needs_3 = lambda s: s.get("x", 0) >= 3
    bump    = lambda s: {**s, "x": s.get("x", 0) + 1}

    ok_node   = self_correct_loop(needs_3, bump, 10)
    print(ok_node({"x": 0}))          # {'x': 3, 'iterations': 3, 'ok': True}

    weak_node = self_correct_loop(needs_3, bump, 2)
    print(weak_node({"x": 0}))        # {'x': 2, 'iterations': 2, 'ok': False}
