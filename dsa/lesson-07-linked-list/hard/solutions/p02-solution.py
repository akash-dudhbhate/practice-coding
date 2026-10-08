"""
SOLUTION: Reorder List — L0,Ln,L1,Ln-1 (Hard)
==============================
Three composed patterns: (1) fast/slow stops on the FIRST middle via
`while fast.next and fast.next.next`; (2) sever, reverse second half;
(3) interleave two chains. In place, O(1) space.
"""
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head):
    if not head or not head.next:
        return
    # 1. slow lands on the first middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    # 2. cut the list; reverse the second half
    second = slow.next
    slow.next = None
    prev = None
    while second:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt
    # 3. interleave first half (head) with reversed half (prev)
    first, second = head, prev
    while second:
        t1, t2 = first.next, second.next
        first.next = second
        second.next = t1
        first, second = t1, t2

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
    h = build_list([1, 2, 3, 4]); reorder_list(h)
    assert to_list(h) == [1, 4, 2, 3]
    h = build_list([1, 2, 3, 4, 5]); reorder_list(h)
    assert to_list(h) == [1, 5, 2, 4, 3]
    h = build_list([1, 2, 3]); reorder_list(h)
    assert to_list(h) == [1, 3, 2]
    h = build_list([1]); reorder_list(h)
    assert to_list(h) == [1]
    reorder_list(None)   # must not crash
    print("All tests passed!")
