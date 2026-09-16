"""
Auto-Check System — Level 06 (Advanced ML)
============================================
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
    if not hasattr(module, 'compare_linear_poly'):
        return False, "Function 'compare_linear_poly' not found"
    l, p = module.compare_linear_poly()
    if not (l < 0.2):
        return False, f"Linear R² should be ~0 or negative, got {l:.4f}"
    if not (p > 0.7):
        return False, f"Poly R² should be ~0.79, got {p:.4f}"
    if not p > l:
        return False, "Poly should beat linear on nonlinear data"
    return True, "All tests passed!"


def check_easy_p02(module):
    import pandas as pd
    if not hasattr(module, 'encode'):
        return False, "Function 'encode' not found"
    df = module.encode()
    if not isinstance(df, pd.DataFrame):
        return False, f"Expected DataFrame, got {type(df)}"
    if df.shape != (5, 6):
        return False, f"Expected (5,6), got {df.shape}"
    expected_cols = {'color_blue', 'color_green', 'color_red',
                     'size_L', 'size_M', 'size_S'}
    if set(df.columns) != expected_cols:
        return False, f"Wrong columns: {list(df.columns)}"
    return True, "All tests passed!"


def check_easy_p03(module):
    import pandas as pd
    if not hasattr(module, 'scale_features'):
        return False, "Function 'scale_features' not found"
    df = module.scale_features()
    if not isinstance(df, pd.DataFrame):
        return False, f"Expected DataFrame, got {type(df)}"
    if abs(df['age'].mean()) > 0.001:
        return False, f"Age mean should be ~0, got {df['age'].mean()}"
    if abs(df['income'].mean()) > 0.001:
        return False, f"Income mean should be ~0, got {df['income'].mean()}"
    if abs(df['age'].std() - 1.0) > 0.2:
        return False, f"Age std should be ~1, got {df['age'].std():.4f}"
    return True, "All tests passed!"


def check_medium_p01(module):
    import numpy as np
    if not hasattr(module, 'oversample'):
        return False, "Function 'oversample' not found"
    X = np.arange(100).reshape(-1, 1)
    y = np.array([0]*95 + [1]*5)
    Xb, yb = module.oversample(X, y)
    counts = np.bincount(yb)
    if counts[0] != counts[1]:
        return False, f"Classes still imbalanced: {counts}"
    if len(yb) != 190:
        return False, f"Expected 190 samples, got {len(yb)}"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'select_top'):
        return False, "Function 'select_top' not found"
    result = module.select_top()
    if not isinstance(result, tuple) or len(result) != 3:
        return False, "Should return (all_acc, top5_acc, indices)"
    all_acc, top5_acc, idx = result
    if abs(all_acc - 0.90) > 0.03:
        return False, f"All-features acc should be ~0.90, got {all_acc:.4f}"
    if abs(top5_acc - 0.95) > 0.03:
        return False, f"Top5 acc should be ~0.95, got {top5_acc:.4f}"
    if len(idx) != 5:
        return False, f"Expected 5 feature indices, got {len(idx)}"
    return True, "All tests passed!"


def check_medium_p03(module):
    import numpy as np
    if not hasattr(module, 'reduce_pca'):
        return False, "Function 'reduce_pca' not found"
    result = module.reduce_pca()
    if not isinstance(result, tuple) or len(result) != 2:
        return False, "Should return (X_reduced, variance_ratios)"
    Xr, ev = result
    if Xr.shape != (200, 3):
        return False, f"Expected (200,3), got {Xr.shape}"
    if not (0.4 < ev.sum() < 0.7):
        return False, f"Explained variance should be ~0.53, got {ev.sum():.4f}"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'run_pipeline'):
        return False, "Function 'run_pipeline' not found"
    if not hasattr(module, 'LogTransformer'):
        return False, "Class 'LogTransformer' not found"
    acc = module.run_pipeline()
    if not (0.8 < acc < 1.0):
        return False, f"Accuracy should be ~0.875, got {acc:.4f}"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'engineer_and_train'):
        return False, "Function 'engineer_and_train' not found"
    result = module.engineer_and_train()
    if not isinstance(result, tuple) or len(result) != 2:
        return False, "Should return (accuracy, feature_names)"
    acc, feats = result
    if acc < 0.9:
        return False, f"Accuracy should be ~0.95, got {acc:.4f}"
    if 'income_per_age' not in feats:
        return False, f"Missing engineered feature 'income_per_age': {feats}"
    if len(feats) != 7:
        return False, f"Expected 7 features, got {len(feats)}"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'compare_balanced'):
        return False, "Function 'compare_balanced' not found"
    result = module.compare_balanced()
    if not isinstance(result, tuple) or len(result) != 4:
        return False, "Should return (recall_d, recall_b, f1_d, f1_b)"
    rd, rb, fd, fb = result
    if rb <= rd:
        return False, f"Balanced recall ({rb:.4f}) should exceed default ({rd:.4f})"
    if rd != 0.0:
        return False, f"Default recall should be 0 (all missed), got {rd:.4f}"
    if rb < 0.7:
        return False, f"Balanced recall should be ~0.86, got {rb:.4f}"
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
        print("  LEVEL 06 — AUTO-CHECK ALL")
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
        print(f"ERROR — {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
