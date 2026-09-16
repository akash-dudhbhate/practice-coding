"""Level 08 — Neural Networks — Easy P03 Solution"""

import torch

def tensor_basics():
    a = torch.tensor([1., 2., 3.], requires_grad=True)
    b = torch.tensor([4., 5., 6.])
    s = a + b
    p = a * b
    d = torch.dot(a, b).item()
    return s, p, d

if __name__ == "__main__":
    s, p, d = tensor_basics()
    print(s)
    print(p)
    print(d)
