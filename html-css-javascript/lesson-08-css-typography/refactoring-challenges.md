# Lesson 08 — Refactoring Challenges

## Refactor 01 (Easy): onclick Property
### Before
```javascript
btn.onclick = handleClick;
```
### After
```javascript
btn.addEventListener("click", handleClick);
```

## Refactor 02 (Medium): Many Individual Listeners
### Before
```javascript
document.querySelectorAll(".btn").forEach(b => {
  b.addEventListener("click", handleClick);
});
```
### After
```javascript
document.addEventListener("click", e => {
  if (e.target.matches(".btn")) handleClick(e);
});
```

## Refactor 03 (Hard): No Event Delegation
### Before
```javascript
list.forEach(item => item.addEventListener("click", () => deleteItem(item.id)));
```
### After
```javascript
parent.addEventListener("click", e => {
  const item = e.target.closest(".item");
  if (item) deleteItem(item.dataset.id);
});
```
