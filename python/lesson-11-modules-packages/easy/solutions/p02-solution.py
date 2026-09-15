"""SOLUTION: Import math and random (Easy)"""
import math
import random

if __name__ == "__main__":
    nums = [random.randint(1, 100) for _ in range(3)]
    for n in nums:
        print(f"sqrt({n}) = {math.sqrt(n):.2f}")
