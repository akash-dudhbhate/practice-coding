"""
Auto-Check System — Level 17 (Fine-Tuning / LoRA)
=================================================
Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import importlib.util, os, sys, glob


def load_mod(fp):
    spec = importlib.util.spec_from_file_location("work", fp)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _data():
    """Shared dataset: 200 samples, 8 features, 3 classes → 150/50 split."""
    import torch
    from sklearn.datasets import make_classification
    X, y = make_classification(n_samples=200, n_features=8, n_classes=3,
                               n_informative=6, n_clusters_per_class=1,
                               class_sep=1.5, random_state=42)
    X = torch.tensor(X, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.long)
    return X[:150], y[:150], X[150:], y[150:]


def _new_task():
    """A conflicting 'new task' dataset for the forgetting check."""
    import torch
    from sklearn.datasets import make_classification
    X, y = make_classification(n_samples=150, n_features=8, n_classes=3,
                               n_informative=6, n_clusters_per_class=1,
                               class_sep=1.5, random_state=7)
    return torch.tensor(X, dtype=torch.float32), torch.tensor(y, dtype=torch.long)


def _base_model():
    import torch, torch.nn as nn
    torch.manual_seed(42)
    return nn.Sequential(nn.Linear(8, 32), nn.ReLU(), nn.Linear(32, 3))


def check_easy_p01(module):
    import torch
    if not hasattr(module, 'freeze_backbone'):
        return False, "Function 'freeze_backbone' not found"
    model = _base_model()
    n = module.freeze_backbone(model)
    if n != 99:
        return False, f"Expected 99 trainable params (32*3+3), got {n}"
    if model[0].weight.requires_grad or model[0].bias.requires_grad:
        return False, "Backbone params should be frozen"
    if not model[2].weight.requires_grad:
        return False, "Last layer should stay trainable"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'count_trainable'):
        return False, "Function 'count_trainable' not found"
    model = _base_model()
    total, trainable = module.count_trainable(model)
    if total != 387 or trainable != 387:
        return False, f"Fresh model: expected (387, 387), got ({total}, {trainable})"
    for p in model[0].parameters():
        p.requires_grad_(False)
    total2, trainable2 = module.count_trainable(model)
    if total2 != 387 or trainable2 != 99:
        return False, f"After freezing: expected (387, 99), got ({total2}, {trainable2})"
    return True, "All tests passed!"


def check_easy_p03(module):
    import torch
    if not hasattr(module, 'replace_head'):
        return False, "Function 'replace_head' not found"
    model = _base_model()
    w0 = model[0].weight.clone()
    model = module.replace_head(model, 5)
    if model[-1].out_features != 5 or model[-1].in_features != 32:
        return False, f"Head should be Linear(32, 5), got {model[-1]}"
    out = model(torch.randn(4, 8))
    if tuple(out.shape) != (4, 5):
        return False, f"Forward output should be (4, 5), got {tuple(out.shape)}"
    if not torch.equal(model[0].weight, w0):
        return False, "Backbone weights should be untouched"
    if not model[-1].weight.requires_grad:
        return False, "New head should be trainable"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'feature_extract_finetune'):
        return False, "Function 'feature_extract_finetune' not found"
    X_tr, y_tr, X_te, y_te = _data()
    acc = module.feature_extract_finetune(X_tr, y_tr, X_te, y_te)
    if not isinstance(acc, float):
        acc = float(acc)
    if not (0.0 <= acc <= 1.0):
        return False, f"Accuracy should be in [0,1], got {acc}"
    if acc < 0.85:
        return False, f"Head-only accuracy too low: {acc:.3f} (expected ≥0.85)"
    return True, f"All tests passed! (test acc={acc:.3f})"


def check_medium_p02(module):
    import torch
    if not hasattr(module, 'lora_linear'):
        return False, "Function 'lora_linear' not found"
    layer = module.lora_linear(8, 32, 4)
    out = layer(torch.randn(5, 8))
    if tuple(out.shape) != (5, 32):
        return False, f"Output shape should be (5, 32), got {tuple(out.shape)}"
    trainable = sum(p.numel() for p in layer.parameters() if p.requires_grad)
    total = sum(p.numel() for p in layer.parameters())
    if trainable != 160:
        return False, f"Expected 160 trainable params (4*8 + 32*4), got {trainable}"
    if total != 448:
        return False, f"Expected 448 total params (base 288 + adapter 160), got {total}"
    # At init the adapter must contribute nothing (B = 0)
    x = torch.randn(3, 8)
    with torch.no_grad():
        base_out = x @ layer.base.weight.T + layer.base.bias
        if not torch.allclose(layer(x), base_out, atol=1e-5):
            return False, "With B=0, output should equal base Linear output"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'full_vs_head'):
        return False, "Function 'full_vs_head' not found"
    X_tr, y_tr, X_te, y_te = _data()
    result = module.full_vs_head(X_tr, y_tr, X_te, y_te)
    if not isinstance(result, tuple) or len(result) != 2:
        return False, f"Should return (full_acc, head_acc), got {result}"
    full_acc, head_acc = float(result[0]), float(result[1])
    if full_acc < 0.85:
        return False, f"Full FT acc too low: {full_acc:.3f} (expected ≥0.85)"
    if head_acc < 0.85:
        return False, f"Head-only acc too low: {head_acc:.3f} (expected ≥0.85)"
    return True, f"All tests passed! (full={full_acc:.3f}, head={head_acc:.3f})"


def check_hard_p01(module):
    if not hasattr(module, 'lora_finetune'):
        return False, "Function 'lora_finetune' not found"
    X_tr, y_tr, X_te, y_te = _data()
    acc = float(module.lora_finetune(X_tr, y_tr, X_te, y_te, rank=4))
    if not (0.0 <= acc <= 1.0):
        return False, f"Accuracy should be in [0,1], got {acc}"
    if acc < 0.85:
        return False, f"LoRA accuracy too low: {acc:.3f} (expected ≥0.85)"
    return True, f"All tests passed! (test acc={acc:.3f})"


def check_hard_p02(module):
    if not hasattr(module, 'param_efficiency'):
        return False, "Function 'param_efficiency' not found"
    model = _base_model()
    lora_model = _base_model()
    for p in lora_model[0].parameters():
        p.requires_grad_(False)
    r = module.param_efficiency(model, lora_model)
    if not isinstance(r, dict):
        return False, f"Should return a dict, got {type(r)}"
    for key in ('full_trainable', 'lora_trainable', 'ratio'):
        if key not in r:
            return False, f"Missing key '{key}'"
    if r['full_trainable'] != 387:
        return False, f"full_trainable should be 387, got {r['full_trainable']}"
    if r['lora_trainable'] != 99:
        return False, f"lora_trainable should be 99, got {r['lora_trainable']}"
    if abs(r['ratio'] - 99 / 387) > 0.001:
        return False, f"ratio should be ~{99/387:.4f}, got {r['ratio']}"
    return True, "All tests passed!"


def check_hard_p03(module):
    import torch
    if not hasattr(module, 'catastrophic_forgetting'):
        return False, "Function 'catastrophic_forgetting' not found"
    from sklearn.datasets import make_classification
    X, y = make_classification(n_samples=200, n_features=8, n_classes=3,
                               n_informative=6, n_clusters_per_class=1,
                               class_sep=1.5, random_state=42)
    orig = (torch.tensor(X, dtype=torch.float32),
            torch.tensor(y, dtype=torch.long))
    new = _new_task()
    r = module.catastrophic_forgetting(orig, new)
    if not isinstance(r, dict):
        return False, f"Should return a dict, got {type(r)}"
    for key in ('orig_before', 'after_full', 'after_lora', 'lora_recovered'):
        if key not in r:
            return False, f"Missing key '{key}'"
    r = {k: float(v) for k, v in r.items()}
    if r['orig_before'] < 0.85:
        return False, f"Pretrained orig acc too low: {r['orig_before']:.3f}"
    if r['after_full'] >= r['orig_before'] - 0.3:
        return False, (f"Full FT should forget: orig {r['orig_before']:.2f} → "
                       f"{r['after_full']:.2f} (expected drop ≥0.3)")
    if r['lora_recovered'] < r['orig_before'] - 0.05:
        return False, (f"Removing LoRA adapter should restore orig acc: "
                       f"got {r['lora_recovered']:.2f} vs {r['orig_before']:.2f}")
    if r['lora_recovered'] <= r['after_full'] + 0.3:
        return False, (f"Recovered acc ({r['lora_recovered']:.2f}) should beat "
                       f"post-full-FT acc ({r['after_full']:.2f}) by ≥0.3")
    return True, (f"All tests passed! (before={r['orig_before']:.2f}, "
                  f"full→{r['after_full']:.2f}, recovered→{r['lora_recovered']:.2f})")


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
        print("Usage: python3 check.py <difficulty/pXX> or 'all'")
        return
    t = sys.argv[1]
    if t == "all":
        [run_one(c) for c in sorted(CHECKS)]
        return
    run_one(t)


def run_one(cid):
    if cid not in CHECKS:
        print(f"Unknown: {cid}")
        return
    diff, num = cid.split("/")
    nc = num.lstrip("p")
    d = os.path.join(os.path.dirname(__file__), diff)
    ms = [f for f in glob.glob(os.path.join(d, f"p{nc}-*.py"))
          if "solutions" not in f]
    w = ms[0] if ms else None
    if not w:
        print(f"{cid}: FILE NOT FOUND")
        return
    try:
        mod = load_mod(w)
        passed, msg = CHECKS[cid](mod)
        print(f"{cid}: {'PASS' if passed else 'FAIL'} — {msg}")
        if passed:
            with open(w) as f:
                if "DONE" not in f.readline().strip():
                    print("  → add '# DONE' to mark complete")
    except Exception as e:
        if "NoneType" in str(e):
            print(f"FAIL — a function returned None — write the body!")
        else:
            print(f"{cid}: ERROR — {e}")


if __name__ == "__main__":
    main()
