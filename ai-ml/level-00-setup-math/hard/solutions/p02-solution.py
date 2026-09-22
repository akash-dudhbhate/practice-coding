"""Level 00 — Setup & Math — Hard P02 Solution"""

def bayes(prior, sensitivity, false_positive_rate):
    numerator = sensitivity * prior
    denominator = numerator + false_positive_rate * (1 - prior)
    return numerator / denominator

if __name__ == "__main__":
    p = bayes(0.01, 0.95, 0.10)
    print(f"{p:.4f}")
