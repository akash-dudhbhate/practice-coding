"""Level 00 — Setup & Math — Medium P01 Solution"""

def weighted_sum(inputs, weights, bias):
    return sum(x * w for x, w in zip(inputs, weights)) + bias

if __name__ == "__main__":
    print(weighted_sum([2, 3], [0.5, 1.5], 1))
    print(weighted_sum([1, 1], [2, 2], 0))
