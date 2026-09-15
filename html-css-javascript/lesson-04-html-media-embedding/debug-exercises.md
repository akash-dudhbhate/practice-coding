# Lesson 04 — Debug Exercises

## Debug 01 (Easy): Missing alt
```html
<img src="banner.jpg">
```
<details><summary>Answer</summary>
**Bug:** No `alt` attribute — accessibility failure.
**Fix:** `alt=""` for decorative, `alt="Description"` for meaningful images.
</details>

## Debug 02 (Medium): Video Without Controls
```html
<video src="movie.mp4"></video>
```
<details><summary>Answer</summary>
**Bug:** No `controls` attribute — user can't play/pause.
**Fix:** `<video src="movie.mp4" controls></video>`.
</details>

## Debug 03 (Hard): Iframe Without title
```html
<iframe src="https://example.com"></iframe>
```
<details><summary>Answer</summary>
**Bug:** No `title` — screen readers announce it as "frame" with no context.
**Fix:** `<iframe src="..." title="Example Site"></iframe>`.
</details>
