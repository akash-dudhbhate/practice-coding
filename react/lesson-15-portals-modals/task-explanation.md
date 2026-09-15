# Lesson 15 — Portals & Modals

## What you'll learn
- The z-index stacking problem
- createPortal (rendering outside the parent DOM)
- Event bubbling through portals
- Building a complete modal component
- Accessibility for modals (focus trap, ARIA)
- Tooltips with portals
- Animations with portals (enter/exit transitions)

## Lesson

### Portal
```jsx
import { createPortal } from 'react-dom';
return createPortal(<Modal />, document.body);
```

### Modal pattern
```jsx
function Modal({ isOpen, onClose, children }) {
    if (!isOpen) return null;
    return createPortal(
        <div className="overlay" onClick={onClose}>
            <div className="content" onClick={e => e.stopPropagation()}>
                {children}
            </div>
        </div>, document.body
    );
}
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.jsx` — Create a simple modal using `createPortal` that renders to `document.body`. Include an open button, overlay, and close button.
2. `easy/p02-solve.jsx` — Create a modal that closes when clicking the overlay (outside the content). Use `stopPropagation` on the content to prevent closing when clicking inside.
3. `easy/p03-solve.jsx` — Create a tooltip component using portals. On hover, show a small tooltip near the element. Use `getBoundingClientRect` for positioning.

### Medium
4. `medium/p01-solve.jsx` — Create a modal with escape key support: pressing Escape closes the modal. Add body scroll lock when modal is open (and restore on close).
5. `medium/p02-solve.jsx` — Create a confirmation dialog component: "Are you sure?" with Confirm and Cancel buttons. Use portals. Return the user's choice via callbacks (`onConfirm`, `onCancel`).
6. `medium/p03-solve.jsx` — Create a tooltip that positions itself intelligently: if near the right edge, position to the left; if near the bottom, position above. Use `getBoundingClientRect` and viewport dimensions.

### Hard
7. `hard/p01-solve.jsx` — Build an accessible modal with: focus trap (Tab cycles within modal), focus restore on close, ARIA attributes (`role="dialog"`, `aria-modal="true"`), and escape key support.
8. `hard/p02-solve.jsx` — Build an animated modal with enter/exit transitions. Use delayed unmount (setTimeout) to allow exit animation. Include fade-in/fade-out for overlay and slide-in/slide-out for content.
9. `hard/p03-solve.jsx` — Build a notification/toast system using portals: `toast.success("Saved!")` shows a toast in the corner. Auto-dismiss after 3s. Stack multiple toasts. Include manual close button. Animate enter/exit.

### How to work
- Write your complete React solution.
- Remove the TODO comment when done.
- Test by importing into a React app or using a sandbox.
