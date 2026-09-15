# Lesson 01 — Debug Exercises

## Debug 01 (Easy): Unclosed Tag
```html
<div>
  <p>Hello world
</div>
```
<details><summary>Answer</summary>
**Bug:** `<p>` is never closed. Browsers auto-close it, but it's invalid HTML.
**Fix:** `<p>Hello world</p>`.
</details>

## Debug 02 (Medium): Wrong Heading Hierarchy
```html
<h1>Title</h1>
<h3>Subtitle</h3>
<h2>Section</h2>
```
<details><summary>Answer</summary>
**Bug:** Skips h2 before h3. Bad for accessibility and SEO.
**Fix:** Use h1 → h2 → h3 in order. Don't skip levels.
</details>

## Debug 03 (Hard): Missing DOCTYPE
```html
<html>
<head><title>Test</title></head>
<body>Hello</body>
</html>
```
<details><summary>Answer</summary>
**Bug:** No `<!DOCTYPE html>`. Browser may render in quirks mode (inconsistent behavior).
**Fix:** Add `<!DOCTYPE html>` as the first line.
</details>
