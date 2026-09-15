"""SOLUTION: Generator Pipeline (Hard)"""
def filter_positive(data):
    return (x for x in data if x > 0)

def double(data):
    return (x * 2 for x in data)

def to_strings(data):
    return (str(x) for x in data)

def pipeline(data):
    return list(to_strings(double(filter_positive(data))))

if __name__ == "__main__":
    assert pipeline([-1, 2, -3, 4]) == ["4", "8"]
    assert pipeline([]) == []
    print("All tests passed!")
