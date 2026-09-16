"""
Auto-Check System — Level 02 (Python for ML)
=============================================
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
    """Find the problem file by number (supports p01-*.py names)."""
    num_clean = num.lstrip("p")
    filepath = os.path.join(level_dir, level, f"p{num_clean}-solve.py")
    if not os.path.exists(filepath):
        pattern = os.path.join(level_dir, level, f"p{num_clean}-*.py")
        matches = [f for f in glob.glob(pattern) if "solutions" not in f]
        if matches:
            filepath = matches[0]
    return filepath


# ---------- EASY ----------

def check_easy_p01(module):
    import numpy as np
    if not hasattr(module, 'create_array'):
        return False, "Function 'create_array' not found"
    arr = module.create_array()
    expected = np.array([[51, 92, 14, 71, 60],
                         [20, 82, 86, 74, 74],
                         [87, 99, 23, 2, 21],
                         [52, 1, 87, 29, 37]])
    if not isinstance(arr, np.ndarray):
        return False, f"Expected np.ndarray, got {type(arr)}"
    if arr.shape != (4, 5):
        return False, f"Wrong shape: {arr.shape}, expected (4, 5)"
    if not np.array_equal(arr, expected):
        return False, "Values don't match — did you use seed 42 and randint(0, 100, (4,5))?"
    return True, "All tests passed!"


def check_easy_p02(module):
    import pandas as pd
    if not hasattr(module, 'load_data'):
        return False, "Function 'load_data' not found"
    df = module.load_data()
    if not isinstance(df, pd.DataFrame):
        return False, f"Expected DataFrame, got {type(df)}"
    if df.shape != (4, 3):
        return False, f"Wrong shape: {df.shape}, expected (4, 3)"
    if list(df.columns) != ['name', 'age', 'city']:
        return False, f"Wrong columns: {list(df.columns)}"
    if df['age'].tolist() != [25, 30, 35, 28]:
        return False, f"Wrong ages: {df['age'].tolist()}"
    return True, "All tests passed!"


def check_easy_p03(module):
    import pandas as pd
    if not hasattr(module, 'fill_missing'):
        return False, "Function 'fill_missing' not found"
    df = module.fill_missing()
    if not isinstance(df, pd.DataFrame):
        return False, f"Expected DataFrame, got {type(df)}"
    if df.isna().any().any():
        return False, "DataFrame still has NaN values"
    if df['age'].tolist() != [25.0, 30.0, 30.0, 30.0, 35.0]:
        return False, f"Wrong ages after fill: {df['age'].tolist()} (median should be 30)"
    if df['city'].tolist() != ['Mumbai', 'Delhi', 'Chennai', 'Chennai', 'Chennai']:
        return False, f"Wrong cities: {df['city'].tolist()} (mode should be Chennai)"
    if df['score'].tolist() != [85.0, 90.0, 87.5, 78.0, 92.0]:
        return False, f"Wrong scores: {df['score'].tolist()} (median should be 87.5)"
    return True, "All tests passed!"


# ---------- MEDIUM ----------

def check_medium_p01(module):
    if not hasattr(module, 'build_pipeline'):
        return False, "Function 'build_pipeline' not found"
    acc = module.build_pipeline()
    if not isinstance(acc, (int, float)):
        return False, f"Expected a number, got {type(acc)}"
    if abs(acc - 0.875) > 0.01:
        return False, f"Accuracy {acc:.4f} != expected 0.8750 (check seeds and test_size=0.2)"
    return True, "All tests passed!"


def check_medium_p02(module):
    import numpy as np
    if not hasattr(module, 'detect_outliers'):
        return False, "Function 'detect_outliers' not found"
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 100])
    result = module.detect_outliers(data)
    if not isinstance(result, tuple) or len(result) != 2:
        return False, "Should return (cleaned_array, outlier_count)"
    cleaned, count = result
    if count != 1:
        return False, f"Expected 1 outlier, got {count}"
    if not np.isclose(cleaned[-1], 14.5):
        return False, f"Last value should be capped at 14.5, got {cleaned[-1]}"
    return True, "All tests passed!"


def check_medium_p03(module):
    import pandas as pd
    if not hasattr(module, 'process'):
        return False, "Function 'process' not found"
    df = module.process()
    if not isinstance(df, pd.DataFrame):
        return False, f"Expected DataFrame, got {type(df)}"
    if 'city_encoded' not in df.columns:
        return False, "Missing 'city_encoded' column (use LabelEncoder)"
    if 'age_scaled' not in df.columns:
        return False, "Missing 'age_scaled' column (use StandardScaler)"
    if not pd.api.types.is_datetime64_any_dtype(df['signup_date']):
        return False, "signup_date should be datetime type (use pd.to_datetime)"
    if not abs(df['age_scaled'].mean()) < 0.01:
        return False, "age_scaled should be standardized (mean≈0)"
    return True, "All tests passed!"


# ---------- HARD ----------

def check_hard_p01(module):
    if not hasattr(module, 'train_clean'):
        return False, "Function 'train_clean' not found"
    result = module.train_clean()
    if not isinstance(result, tuple) or len(result) != 2:
        return False, "Should return (train_acc, test_acc)"
    tr, te = result
    if te < 0.8:
        return False, f"Test accuracy {te:.4f} too low — check split-then-fit order and seeds"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'build'):
        return False, "Function 'build' not found"
    acc = module.build()
    if not isinstance(acc, (int, float)):
        return False, f"Expected a number, got {type(acc)}"
    if abs(acc - 0.975) > 0.02:
        return False, f"Accuracy {acc:.4f} != expected ~0.975 (check np.random.seed for the category column)"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'compare_splits'):
        return False, "Function 'compare_splits' not found"
    result = module.compare_splits()
    if not isinstance(result, tuple) or len(result) != 2:
        return False, "Should return (acc_without, acc_with)"
    a, b = result
    if not (0.9 < a < 1.0 and 0.9 < b < 1.0):
        return False, f"Accuracies look wrong: {a}, {b}"
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
        print("Example: python3 check.py easy/p01")
        print("         python3 check.py all")
        sys.exit(1)

    target = sys.argv[1]
    level_dir = os.path.dirname(os.path.abspath(__file__))

    if target == "all":
        print("=" * 60)
        print("  LEVEL 02 — AUTO-CHECK ALL")
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

    if "/" not in target:
        print("Error: use format <level>/<problem>, e.g., easy/p01")
        sys.exit(1)

    level, num = target.split("/")
    check_id = f"{level}/{num}"

    if check_id not in CHECKS:
        print(f"Error: unknown problem '{check_id}'")
        print(f"Available: {list(CHECKS.keys())}")
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
