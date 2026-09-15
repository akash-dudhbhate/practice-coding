# Lesson 15 — Coding Check

## Easy

### p01-solve.jsx — Simple portal modal
- [ ] `createPortal` imported from 'react-dom'
- [ ] Modal renders to `document.body`
- [ ] Open button exists
- [ ] Close button exists
- [ ] Modal appears above all content

### p02-solve.jsx — Overlay click to close
- [ ] Overlay has `onClick={onClose}`
- [ ] Content has `onClick={e => e.stopPropagation()}`
- [ ] Clicking overlay closes modal
- [ ] Clicking inside content does NOT close
- [ ] Close button works

### p03-solve.jsx — Portal tooltip
- [ ] Tooltip uses `createPortal`
- [ ] Shows on mouse enter
- [ ] Hides on mouse leave
- [ ] Uses `getBoundingClientRect` for position
- [ ] Tooltip is not clipped by parent overflow

## Medium

### p01-solve.jsx — Escape key + scroll lock
- [ ] Escape key closes the modal
- [ ] `keydown` event listener added in useEffect
- [ ] Body scroll locked when modal opens (`overflow: hidden`)
- [ ] Body scroll restored on close
- [ ] Event listener cleaned up on unmount

### p02-solve.jsx — Confirmation dialog
- [ ] "Are you sure?" message displayed
- [ ] Confirm button calls `onConfirm`
- [ ] Cancel button calls `onCancel`
- [ ] Uses portals
- [ ] Overlay click calls `onCancel`
- [ ] Escape key calls `onCancel`

### p03-solve.jsx — Smart positioning tooltip
- [ ] Tooltip position calculated from `getBoundingClientRect`
- [ ] If near right edge → positions to the left
- [ ] If near bottom edge → positions above
- [ ] Uses `window.innerWidth` and `window.innerHeight`
- [ ] Tooltip stays within viewport

## Hard

### p01-solve.jsx — Accessible modal
- [ ] `role="dialog"` on modal content
- [ ] `aria-modal="true"` attribute
- [ ] `aria-labelledby` pointing to title
- [ ] Focus trap: Tab cycles within modal
- [ ] Shift+Tab cycles backwards
- [ ] Focus moves to modal on open
- [ ] Focus restored to trigger element on close
- [ ] Escape key closes modal

### p02-solve.jsx — Animated modal
- [ ] Enter animation: overlay fade-in, content slide-in
- [ ] Exit animation: overlay fade-out, content slide-out
- [ ] Delayed unmount (setTimeout) for exit animation
- [ ] Timeout cleaned up on unmount
- [ ] CSS transitions defined
- [ ] No layout shift during animation

### p03-solve.jsx — Toast notification system
- [ ] `toast.success()`, `toast.error()` functions
- [ ] Toasts render via portal in a corner
- [ ] Auto-dismiss after 3 seconds
- [ ] Multiple toasts stack vertically
- [ ] Manual close button on each toast
- [ ] Enter animation (slide in from corner)
- [ ] Exit animation (fade out or slide out)
- [ ] Toasts don't overlap
