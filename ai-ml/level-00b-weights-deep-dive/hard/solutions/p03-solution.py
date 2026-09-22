"""Solution — hard/p03"""


def fit_multi(data, step, rounds):
    n_feats = len(data[0][0])
    ws = [0.0] * n_feats
    b = 0.0
    for _ in range(rounds):
        res_sum = 0.0
        resx_sum = [0.0] * n_feats
        for xs, truth in data:
            res = sum(w * x for w, x in zip(ws, xs)) + b - truth
            res_sum += res
            for i in range(n_feats):
                resx_sum[i] += res * xs[i]
        n = len(data)
        for i in range(n_feats):
            ws[i] -= step * resx_sum[i] / n
        b -= step * res_sum / n
    return ws, b
