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
1. `easy/p01-image-gallery.html` — An image gallery with 3 `<img>` tags, each with `src`, `alt`, and `width`.

   ```
   WHAT IT SHOULD LOOK LIKE:
   Image Gallery                           <- <h2> heading
   [photo]  [photo]  [photo]                 <- three 200px-wide
                                               images in a row
   ```
2. `easy/p02-audio-player.html` — An `<audio>` player with controls, one MP3 `<source>`, and fallback text.

   ```
   WHAT IT SHOULD LOOK LIKE:
   | |> ====o========== 0:00 ((.))|   <- native audio player bar:
                                        play button, timeline, volume
   ```
3. `easy/p03-video-player.html` — A `<video>` element with controls, `width="400"`, one MP4 `<source>`, and fallback text.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +-----------------------------+
   |                             |
   |        [ video area ]       |   <- 400px-wide video
   |                             |
   | |> ======o========= 0:00    |   <- native controls + timeline
   +-----------------------------+
   ```

### Medium
4. `medium/p01-responsive-picture.html` — A `<picture>` element serving different images per screen size via `<source media="...">`, with an `<img>` fallback.

   ```
   WHAT IT SHOULD LOOK LIKE:
   DESKTOP (>=800px):              TABLET (>=400px):   PHONE (<400px):
   +------------------------+      +-------------+     +--------+
   |    big image loads     |      | medium img  |     | small  |
   +------------------------+      +-------------+     +--------+
   (browser picks the first matching <source>; <img> is the fallback)
   ```
5. `medium/p02-youtube-embed.html` — A YouTube video embedded with `<iframe>` using an `/embed/` URL, plus `title` and `allowfullscreen`.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +-----------------------------+
   |                             |
   |   [ YouTube thumbnail ]     |   <- 560x315 playable player
   |          >                  |      embedded in the page
   |                             |
   +-----------------------------+
   (a /watch?v= URL would refuse to load — /embed/ is required)
   ```
6. `medium/p03-audio-playlist.html` — A playlist: a `<ul>` where each `<li>` has a track label and its own `<audio controls>` player.

   ```
   WHAT IT SHOULD LOOK LIKE:
   Tracklist
   - Track 1   |> ====o====== 0:00   <- own player per track
   - Track 2   |> ======o==== 0:00
   ```

### Hard
7. `hard/p01-video-gallery-captions.html` — A gallery of 2+ videos, each in `<figure>` with `<figcaption>`; at least one video gets a subtitle `<track>`.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +-----------+     +-----------+
   | [video]   |     | [video]   |   <- two 300px videos
   | |> ==o=== |     | |> ==o=== |      first has CC subtitles
   +-----------+     +-----------+
   caption text      caption text    <- <figcaption> under each
   ```
8. `hard/p02-maps-embed.html` — A Google Maps `<iframe>` embed, `600x450`, `loading="lazy"`, `allowfullscreen`, `border:0`.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +-------------------------------+
   |      [ interactive map ]      |   <- 600x450 Google map;
   |   (roads, labels, zoom UI)    |      only loads when scrolled
   +-------------------------------+      into view (lazy)
   ```
9. `hard/p03-media-landing-page.html` — A landing page combining it all: `<header>` title, auto-playing muted looping hero `<video>`, a 3-photo gallery, `<footer>`, and `object-fit: cover` styling.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +-------------------------------+
   |        PAGE TITLE             |   <- <header>
   +-------------------------------+
   |   [ hero video playing ]      |   <- autoplay+muted+loop,
   |      (fills the box)          |      object-fit: cover
   +-------------------------------+
   | [photo] [photo] [photo]       |   <- 3-image gallery, alt each
   +-------------------------------+
   |        footer text            |   <- <footer>
   +-------------------------------+
   ```

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete HTML from scratch** below the TODO marker.
- Remove the TODO comment when done.
- Open the file in a browser to check it renders correctly.
- When done, tell me and I'll review. Say **"give me next task"** to advance.
