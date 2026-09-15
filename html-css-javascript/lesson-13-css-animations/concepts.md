# Lesson 13 — Concepts Explained (CSS Animations & Transitions)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## transition

**What:** `transition` smoothly animates CSS property changes. When a property changes (e.g., on hover), it transitions over a duration instead of changing instantly.

```css
.button {
    background: blue;
    transition: background 0.3s ease, transform 0.3s ease;
}
.button:hover {
    background: darkblue;
    transform: scale(1.1);
}
/* Background smoothly changes over 0.3s when hovering */
```

**Why it exists:** Without transitions, property changes are instant → jarring, abrupt. Transitions make UI feel smooth and polished — buttons that grow on hover, menus that slide open, colors that fade.

**Where it's used:** Hover effects, focus states, button presses, menu toggles, card flips, any interactive element.

**What goes wrong without it:**
- Transitioning `display` → doesn't work (display is not animatable). Use `opacity` or `visibility` instead.
- Transitioning `width`/`height` → causes layout recalculations → janky. Prefer `transform: scale()`.
- No duration specified → defaults to 0s → instant change, no animation. Always specify duration.
- `transition: all` → transitions ALL properties → performance issues. Be specific: `transition: opacity 0.3s`.

---

## transition-property, duration, timing-function, delay

**What:** The four components of a transition:

```css
.element {
    transition-property: transform, opacity;  /* what to animate */
    transition-duration: 0.3s;                 /* how long */
    transition-timing-function: ease-in-out;   /* acceleration curve */
    transition-delay: 0.1s;                    /* wait before starting */

    /* Shorthand: property duration timing delay */
    transition: transform 0.3s ease-in-out 0.1s;
}
```

Timing functions:
- `ease` (default) — slow start, fast middle, slow end
- `linear` — constant speed
- `ease-in` — slow start, fast end
- `ease-out` — fast start, slow end
- `ease-in-out` — slow start and end
- `cubic-bezier(x1, y1, x2, y2)` — custom curve

**Why it exists:** Different timing functions create different feels. `ease-out` feels responsive (fast start). `ease-in` feels deliberate (slow start). Linear feels mechanical. Choosing the right one is key to good UX.

**Where it's used:** Every transition. The timing function is what makes an animation feel "natural" vs "robotic."

**What goes wrong without it:**
- `linear` for everything → feels mechanical, unnatural. Natural motion accelerates and decelerates.
- Too long duration (> 0.5s) → feels sluggish. Most UI transitions should be 0.2-0.4s.
- Negative delay → animation starts partway through → useful for staggered animations but confusing if unintended.

---

## transform

**What:** `transform` modifies an element's position, size, or rotation WITHOUT affecting layout.

```css
/* Move */
transform: translate(50px, 100px);   /* x, y */
transform: translateX(50px);
transform: translateY(100px);

/* Scale */
transform: scale(1.5);               /* 1.5x size */
transform: scale(2, 1);              /* 2x wide, 1x tall */

/* Rotate */
transform: rotate(45deg);            /* 45 degrees clockwise */
transform: rotate(-15deg);           /* counterclockwise */

/* Skew */
transform: skew(10deg, 5deg);        /* skew x and y */

/* Combine */
transform: translate(50px, 0) rotate(45deg) scale(1.2);
```

**Why it exists:** Without transform, you'd use `top`/`left` to move elements → triggers layout recalculation → slow. Transform uses the GPU → smooth 60fps. It also doesn't affect surrounding elements.

**Where it's used:** Hover effects (scale up), entrance animations (translate from off-screen), rotations, card flips, parallax.

**What goes wrong without it:**
- Animating `top`/`left` instead of `transform: translate()` → layout recalculations → janky. Always use transform.
- `transform: scale(2)` → element scales from center. To scale from a different point, use `transform-origin: top left`.
- Order matters: `translate(50px) rotate(45deg)` ≠ `rotate(45deg) translate(50px)`. The element translates, then rotates around the new position.

---

## @keyframes

**What:** Define multi-step animations with `@keyframes`.

```css
@keyframes bounce {
    0%   { transform: translateY(0); }
    50%  { transform: translateY(-50px); }
    100% { transform: translateY(0); }
}

.element {
    animation: bounce 1s ease-in-out infinite;
}
```

**Why it exists:** Transitions only go from A to B (start state to end state). `@keyframes` can have multiple steps (0%, 25%, 50%, 75%, 100%) → complex animations like bouncing, pulsing, wave effects.

**Where it's used:** Loading spinners, bounce effects, pulse animations, wave effects, entrance animations, continuous loops.

**What goes wrong without it:**
- `0%` and `100%` vs `from` and `to` → both work. `from { } to { }` is shorthand for `0% { } 100% { }`.
- Forgetting `infinite` → animation plays once and stops. Use `infinite` for loops.
- Keyframe percentages must be 0-100%. `50%` = halfway through the duration.

---

## animation Properties

**What:** Control how `@keyframes` animations play.

```css
.element {
    animation-name: bounce;           /* which keyframes to use */
    animation-duration: 1s;            /* how long one cycle takes */
    animation-timing-function: ease;   /* acceleration curve */
    animation-delay: 0.5s;             /* wait before starting */
    animation-iteration-count: 3;      /* play 3 times (or infinite) */
    animation-direction: alternate;    /* forward, reverse, alternate */
    animation-fill-mode: forwards;     /* retain end state after finishing */
    animation-play-state: paused;      /* running or paused */

    /* Shorthand: name duration timing delay count direction fill-mode */
    animation: bounce 1s ease 0s infinite alternate forwards;
}
```

**Why it exists:** Without these controls, animations can only play once, forward, from start. These properties let you loop, reverse, pause, and retain the end state → complex animation sequences.

**Where it's used:** Every `@keyframes` animation.

**What goes wrong without it:**
- `animation-fill-mode: forwards` → without it, the element returns to its original state after the animation ends. With `forwards`, it keeps the final keyframe state.
- `animation-direction: alternate` → plays forward then backward → great for ping-pong effects.
- `animation-play-state: paused` → pause animation on hover or scroll. Useful for performance (pause off-screen animations).

---

## Common Animation Patterns

**What:** Real-world animation patterns:

```css
/* 1. Fade in */
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

/* 2. Slide in from left */
@keyframes slideInLeft { from { transform: translateX(-100px); opacity: 0; } to { transform: translateX(0); opacity: 1; } }

/* 3. Bounce */
@keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-30px); } }

/* 4. Pulse */
@keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }

/* 5. Spin (loader) */
@keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

/* 6. Shake (error) */
@keyframes shake { 0%, 100% { transform: translateX(0); } 25% { transform: translateX(-10px); } 75% { transform: translateX(10px); } }
```

**Why it exists:** These patterns cover 90% of UI animation needs. Memorizing them saves time and ensures consistency.

**Where it's used:** Everywhere — loaders, hover effects, entrance animations, error feedback, attention-grabbing pulses.

**What goes wrong without it:**
- Over-animating → every element bounces and pulses → distracting, unprofessional. Animate purposefully.
- Animating on page load → too many elements animate at once → chaotic. Stagger them with `animation-delay`.

---

## transform-origin

**What:** Sets the point around which transforms happen.

```css
.element {
    transform-origin: center;        /* default */
    transform-origin: top left;      /* rotate from top-left corner */
    transform-origin: 50% 100%;      /* bottom center */
    transform-origin: 20px 30px;     /* specific point */
}
```

**Why it exists:** Without `transform-origin`, all transforms happen from the center. `transform: rotate(45deg)` rotates from center → element stays in place. With `transform-origin: top left`, it rotates from the corner → element swings.

**Where it's used:** Card flips (origin at left for page-turn effect), door opening (origin at left edge), pendulum (origin at top).

**What goes wrong without it:**
- Default is center → if you need a different pivot point, the animation looks wrong. Set `transform-origin`.
- `transform-origin: 0 0` → top-left corner. `50% 50%` → center. `100% 100%` → bottom-right.
- For 3D transforms, add a Z value: `transform-origin: 50% 50% 0`.

---

## Performance: will-change

**What:** `will-change` hints to the browser that an element will animate, allowing it to optimize.

```css
.animated-element {
    will-change: transform, opacity;
}
```

**Why it exists:** Without `will-change`, the browser doesn't know which elements will animate → it can't pre-optimize → first animation frame may be janky. `will-change` lets the browser prepare → smoother first animation.

**Where it's used:** Elements that animate on scroll, hover, or interaction. Don't overuse — it consumes memory.

**What goes wrong without it:**
- `will-change: all` → invalid. Must specify properties: `will-change: transform, opacity`.
- Overusing `will-change` → browser allocates GPU layers for every element → memory bloat → worse performance.
- Best practice: add `will-change` just before animation, remove after. Or use it sparingly on elements that animate frequently.

---

## prefers-reduced-motion

**What:** Respect the user's OS setting for reduced motion.

```css
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}
```

**Why it exists:** Some users have vestibular disorders → animations cause nausea, dizziness. `prefers-reduced-motion` is an accessibility feature that lets users disable animations system-wide. Your CSS should respect it.

**Where it's used:** Every site with animations. It's an accessibility requirement (WCAG 2.1).

**What goes wrong without it:**
- Ignoring `prefers-reduced-motion` → users who disabled animations still see them → accessibility violation, physical discomfort.
- Disabling ALL motion → some transitions are essential (like indicating state change). Use `reduce`, not `none` — keep essential transitions, remove decorative ones.
