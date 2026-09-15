"""
Tensor basics: creation, shapes, dtypes, devices, operations
=============================================================
Create 1D, 2D, 3D tensors. Print shapes, dtypes, devices.
Perform addition, multiplication, matrix multiplication.
Convert between PyTorch and NumPy.
"""

import torch
import numpy as np


if __name__ == "__main__":
    print("=" * 60)
    print("Tensor Creation: 1D, 2D, 3D")
    print("=" * 60)

    # 1D tensor
    t1 = torch.tensor([1.0, 2.0, 3.0, 4.0])
    print(f"\n1D tensor: {t1}")
    print(f"  Shape: {t1.shape}, dtype: {t1.dtype}, device: {t1.device}")

    # 2D tensor (matrix)
    t2 = torch.tensor([[1, 2], [3, 4], [5, 6]], dtype=torch.float32)
    print(f"\n2D tensor:\n{t2}")
    print(f"  Shape: {t2.shape}, dtype: {t2.dtype}, device: {t2.device}")

    # 3D tensor
    t3 = torch.zeros(2, 3, 4)
    print(f"\n3D tensor (zeros):")
    print(f"  Shape: {t3.shape}, dtype: {t3.dtype}, device: {t3.device}")

    # --- Operations ---
    print(f"\n{'=' * 60}")
    print("Operations")
    print("=" * 60)

    a = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
    b = torch.tensor([[5.0, 6.0], [7.0, 8.0]])

    print(f"\nTensor a:\n{a}")
    print(f"Tensor b:\n{b}")

    # Element-wise addition
    print(f"\nAddition (a + b):\n{a + b}")

    # Element-wise multiplication (Hadamard)
    print(f"\nElement-wise multiplication (a * b):\n{a * b}")

    # Matrix multiplication
    print(f"\nMatrix multiplication (a @ b):\n{a @ b}")
    print(f"  (Also torch.matmul(a, b):\n{torch.matmul(a, b)})")

    # --- PyTorch <-> NumPy conversion ---
    print(f"\n{'=' * 60}")
    print("PyTorch <-> NumPy Conversion")
    print("=" * 60)

    # PyTorch to NumPy
    t = torch.tensor([1.0, 2.0, 3.0])
    n = t.numpy()
    print(f"\nPyTorch tensor: {t} (type: {type(t)})")
    print(f"Converted to NumPy: {n} (type: {type(n)})")
    print(f"  Note: Shares memory with CPU tensor — modifying one affects the other.")

    # NumPy to PyTorch
    arr = np.array([4.0, 5.0, 6.0])
    t_from_np = torch.from_numpy(arr)
    print(f"\nNumPy array: {arr} (type: {type(arr)})")
    print(f"Converted to PyTorch: {t_from_np} (type: {type(t_from_np)})")

    # Verify shared memory
    arr[0] = 99.0
    print(f"\nAfter modifying NumPy arr[0]=99: PyTorch tensor = {t_from_np}")
    print(f"  (Confirms shared memory on CPU)")
