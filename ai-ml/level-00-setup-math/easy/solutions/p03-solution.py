"""Level 00 — Setup & Math — Easy P03 Solution"""

def stats(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    std = variance ** 0.5
    return mean, variance, std

if __name__ == "__main__":
    m, v, s = stats([2, 4, 6])
    print(f"{m:.2f} {v:.2f} {s:.2f}")
