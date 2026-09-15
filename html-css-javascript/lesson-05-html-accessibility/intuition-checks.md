# Lesson 05 — Intuition Checks

## Check 01: Tab order
What determines tab order?
<details><summary>Answer</summary>
DOM order by default. Use `tabindex` to modify: `tabindex="0"` makes focusable, `tabindex="-1"` removes from tab flow, positive values are discouraged.
</details>

## Check 02: ARIA roles
When should you use ARIA?
<details><summary>Answer</summary>
Only when HTML doesn't provide the semantics you need. "No ARIA is better than bad ARIA." Use `<button>` not `<div role="button">`.
</details>

## Check 03: Color contrast
What's the minimum contrast ratio for normal text (WCAG AA)?
<details><summary>Answer</summary>
4.5:1 for normal text, 3:1 for large text. Use a contrast checker.
</details>

## Check 04: Focus indicator
Why must you never remove `outline` without replacing it?
<details><summary>Answer</summary>
Keyboard users need a visible focus indicator to know where they are. If you remove `outline: none`, provide an alternative focus style.
</details>

## Check 05: Screen reader testing
How do you test with a screen reader?
<details><summary>Answer</summary>
- NVDA (Windows, free)
- VoiceOver (macOS/iOS, built-in)
- JAWS (Windows, paid)
Test at least with one. Don't rely on visual testing alone.
</details>
