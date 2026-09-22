# lesson-15-portals-modals — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: What is a Portal?
<details><summary>Answer</summary>
Portal renders children into a DOM node outside the parent component's DOM hierarchy. Visually escapes parent constraints (z-index, overflow).
</details>

## Check 02: createPortal
```jsx
ReactDOM.createPortal(children, container)
```
<details><summary>Answer</summary>
`children` — React elements to render. `container` — DOM node to render into. Returns React element.
</details>

## Check 03: Portal event bubbling
Do events bubble through portals?
<details><summary>Answer</summary>
Yes — in React's synthetic event system, events bubble through the React component tree, not the DOM tree. A portal's events still reach parent components in React.
</details>

## Check 04: Modal use case
Why use portals for modals?
<details><summary>Answer</summary>
Modals need to: escape parent overflow/z-index, be on top of everything, be accessible. Portals render at body level, avoiding parent clipping.
</details>

## Check 05: Accessibility
What accessibility concerns do modals have?
<details><summary>Answer</summary>
Focus trap (Tab stays in modal), escape key to close, aria-modal="true", return focus to trigger on close, screen reader announcement.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy: Modal Inside Component Tree
```jsx
function App() {
  return (
    <div style={{ overflow: "hidden" }}>
      <Modal /> {/* can't overflow parent */}
    </div>
  );
}
```
<details><summary>Answer</summary>
**Bug:** Modal is trapped inside `overflow: hidden` parent. May be clipped.
**Fix:** Use Portal to render at document.body level.
</details>

## Debug 02 (Medium): Portal Without DOM Node
```jsx
return ReactDOM.createPortal(<Modal />, document.getElementById("modal-root"));
// modal-root div doesn't exist
```
<details><summary>Answer</summary>
**Bug:** `getElementById` returns null. `createPortal` throws.
**Fix:** Ensure `<div id="modal-root"></div>` exists in HTML, or create it dynamically.
</details>

## Debug 03 (Hard): Event Bubbling Through Portals
```jsx
<div onClick={() => console.log("parent")}>
  {ReactDOM.createPortal(<button onClick={handleClick}>Click</button>, document.body)}
</div>
```
<details><summary>Answer</summary>
**Note:** Portal events bubble through React tree (not DOM tree). Clicking button triggers parent's onClick in React, even though DOM-wise they're separate.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Modal without portal
```jsx
// WRONG — trapped in parent's overflow/z-index
<div style={{ overflow: "hidden" }}>
  <Modal />
</div>
// CORRECT — portal to body
ReactDOM.createPortal(<Modal />, document.body)
```

## Mistake 02: No focus trap
```jsx
// WRONG — Tab escapes modal
<Modal><input /></Modal>
// CORRECT — trap focus
// Use a library like focus-trap-react
```

## Mistake 03: No escape key handler
```jsx
// WRONG — can't close with Escape
// CORRECT
useEffect(() => {
  const handler = (e) => { if (e.key === "Escape") onClose(); };
  window.addEventListener("keydown", handler);
  return () => window.removeEventListener("keydown", handler);
}, []);
```

## Mistake 04: No backdrop click to close
```jsx
// Add onClick to backdrop
<div className="backdrop" onClick={onClose}>
  <div className="modal" onClick={e => e.stopPropagation()}>...</div>
</div>
```

## Mistake 05: Body scroll not locked
```jsx
// WRONG — background scrolls
// CORRECT
useEffect(() => {
  document.body.style.overflow = "hidden";
  return () => { document.body.style.overflow = ""; };
}, []);
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Modal in Component Tree
### Before
```jsx
<div className="layout">
  <Modal /> // z-index issues, parent overflow clips
</div>
```
### After
```jsx
{createPortal(<Modal />, document.body)}
```

## Refactor 02 (Medium): No Escape Handling
### Before
```jsx
<Modal open={isOpen}>Content</Modal>
```
### After
```jsx
useEffect(() => {
  const handler = (e) => e.key === "Escape" && onClose();
  window.addEventListener("keydown", handler);
  return () => window.removeEventListener("keydown", handler);
}, [onClose]);
```

## Refactor 03 (Hard): Modal State Everywhere
### Before
```jsx
const [isModalOpen, setIsModalOpen] = useState(false);
// passed through 5 levels
```
### After
```jsx
// Use a modal context or library
const { openModal } = useModal();
```

---

## Approach Comparison — different ways to solve it

## Problem: Render Modal

### Approach 1: Inline in component
```jsx
return <div><Content /><Modal /></div>;
```
**Cons:** Trapped in parent's z-index/overflow.

### Approach 2: Portal
```jsx
return <>
  <Content />
  {ReactDOM.createPortal(<Modal />, document.body)}
</>;
```

**Winner:** Approach 2 — modal escapes parent constraints.

---

## Problem: Modal Library

### Approach 1: Build from scratch
```jsx
function Modal({ children, onClose }) { ... }
```

### Approach 2: Use library (Headless UI, Radix)
```jsx
import { Dialog } from "@headlessui/react";
<Dialog open={isOpen} onClose={close}>...</Dialog>
```

**Winner:** Approach 2 for production — handles accessibility, focus trap, animations.
