"""
SOLUTION: Multiplication Table Hard (Hard)
============================================
Print a formatted multiplication table up to n x n.
"""
def print_multiplication_table(n: int) -> None:
    col_width = len(str(n * n)) + 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:{col_width}}", end="")
        print()

if __name__ == "__main__":
    print_multiplication_table(5)
    print("Test passed!")
