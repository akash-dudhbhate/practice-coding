# Lesson 01 — Refactoring Challenges

## Refactor 01 (Easy): Div Soup
### Before
```html
<div class="header"><div class="nav">...</div></div>
<div class="main"><div class="article">...</div></div>
<div class="footer">...</div>
```
### After
```html
<header><nav>...</nav></header>
<main><article>...</article></main>
<footer>...</footer>
```

## Refactor 02 (Medium): Inline Styles
### Before
```html
<p style="color: red; font-size: 18px; margin: 10px;">Text</p>
```
### After
```html
<p class="warning">Text</p>
<style>.warning { color: red; font-size: 18px; margin: 10px; }</style>
```

## Refactor 03 (Hard): No Semantic Structure
### Before
```html
<div id="page">
  <div id="top"><div class="links">...</div></div>
  <div id="content"><div class="post">...</div></div>
</div>
```
### After
```html
<body>
  <header><nav>...</nav></header>
  <main><article>...</article></main>
</body>
