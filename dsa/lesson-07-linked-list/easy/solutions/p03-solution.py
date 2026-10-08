"""
SOLUTION: Find the Middle (Easy)
==============================
Fast hops 2, slow hops 1. When fast can no longer move twice, slow is
on the middle node (second middle for even length — what we want).
"""
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle(head) -> int:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val

def build_list(values):
    dummy = Node()
    tail = dummy
    for v in values:
        tail.next = Node(v)
        tail = tail.next
    return dummy.next

if __name__ == "__main__":
    assert find_middle(build_list([1, 2, 3, 4, 5])) == 3
    assert find_middle(build_list([1, 2, 3, 4])) == 3
    assert find_middle(build_list([1])) == 1
    assert find_middle(build_list([1, 2])) == 2
    print("All tests passed!")
