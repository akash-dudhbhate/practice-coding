"""
SOLUTION: Sort By Multiple Keys (Medium)
============================================
Score desc + name asc can't be a single ascending tuple — but a
NEGATED number flips direction inside an ascending sort:
key=(-score, name). Equivalent stable alternative: sort by name
first, then by score descending — stability keeps the name order
inside equal-score ties.
"""
def sort_students(records: list) -> list:
    return sorted(records, key=lambda r: (-r[1], r[0]))


def sort_students_stable(records: list) -> list:
    by_name = sorted(records, key=lambda r: r[0])          # secondary first
    return sorted(by_name, key=lambda r: -r[1])            # primary last

if __name__ == "__main__":
    assert sort_students([("bob", 75), ("amy", 90), ("cal", 90), ("dan", 60)]) == \
        [("amy", 90), ("cal", 90), ("bob", 75), ("dan", 60)]
    assert sort_students([]) == []
    assert sort_students([("zed", 50), ("ann", 50)]) == [("ann", 50), ("zed", 50)]
    assert sort_students([("moe", 70), ("leo", 80), ("kim", 80), ("abe", 60)]) == \
        [("kim", 80), ("leo", 80), ("moe", 70), ("abe", 60)]
    # the stable two-pass version agrees
    assert sort_students_stable([("bob", 75), ("amy", 90), ("cal", 90)]) == \
        [("amy", 90), ("cal", 90), ("bob", 75)]
    print("All tests passed!")
