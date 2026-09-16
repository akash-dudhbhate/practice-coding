"""Level 08 Neural Networks — Easy P03 Solution"""

import torch

def solve():
    # Create tensors
    a = torch.tensor([1.0, 2.0, 3.0])
    b = torch.tensor([4.0, 5.0, 6.0])
    print(f"a + b = {a + b}")
    print(f"a * b = {a * b}")
    print(f"dot product = {torch.dot(a, b)}")
    # Autograd
    x = torch.tensor(2.0, requires_grad=True)
    y = x ** 2 + 3 * x + 1
    y.backward()
    print(f"x = {x.item()}")
    print(f"dy/dx = {x.grad.item()}")
    return a, b, x

if __name__ == "__main__":
    solve()