"""
SOLUTION: Reverse Nodes in k-Group (Hard)
==============================
For each group: probe k nodes ahead (bail if fewer), then reverse that
block — starting prev at group_next makes the group's old head link
forward for free. Splice via group_prev; old group head becomes the
new group_prev. O(n) time, O(1) space.
"""
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head, k):
    dummy = Node(0, head)
    group_prev = dummy
    while True:
        kth = group_prev                  # probe: is a full k-group left?
        for _ in range(k):
            kth = kth.next
            if kth is None:
                return dummy.next
        group_next = kth.next             # first node after this group
        # reverse the group [group_prev.next .. kth]; seeding prev with
        # group_next links the group's tail forward automatically
        prev, curr = group_next, group_prev.next
        while curr is not group_next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        group_tail = group_prev.next      # old head -> becomes tail
        group_prev.next = kth             # kth is the new group head
        group_prev = group_tail

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
    assert to_list(reverse_k_group(build_list([1, 2, 3, 4, 5]), 2)) == [2, 1, 4, 3, 5]
    assert to_list(reverse_k_group(build_list([1, 2, 3, 4, 5]), 3)) == [3, 2, 1, 4, 5]
    assert to_list(reverse_k_group(build_list([1, 2, 3]), 5)) == [1, 2, 3]
    assert to_list(reverse_k_group(build_list([1]), 1)) == [1]
    assert to_list(reverse_k_group(build_list([1, 2, 3, 4, 5, 6]), 3)) == [3, 2, 1, 6, 5, 4]
    print("All tests passed!")
