"""Solution — hard/p02"""


def predict_multi(features, weights, bias):
    return sum(w * x for w, x in zip(weights, features)) + bias
