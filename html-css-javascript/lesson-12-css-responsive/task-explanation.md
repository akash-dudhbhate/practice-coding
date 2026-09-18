# Lesson 12 — CSS Responsive Design

## What you'll learn
- Viewport meta tag
- Media queries (min-width, max-width)
- Mobile-first design approach
- Common breakpoints
- Relative units (rem, em, %, vw, vh)
- clamp() for fluid typography
- Responsive images (srcset, picture)
- Flexbox/Grid responsive patterns
- Hide/show elements per breakpoint
- Mobile navigation (hamburger menu)

## Lesson

### Media query
```css
@media (min-width: 768px) {
    .container { flex-direction: row; }
}
```

### Fluid typography
```css
font-size: clamp(1rem, 5vw, 3rem);
```

### Responsive grid
```css
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.html` — Create a page with viewport meta tag. Make the body font-size change at 768px breakpoint (16px mobile, 18px desktop).

   ```
   WHAT IT SHOULD LOOK LIKE:
   NARROW (<768px):                WIDE (>=768px):
   normal 16px body text           slightly larger 18px body text
   ```
2. `easy/p02-solve.html` — Create a container that is full-width on mobile, max-width 1200px centered on desktop. Use media queries.

   ```
   WHAT IT SHOULD LOOK LIKE:
   MOBILE:                         DESKTOP:
   +----------------------+        | +------------------+ |
   | content edge-to-edge |        | | max 1200px,        | |  <- centered,
   +----------------------+        | | space on the sides | |      auto margins
                                   | +------------------+ |
   ```
3. `easy/p03-solve.html` — Create a responsive heading using `clamp()`: minimum 1.5rem, preferred 5vw, maximum 3rem.

   ```
   WHAT IT SHOULD LOOK LIKE:
   NARROW:          MEDIUM:               WIDE:
   Heading          Heading               HEADING
   (1.5rem floor)   (5vw - fluid)         (3rem ceiling, stops growing)
   ```

### Medium
4. `medium/p01-solve.html` — Create a responsive card grid: 1 column on mobile, 2 on tablet (768px), 3 on desktop (1024px). Use media queries.

   ```
   WHAT IT SHOULD LOOK LIKE:
   MOBILE (1 col):    TABLET (2):         DESKTOP (3):
   +---------+        +-----+  +-----+    +-----+-----+-----+
   |  card   |        |card |  |card |    |card |card |card |
   +---------+        +-----+  +-----+    +-----+-----+-----+
   |  card   |        |card |  |card |    |card |card |card |
   +---------+        +-----+  +-----+    +-----+-----+-----+
   ```
5. `medium/p02-solve.html` — Create a responsive navigation: horizontal links on desktop, hamburger menu on mobile. Use CSS-only toggle (checkbox hack) or simple JS.

   ```
   WHAT IT SHOULD LOOK LIKE:
   DESKTOP:                        MOBILE:
   +----------------------------+  +---------+
   | LOGO   Home About Contact  |  | LOGO [=]|  <- hamburger icon
   +----------------------------+  +---------+
                                      | Home  |  <- tap toggles the
                                      | About |     vertical menu
                                      |Contact|
                                      +-------+
   ```
6. `medium/p03-solve.html` — Create a responsive hero section: full viewport height, fluid title with clamp(), background image that changes size with `background-size: cover`. Add a CTA button that's full-width on mobile, auto-width on desktop.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +------------------------------------------+
   |~~~~~~ cover background image ~~~~~~~~~~~~|
   |                                          |
   |         FLUID TITLE (clamp)              |
   |                                          |
   |   DESKTOP: [CTA]                         |   <- auto width
   |   MOBILE:  [========CTA========]         |   <- stretches full width
   +------------------------------------------+
   ```

### Hard
7. `hard/p01-solve.html` — Build a full responsive landing page: header with nav, hero section, features grid (1/2/3 columns), testimonials, footer. All sections adapt to mobile/tablet/desktop.

   ```
   WHAT IT SHOULD LOOK LIKE:
   DESKTOP:                        MOBILE:
   +----------------------------+    +----------+
   | nav (row of links)         |    | nav  [=] |
   | HERO: big title + CTA      |    | HERO     |
   | [feat][feat][feat]         |    | [feat]   |   <- stacks 1 col
   | "quote"      "quote"       |    | [feat]   |
   | footer                     |    | [feat]   |
   +----------------------------+    | "quote"  |
                                     | footer   |
                                     +----------+
   ```
8. `hard/p02-solve.html` — Build a responsive dashboard: sidebar collapses to icons on tablet, hidden on mobile (toggle button). Content area has a widget grid that reflows. Use CSS transitions for smooth changes.

   ```
   WHAT IT SHOULD LOOK LIKE:
   DESKTOP:             TABLET:              MOBILE:
   +-----+----------+   +--+-----------+     +----------+
   |side| w1 w2 w3 w4|  |i | w1    w2  |     | [=]  w1  |
   |bar |            |  |co| w3    w4  |     |      w2  |
   |(txt| 4 across   |  |ns| 2 across  |     |      w3  |
   +-----+----------+   +--+-----------+     | (sidebar |
                                             |  hidden) |
                                             +----------+
   ```
9. `hard/p03-solve.html` — Build a responsive image gallery: uses `<picture>` with different images per breakpoint. Grid layout with `auto-fit` and `minmax`. Lightbox effect on click (CSS-only or minimal JS). Images have `loading="lazy"`.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +------------------------------------------+
   | [pic] [pic] [pic]   <- auto-fit grid of  |
   | [pic] [pic] [pic]      <picture> images  |
   +------------------------------------------+
   CLICK ONE ->
   +##########################################+
   |#         +------------------+           #|   <- dark full-screen
   |#         |   LARGE IMAGE    |           #|      overlay (lightbox),
   |#         +------------------+           #|      no JS needed
   +##########################################+
   ```

### How to work
- Write your complete HTML + CSS solution (inline or in `<style>` tags).
- Remove the TODO comment when done.
- Test in browser: resize window, use DevTools mobile emulation.
