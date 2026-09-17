# lesson-18-quasar-ssr — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: What is SSR?
<details><summary>Answer</summary>
Server-Side Rendering — HTML generated on server, sent to browser. Better SEO, faster first paint. Client then "hydrates" into interactive Vue app. Quasar: `quasar build -m ssr`.
</details>

## Check 02: process.env.CLIENT
```javascript
if (process.env.CLIENT) { /* browser only */ }
if (process.env.SERVER) { /* server only */ }
```
<details><summary>Answer</summary>
Quasar provides these flags. Use to guard browser-only APIs (window, document, localStorage). Code is tree-shaken for each build.
</details>

## Check 03: onMounted for browser code
```javascript
onMounted(() => {
  // runs only in browser, after hydration
  localStorage.getItem("key");
});
```
<details><summary>Answer</summary>
`onMounted` runs only in browser. Safe for browser APIs. `setup()` runs on both server and client.
</details>

## Check 04: PreFetch
```javascript
// routes.js
{
  path: "/",
  component: () => import("layouts/MainLayout"),
  preFetch: async ({ store, currentRoute }) => {
    await store.dispatch("fetchData");
  }
}
```
<details><summary>Answer</summary>
Fetch data on server before rendering. Data available in HTML immediately. Better SEO and UX.
</details>

## Check 05: Hydration
<details><summary>Answer</summary>
Server sends static HTML. Browser loads JS, Vue "hydrates" HTML into interactive app. If server and client render differently → hydration mismatch warning.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01: Window Used on Server
```javascript
if (window.innerWidth < 600) { /* responsive */ }
// Error: window is not defined (SSR)
```
<details><summary>Answer</summary>
**Bug:** `window` not available during SSR. Only in browser.
**Fix:** `if (process.env.CLIENT && window.innerWidth < 600)`.
</details>

## Debug 02: localStorage on Server
```javascript
const token = localStorage.getItem("token");
// SSR: localStorage not defined
```
<details><summary>Answer</summary>
**Bug:** localStorage only exists in browser.
**Fix:** Wrap in `if (process.env.CLIENT)` or use `onMounted`.
</details>

## Debug 03: No Hydration Mismatch
```javascript
const time = new Date().toISOString();
// Server renders one time, client another → mismatch
```
<details><summary>Answer</summary>
**Bug:** Different output on server vs client → hydration error.
**Fix:** Use `onMounted` for time-dependent content, or use consistent data.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Using window on server
```javascript
// WRONG
if (window.innerWidth < 600)
// CORRECT
if (process.env.CLIENT && window.innerWidth < 600)
```

## Mistake 02: localStorage in setup
```javascript
// WRONG — runs on server
setup() { const x = localStorage.getItem("key"); }
// CORRECT — onMounted
onMounted(() => { const x = localStorage.getItem("key"); });
```

## Mistake 03: Hydration mismatch
```javascript
// WRONG — different output server vs client
const time = Date.now();
// CORRECT — consistent or onMounted
```

## Mistake 04: Not using preFetch
```javascript
// Fetch data on server for SEO
preFetch: async ({ store }) => { await store.dispatch("load"); }
```

## Mistake 05: Not handling SSR state
```javascript
// Server state must transfer to client
// Quasar handles this automatically with Pinia
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): window on Server
### Before
```javascript
if (window.innerWidth < 600)
```
### After
```javascript
if (process.env.CLIENT && window.innerWidth < 600)
```

## Refactor 02 (Medium): localStorage in setup
### Before
```javascript
setup() { const x = localStorage.getItem("key"); }
```
### After
```javascript
onMounted(() => { const x = localStorage.getItem("key"); });
```

## Refactor 03 (Hard: SPA for SEO
### Before
```bash
quasar build -m spa
```
### After
```bash
quasar build -m ssr
```

---

## Approach Comparison — different ways to solve it

## Problem: SEO

### Approach 1: SPA
```bash
quasar build -m spa
```
**Cons:** Poor SEO — content loaded by JS.

### Approach 2: SSR
```bash
quasar build -m ssr
```

**Winner:** Approach 2 — HTML in source, good SEO.

---

## Problem: Browser APIs

### Approach 1: process.env check
```javascript
if (process.env.CLIENT) { window... }
```

### Approach 2: onMounted
```javascript
onMounted(() => { window... });
```

**Winner:** Approach 2 — cleaner, guaranteed browser.
