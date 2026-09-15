# Lesson 15 — Refactoring Challenges

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
