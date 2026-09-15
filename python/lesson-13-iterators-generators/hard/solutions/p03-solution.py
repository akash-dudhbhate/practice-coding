"""SOLUTION: Cycle Forever Generator (Hard)"""
def cycle_forever(iterable):
    items = list(iterable)
    if not items:
        return
    while True:
        for item in items:
            yield item

if __name__ == "__main__":
    from itertools import islice
    c = cycle_forever(["a", "b", "c"])
    result = list(islice(c, 7))
    assert result == ["a", "b", "c", "a", "b", "c", "a"]
    # Round-robin assignment
    workers = ["w1", "w2", "w3"]
    tasks = ["t1", "t2", "t3", "t4", "t5", "t6", "t7"]
    assigner = cycle_forever(workers)
    assignments = {w: [] for w in workers}
    for task in tasks:
        w = next(assigner)
        assignments[w].append(task)
    assert "t1" in assignments["w1"]
    assert "t2" in assignments["w2"]
    print("All tests passed!")
