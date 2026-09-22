"""Solution — medium/p02"""


def simulate(x, truth, w, b, step, rounds):
    ws = []
    for _ in range(rounds):
        res = w * x + b - truth
        w = w - step * res * x
        b = b - step * res
        ws.append(w)
    return ws
