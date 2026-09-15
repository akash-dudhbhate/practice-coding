# Lesson 15 — Common Mistakes

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
