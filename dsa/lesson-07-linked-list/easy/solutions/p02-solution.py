"""
SOLUTION: Traverse and Collect (Easy)
==============================
Walk `while head:` collecting .val, advance with head = head.next.
The only forward motion a linked list has is one pointer hop at a time.
"""
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_list(head) -> list:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def build_list(values):
    dummy = Node()
    tail = dummy
    for v in values:
        tail.next = Node(v)
        tail = tail.next
    return dummy.next

if __name__ == "__main__":
    assert to_list(build_list([1, 2, 3, 4])) == [1, 2, 3, 4]
    assert to_list(None) == []
    assert to_list(build_list([9])) == [9]
    print("All tests passed!")
