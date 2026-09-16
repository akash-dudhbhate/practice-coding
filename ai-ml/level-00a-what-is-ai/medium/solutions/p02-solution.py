"""Solution — medium/p02-prediction.py"""


def predict_price(size, rooms, age):
    return size * 0.15 + rooms * 5.0 + age * (-0.5) + 10.0
