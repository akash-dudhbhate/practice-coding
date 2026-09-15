# Lesson 04 — Concepts Explained (HTML Media & Embedding)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## The `<img>` Element

**What:** The `<img>` tag embeds an image. It's a self-closing tag that requires `src` and `alt`.

```html
<img src="photo.jpg" alt="A golden retriever playing in the park" width="400" />
```

- `src` = the image file path or URL.
- `alt` = text describing the image (for screen readers and when the image fails to load).
- `width`/`height` = set dimensions to prevent layout shift.

**Why it exists:** Web pages would be text-only without images. The `<img>` tag lets you embed pictures, charts, icons, and photos directly into content.

**Where it's used:** Every web page — photos, logos, charts, thumbnails, illustrations, banners.

**What goes wrong without it:**
- Missing `alt` → screen readers say "image" with no context; blind users get nothing. Also fails accessibility audits (WCAG).
- Missing `width`/`height` → the page jumps (layout shift) as images load, causing a poor CLS (Cumulative Layout Shift) score.
- Broken `src` path → broken image icon; always test paths.
- Using `alt` for SEO keyword stuffing → accessibility penalty, bad practice. Describe the image, don't stuff keywords.

---

## Responsive Images (`srcset` and `sizes`)

**What:** The `srcset` attribute lets you provide multiple image files at different resolutions. The browser picks the best one for the user's screen.

```html
<img
  src="photo-400.jpg"
  srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1200.jpg 1200w"
  sizes="(max-width: 600px) 400px, 800px"
  alt="A landscape photo"
/>
```

- `srcset` lists images with their intrinsic width (`400w` = 400 pixels wide).
- `sizes` tells the browser how wide the image will be displayed at different viewport sizes.
- `src` is the fallback for old browsers.

**Why it exists:** A phone doesn't need a 4000px image — it wastes bandwidth and slows the page. A retina laptop needs a higher-res image to look sharp. `srcset` lets the browser download the right file for each device.

**Where it's used:** Hero images, photo galleries, article images, any image shown on both mobile and desktop.

**What goes wrong without it:**
- Serving one huge image to everyone → slow page on mobile, wasted data.
- Serving one tiny image to everyone → blurry on retina/high-res screens.
- Wrong `sizes` → browser downloads the wrong file, wasting bandwidth.
- Forgetting the `w` unit (using `2x` instead) → `sizes` won't work with `w` descriptors; pick one system.

---

## The `<picture>` Element (Art Direction)

**What:** `<picture>` lets you swap entirely different images based on conditions (screen size, format support) — not just different sizes of the same image.

```html
<picture>
  <source media="(max-width: 600px)" srcset="mobile-photo.jpg" />
  <source media="(min-width: 601px)" srcset="desktop-photo.jpg" />
  <img src="desktop-photo.jpg" alt="A scenic mountain view" />
</picture>
```

- `<source>` defines conditions; the browser uses the first match.
- `<img>` is the fallback (always required inside `<picture>`).

You can also use it for modern image formats:
```html
<picture>
  <source type="image/webp" srcset="photo.webp" />
  <source type="image/jpeg" srcset="photo.jpg" />
  <img src="photo.jpg" alt="..." />
</picture>
```

**Why it exists:** `srcset` only serves different SIZES of the same image. But sometimes you need a different CROP or composition for mobile (a close-up) vs desktop (a wide shot). `<picture>` handles art direction. It also serves modern formats (WebP, AVIF) with a fallback.

**Where it's used:** Hero banners with different crops for mobile/desktop, serving WebP/AVIF with JPEG fallback, art-directed photo galleries.

**What goes wrong without it:**
- Using `srcset` when you need a different crop → mobile gets a tiny version of a wide image, subject is unrecognizable.
- Forgetting the `<img>` fallback inside `<picture>` → old browsers show nothing.
- `<source>` order matters — put the most specific conditions first.

---

## The `<video>` Element

**What:** Embeds a video player with native controls.

```html
<video controls width="640" poster="thumbnail.jpg">
  <source src="movie.mp4" type="video/mp4" />
  <source src="movie.webm" type="video/webm" />
  Your browser does not support the video tag.
</video>
```

- `controls` = show play/pause/seek controls.
- `poster` = image shown before the video plays.
- `width`/`height` = set dimensions.
- Multiple `<source>` tags = browser picks the first format it supports.
- Text inside the tag = fallback for very old browsers.

**Why it exists:** Before HTML5, videos required Flash plugins (which had security issues and didn't work on iPhones). The `<video>` element gives native, plugin-free video playback.

**Where it's used:** Tutorial videos, product demos, background videos, video blogs, streaming previews.

**What goes wrong without it:**
- Missing `controls` → users can't play/pause the video (unless you build custom controls with JS).
- No `poster` → blank space or first frame flash before playback.
- Only one format → some browsers can't play it (Safari needs MP4/H.264; Chrome prefers WebM). Always provide MP4 + WebM.
- Huge video files with no preload control → page loads slowly. Use `preload="none"` or `preload="metadata"`.

---

## The `<audio>` Element

**What:** Embeds an audio player with native controls.

```html
<audio controls>
  <source src="song.mp3" type="audio/mpeg" />
  <source src="song.ogg" type="audio/ogg" />
  Your browser does not support the audio tag.
</audio>
```

- `controls` = show play/pause/seek/volume controls.
- Multiple `<source>` tags = browser picks the first supported format.
- Unlike `<video>`, there's no `poster` (no visual element).

**Why it exists:** Like `<video>`, this replaced plugin-based audio (Flash, QuickTime) with native browser playback.

**Where it's used:** Podcast players, music sites, pronunciation guides, notification sounds.

**What goes wrong without it:**
- Missing `controls` → invisible player, users can't play it.
- Autoplaying audio on page load → terrible UX, most browsers block it anyway. Always let the user press play.
- Only one format → some browsers can't play it. Provide MP3 + OGG.
- No fallback text → old browsers show nothing with no explanation.

---

## The `<iframe>` Element

**What:** An inline frame that embeds another web page inside your page.

```html
<iframe
  src="https://www.google.com/maps/embed?..."
  width="600"
  height="400"
  title="Map of Delhi"
  loading="lazy"
></iframe>
```

- `src` = the URL to embed.
- `title` = describes the iframe for screen readers (required for accessibility).
- `loading="lazy"` = only load the iframe when it scrolls into view (saves bandwidth).
- `sandbox` = restricts what the embedded page can do (security).

**Why it exists:** Sometimes you need to show content from another site — a Google Map, a YouTube video, a social media widget — without hosting it yourself. The iframe embeds it in a sandboxed frame.

**Where it's used:** Google Maps embeds, YouTube videos, social media widgets (Twitter, Instagram), payment forms (Stripe), ads.

**What goes wrong without it:**
- Missing `title` → screen readers announce "iframe" with no context → inaccessible.
- No `sandbox` → the embedded page can run scripts, access your cookies, redirect your page. Always use `sandbox` for untrusted content.
- Embedding without permission → some sites block iframes via `X-Frame-Options` header (they show a blank page).
- Fixed width/height with no responsive handling → iframe overflows on mobile.

---

## The `<figure>` and `<figcaption>` Elements

**What:** `<figure>` wraps an image (or other media) that is referenced in the text. `<figcaption>` gives it a caption.

```html
<figure>
  <img src="chart.png" alt="Sales chart showing 2026 revenue" />
  <figcaption>Figure 1: Monthly revenue for 2026</figcaption>
</figure>
```

- The image and caption are grouped as a unit.
- `<figcaption>` is optional but recommended.

**Why it exists:** Images and their captions belong together. Without `<figure>`, the image and caption are separate elements that could get separated by layout. `<figure>` says "these belong together" and lets the caption stay with the image.

**Where it's used:** Blog posts with images, scientific articles, documentation, photo galleries, charts with captions.

**What goes wrong without it:**
- Image and caption get separated in responsive layouts.
- Screen readers don't know the caption is related to the image.
- Using `<div>` → no semantic relationship between image and caption.
- Putting text after an `<img>` without `<figcaption>` → it's just a paragraph, not a caption.

---

## The `loading="lazy"` Attribute

**What:** Tells the browser to delay loading an image/iframe until it's about to scroll into view.

```html
<img src="photo.jpg" alt="..." loading="lazy" />
<iframe src="map.html" loading="lazy"></iframe>
```

- `lazy` = load when near viewport.
- `eager` = load immediately (default).

**Why it exists:** A page with 50 images loads all 50 at once by default, even if 40 are below the fold. Lazy loading only loads what's needed, saving bandwidth and speeding up the initial page load.

**Where it's used:** Image galleries, long articles with many images, iframes (maps, videos) below the fold.

**What goes wrong without it:**
- All images load immediately → slow page load, high data usage on mobile.
- Don't use `lazy` on above-the-fold images (like hero images) → it delays the most important content.
- Lazy loading without `width`/`height` → layout shift as images load (browser doesn't know the size until it loads).
