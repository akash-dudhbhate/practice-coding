# Lesson 04 — HTML Media & Embedding

## What you'll learn
- How to embed images with `<img>` and write good `alt` text.
- How to serve responsive images with `srcset` and `sizes`.
- How to use `<picture>` for art direction and modern formats.
- How to embed video, audio, and iframes.
- How to group media with `<figure>` and `<figcaption>`.

## Lesson

Web pages aren't just text. HTML lets you embed images, video, audio, and other pages.

### Images
```html
<img src="photo.jpg" alt="A cat sleeping" width="400" height="300" />
```
- `alt` is required — it describes the image for screen readers and broken links.
- `width`/`height` prevent layout shift.

### Responsive images
```html
<img src="photo-400.jpg"
     srcset="photo-400.jpg 400w, photo-800.jpg 800w"
     sizes="(max-width: 600px) 400px, 800px"
     alt="..." />
```
The browser picks the right file for the screen size.

### Art direction with `<picture>`
```html
<picture>
  <source media="(max-width: 600px)" srcset="mobile.jpg" />
  <img src="desktop.jpg" alt="..." />
</picture>
```

### Video and audio
```html
<video controls poster="thumb.jpg">
  <source src="movie.mp4" type="video/mp4" />
</video>

<audio controls>
  <source src="song.mp3" type="audio/mpeg" />
</audio>
```

### Iframes
```html
<iframe src="https://maps.google.com/..." title="Map" loading="lazy"></iframe>
```
- Always include `title` for accessibility.

### Figure with caption
```html
<figure>
  <img src="chart.png" alt="Revenue chart" />
  <figcaption>Figure 1: 2026 Revenue</figcaption>
</figure>
```

### Key rules
- Every `<img>` needs `alt`.
- Every `<iframe>` needs `title`.
- Provide multiple video/audio formats (MP4 + WebM, MP3 + OGG).
- Use `loading="lazy"` for below-the-fold media.
- Use `<figure>`/`<figcaption>` to group images with captions.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete HTML from scratch below** to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.html` — An image gallery with 3 `<img>` tags, each with `src`, `alt`, and `width`.
2. `easy/p02-solve.html` — A `<figure>` with an image and `<figcaption>` caption.
3. `easy/p03-solve.html` — A `<video>` element with controls, a poster image, and one MP4 source.

### Medium
4. `medium/p01-solve.html` — A responsive image using `srcset` with 3 sizes and `sizes` attribute.
5. `medium/p02-solve.html` — A `<picture>` element with a mobile and desktop source, plus a WebP source with JPEG fallback.
6. `medium/p03-solve.html` — An `<audio>` player with controls and two sources (MP3 + OGG), plus a `<video>` with MP4 + WebM sources.

### Hard
7. `hard/p01-solve.html` — A photo gallery with 6 `<figure>` elements, each with responsive `srcset` images, captions, and `loading="lazy"`.
8. `hard/p02-solve.html` — A media page with a `<video>` (poster, controls, two formats, fallback text), an `<audio>` player, and a responsive `<picture>` hero image.
9. `hard/p03-solve.html` — An embed page with a Google Maps `<iframe>` (title, lazy loading), a YouTube iframe, and a `<figure>` containing the iframe with a caption.

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete HTML from scratch** below the TODO marker.
- Remove the TODO comment when done.
- Open the file in a browser to check it renders correctly.
- When done, tell me and I'll review. Say **"give me next task"** to advance.
