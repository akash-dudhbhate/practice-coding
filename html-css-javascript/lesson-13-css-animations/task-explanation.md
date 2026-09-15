# Lesson 13 — CSS Animations & Transitions

## What you'll learn
- transition (property, duration, timing, delay)
- transform (translate, scale, rotate, skew)
- @keyframes for multi-step animations
- animation properties (iteration, direction, fill-mode)
- Common animation patterns (fade, slide, bounce, pulse, spin)
- transform-origin
- will-change for performance
- prefers-reduced-motion for accessibility

## Lesson

### Transition
```css
.btn { transition: transform 0.3s ease; }
.btn:hover { transform: scale(1.1); }
```

### Keyframes
```css
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
.element { animation: fadeIn 0.5s ease forwards; }
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.html` — Create a button that smoothly changes background color and scales up on hover using `transition`.
2. `easy/p02-solve.html` — Create a loading spinner using `@keyframes spin` (360-degree rotation, infinite loop).
3. `easy/p03-solve.html` — Create a card that lifts up (translateY + box-shadow) on hover with a smooth transition.

### Medium
4. `medium/p01-solve.html` — Create a fade-in-up entrance animation using `@keyframes`: element starts invisible and 50px below, animates to visible and in position. Apply to 3 elements with staggered delays.
5. `medium/p02-solve.html` — Create a bouncing ball animation using `@keyframes`. Ball bounces up and down with realistic timing (ease-in going down, ease-out going up). Add a shadow that scales with the bounce.
6. `medium/p03-solve.html` — Create a pulsing notification badge: red circle that scales between 1.0 and 1.2 with a glow effect. Use `@keyframes pulse` with `infinite` iteration.

### Hard
7. `hard/p01-solve.html` — Build an animated hamburger menu icon: 3 lines that smoothly transform into an X when clicked (use transform rotate and translate). No JavaScript for the animation (CSS-only with checkbox hack).
8. `hard/p02-solve.html` — Build an animated card flip: card flips on click showing front and back faces. Use `transform: rotateY(180deg)`, `transform-style: preserve-3d`, and `backface-visibility: hidden`.
9. `hard/p03-solve.html` — Build a page with scroll-triggered animations: elements fade in as you scroll. Use CSS animations with `animation-play-state: paused` and minimal JS to trigger them when visible (IntersectionObserver).

### How to work
- Write your complete HTML + CSS solution (inline or in `<style>` tags).
- Remove the TODO comment when done.
- Open in browser to test visually.
