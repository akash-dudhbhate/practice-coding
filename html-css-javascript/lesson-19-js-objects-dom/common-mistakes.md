# Lesson 19 — Common Mistakes

## Mistake 01: innerHTML with user input
```javascript
// WRONG — XSS risk
el.innerHTML = userInput;
// CORRECT
el.textContent = userInput;
```

## Mistake 02: Confusing getElementById and querySelector
```javascript
// WRONG — . is for class selectors
document.getElementById(".box");
// CORRECT
document.getElementById("box");     // by ID, no #
document.querySelector(".box");     // CSS selector
```

## Mistake 03: NodeList doesn't have array methods
```javascript
// WRONG
document.querySelectorAll(".x").map(...);
// CORRECT
[...document.querySelectorAll(".x")].map(...);
```

## Mistake 04: className overwriting
```javascript
// WRONG — overwrites all classes
el.className = "active";
// CORRECT — adds to existing
el.classList.add("active");
```

## Mistake 05: Not using textContent
```javascript
// WRONG — slower, parses HTML
el.innerHTML = "Just text";
// CORRECT — faster, safer
el.textContent = "Just text";
```
