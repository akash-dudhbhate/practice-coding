# Lesson 13 — Quasar Animations & Transitions

## What you'll learn
- CSS transitions in Quasar (built-in)
- Quasar animation classes (animated bounce, fadeIn)
- Vue Transition and TransitionGroup components
- QSlideTransition (expand/collapse)
- Scroll animations (v-intersection)
- Loading and skeleton animations
- Animation performance (GPU-accelerated)

## Lesson

### Vue Transition
```vue
<Transition name="fade">
    <div v-if="show">Content</div>
</Transition>
```

### QSlideTransition
```vue
<q-slide-transition>
    <div v-show="expanded">Content</div>
</q-slide-transition>
```

### Skeleton
```vue
<q-skeleton type="rect" height="200px" />
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.vue` — Create a toggle button that shows/hides a div with a fade transition. Use Vue's `<Transition>` component. Define the CSS classes (fade-enter-active, fade-leave-active).

   WHAT IT SHOULD LOOK LIKE:
   ```
   [ Toggle ]
   +------------------+
   |  box fades in /  |   <- <Transition name="fade">,
   |  out over ~0.4s  |       opacity animates smoothly
   +------------------+
   ```
2. `easy/p02-solve.vue` — Create an expandable section using `q-slide-transition`. Button toggles between "Expand" and "Collapse". Content slides in/out smoothly. Use `v-show` (not `v-if`).

   WHAT IT SHOULD LOOK LIKE:
   ```
   COLLAPSED:              EXPANDED:
   +------------------+    +------------------+
   | [ Expand ]       |    | [ Collapse ]     |
   +------------------+    |  content slides  |
                           |  open smoothly   |
                           +------------------+
   ```
3. `easy/p03-solve.vue` — Create a card with skeleton loading. Show skeletons for 2 seconds (setTimeout), then show the actual content (image, title, text). Match skeleton sizes to content sizes.

   WHAT IT SHOULD LOOK LIKE:
   ```
   FIRST 2s:               THEN:
   +------------------+    +------------------+
   |~~~~~~~~~~~~~~~~~~|    |## real image ####|
   |~~~~ waving ~~~~~~|    | Card Title       |
   |~~~~ skeleton ~~~~|    | Body text here.. |
   +------------------+    +------------------+
   ```

### Medium
4. `medium/p01-solve.vue` — Create a list with animated add/remove using `TransitionGroup`. Add button adds a random item. Remove button (per item) removes it. Items animate in (slide from left) and out (slide to right).

   WHAT IT SHOULD LOOK LIKE:
   ```
   [ Add item ]
   -> * New item slides in from LEFT
   * Item 1                [x]   <- [x] slides it out RIGHT,
   * Item 2                [x]       siblings glide into the gap
   ```
5. `medium/p02-solve.vue` — Create a scroll-animated section: 5 cards that fade in as the user scrolls to them. Use `v-intersection` directive. Each card animates only once (don't re-animate on scroll up).

   WHAT IT SHOULD LOOK LIKE:
   ```
   |  viewport  |
   +------------+
   | Card 1     |   <- already faded in
   | Card 2     |   <- fading/sliding up now
   +- - - - - - +
     Card 3-5 invisible below the fold
     (each animates once on first scroll into view)
   ```
6. `medium/p03-solve.vue` — Create a page with route transition. Use `<Transition>` with `mode="out-in"` around `<router-view>`. Define a slide-fade transition. Navigate between 3 pages and verify smooth transitions.

   WHAT IT SHOULD LOOK LIKE:
   ```
   [Home] [About] [Contact]
   click About:
   |<- Home slides out left .. About fades in from right ->|
   +--------------------------------+
   |            About               |
   +--------------------------------+
   ```

### Hard
7. `hard/p01-solve.vue` — Build an animated accordion FAQ: 5 questions, click to expand/collapse answers. Use `q-slide-transition`. Only one open at a time (closing others when a new one opens). Smooth rotation on the expand/collapse icon.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +--------------------------------------+
   | v Q1 (highlighted)                   |  <- open, answer slides
   |   Answer text slides open...         |
   |--------------------------------------|
   | > Q2                                 |  <- collapsed; chevron
   |--------------------------------------|     rotates on toggle
   | > Q3                                 |
   +--------------------------------------+
   ```
8. `hard/p02-solve.vue` — Build a card grid with staggered entrance animation: 6 cards that fade in one by one (100ms delay between each). Use CSS animation with `animation-delay`. Cards animate on page load. Include hover effect (scale up).

   WHAT IT SHOULD LOOK LIKE:
   ```
   +---+  +---+  +---+
   | 1 |  | 2 |  | 3 |   <- cascade in left-to-right
   +---+  +---+  +---+      on page load (100ms apart)
   +---+  +---+  +---+
   | 4 |  | 5 |  | 6 |   <- hovering a card lifts/scales it
   +---+  +---+  +---+
   ```
9. `hard/p03-solve.vue` — Build a complete loading experience: skeleton loading (2s), then content fades in. Include a loading bar at the top (QAjaxBar or custom). Show a success notification after load. All animations are GPU-accelerated (transform/opacity only).

   WHAT IT SHOULD LOOK LIKE:
   ```
   =================> <- loading bar across the top
   +~~~~~+ +~~~~~+ +~~~~~+
   |skel | |skel | |skel |   <- 2s of waving skeletons
   +~~~~~+ +~~~~~+ +~~~~~+
        -> cards fade in -> "Content loaded" toast
   [ Reload ]  <- replays the whole sequence
   ```

### How to work
- Write your complete Vue/Quasar solution.
- Remove the TODO comment when done.
- Test by importing into a Quasar app.
