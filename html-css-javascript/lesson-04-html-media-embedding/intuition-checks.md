# Lesson 04 — Intuition Checks

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
