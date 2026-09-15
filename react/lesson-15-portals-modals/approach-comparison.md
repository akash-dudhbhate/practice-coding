# Lesson 15 — Approach Comparison

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
