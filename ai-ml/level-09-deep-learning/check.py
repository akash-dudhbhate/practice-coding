"""
Auto-Check System — Level 09 (Deep Learning)
==============================================
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
    if not hasattr(module, 'convolve'):
        return False, "Function 'convolve' not found"
    img = np.array([[1,2,3,0],[4,5,6,0],[7,8,9,0],[0,0,0,0]])
    kernel = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
    out = module.convolve(img, kernel)
    if out.shape != (2, 2):
        return False, f"Expected (2,2), got {out.shape}"
    if not np.isclose(out[0][0], -6.0):
        return False, f"out[0][0] should be -6.0, got {out[0][0]}"
    return True, "All tests passed!"


def check_easy_p02(module):
    import torch
    if not hasattr(module, 'build_cnn'):
        return False, "Function 'build_cnn' not found"
    model = module.build_cnn()
    x = torch.randn(1, 1, 28, 28)
    out = model(x)
    if out.shape != torch.Size([1, 10]):
        return False, f"Expected [1,10], got {out.shape}"
    return True, "All tests passed!"


def check_easy_p03(module):
    import numpy as np
    if not hasattr(module, 'max_pool'):
        return False, "Function 'max_pool' not found"
    img = np.array([[1,3,2,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    out = module.max_pool(img)
    expected = np.array([[6., 8.], [14., 16.]])
    if not np.array_equal(out, expected):
        return False, f"Expected [[6,8],[14,16]], got {out}"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'train_cnn'):
        return False, "Function 'train_cnn' not found"
    acc, model = module.train_cnn()
    if acc < 0.3:
        return False, f"CIFAR-10 accuracy too low: {acc:.4f}"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'compare_bn'):
        return False, "Function 'compare_bn' not found"
    a, b = module.compare_bn()
    if not (0.0 < a < 1.0 and 0.0 < b < 1.0):
        return False, f"Losses look wrong: {a:.4f}, {b:.4f}"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'compare_dropout'):
        return False, "Function 'compare_dropout' not found"
    a, b = module.compare_dropout()
    if not (0.4 < a < 1.0 and 0.4 < b < 1.0):
        return False, f"Accuracies look wrong: {a:.4f}, {b:.4f}"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'transfer_learn'):
        return False, "Function 'transfer_learn' not found"
    acc, model = module.transfer_learn()
    if acc < 0.3:
        return False, f"Transfer learning acc too low: {acc:.4f}"
    return True, "All tests passed!"


def check_hard_p02(module):
    import torch
    if not hasattr(module, 'augment_pipeline'):
        return False, "Function 'augment_pipeline' not found"
    t = module.augment_pipeline()
    from PIL import Image
    import numpy as np
    img = Image.fromarray(np.random.randint(0, 255, (32, 32, 3), dtype=np.uint8))
    out = t(img)
    if out.shape != torch.Size([3, 32, 32]):
        return False, f"Expected [3,32,32], got {out.shape}"
    return True, "All tests passed!"


def check_hard_p03(module):
    import torch
    if not hasattr(module, 'CustomCNN'):
        return False, "Class 'CustomCNN' not found"
    if not hasattr(module, 'count_params'):
        return False, "Function 'count_params' not found"
    model = module.CustomCNN()
    x = torch.randn(4, 3, 32, 32)
    out = model(x)
    if out.shape != torch.Size([4, 10]):
        return False, f"Expected [4,10], got {out.shape}"
    n = module.count_params(model)
    if not (500000 < n < 600000):
        return False, f"Expected ~545K params, got {n}"
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
        print("  LEVEL 09 — AUTO-CHECK ALL")
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
