# Lesson 03 — Common Mistakes

## Mistake 01: Tables for layout
```html
<!-- WRONG -->
<table>
  <tr><td class="sidebar">...</td><td class="content">...</td></tr>
</table>

<!-- CORRECT — use CSS -->
<div class="layout">
  <aside>...</aside>
  <main>...</main>
</div>
```

## Mistake 02: Missing th scope
```html
<!-- WRONG -->
<th>Name</th>

<!-- CORRECT -->
<th scope="col">Name</th>
```

## Mistake 03: No thead/tbody
```html
<!-- WRONG — all in one block -->
<table>
  <tr><th>A</th></tr>
  <tr><td>1</td></tr>
</table>

<!-- CORRECT -->
<table>
  <thead><tr><th>A</th></tr></thead>
  <tbody><tr><td>1</td></tr></tbody>
</table>
```

## Mistake 04: Forgetting caption
```html
<!-- Add caption for accessibility -->
<table>
  <caption>Monthly Sales</caption>
  ...
</table>
```

## Mistake 05: Not handling responsive tables
```html
<!-- Tables overflow on mobile — wrap in a scroll container -->
<div style="overflow-x: auto;">
  <table>...</table>
</div>
```
