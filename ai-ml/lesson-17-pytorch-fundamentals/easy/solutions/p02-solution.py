"""
Autograd: automatic differentiation
====================================
Create a tensor with requires_grad=True. Compute y = x^3 + 2x^2 + 1.
Call backward(). Print the gradient (should be 3x^2 + 4x). Verify manually.
"""

import torch


if __name__ == "__main__":
    # Create a tensor with gradient tracking enabled
    x = torch.tensor([2.0], requires_grad=True)
    print(f"x = {x.item()}, requires_grad = {x.requires_grad}")

    # Define y = x^3 + 2x^2 + 1
    y = x**3 + 2 * x**2 + 1
    print(f"y = x^3 + 2x^2 + 1 = {y.item():.4f}")

    # Backward pass — computes dy/dx
    y.backward()

    # PyTorch computed gradient
    auto_grad = x.grad.item()
    print(f"\nAutograd dy/dx = {auto_grad:.4f}")

    # Manual verification: derivative of x^3 + 2x^2 + 1 is 3x^2 + 4x
    x_val = 2.0
    manual_grad = 3 * x_val**2 + 4 * x_val
    print(f"Manual  dy/dx = 3x^2 + 4x = 3*{x_val}^2 + 4*{x_val} = {manual_grad:.4f}")

    # Verify they match
    print(f"\nMatch: {torch.isclose(torch.tensor(auto_grad), torch.tensor(manual_grad))}")
    print(f"\nExplanation: d/dx(x^3) = 3x^2, d/dx(2x^2) = 4x, d/dx(1) = 0")
    print(f"  So dy/dx = 3x^2 + 4x. At x=2: 3(4) + 4(2) = 12 + 8 = 20.")
