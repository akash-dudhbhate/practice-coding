"""
SOLUTION: Find The Bottleneck (Medium)
==============================
The program's Big-O is the Big-O of its largest phase.
"""
import math

def phase_ops(n: int) -> dict:
    return {
        "linear": n,
        "nlogn": int(n * math.log2(n)) if n > 0 else 0,
        "quadratic": n * n,
    }

def bottleneck_phase(n: int) -> str:
    phases = phase_ops(n)
    return max(phases, key=phases.get)

if __name__ == "__main__":
    assert phase_ops(8) == {"linear": 8, "nlogn": 24, "quadratic": 64}
    assert bottleneck_phase(8) == "quadratic"
    assert bottleneck_phase(2) == "quadratic"
    print("All tests passed!")
