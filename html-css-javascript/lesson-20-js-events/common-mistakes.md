# Lesson 20 — Common Mistakes

## Mistake 01: Inline event handlers
```html
<!-- WRONG — mixes HTML and JS -->
<button onclick="handleClick()">
<!-- CORRECT -->
<button id="myBtn">
<script>
document.getElementById("myBtn").addEventListener("click", handleClick);
</script>
```

## Mistake 02: Not using event delegation
```javascript
// WRONG — listener per item
items.forEach(item => item.addEventListener("click", handler));
// CORRECT — one listener on parent
list.addEventListener("click", (e) => {
  if (e.target.matches(".item")) handler(e);
});
```

## Mistake 03: Memory leaks
```javascript
// WRONG — never removed
el.addEventListener("click", handler);
// CORRECT — remove when done
el.removeEventListener("click", handler);
// or use { once: true }
```

## Mistake 04: Forgetting preventDefault
```javascript
// WRONG — form submits and reloads page
form.addEventListener("submit", () => {
  saveData();
});
// CORRECT
form.addEventListener("submit", (e) => {
  e.preventDefault();
  saveData();
});
```

## Mistake 05: Not checking event target
```javascript
// WRONG — fires for any click in container
container.addEventListener("click", handler);
// CORRECT — check what was actually clicked
container.addEventListener("click", (e) => {
  if (e.target.matches(".button")) handler(e);
});
```
