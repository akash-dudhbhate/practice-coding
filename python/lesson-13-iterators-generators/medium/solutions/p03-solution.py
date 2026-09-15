"""SOLUTION: Generator Pipeline (Medium)"""
def generate_nums(n):
    for i in range(1, n + 1):
        yield i

def filter_multiples_of_3(gen):
    for x in gen:
        if x % 3 == 0:
            yield x

def square_them(gen):
    for x in gen:
        yield x * x

def take_first(gen, n):
    for i, x in enumerate(gen):
        if i >= n:
            break
        yield x

if __name__ == "__main__":
    pipeline = take_first(square_them(filter_multiples_of_3(generate_nums(100))), 5)
    assert list(pipeline) == [9, 36, 81, 144, 225]
    print("All tests passed!")
