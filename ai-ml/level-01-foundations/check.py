"""
Auto-Check System — Level 01
=============================
Run this to verify your solutions automatically.

Usage:
    python3 check.py easy/p01
    python3 check.py medium/p02
    python3 check.py hard/p03
    python3 check.py all
"""

import os
import sys
import glob
import importlib.util
import re


def load_module(filepath):
    """Load a Python file as a module."""
    spec = importlib.util.spec_from_file_location("solution", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_p01(module):
    """Check easy/p01 — classify problem type."""
    if not hasattr(module, 'classify'):
        return False, "Function 'classify' not found"

    classify = module.classify
    tests = [
        ("A", "supervised-regression"),
        ("B", "unsupervised"),
        ("C", "supervised-classification"),
    ]

    for input_val, expected in tests:
        result = classify(input_val)
        if result != expected:
            return False, f"classify('{input_val}') returned '{result}', expected '{expected}'"

    return True, "All tests passed!"


def check_p02(module):
    """Check easy/p02 — identify features and labels."""
    if not hasattr(module, 'identify'):
        return False, "Function 'identify' not found"

    identify = module.identify
    result = identify("A")

    if not isinstance(result, dict):
        return False, f"Expected dict, got {type(result)}"

    if "features" not in result or "label" not in result:
        return False, "Result must have 'features' and 'label' keys"

    if not isinstance(result["features"], list):
        return False, "features must be a list"

    return True, "All tests passed!"


def check_p03(module):
    """Check easy/p03 — traditional vs ML."""
    if not hasattr(module, 'choose'):
        return False, "Function 'choose' not found"

    choose = module.choose
    tests = [
        ("A", "traditional"),
        ("B", "ml"),
        ("C", "traditional"),
        ("D", "ml"),
    ]

    for input_val, expected in tests:
        result = choose(input_val)
        if result != expected:
            return False, f"choose('{input_val}') returned '{result}', expected '{expected}'"

    return True, "All tests passed!"


def check_medium_p01(module):
    """Check medium/p01 — design spam classifier."""
    if not hasattr(module, 'design'):
        return False, "Function 'design' not found"

    design = module.design()
    required = ["problem_type", "features", "label", "data_source", "metric"]

    for key in required:
        if key not in design:
            return False, f"Missing key: {key}"

    if not isinstance(design["features"], list) or len(design["features"]) < 3:
        return False, "features must be a list with at least 3 items"

    return True, "All tests passed!"


def check_medium_p02(module):
    """Check medium/p02 — train/test split."""
    if not hasattr(module, 'explain'):
        return False, "Function 'explain' not found"

    explain = module.explain()
    required = ["why_split", "typical_ratio", "overfitting", "interpret"]

    for key in required:
        if key not in explain:
            return False, f"Missing key: {key}"

    return True, "All tests passed!"


def check_medium_p03(module):
    """Check medium/p03 — match algorithm."""
    if not hasattr(module, 'match'):
        return False, "Function 'match' not found"

    match = module.match
    tests = [
        ("A", "linear-regression"),
        ("B", "kmeans-clustering"),
        ("C", "logistic-regression"),
        ("D", "linear-regression"),
        ("E", "neural-network"),
    ]

    for input_val, expected in tests:
        result = match(input_val)
        if result != expected:
            return False, f"match('{input_val}') returned '{result}', expected '{expected}'"

    return True, "All tests passed!"


def check_hard_p01(module):
    """Check hard/p01 — ML pipeline."""
    if not hasattr(module, 'design_pipeline'):
        return False, "Function 'design_pipeline' not found"

    pipeline = module.design_pipeline()
    required = ["problem", "data", "preprocessing", "split", "model", "training", "evaluation", "deployment"]

    for key in required:
        if key not in pipeline:
            return False, f"Missing key: {key}"

    return True, "All tests passed!"


def check_hard_p02(module):
    """Check hard/p02 — confusion matrix."""
    if not hasattr(module, 'analyze'):
        return False, "Function 'analyze' not found"

    result = module.analyze()
    required = ["TP", "FP", "TN", "FN", "accuracy", "worse_error"]

    for key in required:
        if key not in result:
            return False, f"Missing key: {key}"

    if result["TP"] != 70 or result["FN"] != 10:
        return False, "TP and FN values are wrong"

    if result["TN"] != 890 or result["FP"] != 30:
        return False, "TN and FP values are wrong"

    expected_acc = (70 + 890) / 1000
    if abs(result["accuracy"] - expected_acc) > 0.01:
        return False, f"Accuracy wrong: got {result['accuracy']}, expected ~{expected_acc}"

    return True, "All tests passed!"


def check_hard_p03(module):
    """Check hard/p03 — bias-variance."""
    if not hasattr(module, 'explain'):
        return False, "Function 'explain' not found"

    result = module.explain()
    required = ["bias", "variance", "high_bias", "high_variance", "tree_100_65", "linear_70_70", "tradeoff"]

    for key in required:
        if key not in result:
            return False, f"Missing key: {key}"

    if result["high_bias"] != "underfitting":
        return False, "high_bias should be 'underfitting'"

    if result["high_variance"] != "overfitting":
        return False, "high_variance should be 'overfitting'"

    return True, "All tests passed!"


CHECKS = {
    "easy/p01": check_p01,
    "easy/p02": check_p02,
    "easy/p03": check_p03,
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
        print("  LEVEL 01 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id, check_func in CHECKS.items():
            level, num = check_id.split("/")
            # num is like "p01" — strip the "p" prefix
            num_clean = num.lstrip("p")
            # Try both naming patterns
            filepath = os.path.join(level_dir, level, f"p{num_clean}-solve.py")
            if not os.path.exists(filepath):
                # Try descriptive name
                pattern = os.path.join(level_dir, level, f"p{num_clean}-*.py")
                matches = [f for f in glob.glob(pattern) if "solutions" not in f]
                if matches:
                    filepath = matches[0]

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

    # Single check
    if "/" not in target:
        print("Error: use format <level>/<problem>, e.g., easy/p01")
        sys.exit(1)

    level, num = target.split("/")
    check_id = f"{level}/{num}"

    if check_id not in CHECKS:
        print(f"Error: unknown problem '{check_id}'")
        print(f"Available: {list(CHECKS.keys())}")
        sys.exit(1)

    # num is like "p01" — strip the "p" prefix for filename lookup
    num_clean = num.lstrip("p")
    filepath = os.path.join(level_dir, level, f"p{num_clean}-solve.py")
    if not os.path.exists(filepath):
        # Try descriptive name
        pattern = os.path.join(level_dir, level, f"p{num_clean}-*.py")
        matches = [f for f in glob.glob(pattern) if "solutions" not in f]
        if matches:
            filepath = matches[0]

    if not os.path.exists(filepath):
        print(f"Error: file not found: {filepath}")
        sys.exit(1)

    try:
        module = load_module(filepath)
        passed, msg = CHECKS[check_id](module)

        if passed:
            print(f"✓ PASS — {msg}")
            print(f"  Add '# DONE' to the first line of {filepath}")
        else:
            print(f"✗ FAIL — {msg}")
    except Exception as e:
        print(f"✗ ERROR — {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
