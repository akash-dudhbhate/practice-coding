# Lesson 13 — Coding Check

## Easy

### p01-solve.html — Hover button transition
- [ ] Button has a background color
- [ ] On hover: background changes AND scales up
- [ ] Uses `transition` with duration (0.3s or similar)
- [ ] Transition is smooth (not instant)

### p02-solve.html — Loading spinner
- [ ] Circular element (border-radius: 50%)
- [ ] Uses `@keyframes` with `rotate(0deg)` to `rotate(360deg)`
- [ ] Animation is `infinite`
- [ ] Spinner spins continuously

### p03-solve.html — Card lift on hover
- [ ] Card has default state (flat)
- [ ] On hover: card moves up (translateY) and shadow increases
- [ ] Uses `transition` for smooth effect
- [ ] Transition includes both transform and box-shadow

## Medium

### p01-solve.html — Staggered fade-in-up
- [ ] `@keyframes` defined: from opacity 0 + translateY(50px) to opacity 1 + translateY(0)
- [ ] 3 elements with the animation
- [ ] Each element has a different `animation-delay` (staggered)
- [ ] Uses `animation-fill-mode: forwards` (retains end state)
- [ ] Elements appear one by one

### p02-solve.html — Bouncing ball
- [ ] Ball animates up and down with `@keyframes`
- [ ] Uses ease-in for downward motion, ease-out for upward
- [ ] Animation loops infinitely
- [ ] Shadow scales (smaller/flatter when ball is higher)
- [ ] Shadow and ball are synchronized

### p03-solve.html — Pulsing badge
- [ ] Red circle badge
- [ ] Scales between 1.0 and 1.2 using `@keyframes`
- [ ] Glow effect (box-shadow) pulses with the scale
- [ ] Animation is `infinite`
- [ ] Smooth pulse rhythm

## Hard

### p01-solve.html — Animated hamburger to X
- [ ] 3 horizontal lines (spans or divs)
- [ ] On click/checkbox toggle: lines transform into X
- [ ] Top line rotates 45deg and translates down
- [ ] Middle line fades out (opacity 0)
- [ ] Bottom line rotates -45deg and translates up
- [ ] Smooth transition on all lines
- [ ] CSS-only (no JS, or minimal JS)

### p02-solve.html — Card flip
- [ ] Card has front and back faces
- [ ] Uses `transform-style: preserve-3d`
- [ ] Uses `backface-visibility: hidden` on both faces
- [ ] Back face is pre-rotated `rotateY(180deg)`
- [ ] On click: container rotates `rotateY(180deg)`
- [ ] Smooth 3D flip animation
- [ ] Both faces have content

### p03-solve.html — Scroll-triggered animations
- [ ] Multiple elements on the page
- [ ] Elements start with `animation-play-state: paused` or opacity 0
- [ ] IntersectionObserver detects when elements enter viewport
- [ ] Elements animate (fade/slide in) when visible
- [ ] Elements below the fold don't animate until scrolled to
- [ ] Smooth animation on each element
- [ ] `prefers-reduced-motion` respected (animations disabled)
