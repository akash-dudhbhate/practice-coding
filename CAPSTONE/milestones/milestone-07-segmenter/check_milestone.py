"""Milestone 07 Check — Segmenter"""

import importlib.util
import os
import sys


def check():
    path = os.path.join(os.path.dirname(__file__), "datamind.py")
    spec = importlib.util.spec_from_file_location("datamind", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    pred = mod.predict([10, 20, 30]) if hasattr(mod, 'predict') else None
    if pred is None:
        print("FAIL — predict() missing or still a TODO")
        return False
    if abs(mod.predict([10, 20, 30]) - 17.1) > 0.01:
        print("FAIL — predict() broken")
        return False

    import numpy as np
    from sklearn.datasets import make_blobs
    X, _ = make_blobs(n_samples=200, centers=4, n_features=3, random_state=42)
    labels, k, sil = mod.segment(X)
    if k != 4:
        print(f"FAIL — should find K=4, got {k}")
        return False
    if sil < 0.5:
        print(f"FAIL — silhouette should be high (>0.5), got {sil:.4f}")
        return False
    prof = mod.profile(np.array(X), labels)
    if len(prof) != 4:
        print(f"FAIL — expected 4 cluster profiles, got {len(prof)}")
        return False
    if len(prof[0]) != 3:
        print("FAIL — each profile should have 3 feature means")
        return False

    print("PASS — Milestone 07 complete!")
    print("  DataMind finds hidden segments. Move to level-08.")
    return True


if __name__ == "__main__":
    sys.exit(0 if check() else 1)
