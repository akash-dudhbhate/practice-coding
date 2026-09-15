# Lesson 19 — Intuition Checks

## Check 01: Testing Library philosophy
What should you test?
<details><summary>Answer</summary>
Test behavior, not implementation. Test what the user sees and does. "The more your tests resemble the way your software is used, the more confidence they give you."
</details>

## Check 02: getBy vs queryBy vs findBy
```jsx
screen.getByText("Hello");    // throws if not found
screen.queryByText("Hello");  // returns null if not found
screen.findByText("Hello");   // waits (async) — returns promise
```
<details><summary>Answer</summary>
getBy — must exist (throws if not). queryBy — check existence (null if not). findBy — async, waits for element.
</details>

## Check 03: userEvent vs fireEvent
```jsx
fireEvent.click(button);    // low-level
userEvent.click(button);    // high-level, simulates real user
```
<details><summary>Answer</summary>
userEvent simulates real browser behavior (focus, blur, events chain). fireEvent is lower-level. Prefer userEvent.
</details>

## Check 04: render cleanup
Do you need to cleanup after render?
<details><summary>Answer</summary>
No — Testing Library auto-cleans up after each test (in most test runners). DOM is reset between tests.
</details>

## Check 05: data-testid
```jsx
<button data-testid="submit">Submit</button>
```
<details><summary>Answer</summary>
Last resort for querying. Prefer text, role, label. Use testid only when text/role aren't unique or available.
</details>
