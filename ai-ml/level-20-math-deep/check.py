"""
Level 20 Checker — Deep Math for ML
====================================
Runs each check function against your work file.
Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import importlib.util, os, sys, glob


def load_mod(fp):
    spec = importlib.util.spec_from_file_location("work", fp)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def check_easy_p01(mod):
    import numpy as np
    if not hasattr(mod, 'eigendecompose'):
        return False, "Function 'eigendecompose' not found"
    A = np.array([[4.0, 1.0, 0.0], [1.0, 3.0, 0.0], [0.0, 0.0, 2.0]])
    vals, vecs = mod.eigendecompose(A)
    if vals.shape != (3,) or vecs.shape != (3, 3):
        return False, f"Bad shapes: vals {vals.shape}, vecs {vecs.shape}"
    if not np.all(np.diff(vals) <= 1e-9):
        return False, f"Eigenvalues not sorted descending: {vals}"
    # A v = λ v for every eigenpair
    for i in range(3):
        if not np.allclose(A @ vecs[:, i], vals[i] * vecs[:, i], atol=1e-8):
            return False, f"Eigenpair {i} fails A·v = λ·v"
    # symmetric A → orthonormal eigenvectors
    if not np.allclose(vecs.T @ vecs, np.eye(3), atol=1e-8):
        return False, "Eigenvectors not orthonormal"
    if not np.isclose(vals[0], 4.6180339887, atol=1e-6):
        return False, f"Top eigenvalue wrong: {vals[0]}"
    return True, "All tests passed!"


def check_easy_p02(mod):
    import numpy as np
    if not hasattr(mod, 'project'):
        return False, "Function 'project' not found"
    out = mod.project(np.array([3.0, 4.0]), np.array([1.0, 0.0]))
    if not np.allclose(out, [3.0, 0.0]):
        return False, f"project([3,4],[1,0]) should be [3,0], got {out}"
    out = mod.project(np.array([1.0, 1.0]), np.array([2.0, 0.0]))
    if not np.allclose(out, [1.0, 0.0]):
        return False, f"project([1,1],[2,0]) should be [1,0], got {out}"
    # projection must be parallel to u: residual perpendicular
    v = np.array([1.0, 2.0, 3.0]); u = np.array([1.0, 1.0, 1.0])
    p = mod.project(v, u)
    if not np.isclose(np.dot(v - p, u), 0.0, atol=1e-8):
        return False, "Residual (v - proj) should be perpendicular to u"
    return True, "All tests passed!"


def check_easy_p03(mod):
    import numpy as np
    if not hasattr(mod, 'entropy'):
        return False, "Function 'entropy' not found"
    if not np.isclose(mod.entropy(np.array([0.5, 0.5])), 1.0):
        return False, "entropy([0.5,0.5]) should be 1.0"
    if not np.isclose(mod.entropy(np.array([0.25] * 4)), 2.0):
        return False, "entropy([0.25]*4) should be 2.0"
    e = mod.entropy(np.array([1.0, 0.0, 0.0]))
    if not np.isfinite(e) or not np.isclose(e, 0.0):
        return False, f"entropy([1,0,0]) should be 0.0 (handle zeros), got {e}"
    e = mod.entropy(np.array([0.9, 0.1]))
    if not np.isclose(e, 0.4689956, atol=1e-5):
        return False, f"entropy([0.9,0.1]) should be ~0.469, got {e}"
    return True, "All tests passed!"


def check_medium_p01(mod):
    import numpy as np
    if not hasattr(mod, 'pca_scratch'):
        return False, "Function 'pca_scratch' not found"
    np.random.seed(42)
    X = np.random.randn(100, 3) @ np.diag([2.0, 1.0, 0.1])
    Z = mod.pca_scratch(X, 2)
    if Z.shape != (100, 2):
        return False, f"Expected (100,2), got {Z.shape}"
    var = Z.var(axis=0)
    if var[0] < var[1]:
        return False, f"PC1 should have max variance, got {var}"
    # PC1 should capture the majority of total variance (built ~4:1:0.04)
    total_var = (X - X.mean(axis=0)).var(axis=0).sum()
    if var[0] / total_var < 0.5:
        return False, f"PC1 explains too little variance: {var[0]/total_var:.3f}"
    # k=3: full rotation preserves total variance exactly
    Z3 = mod.pca_scratch(X, 3)
    if Z3.shape != (100, 3):
        return False, f"Expected (100,3) for k=3, got {Z3.shape}"
    if not np.isclose(Z3.var(axis=0).sum(), total_var, rtol=0.01):
        return False, "k=3 should preserve total variance (PCA is a rotation)"
    return True, "All tests passed!"


def check_medium_p02(mod):
    import numpy as np
    if not hasattr(mod, 'gradient_descent'):
        return False, "Function 'gradient_descent' not found"
    f = lambda x: (x - 3.0) ** 2
    df = lambda x: 2.0 * (x - 3.0)
    x, hist = mod.gradient_descent(f, df, 0.0, lr=0.1, iters=50)
    if len(hist) != 50:
        return False, f"history should have 50 entries, got {len(hist)}"
    if not np.isclose(float(x), 3.0, atol=1e-3):
        return False, f"x should converge to 3.0, got {x}"
    if hist[-1] >= hist[0]:
        return False, f"loss did not decrease: {hist[0]} → {hist[-1]}"
    # vector input
    fv = lambda x: float(np.sum((x - 1.0) ** 2))
    dfv = lambda x: 2.0 * (x - 1.0)
    xv, _ = mod.gradient_descent(fv, dfv, np.zeros(3), lr=0.1, iters=100)
    if not np.allclose(xv, 1.0, atol=1e-3):
        return False, f"vector GD failed, got {xv}"
    return True, "All tests passed!"


def check_medium_p03(mod):
    import numpy as np
    if not hasattr(mod, 'svd_compress'):
        return False, "Function 'svd_compress' not found"
    np.random.seed(42)
    A = np.random.randn(10, 8)
    A_hat, ratio = mod.svd_compress(A, 3)
    if A_hat.shape != (10, 8):
        return False, f"Expected (10,8), got {A_hat.shape}"
    if not np.isclose(ratio, 3 * (10 + 8 + 1) / 80, atol=1e-9):
        return False, f"ratio should be {3*19/80}, got {ratio}"
    # rank-3 approx of full-rank noise should beat rank-1
    A1, _ = mod.svd_compress(A, 1)
    if np.linalg.norm(A - A_hat) >= np.linalg.norm(A - A1):
        return False, "higher k should give lower reconstruction error"
    # low-rank matrix: k=2 reconstructs exactly
    B = np.random.randn(10, 2) @ np.random.randn(2, 8)
    B_hat, _ = mod.svd_compress(B, 2)
    if not np.allclose(B, B_hat, atol=1e-8):
        return False, "rank-2 matrix should reconstruct ~exactly at k=2"
    return True, "All tests passed!"


def check_hard_p01(mod):
    import numpy as np
    if not hasattr(mod, 'newton_sqrt'):
        return False, "Function 'newton_sqrt' not found"
    r, it = mod.newton_sqrt(2.0, 1.0)
    if not np.isclose(r, np.sqrt(2.0), atol=1e-10):
        return False, f"sqrt(2) wrong: {r}"
    if it > 10:
        return False, f"Newton should converge fast, took {it} iters"
    r2, _ = mod.newton_sqrt(144.0, 10.0)
    if not np.isclose(r2, 12.0, atol=1e-8):
        return False, f"sqrt(144) should be 12, got {r2}"
    return True, "All tests passed!"


def check_hard_p02(mod):
    import numpy as np
    if not hasattr(mod, 'kl_divergence'):
        return False, "Function 'kl_divergence' not found"
    p = np.array([0.5, 0.5]); q = np.array([0.25, 0.75])
    if not np.isclose(mod.kl_divergence(p, p), 0.0, atol=1e-9):
        return False, "KL(p||p) should be 0"
    if not np.isclose(mod.kl_divergence(p, q), 0.2075187, atol=1e-5):
        return False, f"KL([.5,.5]||[.25,.75]) should be ~0.2075, got {mod.kl_divergence(p, q)}"
    # zero in p must be skipped (not NaN)
    r = mod.kl_divergence(np.array([0.0, 1.0]), np.array([0.5, 0.5]))
    if not np.isclose(r, 1.0, atol=1e-9):
        return False, f"KL([0,1]||[.5,.5]) should be 1.0, got {r}"
    # zero in q where p > 0 → inf
    r = mod.kl_divergence(np.array([0.5, 0.5]), np.array([1.0, 0.0]))
    if not np.isinf(r):
        return False, f"KL should be inf when q=0 but p>0, got {r}"
    # asymmetry check value
    if not np.isclose(mod.kl_divergence(q, p), 0.1887219, atol=1e-5):
        return False, f"KL([.25,.75]||[.5,.5]) should be ~0.1887"
    return True, "All tests passed!"


def check_hard_p03(mod):
    import numpy as np
    if not hasattr(mod, 'adam_optimize'):
        return False, "Function 'adam_optimize' not found"
    f = lambda x: float(np.sum((x - 3.0) ** 2))
    df = lambda x: 2.0 * (x - 3.0)
    x, hist = mod.adam_optimize(f, df, np.zeros(4), lr=0.1, iters=300)
    if len(hist) != 300:
        return False, f"history should have 300 entries, got {len(hist)}"
    if not np.allclose(x, 3.0, atol=1e-2):
        return False, f"x should converge to 3.0, got {x}"
    if hist[-1] >= hist[0]:
        return False, "loss did not decrease"
    # scalar input should also work
    xs, hs = mod.adam_optimize(lambda x: (x - 2.0) ** 2,
                             lambda x: 2.0 * (x - 2.0),
                             0.0, lr=0.05, iters=300)
    if not np.isclose(float(xs), 2.0, atol=1e-2):
        return False, f"scalar Adam failed, got {xs}"
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
    t = sys.argv[1]
    if t == "all":
        [run_one(c) for c in sorted(CHECKS)]; return
    run_one(t)


def run_one(cid):
    if cid not in CHECKS:
        print(f"Unknown: {cid}"); return
    diff, num = cid.split("/"); nc = num.lstrip("p")
    d = os.path.join(os.path.dirname(__file__), diff)
    ms = [f for f in glob.glob(os.path.join(d, f"p{nc}-*.py")) if "solutions" not in f]
    w = ms[0] if ms else None
    if not w:
        print(f"{cid}: FILE NOT FOUND"); return
    try:
        mod = load_mod(w); passed, msg = CHECKS[cid](mod)
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
