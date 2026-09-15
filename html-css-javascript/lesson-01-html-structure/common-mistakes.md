# Lesson 01 — Common Mistakes

## Mistake 01: Using `<div>` for everything
```html
<!-- WRONG — no semantics -->
<div class="header">...</div>
<div class="nav">...</div>

<!-- CORRECT — semantic HTML -->
<header>...</header>
<nav>...</nav>
```

## Mistake 02: Skipping heading levels
```html
<!-- WRONG -->
<h1>Title</h1>
<h4>Subtitle</h4>

<!-- CORRECT -->
<h1>Title</h1>
<h2>Subtitle</h2>
```

## Mistake 03: Missing alt text
```html
<!-- WRONG — accessibility failure -->
<img src="logo.png">

<!-- CORRECT -->
<img src="logo.png" alt="Company Logo">
```

## Mistake 04: Using `<br>` for spacing
```html
<!-- WRONG -->
<p>Line 1<br><br><br>Line 2</p>

<!-- CORRECT — use CSS margin -->
<p>Line 1</p>
<p>Line 2</p>
```

## Mistake 05: Inline styles
```html
<!-- WRONG -->
<div style="color: red; font-size: 20px;">

<!-- CORRECT — use CSS classes -->
<div class="error">
```
