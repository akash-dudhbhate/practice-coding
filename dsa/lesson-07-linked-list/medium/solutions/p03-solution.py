"""
SOLUTION: Merge Two Sorted Lists (Medium)
==============================
Dummy head + tail: repeatedly splice the smaller front node. When one
input is exhausted, `tail.next = a or b` hooks the whole sorted
remainder in a single pointer move. Relinks existing nodes — O(1) space.
"""
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two(a, b):
    dummy = Node()
    tail = dummy
    while a and b:
        if a.val <= b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a or b          # the survivor list's remainder
    return dummy.next

def build_list(values):
    dummy = Node()
    tail = dummy
    for v in values:
        tail.next = Node(v)
        tail = tail.next
    return dummy.next

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

if __name__ == "__main__":
    assert to_list(merge_two(build_list([1, 2, 4]), build_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(merge_two(None, build_list([1, 2]))) == [1, 2]
    assert merge_two(None, None) is None
    assert to_list(merge_two(build_list([5, 6]), build_list([1, 2, 3, 4]))) == [1, 2, 3, 4, 5, 6]
    print("All tests passed!")
