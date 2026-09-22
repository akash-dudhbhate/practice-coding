"""
Auto-Check System — Level 05 (Model Evaluation)
=================================================
Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import os
import sys
import glob
import importlib.util

import matplotlib
matplotlib.use('Agg')


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
    if not hasattr(module, 'compute_metrics'):
        return False, "Function 'compute_metrics' not found"
    m = module.compute_metrics([0,0,1,1,1,0,1,0,1,1], [0,1,1,1,0,0,1,0,1,1])
    if not isinstance(m, dict):
        return False, f"Expected dict, got {type(m)}"
    if abs(m['accuracy'] - 0.8) > 0.01:
        return False, f"Accuracy should be 0.8, got {m['accuracy']}"
    if abs(m['precision'] - 0.833) > 0.01:
        return False, f"Precision should be ~0.833, got {m['precision']}"
    if abs(m['recall'] - 0.833) > 0.01:
        return False, f"Recall should be ~0.833, got {m['recall']}"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'confusion'):
        return False, "Function 'confusion' not found"
    c = module.confusion([0,0,1,1,1,0,1,0,1,1], [0,1,1,1,0,0,1,0,1,1])
    if c != {"TP": 5, "FP": 1, "TN": 3, "FN": 1}:
        return False, f"Expected {{'TP':5,'FP':1,'TN':3,'FN':1}}, got {c}"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'cross_validate'):
        return False, "Function 'cross_validate' not found"
    result = module.cross_validate()
    if not isinstance(result, tuple) or len(result) != 2:
        return False, "Should return (mean, std)"
    m, s = result
    if abs(m - 0.9667) > 0.02:
        return False, f"Mean should be ~0.967, got {m:.4f}"
    if not (0.005 < s < 0.05):
        return False, f"Std should be ~0.021, got {s:.4f}"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'plot_roc'):
        return False, "Function 'plot_roc' not found"
    auc_val = module.plot_roc()
    if not (0.8 < auc_val < 0.95):
        return False, f"AUC should be ~0.885, got {auc_val:.4f}"
    if not os.path.exists('roc_curve.png'):
        return False, "roc_curve.png was not saved"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'grid_search'):
        return False, "Function 'grid_search' not found"
    result = module.grid_search()
    if not isinstance(result, tuple) or len(result) != 3:
        return False, "Should return (best_params, cv_score, test_score)"
    params, cv, test = result
    if 'n_estimators' not in params or 'max_depth' not in params:
        return False, f"best_params missing keys: {params}"
    if not (0.85 < cv < 0.95):
        return False, f"CV score should be ~0.9, got {cv:.4f}"
    return True, "All tests passed!"


def check_medium_p03(module):
    import numpy as np
    if not hasattr(module, 'plot_learning_curve'):
        return False, "Function 'plot_learning_curve' not found"
    result = module.plot_learning_curve()
    if not isinstance(result, tuple) or len(result) != 3:
        return False, "Should return (train_sizes, train_mean, val_mean)"
    ts, tr, va = result
    if len(ts) != 10:
        return False, f"Expected 10 train sizes, got {len(ts)}"
    if va[-1] < 0.75:
        return False, f"Final val score should be ~0.8+, got {va[-1]:.4f}"
    if not os.path.exists('learning_curve.png'):
        return False, "learning_curve.png was not saved"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'find_threshold'):
        return False, "Function 'find_threshold' not found"
    result = module.find_threshold()
    if not isinstance(result, tuple) or len(result) != 2:
        return False, "Should return (threshold, precision)"
    t, p = result
    if abs(t - 0.1466) > 0.05:
        return False, f"Threshold should be ~0.147, got {t:.4f}"
    if abs(p - 0.50) > 0.05:
        return False, f"Precision should be ~0.50, got {p:.4f}"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'compare_all'):
        return False, "Function 'compare_all' not found"
    r = module.compare_all()
    if not isinstance(r, dict) or len(r) != 5:
        return False, f"Expected 5 models, got {len(r)}"
    if 'Random Forest' not in r:
        return False, "Missing 'Random Forest' key"
    rf = r['Random Forest']
    for key in ['accuracy', 'f1', 'auc']:
        if key not in rf:
            return False, f"Missing metric '{key}'"
    if abs(rf['accuracy'] - 0.94) > 0.03:
        return False, f"RF accuracy should be ~0.94, got {rf['accuracy']:.4f}"
    return True, "All tests passed!"


def check_hard_p03(module):
    import numpy as np
    if not hasattr(module, 'nested_cv'):
        return False, "Function 'nested_cv' not found"
    scores = module.nested_cv()
    if len(scores) != 5:
        return False, f"Expected 5 outer scores, got {len(scores)}"
    if abs(np.mean(scores) - 0.885) > 0.05:
        return False, f"Mean should be ~0.885, got {np.mean(scores):.4f}"
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
        print("  LEVEL 05 — AUTO-CHECK ALL")
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
