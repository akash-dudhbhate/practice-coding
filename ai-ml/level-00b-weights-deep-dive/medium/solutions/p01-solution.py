"""Solution — medium/p01"""


def train_step(x, truth, w, b, step):
    res = w * x + b - truth
    return w - step * res * x, b - step * res
