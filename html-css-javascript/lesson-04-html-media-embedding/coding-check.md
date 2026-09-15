# Lesson 04 — Coding Check

Use this to verify your solutions before asking me to review. Open each HTML file in a browser to check it renders correctly.

## Easy

### p01-solve.html (Image gallery)
- [ ] 3 `<img>` elements.
- [ ] Each has `src` pointing to an image file (use placeholder URLs like `https://picsum.photos/400/300` if no local images).
- [ ] Each has non-empty `alt` text describing the image.
- [ ] Each has `width` and/or `height` set.
- [ ] All 3 images render in the browser.

### p02-solve.html (Figure with caption)
- [ ] Has `<figure>` wrapping an `<img>`.
- [ ] `<img>` has `src` and `alt`.
- [ ] Has `<figcaption>` with a caption text.
- [ ] Caption appears below the image in the browser.

### p03-solve.html (Video element)
- [ ] Has `<video>` with `controls` attribute.
- [ ] Has `poster` attribute pointing to an image.
- [ ] Has at least one `<source>` with `type="video/mp4"`.
- [ ] Has `width` set.
- [ ] Controls are visible in the browser (play/pause/seek bar).

## Medium

### p01-solve.html (Responsive image with srcset)
- [ ] `<img>` has `src` (fallback), `srcset`, and `sizes`.
- [ ] `srcset` lists at least 3 images with `w` descriptors (e.g. `400w`, `800w`, `1200w`).
- [ ] `sizes` has a media condition (e.g. `(max-width: 600px) 400px`).
- [ ] `alt` is set.
- [ ] Image renders and changes source when resizing the browser (check Network tab).

### p02-solve.html (Picture element)
- [ ] Has `<picture>` wrapper.
- [ ] At least one `<source>` with `media` condition for mobile.
- [ ] At least one `<source>` with `type="image/webp"`.
- [ ] Fallback `<img>` with `src` (JPEG) and `alt`.
- [ ] Different image loads on narrow vs wide viewport (check with browser dev tools).

### p03-solve.html (Audio and video with multiple sources)
- [ ] `<audio>` has `controls` and 2 `<source>` tags (MP3 + OGG).
- [ ] `<video>` has `controls` and 2 `<source>` tags (MP4 + WebM).
- [ ] Each `<source>` has a `type` attribute.
- [ ] Both players render with visible controls.
- [ ] Fallback text inside both elements for old browsers.

## Hard

### p01-solve.html (Photo gallery with figures and srcset)
- [ ] 6 `<figure>` elements.
- [ ] Each `<figure>` contains an `<img>` with `srcset` (at least 2 sizes) and `alt`.
- [ ] Each `<img>` has `loading="lazy"`.
- [ ] Each `<figure>` has a `<figcaption>`.
- [ ] Images render and captions are visible.
- [ ] Lazy loading works (check Network tab — below-fold images load on scroll).

### p02-solve.html (Media page)
- [ ] `<video>` has `controls`, `poster`, 2 `<source>` tags (MP4 + WebM), and fallback text.
- [ ] `<audio>` has `controls` and 2 `<source>` tags.
- [ ] `<picture>` has a mobile `<source>`, a WebP `<source>`, and a fallback `<img>`.
- [ ] All three media elements render correctly.
- [ ] All images/video have descriptive `alt` or `title`.

### p03-solve.html (Embed page with iframes)
- [ ] Google Maps `<iframe>` with `src`, `title`, `width`, `height`, and `loading="lazy"`.
- [ ] YouTube `<iframe>` with `title` and appropriate `src`.
- [ ] At least one iframe wrapped in `<figure>` with `<figcaption>`.
- [ ] Both iframes have `title` attributes (accessibility).
- [ ] Iframes render content in the browser.
- [ ] No page-wide horizontal scroll (iframes fit within viewport or scroll internally).

## How to verify

Open each file in a browser:
```bash
xdg-open easy/p01-solve.html
```
- For images: check `alt` text appears if the image fails to load (temporarily break the `src` to test).
- For video/audio: confirm controls are visible and the play button works.
- For responsive images: open DevTools → Network tab, resize the browser, and confirm different image files load at different sizes.
- For iframes: confirm the embedded content displays and `title` is set (inspect element).
- For lazy loading: confirm below-the-fold images don't load until you scroll (Network tab).
