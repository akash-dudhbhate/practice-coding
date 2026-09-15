# Lesson 13 — Intuition Checks

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
