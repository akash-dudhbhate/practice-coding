"""
SOLUTION: LRU Cache (Hard) — dict + doubly-linked list
======================================================
dict: key -> node for O(1) lookup.
doubly-linked list: usage order, most-recently-used at the head.
Sentinel head/tail nodes remove all the edge-case branching for
insert/remove at the ends. get and put both O(1).
"""


class _Node:
    __slots__ = ("key", "val", "prev", "next")

    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        # sentinels: head <-> ... <-> tail (head.next = most recent)
        self.head = _Node()
        self.tail = _Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _push_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if node is None:
            return -1
        self._remove(node)
        self._push_front(node)      # mark as most recently used
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove(node)
            self._push_front(node)
            return
        node = _Node(key, value)
        self.map[key] = node
        self._push_front(node)
        if len(self.map) > self.cap:
            lru = self.tail.prev    # least recently used
            self._remove(lru)
            del self.map[lru.key]


if __name__ == "__main__":
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)                     # evicts 2
    assert c.get(2) == -1
    c.put(4, 4)                     # evicts 1
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4

    c2 = LRUCache(1)
    c2.put(1, 1)
    c2.put(1, 2)                    # update existing key
    assert c2.get(1) == 2
    print("All tests passed!")
