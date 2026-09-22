"""Solution — easy/p03"""


def loss(data, w, b):
    total = 0.0
    for x, truth in data:
        res = w * x + b - truth
        total += res * res
    return total
