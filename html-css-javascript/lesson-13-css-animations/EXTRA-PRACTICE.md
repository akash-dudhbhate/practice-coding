# lesson-13-css-animations — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: transition vs animation
What's the difference?
<details><summary>Answer</summary>
- `transition` — animates between two states (e.g., hover). Needs a trigger.
- `animation` — runs automatically, can loop, has keyframes.
</details>

## Check 02: transform
```css
transform: translateX(100px) rotate(45deg) scale(1.5);
```
<details><summary>Answer</summary>
Moves right 100px, rotates 45deg, scales 1.5x. Order matters — transforms apply right to left.
</details>

## Check 03: Performance
Which properties are cheapest to animate?
<details><summary>Answer</summary>
`transform` and `opacity` — GPU accelerated, no layout recalculation. Avoid animating `width`, `height`, `top`, `left` — they trigger reflow.
</details>

## Check 04: ease vs linear
```css
transition: all 1s ease;     /* A */
transition: all 1s linear;   /* B */
```
<details><summary>Answer</summary>
`ease` — starts slow, speeds up, ends slow (natural). `linear` — constant speed (mechanical). Use ease for most UI, linear for progress bars.
</details>

## Check 05: keyframes
```css
@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}
```
<details><summary>Answer</summary>
0% and 100% are the same (start/end position). 50% is the peak. Creates a bounce effect.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Transition Not Working
```css
.box { transition: width 1s; }
.box:hover { width: 200px; }
```
<details><summary>Answer</summary>
**Bug:** No initial width set. Transition needs a starting value.
**Fix:** `.box { width: 100px; transition: width 1s; }`.
</details>

## Debug 02 (Medium): Animation Not Running
```css
.box { animation: slide 2s; }
```
<details><summary>Answer</summary>
**Bug:** No `@keyframes slide` defined.
**Fix:** Define keyframes: `@keyframes slide { from { transform: translateX(0); } to { transform: translateX(100px); } }`.
</details>

## Debug 03 (Hard): Janky Animation
```css
.box { transition: left 1s; }
.box:hover { left: 100px; }
```
<details><summary>Answer</summary>
**Bug:** Animating `left` triggers layout recalculation — janky.
**Fix:** Animate `transform: translateX(100px)` instead — GPU accelerated, smooth.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Animating layout properties
```css
/* WRONG — janky */
.box { transition: width 1s, height 1s; }
/* CORRECT — use transform */
.box { transition: transform 1s; }
```

## Mistake 02: No initial value for transition
```css
/* WRONG — no starting point */
.box { transition: width 1s; }
/* CORRECT */
.box { width: 100px; transition: width 1s; }
```

## Mistake 03: Too many animations
```css
/* WRONG — distracting */
* { animation: pulse 2s infinite; }
/* CORRECT — purposeful animations only */
```

## Mistake 04: Not respecting prefers-reduced-motion
```css
/* WRONG — ignores accessibility */
/* CORRECT */
@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; transition: none !important; }
}
```

## Mistake 05: Long animations
```css
/* WRONG — users get impatient */
transition: all 3s;
/* CORRECT — 200-400ms for UI */
transition: transform 200ms ease;
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Inline Validation
### Before
```html
<input onblur="validateEmail(this.value)" />
```
### After
```html
<input id="email" required type="email" />
<script>email.addEventListener("blur", validateEmail);</script>
```

## Refactor 02 (Medium): Manual Validation
### Before
```javascript
if (email === "") { showError("Email required"); return false; }
if (!email.includes("@")) { showError("Invalid email"); return false; }
```
### After
```html
<input type="email" required />
<!-- Browser handles validation -->
```

## Refactor 03 (Hard): Repeated Validation Logic
### Before
```javascript
function validateForm() {
  if (!name) return false;
  if (!email) return false;
  if (!phone) return false;
  return true;
}
```
### After
```javascript
const required = ["name", "email", "phone"];
const valid = required.every(field => form[field].value.trim());
```

---

## Approach Comparison — different ways to solve it

## Problem: Hover Effect

### Approach 1: transition
```css
.btn { background: blue; transition: background 200ms; }
.btn:hover { background: darkblue; }
```

### Approach 2: animation
```css
.btn:hover { animation: colorChange 200ms forwards; }
@keyframes colorChange { to { background: darkblue; } }
```

**Winner:** Approach 1 (transition) — simpler for state changes. Use animation for complex sequences.

---

## Problem: Loading Spinner

### Approach 1: CSS animation
```css
.spinner { animation: spin 1s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
```

### Approach 2: JS animation
```javascript
let rotation = 0;
function spin() {
  rotation += 5;
  el.style.transform = `rotate(${rotation}deg)`;
  requestAnimationFrame(spin);
}
```

**Winner:** Approach 1 — CSS is smoother and more efficient.
