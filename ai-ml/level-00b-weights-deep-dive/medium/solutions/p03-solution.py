"""Solution — medium/p03"""


def batch_step(data, w, b, step):
    res_sum, resx_sum = 0.0, 0.0
    for x, truth in data:
        res = w * x + b - truth
        res_sum += res
        resx_sum += res * x
    n = len(data)
    return w - step * resx_sum / n, b - step * res_sum / n
