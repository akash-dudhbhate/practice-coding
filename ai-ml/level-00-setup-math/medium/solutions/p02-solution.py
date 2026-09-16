"""Level 00 — Setup & Math — Medium P02 Solution"""

def normalize(data):
    mn, mx = min(data), max(data)
    if mx == mn:
        return [0.0] * len(data)
    return [(x - mn) / (mx - mn) for x in data]

if __name__ == "__main__":
    print(normalize([10, 20, 30]))
    print(normalize([5, 5, 5]))
