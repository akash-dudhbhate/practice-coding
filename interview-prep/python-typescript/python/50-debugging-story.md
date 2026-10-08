# 50 — Answering "tell me about the hardest bug you ever debugged"

> **Interview question:** "Walk me through the hardest bug you've had to debug. How did you find it?"
> **What the interviewer is really testing:** Not the bug itself — your *process*. Did you follow evidence instead of guessing? Did you reproduce it, isolate it, and verify the fix? A structured story beats a heroic one.

## Theory — what it is

This is a **behavioral + technical hybrid** question. The answer framework is **STAR**:

- **S — Situation:** the system and stakes, one sentence. ("A pricing API serving checkout, p99 latency SLO of 500ms.")
- **T — Task:** what was broken and why it landed on you. ("Every hour at :00, p99 spiked to 8s; I owned the service that week.")
- **A — Action:** the debugging walkthrough — this is 70% of your answer. Symptom → hypothesis → test → evidence → root cause.
- **R — Result:** the fix, the measured outcome, and the prevention. ("P99 flat at 300ms; added jitter and a regression alert.")

What makes a *good* story: a non-obvious root cause (not "I had a typo"), evidence-driven steps (metrics, logs, repro — not luck), and a prevention lesson at the end (tests, alerts, runbooks). What kills a story: "we restarted it and it went away," or a bug so trivial it shows a shallow bar.

## Why it was needed

Interviewers ask this because debugging is the least-teachable, most-seniority-revealing skill: anyone can write greenfield code; production bug hunts expose whether you form hypotheses, instrument instead of printf-guessing, and hold a mental model of concurrency/caching/databases. They're also screening for honesty — a made-up story collapses under "how did you rule that out?" follow-ups.

## Where it's used in a real project

The same STAR shape maps onto real incident work:

- **Symptom gathering**: dashboards (p99 by endpoint), error trackers (Sentry), deploy timelines ("did it start after release X?").
- **Hypothesis ordering**: cheap checks first — recent deploy, config change, traffic shape — before deep dives.
- **Isolation**: reproduce in staging or with a single request ID; bisect by disabling the suspect path.
- **Root cause vs. trigger**: the deploy *triggered* it, but the expiry-aliasing bug *caused* it — fixes target causes.
- **Prevention**: the retro artifact — regression test, alert, jittered TTL, doc update.

## Diagram

```
SYMPTOM          HYPOTHESES (ordered cheap -> deep)        EVIDENCE            ROOT CAUSE
-------          ------------------------------------      --------            ---------
p99 spike        1. bad deploy?         git log shows     DB slow-query    ALL cache keys
every hour       2. DB slow queries?    no schema change  log: 40x rows     expire at the
at :00 exactly   3. traffic burst?      flat RPS          scanned at :00    same second
       |         4. cache hit ratio?    drops to 2%          |                    |
       v                |              at :00 only           v                    v
   "correlated    tests: 1-no 2-no    graphs: hit-     trace: one request    same TTL set
    with a       3-no 4-YES ---->    ratio cliff       fans out to 400      in a loop ->
    clock, not                        at :00:00        concurrent DB        synchronized
    load"                                              queries             stampede
                                                             |
                                          FIX: TTL + random jitter + request coalescing
                                          RESULT: p99 300ms flat; alert on hit-ratio < 80%
```

## Code — explained

The bug, distilled — a "warm the cache" loader that stampedes:

```python
import random, time, threading

TTL = 3600                                   # 1

def cache_key(product_id):                   # 2
    return f"price:{product_id}"

def warm_cache(cache, db, product_ids):      # 3
    for pid in product_ids:
        cache.set(cache_key(pid), db.fetch_price(pid), ttl=TTL)   # 4

# THE FIX — desynchronize expiry:                              # 5
def warm_cache_fixed(cache, db, product_ids):
    for pid in product_ids:
        jitter = random.randint(-300, 300)   # ±5 min
        cache.set(cache_key(pid), db.fetch_price(pid), ttl=TTL + jitter)

_locks = {}
def get_price(cache, db, pid):               # 6
    key = cache_key(pid)
    if (v := cache.get(key)) is not None:
        return v
    with _locks.setdefault(key, threading.Lock()):   # 7
        if (v := cache.get(key)) is not None:        # 8
            return v
        v = db.fetch_price(pid)
        cache.set(key, v, ttl=TTL + random.randint(-300, 300))
        return v
```

1. One constant TTL applied to every key — looks innocent, is the whole bug.
2. Cache keys namespaced per product — fine.
3. `warm_cache` runs at deploy/startup and refreshes the catalog in a tight loop.
4. Every key written in the same second gets the **same expiry instant** — 3,600 seconds later, thousands of keys vanish simultaneously. Every request that follows is a cache miss fanning out to the DB — the "thundering herd" / cache stampede. The hourly rhythm came from a re-warm cron aligned to the TTL.
5. Fix part one — **jittered TTL**: `TTL ± randint` spreads expiries across a 10-minute window, so misses arrive as a drizzle, not a flood.
6. Fix part two — **request coalescing**: on a miss, take a per-key lock before hitting the DB.
7. `setdefault` grabs (or creates) a lock for this key — concurrent misses on the *same* product serialize.
8. Double-checked get inside the lock: the first waiter repopulates the cache; everyone else reads it instead of re-querying. (In real code, use Redis `SET NX` + a lock TTL — this shows the pattern.)

## Practice prompts

### Easy — narrate a small bug you fixed
**Problem:** Tell a 60-second STAR story about a *small* bug — e.g., a timezone-off timestamp or a mutated shared list. Practice compressing: Situation in one sentence, Action in three, Result with a number.
**Try this input:** Your own real bug — or this seed: "CSV export showed yesterday's date for orders placed after 6 PM."
**Expected output:** A story under ~90 seconds with a named root cause and a prevention step.
**Solution (model answer):**
> "**S:** Our order-export CSV fed the finance report. **T:** Orders placed after 6 PM showed the *previous* day's date. **A:** I checked where the date was computed — it used `datetime.now()` (server local time, UTC) while finance read it as IST; an order at 6:30 PM IST was already 'tomorrow' in UTC, and the report grouped by UTC date. I confirmed by diffing a known order's timestamp in the DB vs. the CSV. **R:** Fixed the export to convert to the report's timezone before truncating the date, added a test with an order at 23:30 IST. No more mismatched totals in the daily report."
**Logic explained:**
1. One-sentence Situation — no architecture tour needed for a small bug.
2. The Action names the *evidence* (diffing DB vs. CSV), not just the fix — that's what interviewers score.
3. "Added a test with an order at 23:30" — the prevention step is what separates a story from an anecdote.

### Medium — debugging drill: find the bug
**Problem:** This cache works in dev but mixes up users' data under concurrent tests (and leaks across tests in CI). Find the bug *before* running it.

```python
class UserCache:
    _store = {}                       # shared storage

    def get(self, user_id):
        return self._store.get(user_id)

    def put(self, user_id, profile):
        self._store[user_id] = profile

cache_a = UserCache()
cache_b = UserCache()
cache_a.put("u1", {"name": "Alice"})
print(cache_b.get("u1"))              # ???
```

**Try this input:** run it, then ask: what does `cache_b.get("u1")` return?
**Expected output:** `{'name': 'Alice'}` — `cache_b` sees `cache_a`'s data.
**Solution:**
```python
class UserCache:
    def __init__(self):
        self._store = {}              # instance attribute — one per object
```
**Logic explained:**
1. `_store = {}` at class level creates **one dict on the class**, shared by every instance — `self._store` reads fall through to `UserCache._store` because no instance attribute exists.
2. `self._store[key] = v` mutates that shared dict in place (it never rebinds `self._store`, so no instance attribute is ever created).
3. Symptom in prod: two `UserCache` instances (or a "fresh" cache in tests) silently share data — tests pass alone, fail in a suite; users see each other's profiles. Fix: initialize in `__init__` so each instance owns its dict.
4. Interview narration: "mutable class attribute — same family as the mutable-default-arg bug; found it when `id(cache_a._store) == id(cache_b._store)` printed True."

### Hard — structure a STAR story from this scenario
**Problem:** Turn this raw incident into a full STAR answer. Scenario: *"A nightly batch job marks 'pending' records as processed in pages of 500. Support reports that roughly every other record is silently skipped. The job works perfectly when run manually on small data."*
**Try this input:** Reproduce with 10 pending records, page size 3.
**Expected output:** A STAR story identifying **offset-pagination over a shrinking set** as the root cause.
**Solution (model answer):**
> "**S:** A nightly job processed pending refund requests — paginated `SELECT ... WHERE status='pending' OFFSET n LIMIT 500`, updating each row to `processed` inside the loop. **T:** ~50% of refunds were skipped nightly; manual runs on small batches worked, so it looked 'flaky' and got punted twice. **A:** I reproduced it locally with 10 records and page size 3: page 0 fetched rows 0-2 and marked them processed; page 1 asked for rows 3-5 of the *remaining* pending set — but the pending set had shrunk by 3, so OFFSET 3 now pointed at original rows 6-8. Rows 3-5 were never read. Every page skipped a page — hence 'every other record'. The manual run 'worked' because small datasets fit in one page. **R:** Switched to keyset pagination (`WHERE id > last_seen_id ORDER BY id`) so the cursor is stable under mutation, plus a job-level metric 'pending before vs. processed' that alerts on mismatch. Skips went to zero; I also wrote the regression test that fails on the old code path."
**Logic explained:**
1. **Situation** names the mechanism (offset pagination + mutation) — the interviewer immediately knows the root cause is real, not Hollywood.
2. **Action** is the gold part: *reproduced deterministically* (10 records, page 3), stated the shrink-shift mechanics precisely, and explained why the "works manually" red herring happened — small data never reached page 2.
3. **Result** gives the fix (keyset/seek pagination — cursor tied to a stable column, immune to rows disappearing), a prevention metric, and a regression test. Three closers > one.
4. Backup details for follow-ups: OFFSET also gets slower as it grows (DB scans and discards rows); alternatives — process-by-id queue, `FOR UPDATE SKIP LOCKED` worker pattern.

## The 30-second interview answer

"I structure it as STAR and spend most of the time on Action. Example: our checkout API spiked to 8-second p99 at the top of every hour. I checked deploys and DB schema — clean — then saw cache hit-ratio cliff-dive to 2% at :00 only. A cache-warming loop had written every key with the same TTL, so thousands expired in the same second and every request stampeded the database. Fix: jittered TTLs to spread expiry, plus per-key lock coalescing so concurrent misses produce one DB query. P99 went flat at ~300ms, and we added a hit-ratio alert and a regression test. I lead with the evidence chain — dashboards, the :00 correlation — because the *process* is what the question is really about."

## Follow-up trap

**"Why didn't you catch this earlier / what did you do to prevent recurrence?"** — The trap is skipping prevention, or worse, saying "we monitor it now" vaguely. Have a concrete trio: the *test* (regression covering the mechanism, not the symptom), the *alert* (hit-ratio < 80%, pending-vs-processed mismatch), and the *doc* (runbook entry / postmortem). Second trap: **"What did you rule out first, and why?"** — they want cheap-check ordering: recent deploy → config → traffic shape → then deep instrumentation. Saying "I added logging everywhere" reads as guessing; saying "the :00 correlation ruled out load and pointed at time-based expiry" reads as method. Never end a debugging story without a prevention sentence — that's the seniority signal.
