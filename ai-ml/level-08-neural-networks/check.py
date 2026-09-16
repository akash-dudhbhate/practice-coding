"""
Auto-Check System — Level 08 (Neural Networks)
================================================
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
    import numpy as np
    if not hasattr(module, 'train_perceptron'):
        return False, "Function 'train_perceptron' not found"
    w, b = module.train_perceptron()
    # Verify OR gate behavior
    X = np.array([[0,0],[0,1],[1,0],[1,1]])
    expected = [0,1,1,1]
    for x, exp in zip(X, expected):
        pred = 1 if np.dot(x, np.array(w)) + b > 0 else 0
        if pred != exp:
            return False, f"Perceptron fails on {x}: got {pred}, expected {exp}"
    return True, "All tests passed!"


def check_easy_p02(module):
    import numpy as np
    for fn, val, expected in [
        ('sigmoid', 0, 0.5), ('sigmoid', 100, 1.0),
        ('relu', -5, 0), ('relu', 5, 5),
        ('tanh', 0, 0.0)
    ]:
        if not hasattr(module, fn):
            return False, f"Function '{fn}' not found"
        result = getattr(module, fn)(val)
        if abs(result - expected) > 0.01:
            return False, f"{fn}({val}) should be ~{expected}, got {result}"
    return True, "All tests passed!"


def check_easy_p03(module):
    import torch
    if not hasattr(module, 'tensor_basics'):
        return False, "Function 'tensor_basics' not found"
    s, p, d = module.tensor_basics()
    if not torch.allclose(s, torch.tensor([5., 7., 9.])):
        return False, f"Sum should be [5,7,9], got {s}"
    if not torch.allclose(p, torch.tensor([4., 10., 18.])):
        return False, f"Product should be [4,10,18], got {p}"
    if abs(d - 32.0) > 0.01:
        return False, f"Dot product should be 32, got {d}"
    return True, "All tests passed!"


def check_medium_p01(module):
    import numpy as np
    if not hasattr(module, 'solve_xor'):
        return False, "Function 'solve_xor' not found"
    result = module.solve_xor()
    if not isinstance(result, tuple) or len(result) != 2:
        return False, "Should return (predictions, losses)"
    preds, losses = result
    expected = [0, 1, 1, 0]
    for i, (p, e) in enumerate(zip(preds, expected)):
        if abs(p - e) > 0.1:
            return False, f"XOR[{i}]: expected ~{e}, got {p:.4f}"
    if losses[-1] > 0.01:
        return False, f"Final loss should be <0.01, got {losses[-1]:.6f}"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'train_linear'):
        return False, "Function 'train_linear' not found"
    loss, w, b = module.train_linear()
    if loss > 0.5:
        return False, f"Loss too high: {loss:.4f}"
    if abs(w - 3.0) > 0.5:
        return False, f"Weight should be ~3.0, got {w:.4f}"
    if abs(b - 2.0) > 0.5:
        return False, f"Bias should be ~2.0, got {b:.4f}"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'train_mlp'):
        return False, "Function 'train_mlp' not found"
    acc = module.train_mlp()
    if acc < 0.9:
        return False, f"Accuracy should be ~1.0, got {acc:.4f}"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'train_manual'):
        return False, "Function 'train_manual' not found"
    result = module.train_manual()
    if not isinstance(result, tuple) or len(result) != 2:
        return False, "Should return (predictions, losses)"
    preds, losses = result
    expected = [0, 1, 1, 0]
    for i, (p, e) in enumerate(zip(preds, expected)):
        if abs(p - e) > 0.05:
            return False, f"XOR[{i}]: expected ~{e}, got {p:.4f}"
    if losses[-1] > 0.001:
        return False, f"Final loss should be <0.001, got {losses[-1]:.6f}"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'train'):
        return False, "Function 'train' not found"
    result = module.train()
    if not isinstance(result, tuple) or len(result) != 2:
        return False, "Should return (train_losses, val_accs)"
    losses, accs = result
    if len(losses) < 10:
        return False, f"Expected ≥10 epochs, got {len(losses)}"
    if losses[-1] >= losses[0]:
        return False, "Loss should decrease"
    if accs[-1] < 0.9:
        return False, f"Val accuracy should be ~0.95+, got {accs[-1]:.4f}"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'train_mnist'):
        return False, "Function 'train_mnist' not found"
    acc, model = module.train_mnist()
    if acc < 0.9:
        return False, f"MNIST accuracy should be ~0.97, got {acc:.4f}"
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
    os.chdir(level_dir)

    if target == "all":
        print("=" * 60)
        print("  LEVEL 08 — AUTO-CHECK ALL")
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
