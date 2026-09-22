"""Level 19 — MLOps — Hard P03 Solution"""


def ci_gate(metrics, thresholds):
    """Check metrics against thresholds. Returns pass/fail report."""
    failures = []
    for name, required in thresholds.items():
        if name not in metrics:
            failures.append(f"missing metric: {name}")
        elif metrics[name] < required:
            failures.append(f"{name}: {metrics[name]} < {required}")
    return {"pass": len(failures) == 0, "failures": failures}


if __name__ == "__main__":
    print(ci_gate({"accuracy": 0.9, "f1": 0.85},
                  {"accuracy": 0.8, "f1": 0.8}))
    print(ci_gate({"accuracy": 0.9, "f1": 0.85},
                  {"accuracy": 0.8, "f1": 0.9}))
