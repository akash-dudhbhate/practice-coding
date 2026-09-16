"""Level 00 — Setup & Math — Easy P02 Solution"""

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

if __name__ == "__main__":
    print(dot([1, 2, 3], [4, 5, 6]))
    print(dot([0, 1], [5, 5]))
    print(dot([2, 0, 2], [1, 1, 1]))
