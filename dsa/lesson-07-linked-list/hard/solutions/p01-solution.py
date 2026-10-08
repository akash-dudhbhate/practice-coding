"""
SOLUTION: Remove Nth From End — One Pass (Hard)
==============================
Dummy + gap: fast gets an n-step head start; `while fast.next` lands
slow on the node BEFORE the target — even when the target is the head
(that's why we start both pointers at dummy, not head). One splice.
"""
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth(head, n):
    dummy = Node(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next    # cut the target out
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
    assert to_list(remove_nth(build_list([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert remove_nth(build_list([1]), 1) is None
    assert to_list(remove_nth(build_list([1, 2]), 1)) == [1]
    assert to_list(remove_nth(build_list([1, 2]), 2)) == [2]
    assert to_list(remove_nth(build_list([1, 2, 3]), 3)) == [2, 3]
    print("All tests passed!")
