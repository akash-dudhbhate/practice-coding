"""Milestone 09 Check — Vision Input"""

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
    img = np.array([[0, 128, 255], [64, 32, 16], [200, 100, 50]])
    flat = mod.flatten_image(img)
    if flat is None or len(flat) != 9:
        print(f"FAIL — flatten_image should return 9-element vector, got {flat}")
        return False
    if flat.max() > 1.0:
        print(f"FAIL — values should be normalized to [0,1], max={flat.max()}")
        return False
    if abs(flat[2] - 1.0) > 0.01:  # 255/255
        print(f"FAIL — 255 should normalize to 1.0, got {flat[2]}")
        return False

    if not mod.is_image_like(img):
        print("FAIL — 2D array should be image-like")
        return False
    if mod.is_image_like([1, 2, 3]):
        print("FAIL — 1D list should NOT be image-like")
        return False

    print("PASS — Milestone 09 complete!")
    print("  DataMind accepts images. Move to level-10.")
    return True


if __name__ == "__main__":
    sys.exit(0 if check() else 1)
