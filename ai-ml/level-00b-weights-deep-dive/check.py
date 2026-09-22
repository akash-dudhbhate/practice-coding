"""
Auto-Check System — Level 00B (Weights & Training, chapter by chapter)
=======================================================================
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



def _res(x):
    """Return failure msg if a call returned None (stub), else None."""
    return "function returned None — write the body!" if x is None else None

def check_easy_p01(module):
    if not hasattr(module, 'predict'):
        return False, "Function 'predict' not found"
    if module.predict(1000, 0.2) is None:
        return False, "function returned None — write the body!"
    if abs(module.predict(1000, 0.2) - 200.0) > 0.01:
        return False, "predict(1000, 0.2) should be 200.0"
    if abs(module.predict(1000, 0.5) - 500.0) > 0.01:
        return False, "predict(1000, 0.5) should be 500.0"
    if abs(module.predict(1000, 0.0) - 0.0) > 0.01:
        return False, "predict(1000, 0.0) should be 0.0"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'predict2'):
        return False, "Function 'predict2' not found"
    if module.predict2(0, 0.2, 50) is None:
        return False, "function returned None — write the body!"
    if abs(module.predict2(0, 0.2, 50) - 50.0) > 0.01:
        return False, "predict2(0, 0.2, 50) should be 50.0 — bias makes 0-input work"
    if abs(module.predict2(1000, 0.2, 50) - 250.0) > 0.01:
        return False, "predict2(1000, 0.2, 50) should be 250.0"
    if abs(module.predict2(1000, 0.2, 0) - 200.0) > 0.01:
        return False, "predict2(1000, 0.2, 0) should be 200.0"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'loss'):
        return False, "Function 'loss' not found"
    if module.loss([(1000,200),(2000,400)], 0.3, 0) is None:
        return False, "function returned None — write the body!"
    data = [(1000, 200), (2000, 400)]
    if abs(module.loss(data, 0.3, 0) - 50000.0) > 0.01:
        return False, f"loss(data, 0.3, 0) should be 50000, got {module.loss(data, 0.3, 0)}"
    if abs(module.loss(data, 0.2, 0) - 0.0) > 0.01:
        return False, "loss(data, 0.2, 0) should be 0.0"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'train_step'):
        return False, "Function 'train_step' not found"
    if module.train_step(1000, 200, 0.3, 0, 0.0000001) is None:
        return False, "function returned None — write the body!"
    w, b = module.train_step(1000, 200, 0.3, 0, 0.0000001)
    if abs(w - 0.29) > 0.001:
        return False, f"new weight should be ~0.29, got {w}"
    if abs(b - (-0.00001)) > 0.000001:
        return False, f"new bias should be ~-0.00001, got {b}"
    # second call should keep improving
    w2, b2 = module.train_step(1000, 200, w, b, 0.0000001)
    if w2 >= w:
        return False, "weight should keep shrinking toward 0.2"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'simulate'):
        return False, "Function 'simulate' not found"
    if module.simulate(1000, 200, 0.3, 0.0, 0.0000001, 5) is None:
        return False, "function returned None — write the body!"
    ws = module.simulate(1000, 200, 0.3, 0.0, 0.0000001, 5)
    if ws is None or len(ws) != 5:
        return False, f"should return 5 weights, got {ws}"
    expected = [0.29, 0.281, 0.2729, 0.26561, 0.259049]
    for got, exp in zip(ws, expected):
        if abs(got - exp) > 0.001:
            return False, f"expected ~{expected}, got {[round(x,4) for x in ws]}"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'batch_step'):
        return False, "Function 'batch_step' not found"
    if module.batch_step([(1000,200),(2000,400),(1500,300)], 0.1, 0.0, 0.0000001) is None:
        return False, "function returned None — write the body!"
    data = [(1000, 200), (2000, 400), (1500, 300)]
    w, b = module.batch_step(data, 0.1, 0.0, 0.0000001)
    if abs(w - 0.1241666667) > 0.001:
        return False, f"new w should be ~0.1242, got {w}"
    if abs(b - 0.000015) > 0.000001:
        return False, f"new b should be ~0.000015, got {b}"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'fit'):
        return False, "Function 'fit' not found"
    if module.fit([(1000,200),(2000,400),(1500,300)], 0.0000001, 5) is None:
        return False, "function returned None — write the body!"
    data = [(1000, 200), (2000, 400), (1500, 300)]
    w, b = module.fit(data, step=0.0000001, rounds=500)
    if abs(w - 0.2) > 0.01:
        return False, f"w should converge to ~0.2, got {w}"
    if abs(b - 0.0) > 0.5:
        return False, f"b should converge to ~0, got {b}"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'predict_multi'):
        return False, "Function 'predict_multi' not found"
    if module.predict_multi([1500,3,10],[0.15,5.0,-0.5],10.0) is None:
        return False, "function returned None — write the body!"
    r = module.predict_multi([1500, 3, 10], [0.15, 5.0, -0.5], 10.0)
    if abs(r - 245.0) > 0.01:
        return False, f"expected 245.0, got {r}"
    r = module.predict_multi([1000, 2], [0.2, 0.0], 0.0)
    if abs(r - 200.0) > 0.01:
        return False, f"expected 200.0, got {r}"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'fit_multi'):
        return False, "Function 'fit_multi' not found"
    if module.fit_multi([([1200,2],240),([1500,3],300)], 0.0000002, 5) is None:
        return False, "function returned None — write the body!"
    data = [
        ([1200, 2], 240), ([1500, 3], 300),
        ([2000, 4], 400), ([1000, 2], 200),
    ]
    w, b = module.fit_multi(data, step=0.0000002, rounds=3000)
    if not isinstance(w, (list, tuple)) or len(w) != 2:
        return False, f"weights should be a list of 2, got {w}"
    if abs(w[0] - 0.2) > 0.01:
        return False, f"w1 should converge to ~0.2, got {w[0]}"
    if abs(w[1] - 0.0) > 0.05:
        return False, f"w2 should converge to ~0 (rooms don't matter), got {w[1]}"
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
        print("  LEVEL 00B — AUTO-CHECK ALL")
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
