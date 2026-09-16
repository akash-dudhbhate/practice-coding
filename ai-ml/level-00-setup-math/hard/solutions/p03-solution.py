"""Level 00 — Setup & Math — Hard P03 Solution"""

def matmul(A, B):
    rows_a = len(A)
    cols_b = len(B[0])
    inner = len(B)
    return [[sum(A[i][k] * B[k][j] for k in range(inner))
             for j in range(cols_b)] for i in range(rows_a)]

if __name__ == "__main__":
    print(matmul([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
