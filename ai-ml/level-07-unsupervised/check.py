"""
Auto-Check System — Level 07 (Unsupervised Learning)
======================================================
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
    if not hasattr(module, 'cluster'):
        return False, "Function 'cluster' not found"
    labels, centers = module.cluster()
    if len(labels) != 300:
        return False, f"Expected 300 labels, got {len(labels)}"
    if len(centers) != 3:
        return False, f"Expected 3 centers, got {len(centers)}"
    if set(labels) != {0, 1, 2}:
        return False, f"Expected labels {{0,1,2}}, got {set(labels)}"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'elbow'):
        return False, "Function 'elbow' not found"
    inertias = module.elbow()
    if len(inertias) != 10:
        return False, f"Expected 10 inertias, got {len(inertias)}"
    if inertias[0] < 15000:
        return False, f"K=1 inertia should be ~20402, got {inertias[0]:.0f}"
    if inertias[2] > 700:
        return False, f"K=3 inertia should be ~567, got {inertias[2]:.0f}"
    if not all(inertias[i] > inertias[i+1] for i in range(9)):
        return False, "Inertias should decrease monotonically"
    return True, "All tests passed!"


def check_easy_p03(module):
    import numpy as np
    if not hasattr(module, 'pca_2d'):
        return False, "Function 'pca_2d' not found"
    X2, ev = module.pca_2d()
    if X2.shape != (150, 2):
        return False, f"Expected (150,2), got {X2.shape}"
    if not abs(ev[0] - 0.7296) < 0.01:
        return False, f"First component should explain ~0.73, got {ev[0]:.4f}"
    if not abs(ev.sum() - 0.9581) < 0.01:
        return False, f"Total should be ~0.96, got {ev.sum():.4f}"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'best_k'):
        return False, "Function 'best_k' not found"
    result = module.best_k()
    if not isinstance(result, tuple) or len(result) != 3:
        return False, "Should return (best_k, best_score, all_scores)"
    k, s, all_s = result
    if k != 3:
        return False, f"Best K should be 3, got {k}"
    if not abs(s - 0.8467) < 0.02:
        return False, f"Silhouette should be ~0.847, got {s:.4f}"
    if len(all_s) != 6:
        return False, f"Expected 6 scores (K=2..7), got {len(all_s)}"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'compare_algorithms'):
        return False, "Function 'compare_algorithms' not found"
    result = module.compare_algorithms()
    if not isinstance(result, tuple) or len(result) != 2:
        return False, "Should return (kmeans_labels, dbscan_labels)"
    km, db = result
    if len(km) != 300 or len(db) != 300:
        return False, f"Expected 300 labels each"
    if len(set(km)) != 2:
        return False, f"KMeans should find 2 clusters, got {len(set(km))}"
    if len(set(db)) < 2:
        return False, f"DBSCAN should find ≥2 clusters, got {len(set(db))}"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'hierarchical'):
        return False, "Function 'hierarchical' not found"
    labels = module.hierarchical()
    if len(labels) != 50:
        return False, f"Expected 50 labels, got {len(labels)}"
    if set(labels) != {0, 1, 2}:
        return False, f"Expected 3 clusters, got {set(labels)}"
    return True, "All tests passed!"


def check_hard_p01(module):
    import pandas as pd
    if not hasattr(module, 'segment'):
        return False, "Function 'segment' not found"
    result = module.segment()
    if not isinstance(result, tuple) or len(result) != 2:
        return False, "Should return (df, means)"
    df, means = result
    if df.shape != (200, 4):
        return False, f"Expected (200,4) df, got {df.shape}"
    if means.shape != (5, 3):
        return False, f"Expected (5,3) means, got {means.shape}"
    if 'cluster' not in df.columns:
        return False, "Missing 'cluster' column"
    return True, "All tests passed!"


def check_hard_p02(module):
    import numpy as np
    if not hasattr(module, 'detect_anomalies'):
        return False, "Function 'detect_anomalies' not found"
    result = module.detect_anomalies()
    if not isinstance(result, tuple) or len(result) != 2:
        return False, "Should return (predictions, n_anomalies)"
    preds, n = result
    if len(preds) != 110:
        return False, f"Expected 110 predictions, got {len(preds)}"
    if not (8 <= n <= 15):
        return False, f"Expected ~11 anomalies, got {n}"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'topics'):
        return False, "Function 'topics' not found"
    result = module.topics()
    if not isinstance(result, tuple) or len(result) != 2:
        return False, "Should return (topic_words, W)"
    words, W = result
    if len(words) != 2:
        return False, f"Expected 2 topics, got {len(words)}"
    if W.shape != (4, 2):
        return False, f"Expected W shape (4,2), got {W.shape}"
    all_words = ' '.join(sum(words, []))
    ml_words = ['python', 'learning', 'model', 'data', 'neural']
    has_ml = any(w in all_words for w in ml_words)
    if not has_ml:
        return False, f"Topic words should include ML terms, got {words}"
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
        print("  LEVEL 07 — AUTO-CHECK ALL")
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
