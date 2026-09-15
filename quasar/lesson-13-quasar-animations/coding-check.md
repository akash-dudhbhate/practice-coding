# Lesson 13 — Coding Check

## Easy

### p01-solve.vue — Fade transition
- [ ] Toggle button
- [ ] `<Transition name="fade">` used
- [ ] `v-if` on the content
- [ ] CSS classes defined (fade-enter-active, etc.)
- [ ] Fade in works
- [ ] Fade out works

### p02-solve.vue — Slide transition
- [ ] `q-slide-transition` used
- [ ] Button toggles expand/collapse
- [ ] `v-show` used (not v-if)
- [ ] Content slides smoothly
- [ ] Button label changes

### p03-solve.vue — Skeleton loading
- [ ] `q-skeleton` used for image area
- [ ] `q-skeleton` used for title
- [ ] `q-skeleton` used for text
- [ ] 2-second timer (setTimeout)
- [ ] Content appears after delay
- [ ] Skeleton sizes match content

## Medium

### p01-solve.vue — Animated list
- [ ] `TransitionGroup` used
- [ ] `tag="ul"` set
- [ ] `:key` on each item
- [ ] Add button works
- [ ] Remove button per item
- [ ] Enter animation (slide from left)
- [ ] Leave animation (slide to right)

### p02-solve.vue — Scroll animation
- [ ] `v-intersection` directive used
- [ ] 5 cards in a vertical list
- [ ] Cards fade in on scroll
- [ ] Each card animates only once
- [ ] `min-height` for scroll space
- [ ] Works on scroll down

### p03-solve.vue — Route transition
- [ ] `<Transition>` around `<router-view>`
- [ ] `mode="out-in"` set
- [ ] Slide-fade CSS defined
- [ ] 3 routes defined
- [ ] Navigation works
- [ ] Smooth transition between pages

## Hard

### p01-solve.vue — Animated accordion
- [ ] 5 FAQ questions
- [ ] `q-slide-transition` for answers
- [ ] Click to expand/collapse
- [ ] Only one open at a time
- [ ] Others close when new opens
- [ ] Icon rotates on expand
- [ ] Smooth rotation transition

### p02-solve.vue — Staggered card grid
- [ ] 6 cards in a grid
- [ ] Fade in animation
- [ ] Staggered delay (100ms between each)
- [ ] `animation-delay` used
- [ ] Animation on page load
- [ ] Hover effect (scale up)
- [ ] GPU-accelerated (transform/opacity)

### p03-solve.vue — Complete loading experience
- [ ] Skeleton loading (2s)
- [ ] Content fades in after load
- [ ] Loading bar at top
- [ ] Success notification after load
- [ ] All animations use transform/opacity
- [ ] No janky animations
- [ ] Smooth experience
