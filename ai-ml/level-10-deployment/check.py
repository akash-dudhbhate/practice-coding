"""
Auto-Check System — Level 10 (Model Deployment)
=================================================
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
    if not hasattr(module, 'save_and_load'):
        return False, "Function 'save_and_load' not found"
    preds = module.save_and_load()
    if preds != [1, 0, 2, 1, 1]:
        return False, f"Expected [1,0,2,1,1], got {preds}"
    if not os.path.exists('model.pkl'):
        return False, "model.pkl was not saved"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'create_app'):
        return False, "Function 'create_app' not found"
    app = module.create_app()
    client = app.test_client()
    r = client.post('/predict', json={'features': [5.1, 3.5, 1.4, 0.2]})
    data = r.get_json()
    if data.get('prediction') != 0:
        return False, f"Expected prediction 0, got {data}"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'create_predict_app'):
        return False, "Function 'create_predict_app' not found"
    app = module.create_predict_app()
    client = app.test_client()
    r = client.get('/predict?f=5.1,3.5,1.4,0.2')
    data = r.get_json()
    if data.get('prediction') != 0:
        return False, f"Expected prediction 0, got {data}"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'create_fastapi_app'):
        return False, "Function 'create_fastapi_app' not found"
    app = module.create_fastapi_app()
    from fastapi.testclient import TestClient
    c = TestClient(app)
    r = c.post('/predict', json={'features': [5.1, 3.5, 1.4, 0.2]})
    data = r.json()
    if data.get('prediction') != 0:
        return False, f"Expected prediction 0, got {data}"
    if 'probabilities' not in data:
        return False, "Missing 'probabilities' in response"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'create_batch_app'):
        return False, "Function 'create_batch_app' not found"
    app = module.create_batch_app()
    from fastapi.testclient import TestClient
    c = TestClient(app)
    r = c.post('/predict-batch', json={'features': [[5.1,3.5,1.4,0.2],[6.0,2.2,5.0,1.5]]})
    data = r.json()
    if data.get('predictions') != [0, 2]:
        return False, f"Expected [0,2], got {data}"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'build_registry'):
        return False, "Function 'build_registry' not found"
    reg = module.build_registry()
    if len(reg) != 3:
        return False, f"Expected 3 versions, got {len(reg)}"
    for v in ['v1', 'v2', 'v3']:
        if v not in reg:
            return False, f"Missing {v}"
        if 'accuracy' not in reg[v] or 'model' not in reg[v]:
            return False, f"{v} missing keys: {reg[v]}"
    if reg['v3']['accuracy'] < reg['v1']['accuracy']:
        return False, "v3 should outperform v1"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'generate_dockerfile'):
        return False, "Function 'generate_dockerfile' not found"
    df = module.generate_dockerfile()
    required = ['FROM python', 'WORKDIR', 'COPY requirements.txt',
                'pip install', 'uvicorn', 'main:app']
    for req in required:
        if req not in df:
            return False, f"Missing '{req}' in Dockerfile"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'create_monitored_model'):
        return False, "Function 'create_monitored_model' not found"
    predict, stats = module.create_monitored_model()
    predict([5.1, 3.5, 1.4, 0.2])
    predict([6.0, 2.2, 5.0, 1.5])
    if stats['total_predictions'] != 2:
        return False, f"Expected 2 predictions, got {stats['total_predictions']}"
    if stats['avg_latency'] < 0:
        return False, "avg_latency should be >= 0"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'ab_test'):
        return False, "Function 'ab_test' not found"
    r = module.ab_test()
    if 'model_a' not in r or 'model_b' not in r:
        return False, "Missing model_a or model_b keys"
    total = r['model_a']['count'] + r['model_b']['count']
    if total != 100:
        return False, f"Expected 100 total, got {total}"
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
        print("  LEVEL 10 — AUTO-CHECK ALL")
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
