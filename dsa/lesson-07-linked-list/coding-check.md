# Lesson 07 — Coding Check

Use this to verify your solutions before asking for a review.

## Easy

### p01-build-linked-list.py — Build a chain from values
- [ ] `build_list([1,2,3])` produces `1→2→3→None` (values in ORDER — not reversed)
- [ ] `build_list([])` returns `None`
- [ ] `build_list([7])` is a single node with `.next is None`
- [ ] You keep the head anchored — return `dummy.next`, not `tail`

### p02-traverse-to-list.py — Walk and collect
- [ ] `to_list(1→2→3→4)` returns `[1,2,3,4]`
- [ ] `to_list(None)` returns `[]`
- [ ] `to_list(9)` returns `[9]`
- [ ] Loop condition is `while head:` / `is not None` — not `while head.next:` (drops the last node)

### p03-find-middle.py — Middle via fast/slow
- [ ] `find_middle(1→2→3→4→5)` returns `3`
- [ ] `find_middle(1→2→3→4)` returns `3` — the SECOND middle on even length
- [ ] `find_middle(1)` returns `1`; `find_middle(1→2)` returns `2`
- [ ] Guard is `while fast and fast.next:` — checking only `fast.next` crashes

## Medium

### p01-reverse-iterative.py — Reverse in place
- [ ] `reverse_list(1→2→3→4→5)` produces `5→4→3→2→1`
- [ ] `reverse_list(None)` returns `None`
- [ ] `reverse_list(1)` returns that same single-node list
- [ ] `nxt = curr.next` is saved BEFORE `curr.next = prev`
- [ ] You advance with `curr = nxt`, and return `prev` — not `curr`/`head`

### p02-detect-cycle.py — Floyd's cycle detection
- [ ] Tail→node-1 on `1→2→3→4` returns `True`
- [ ] Tail→head on `1→2` returns `True`
- [ ] Normal list `1→2→3→None` returns `False`
- [ ] `None` and single-node lists return `False`
- [ ] `slow is fast` (identity) — not value comparison; O(1) space, no `set` needed

### p03-merge-two-sorted.py — Dummy-node merge
- [ ] `merge_two(1→2→4, 1→3→4)` produces `1→1→2→3→4→4`
- [ ] `merge_two(None, 1→2)` produces `1→2`
- [ ] `merge_two(None, None)` returns `None`
- [ ] `tail.next = a or b` hooks the un-merged remainder — don't re-loop it
- [ ] `tail` advances every iteration

## Hard

### p01-remove-nth-from-end.py — One-pass nth from end
- [ ] `remove_nth(1→2→3→4→5, 2)` produces `1→2→3→5`
- [ ] `remove_nth(1, 1)` returns `None` (removing the only node)
- [ ] `remove_nth(1→2, 1)` produces `1` (removing the tail)
- [ ] `remove_nth(1→2, 2)` produces `2` (removing the HEAD — dummy needed!)
- [ ] Fast gets an n-step head start; when `fast` hits end, `slow.next` is the target

### p02-reorder-list.py — L0→Ln→L1→Ln-1
- [ ] `reorder_list(1→2→3→4)` mutates to `1→4→2→3`
- [ ] `reorder_list(1→2→3→4→5)` mutates to `1→5→2→4→3`
- [ ] `reorder_list(1)` / `reorder_list(None)` don't crash
- [ ] You CUT the first half's tail (`prev_half.next = None`) before interleaving
- [ ] Second half is reversed before merging — that's where the "from the end" comes from

### p03-reverse-k-group.py — Reverse in blocks of k
- [ ] `reverse_k_group(1→2→3→4→5, 2)` produces `2→1→4→3→5`
- [ ] `reverse_k_group(1→2→3→4→5, 3)` produces `3→2→1→4→5` (tail of 2 untouched)
- [ ] `reverse_k_group(1, 1)` produces `1`; k > length leaves list unchanged
- [ ] You check "are there k nodes left?" BEFORE reversing — not after
- [ ] Each reversed group's tail links to the next group's start; group's old head becomes its tail

## How to verify

```bash
python3 check.py easy/p01     # one problem
python3 check.py all          # everything
```
