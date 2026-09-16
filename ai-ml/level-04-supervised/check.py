"""
Auto-Check System — Level 04 (Supervised Learning)
====================================================
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
    import numpy as np
    if not hasattr(module, 'linreg'):
        return False, "Function 'linreg' not found"
    m, b = module.linreg([1, 2, 3, 4, 5], [2, 4, 5, 4, 5])
    if not np.isclose(m, 0.6, atol=0.01):
        return False, f"Slope should be ~0.6, got {m}"
    if not np.isclose(b, 2.2, atol=0.01):
        return False, f"Intercept should be ~2.2, got {b}"
    return True, "All tests passed!"


def check_easy_p02(module):
    import numpy as np
    if not hasattr(module, 'sigmoid'):
        return False, "Function 'sigmoid' not found"
    if not hasattr(module, 'train_logreg'):
        return False, "Function 'train_logreg' not found"
    if not np.isclose(module.sigmoid(0), 0.5):
        return False, f"sigmoid(0) should be 0.5, got {module.sigmoid(0)}"
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    y = np.array([0, 0, 0, 1, 1])
    w, b = module.train_logreg(X.tolist(), y.tolist(), lr=0.1, epochs=1000)
    preds = (module.sigmoid(X @ np.array(w) + b) > 0.5).astype(int)
    acc = (preds == y).mean()
    if acc < 1.0:
        return False, f"Accuracy {acc:.4f} — should classify perfectly"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'train_tree'):
        return False, "Function 'train_tree' not found"
    result = module.train_tree()
    if not isinstance(result, tuple) or len(result) != 2:
        return False, "Should return (accuracy, tree)"
    acc, tree = result
    if acc < 0.9:
        return False, f"Accuracy {acc:.4f} too low — check max_depth=3 and seeds"
    if tree.get_depth() > 3:
        return False, f"Tree depth {tree.get_depth()} > 3 — set max_depth=3"
    if not os.path.exists('decision_tree.png'):
        return False, "decision_tree.png was not saved"
    return True, "All tests passed!"


def check_medium_p01(module):
    import numpy as np
    if not hasattr(module, 'gradient_descent'):
        return False, "Function 'gradient_descent' not found"
    result = module.gradient_descent()
    if not isinstance(result, tuple) or len(result) != 3:
        return False, "Should return (m, b, losses)"
    m, b, losses = result
    if not np.isclose(m, 2.93, atol=0.1):
        return False, f"m should be ~2.93, got {m:.4f}"
    if not np.isclose(b, 2.0, atol=0.1):
        return False, f"b should be ~2.0, got {b:.4f}"
    if losses[-1] >= losses[0]:
        return False, "Loss should decrease"
    return True, "All tests passed!"


def check_medium_p02(module):
    import numpy as np
    if not hasattr(module, 'train_forest'):
        return False, "Function 'train_forest' not found"
    result = module.train_forest()
    if not isinstance(result, tuple) or len(result) != 2:
        return False, "Should return (accuracy, importances)"
    acc, imp = result
    if abs(acc - 0.95) > 0.03:
        return False, f"Accuracy {acc:.4f} != ~0.95 (check seeds)"
    if not np.isclose(imp.sum(), 1.0):
        return False, "Importances should sum to 1.0"
    if not np.isclose(imp[0], 0.438, atol=0.05):
        return False, f"Feature 0 importance should be ~0.44, got {imp[0]:.4f}"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'compare_models'):
        return False, "Function 'compare_models' not found"
    result = module.compare_models()
    if not isinstance(result, tuple) or len(result) != 2:
        return False, "Should return (svm_acc, knn_acc)"
    svm_acc, knn_acc = result
    if abs(svm_acc - 0.85) > 0.03:
        return False, f"SVM acc {svm_acc:.4f} != ~0.85"
    if abs(knn_acc - 0.80) > 0.03:
        return False, f"KNN acc {knn_acc:.4f} != ~0.80"
    return True, "All tests passed!"


def check_hard_p01(module):
    import numpy as np
    if not hasattr(module, 'compare_regularization'):
        return False, "Function 'compare_regularization' not found"
    result = module.compare_regularization()
    if not isinstance(result, tuple) or len(result) != 3:
        return False, "Should return (lr_coefs, lasso_coefs, ridge_coefs)"
    lr, la, ri = result
    if not np.isclose(lr[0], 18.45, atol=0.1):
        return False, f"Linear coef[0] should be ~18.45, got {lr[0]:.4f}"
    if not np.isclose(la[0], 17.31, atol=0.1):
        return False, f"Lasso coef[0] should be ~17.31, got {la[0]:.4f}"
    if not np.isclose(ri[0], 18.43, atol=0.1):
        return False, f"Ridge coef[0] should be ~18.43, got {ri[0]:.4f}"
    if not abs(la[2]) < abs(lr[2]):
        return False, "Lasso should shrink coef[2] more than linear"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'compare_ensembles'):
        return False, "Function 'compare_ensembles' not found"
    result = module.compare_ensembles()
    if not isinstance(result, dict) or len(result) != 3:
        return False, "Should return dict of 3 models"
    dt = result.get('Decision Tree')
    if dt is None:
        return False, "Missing 'Decision Tree' key"
    if not (dt[0] == 1.0 and abs(dt[1] - 0.92) < 0.02):
        return False, f"Decision Tree should be 1.0/0.92, got {dt}"
    if abs(result['Gradient Boosting'][1] - 0.95) > 0.02:
        return False, f"GB test acc should be ~0.95, got {result['Gradient Boosting'][1]}"
    return True, "All tests passed!"


def check_hard_p03(module):
    import numpy as np
    if not hasattr(module, 'select_features'):
        return False, "Function 'select_features' not found"
    result = module.select_features()
    if not isinstance(result, tuple) or len(result) != 2:
        return False, "Should return (feature_indices, accuracy)"
    feats, acc = result
    if feats != [3, 4, 5, 6, 8]:
        return False, f"Selected features should be [3,4,5,6,8], got {feats}"
    if abs(acc - 0.925) > 0.02:
        return False, f"Accuracy {acc:.4f} != ~0.925"
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
        print("  LEVEL 04 — AUTO-CHECK ALL")
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
