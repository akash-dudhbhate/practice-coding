"""Level 00 — Setup & Math — Hard P01 Solution"""

def descend(x0, lr, steps):
    path = [x0]
    x = x0
    for _ in range(steps):
        x = x - lr * (2 * x)   # f(x) = x², f'(x) = 2x
        path.append(x)
    return path

if __name__ == "__main__":
    path = descend(5.0, 0.1, 20)
    print(f"{path[0]:.2f} -> {path[-1]:.4f}")
