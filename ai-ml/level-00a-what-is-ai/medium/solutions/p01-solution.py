"""Solution — medium/p01-training-loop.py"""


def train_one_step(weight, input_val, true_answer, step):
    prediction = weight * input_val
    error = true_answer - prediction
    return weight + step * error / input_val
