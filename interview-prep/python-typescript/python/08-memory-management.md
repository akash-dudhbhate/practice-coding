# 08 — Memory management: reference counting + the cyclic garbage collector

> **Interview question:** "How does Python know when to free an object — and what happens when two objects reference each other?"
> **What the interviewer is really testing:** Whether you know CPython's *two-layer* system: reference counting frees most objects the instant the last reference dies, and a separate cyclic GC periodically collects the reference cycles that refcounting can't.

## Theory — what it is

CPython manages memory in **two cooperating layers**:

**Layer 1 — reference counting (the workhorse).** Every object carries a count of how many things point at it — names, containers, function arguments. The count goes **up** on `y = x`, `lst.append(x)`, passing `x` to a function; **down** on `del y`, rebinding (`y = other`), containers being freed, or a function returning (locals die). The moment the count hits **zero**, the object is freed **immediately** — `tp_dealloc` runs `__del__` and returns the memory. This is *deterministic* — no waiting for a GC sweep. Check it with `sys.getrefcount(obj)` (note it adds one temporary ref itself).

`del` deletes a **name**, not an object — it just decrements the count. The object dies only when the *last* reference goes away.

**Layer 2 — the cyclic garbage collector (`gc` module).** Refcounting has a blind spot: a **reference cycle** — objects pointing at each other — keeps every member's count ≥ 1 even after nothing outside can reach them:

```python
a.peer = b; b.peer = a
del a, b        # counts stay 1,1 — leaked forever by refcounting alone
```

So a separate **generational tracing collector** periodically walks all *container* objects (things that can hold references — lists, dicts, class instances), computes which clusters are unreachable from the roots (locals, globals, module state), and frees them — cycles included.

It's **generational**: objects start in generation 0; each collection they survive promotes them (gen 0 → 1 → 2). Gen 0 is collected most often — when allocations minus deallocations exceeds a threshold (default 700) — because *most objects die young* (the "generational hypothesis"). `gc.collect()` forces a collection; `gc.disable()` turns it off; `gc.get_count()` shows current per-generation tallies.

**The manual fix:** `weakref.ref(obj)` creates a reference that *doesn't* increment the count — the classic way to break cycles (a child's back-pointer to its parent).

Caveats: refcounting is a **CPython implementation detail** — PyPy/Jython use pure tracing GCs, so `__del__` timing isn't portable. Cycles containing `__del__` were uncollectable before Python 3.4; now they're freed but finalizer *order* is undefined — prefer context managers or `weakref.finalize` over `__del__`.

## Why it was needed

Refcounting is cheap, incremental, and deterministic — memory is reclaimed the instant it dies, and cleanup like file closing happens promptly. But it's *provably* unable to collect cycles, and real programs create them constantly (parent/child trees, ORM back-references, callbacks).

Rather than replace refcounting, CPython *added* the cyclic GC — paid only occasionally, only on container objects. The generational design amortizes the cost: scanning all of memory is expensive, but scanning just the young generation — where nearly all garbage lives — is cheap and frequent.

## Where it's used in a real project

- **ORM back-references:** SQLAlchemy's `user.posts` / `post.user` creates cycles everywhere — the cyclic GC handles them; heavy workloads tune `gc` thresholds to avoid pauses.
- **Trees/graphs/doubly-linked lists:** `parent.children` + `child.parent` cycles — or `child.parent = weakref.ref(parent)` to avoid cycles entirely.
- **Caches & observer lists:** `weakref.WeakValueDictionary` / `WeakSet` — entries vanish automatically when the object dies elsewhere; no manual cleanup.
- **Long-running services:** teams disable GC and `gc.collect()` on a schedule to kill unpredictable pauses (Instagram famously ran with `gc.disable()`); `gc.freeze()` after fork keeps COW memory shareable in prefork servers like gunicorn/uWSGI.
- **Leak debugging:** `gc.get_objects()`, `gc.garbage`, `objgraph` to find what's keeping objects alive.

## Diagram

```
REFCOUNTING (instant, deterministic):
  x = []          count 1      a.peer = b; b.peer = a     counts 1,1
  y = x           count 2      del a, del b               counts STILL 1,1
  del x, del y    count 0 ──>  FREED immediately            but unreachable!
                                   │
                               cyclic GC sweeps ──> both FREED

GENERATIONS:   gen0 (new, scanned often) ──survive──> gen1 ──> gen2 (old, rarely)
               trigger: allocations - deallocations > threshold (700 default)
```

## Code — explained

```python
import sys, gc, weakref

o = object()
print(sys.getrefcount(o))    # 2 — o itself + the temp ref inside getrefcount
r = o
print(sys.getrefcount(o))    # 3
del r                        # del removes a NAME, not the object
print(sys.getrefcount(o))    # 2

class Node:
    def __del__(self):
        print("freed")

a, b = Node(), Node()
a.peer = b
b.peer = a                   # cycle: a keeps b alive, b keeps a alive
del a, b                     # (silence) — refcount can't free the cycle!
gc.collect()                 # freed / freed — the cyclic GC got them

c = Node()
w = weakref.ref(c)           # weakref does NOT bump the count
print(w() is c)              # True — dereferences while c lives
del c                        # freed — refcount hit 0 instantly
print(w())                   # None — weakref now points at nothing
```

1. `sys.getrefcount(o)` returns `2`, not `1` — calling it passes `o` as an argument, adding a temporary reference. Mentally subtract one.
2. `del r` removes the *name* `r` — the object survives because `o` still points at it. `del` never "deletes the object."
3. The `a`/`b` cycle: after `del a, b`, each count is still 1 (held by the peer) — nothing prints, nothing is freed. The objects are unreachable but alive.
4. `gc.collect()` walks containers, finds the unreachable `a↔b` cluster, frees both — `__del__` prints `freed` twice during the call.
5. `weakref.ref(c)` doesn't count — `del c` drops `c`'s count to 0 → `freed` prints immediately, no GC needed; `w()` returns `None` afterward. This is how you break cycles by design instead of relying on the sweeper.

## Problems

### Easy — what does `getrefcount` print?
**Problem:** Predict the output — and explain why it's not `1`.
**Try this input:**
```python
import sys
x = object()
print(sys.getrefcount(x))
```
**Expected output:** `2`
**Solution:**
```python
import sys
x = object()
print(sys.getrefcount(x))    # 2 — one ref is x, one is the call itself
```
**Logic explained:**
1. `x` holds one reference — that's the count you'd expect.
2. `sys.getrefcount(x)` receives `x` as an argument — that parameter binding is a *second* reference, counted while the function runs.
3. So `getrefcount` always reads one higher than "real" refs — subtract one mentally. (Don't demo this with small ints or short strings — CPython interns/caches those, giving huge misleading counts.)

### Medium — prove a cycle survives `del`
**Problem:** Two `Node` objects reference each other. Show that `del` does **not** free them, then force cleanup and prove it happened.
**Try this input:** create `a`, `b` with `a.peer = b; b.peer = a`, `del a, b`, then `gc.collect()`.
**Expected output:** nothing on `del`; `freed` `freed` printed during `gc.collect()`.
**Solution:**
```python
import gc

class Node:
    def __del__(self):
        print("freed")

a, b = Node(), Node()
a.peer = b
b.peer = a                   # cycle born
del a, b                     # nothing prints — both counts still 1
gc.collect()                 # freed  /  freed — GC finds unreachable cycle
```
**Logic explained:**
1. After `del a, b`, `a`'s count is 1 (held by `b.peer`) and `b`'s is 1 (held by `a.peer`) — refcounting sees live objects.
2. From the program's roots, though, the pair is unreachable — that's exactly what the cyclic GC's reachability pass detects.
3. `gc.collect()` frees the cluster; each `__del__` runs and prints. (Python ≥3.4 — before that, `__del__` in a cycle made the objects *uncollectable*.)

### Hard — break the cycle with `weakref`
**Problem:** A parent/child tree leaks: `parent.children.append(child)` plus `child.parent = parent` forms a cycle, so `del parent` frees nothing without a GC sweep. Redesign it so `del parent` frees immediately — while `child` can still *reach* its parent — and prove it.
**Try this input:** build parent `p` + child `c`, `del p` (child `c` still held).
**Expected output:** `freed p` prints at `del p` — no `gc.collect()` needed.
**Solution:**
```python
import weakref

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
    def __del__(self):
        print(f"freed {self.name}")

p = Node("p")
c = Node("c")
p.children.append(c)
c.parent = weakref.ref(p)     # weak back-edge: doesn't keep p alive
print(c.parent() is p)        # True — child can still reach parent
del p                         # freed p — refcount hits 0 NOW, no cycle
# del c                       # freed c
```
**Logic explained:**
1. With `c.parent = p` (strong ref), `del p` leaves `p`'s count at 1 — held by `c` — so `freed p` would *not* print; the `p → children → c → parent → p` cycle would wait for the GC.
2. `weakref.ref(p)` lets `c` *reach* `p` via `c.parent()` without *owning* it — the count stays at 1 (just `p`).
3. `del p` → count 0 → `p` freed instantly, which frees `p.children`, which decrefs `c` — `c` survives only because we still hold the name `c`; `del c` frees it too.
4. This is the real-world pattern: tree/graph back-edges, ORM relationships, and observer lists use `weakref` so teardown is prompt and doesn't depend on the collector.

## The 30-second interview answer

"CPython frees objects primarily by *reference counting* — every object tracks how many references point at it; when the count hits zero — via `del`, rebinding, or scope exit — it's freed immediately and `__del__` runs deterministically. The gap is *reference cycles*: `a.peer = b; b.peer = a` keeps both counts at 1 even when unreachable, so a second system — the cyclic garbage collector in `gc` — periodically scans container objects, finds unreachable clusters, and frees them. It's *generational*: young objects are scanned often since most die young. You break cycles yourself with `weakref`, and in services you can tune or disable `gc` — Instagram famously ran with it off. Note refcounting is CPython-specific; PyPy uses a pure tracing GC."

## Follow-up trap

**"Does `del obj` delete the object?"** — no, it deletes a *name* (or decrefs through one reference); the object dies only when its count hits zero — `del` is why juniors think Python has "manual" memory management when it doesn't. Second trap: *"What can't the cyclic GC handle?"* — before Python 3.4, cycles containing `__del__` were uncollectable (leaked into `gc.garbage`); now collectable but finalizer order is undefined — so don't put critical teardown in `__del__`, use context managers or `weakref.finalize`. Third: *"Why generations?"* — the generational hypothesis: most objects die young (temporaries, locals), so scanning gen0 often and old objects rarely gets most of the garbage at a fraction of the cost of a full heap scan. Bonus: `gc.set_threshold(700, 10, 10)` — gen1/gen2 collections trigger every N gen0 collections.
