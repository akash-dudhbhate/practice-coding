"""
Auto-Check System — Level 15 (Transformers from Scratch)
=========================================================
Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import importlib.util, os, sys, glob
import numpy as np


def load_mod(fp):
    spec = importlib.util.spec_from_file_location("sol", fp)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# ---------- reference helpers (used to verify real behavior) ----------

def _softmax(s):
    s = np.asarray(s, dtype=float)
    e = np.exp(s - s.max())
    return e / e.sum()


def _attention_ref(Q, K, V):
    d = Q.shape[1]
    w = np.stack([_softmax(r) for r in (Q @ K.T / np.sqrt(d))])
    return w @ V


def _layernorm_ref(x, eps=1e-6):
    return (x - x.mean(axis=-1, keepdims=True)) / np.sqrt(x.var(axis=-1, keepdims=True) + eps)


def _block_ref(X, p):
    a = _attention_ref(X @ p["W_q"], X @ p["W_k"], X @ p["W_v"])
    X1 = _layernorm_ref(X + a)
    ffn = np.maximum(0, X1 @ p["W1"] + p["b1"]) @ p["W2"] + p["b2"]
    return _layernorm_ref(X1 + ffn)


# ---------- easy ----------

def check_easy_p01(mod):
    if not hasattr(mod, "tokenize"):
        return False, "Function 'tokenize' not found"
    r = list(mod.tokenize("the cat sat"))
    if r != [1, 2, 3]:
        return False, f"tokenize('the cat sat') expected [1,2,3], got {r}"
    r = list(mod.tokenize("a dog"))
    if r != [7, 6]:
        return False, f"tokenize('a dog') expected [7,6], got {r}"
    r = list(mod.tokenize("the bird sat"))
    if r != [1, 0, 3]:
        return False, f"unknown word should map to 0 (<unk>), got {r}"
    return True, "All tests passed!"


def check_easy_p02(mod):
    if not hasattr(mod, "embed"):
        return False, "Function 'embed' not found"
    emb = np.arange(12).reshape(4, 3).astype(float)
    out = np.asarray(mod.embed([1, 3], emb))
    if out.shape != (2, 3):
        return False, f"expected shape (2,3), got {out.shape}"
    if not np.allclose(out, emb[[1, 3]]):
        return False, f"wrong vectors: {out}"
    out2 = np.asarray(mod.embed([3, 1, 1], emb))
    if out2.shape != (3, 3) or not np.allclose(out2, emb[[3, 1, 1]]):
        return False, "order/repeat handling wrong"
    return True, "All tests passed!"


def check_easy_p03(mod):
    if not hasattr(mod, "softmax_row"):
        return False, "Function 'softmax_row' not found"
    p = np.asarray(mod.softmax_row([1.0, 2.0, 3.0]))
    if p.shape != (3,):
        return False, f"expected shape (3,), got {p.shape}"
    if not np.allclose(p, [0.09, 0.2447, 0.6652], atol=1e-3):
        return False, f"wrong values: {p}"
    if not np.isclose(p.sum(), 1.0):
        return False, f"should sum to 1, got {p.sum()}"
    big = np.asarray(mod.softmax_row([1000.0, 1001.0]))
    if not np.all(np.isfinite(big)):
        return False, "overflowed on large scores — subtract the max first"
    if not np.isclose(big.sum(), 1.0):
        return False, "large-score softmax must still sum to 1"
    return True, "All tests passed!"


# ---------- medium ----------

def check_medium_p01(mod):
    if not hasattr(mod, "attention"):
        return False, "Function 'attention' not found"
    np.random.seed(0)
    Q = np.random.randn(2, 4)
    K = np.random.randn(2, 4)
    V = np.random.randn(2, 4)
    out = np.asarray(mod.attention(Q, K, V))
    if out.shape != (2, 4):
        return False, f"expected shape (2,4), got {out.shape}"
    ref = _attention_ref(Q, K, V)
    if not np.allclose(out, ref, atol=1e-6):
        return False, f"values wrong; expected\n{ref}\ngot\n{out}"
    # rows must be convex mixes of V rows -> bounded by V's min/max per col
    if not np.all(out <= V.max(axis=0) + 1e-6) or not np.all(out >= V.min(axis=0) - 1e-6):
        return False, "output rows should be weighted averages of V rows"
    return True, "All tests passed!"


def check_medium_p02(mod):
    if not hasattr(mod, "positional_encode"):
        return False, "Function 'positional_encode' not found"
    pe = np.asarray(mod.positional_encode(4, 6))
    if pe.shape != (4, 6):
        return False, f"expected shape (4,6), got {pe.shape}"
    if not np.allclose(pe[0], [0, 1, 0, 1, 0, 1], atol=1e-6):
        return False, f"row 0 should be [0 1 0 1 0 1], got {pe[0]}"
    if not np.isclose(pe[1, 0], 0.8415, atol=1e-3):
        return False, f"PE[1,0] should be sin(1)=0.8415, got {pe[1,0]}"
    if np.allclose(pe[0], pe[1]) or np.allclose(pe[1], pe[3]):
        return False, "different positions must get different encodings"
    return True, "All tests passed!"


def check_medium_p03(mod):
    if not hasattr(mod, "multi_head"):
        return False, "Function 'multi_head' not found"
    np.random.seed(1)
    X = np.random.randn(3, 8)
    W_q = np.random.randn(8, 8) * 0.1
    W_k = np.random.randn(8, 8) * 0.1
    W_v = np.random.randn(8, 8) * 0.1
    out = np.asarray(mod.multi_head(X, W_q, W_k, W_v))
    if out.shape != (3, 8):
        return False, f"expected shape (3,8), got {out.shape}"
    ref = _attention_ref(X @ W_q, X @ W_k, X @ W_v)
    if not np.allclose(out, ref, atol=1e-6):
        return False, "output doesn't match attention(X@W_q, X@W_k, X@W_v)"
    out2 = np.asarray(mod.multi_head(X, W_q, W_k, W_v * 2))
    if np.allclose(out, out2):
        return False, "changing W_v should change the output"
    return True, "All tests passed!"


# ---------- hard ----------

def check_hard_p01(mod):
    if not hasattr(mod, "transformer_block"):
        return False, "Function 'transformer_block' not found"
    np.random.seed(2)
    d = 8
    params = {
        "W_q": np.random.randn(d, d) * 0.1,
        "W_k": np.random.randn(d, d) * 0.1,
        "W_v": np.random.randn(d, d) * 0.1,
        "W1": np.random.randn(d, 16) * 0.1, "b1": np.zeros(16),
        "W2": np.random.randn(16, d) * 0.1, "b2": np.zeros(d),
    }
    X = np.random.randn(4, d)
    out = np.asarray(mod.transformer_block(X, params))
    if out.shape != X.shape:
        return False, f"expected shape {X.shape}, got {out.shape}"
    if not np.all(np.isfinite(out)):
        return False, "output contains non-finite values"
    ref = _block_ref(X, params)
    if not np.allclose(out, ref, atol=1e-5):
        return False, f"values wrong; expected row0 {ref[0]}, got {out[0]}"
    out2 = np.asarray(mod.transformer_block(X, params))
    if not np.allclose(out, out2):
        return False, "should be deterministic (same input -> same output)"
    return True, "All tests passed!"


def check_hard_p02(mod):
    if not hasattr(mod, "next_token_probs"):
        return False, "Function 'next_token_probs' not found"
    logits = np.array([2.0, 1.0, 0.1, -1.0])
    p1 = np.asarray(mod.next_token_probs(logits, 1.0))
    if p1.shape != (4,) or not np.isclose(p1.sum(), 1.0):
        return False, f"must return 4 probabilities summing to 1, got {p1}"
    if not np.allclose(p1, [0.6381, 0.2347, 0.0954, 0.0318], atol=1e-3):
        return False, f"T=1.0 values wrong: {p1}"
    if np.argmax(p1) != 0:
        return False, "argmax of probs should match argmax of logits"
    p_low = np.asarray(mod.next_token_probs(logits, 0.5))
    p_high = np.asarray(mod.next_token_probs(logits, 2.0))
    if not p_low[0] > p1[0]:
        return False, "T<1 should SHARPEN the distribution"
    if not (p_high.max() - p_high.min()) < (p1.max() - p1.min()):
        return False, "T>1 should FLATTEN the distribution"
    return True, "All tests passed!"


def check_hard_p03(mod):
    if not hasattr(mod, "generate"):
        return False, "Function 'generate' not found"
    VS = 10

    def toy(tokens):
        lg = np.zeros(VS)
        lg[(tokens[-1] + 1) % VS] = 5.0
        return lg

    r = list(mod.generate([3], toy, 4))
    if r != [3, 4, 5, 6, 7]:
        return False, f"expected [3,4,5,6,7], got {r}"
    r0 = list(mod.generate([5], toy, 0))
    if r0 != [5]:
        return False, "n=0 should return just the seed tokens"
    r2 = list(mod.generate([1, 9], toy, 2))
    if r2[:2] != [1, 9] or len(r2) != 4:
        return False, f"seed must be preserved and n tokens appended, got {r2}"
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
        print("Usage: python3 check.py <difficulty/pXX> or 'all'"); return
    target = sys.argv[1]
    if target == "all":
        for cid in sorted(CHECKS): run_one(cid)
        return
    run_one(target)


def run_one(check_id):
    if check_id not in CHECKS: print(f"Unknown: {check_id}"); return
    diff, num = check_id.split("/")
    num_clean = num.lstrip("p")
    d = os.path.join(os.path.dirname(__file__), diff)
    matches = [f for f in glob.glob(os.path.join(d, f"p{num_clean}-*.py")) if "solutions" not in f]
    work = matches[0] if matches else None
    if not work: print(f"{check_id}: FILE NOT FOUND"); return
    try:
        mod = load_mod(work)
        passed, msg = CHECKS[check_id](mod)
        print(f"{check_id}: {'PASS' if passed else 'FAIL'} — {msg}")
        if passed:
            with open(work) as f:
                if "DONE" not in f.readline().strip():
                    print("  → add '# DONE' to mark complete")
    except Exception as e:
        print(f"{check_id}: ERROR — {e}")


if __name__ == "__main__":
    main()
