# lesson-04-html-media-embedding — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: img formats
When should you use SVG vs PNG vs JPG?
<details><summary>Answer</summary>
- SVG — logos, icons, simple graphics (scalable, small)
- PNG — graphics with transparency
- JPG — photos (lossy compression)
- WebP — modern format, better compression (use when supported)
</details>

## Check 02: video attributes
What do `autoplay`, `muted`, `loop` do?
<details><summary>Answer</summary>
- `autoplay` — starts playing immediately (often blocked unless `muted`)
- `muted` — no audio
- `loop` — repeats
</details>

## Check 03: picture element
```html
<picture>
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="Photo">
</picture>
```
<details><summary>Answer</summary>
Serves WebP if supported, falls back to JPG. Progressive enhancement for image formats.
</details>

## Check 04: audio vs video
Can `<audio>` have a `poster` attribute?
<details><summary>Answer</summary>
No — `poster` is only for `<video>` (shows an image before playing). Audio has no visual component.
</details>

## Check 05: lazy loading
```html
<img src="photo.jpg" loading="lazy" alt="Photo">
```
<details><summary>Answer</summary>
`loading="lazy"` defers loading until the image is near the viewport. Saves bandwidth and improves initial page load.
</details>

---

## Debug Exercises — find and fix the bug

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

---

## Common Mistakes — the traps learners hit

## Mistake 01: No alt text
```html
<!-- WRONG -->
<img src="photo.jpg">
<!-- CORRECT -->
<img src="photo.jpg" alt="Sunset over mountains">
```

## Mistake 02: Huge images
```html
<!-- WRONG — 5MB image for a 200px thumbnail -->
<img src="huge-photo.jpg" width="200">
<!-- CORRECT — resize on server -->
<img src="thumbnail.jpg" width="200" alt="...">
```

## Mistake 03: No video controls
```html
<!-- WRONG -->
<video src="movie.mp4"></video>
<!-- CORRECT -->
<video src="movie.mp4" controls></video>
```

## Mistake 04: Iframe without title
```html
<!-- WRONG -->
<iframe src="..."></iframe>
<!-- CORRECT -->
<iframe src="..." title="Map"></iframe>
```

## Mistake 05: Not using lazy loading
```html
<!-- WRONG — loads all images immediately -->
<img src="photo.jpg" alt="...">
<!-- CORRECT — loads when needed -->
<img src="photo.jpg" loading="lazy" alt="...">
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Flex for Grid Layout
### Before
```css
.row { display: flex; flex-wrap: wrap; }
.col { flex: 1 1 33.33%; }
```
### After
```css
.grid { display: grid; grid-template-columns: repeat(3, 1fr); }
```

## Refactor 02 (Medium): Media Query for Columns
### Before
```css
.grid { grid-template-columns: 1fr; }
@media (min-width: 768px) { .grid { grid-template-columns: 1fr 1fr; } }
@media (min-width: 1024px) { .grid { grid-template-columns: 1fr 1fr 1fr; } }
```
### After
```css
.grid { grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }
```

## Refactor 03 (Hard): Nested Flex for Grid
### Before
```css
.layout { display: flex; }
.sidebar { width: 250px; }
.content { display: flex; flex-direction: column; }
```
### After
```css
.layout { display: grid; grid-template-columns: 250px 1fr; }

---

## Approach Comparison — different ways to solve it

## Problem: Responsive Images

### Approach 1: srcset
```html
<img src="small.jpg"
     srcset="small.jpg 500w, medium.jpg 1000w, large.jpg 2000w"
     sizes="(max-width: 600px) 100vw, 50vw"
     alt="Photo">
```

### Approach 2: picture
```html
<picture>
  <source media="(max-width: 600px)" srcset="mobile.jpg">
  <source media="(min-width: 601px)" srcset="desktop.jpg">
  <img src="fallback.jpg" alt="Photo">
</picture>
```

**Winner:** `srcset` for same image at different resolutions. `picture` for different images at different breakpoints or formats.
