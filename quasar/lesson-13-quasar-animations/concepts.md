# Lesson 13 — Concepts Explained (Quasar Animations & Transitions)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## CSS Transitions in Quasar

**What:** Quasar provides built-in CSS animations and transition components.

```vue
<!-- Built-in transition component -->
<q-transition name="fade">
    <div v-if="show">Content appears with fade</div>
</q-transition>

<!-- Common transitions -->
<q-transition name="slide-fade">...</q-transition>
<q-transition name="scale">...</q-transition>
<q-transition name="flip">...</q-transition>

<!-- Page transitions (in router) -->
<q-transition name="slide-fade" mode="out-in">
    <router-view />
</q-transition>
```

**Why it exists:** Without transitions, content appears/disappears instantly → jarring. Transitions smooth the change → polished, professional feel.

**Where it's used:** Show/hide content, route changes, modal open/close, list item add/remove.

**What goes wrong without it:**
- `mode="out-in"` missing on route transitions → old and new pages both visible briefly → flicker.
- Transition on `v-if` but not `v-show` → `v-if` adds/removes from DOM (transition works). `v-show` just hides (transition may not work the same).
- Not importing the animation CSS → transition name doesn't match any CSS → no animation.

---

## Quasar Animation Classes

**What:** Quasar includes pre-built CSS animations.

```vue
<!-- Apply animation class -->
<div class="animated bounce">Bounces</div>
<div class="animated fadeIn">Fades in</div>
<div class="animated slideInUp">Slides up</div>

<!-- With delay -->
<div class="animated fadeIn delay-1s">Delayed fade</div>

<!-- With duration -->
<div class="animated fadeIn slow">Slow fade</div>
<div class="animated fadeIn fast">Fast fade</div>
```

**Why it exists:** Writing CSS animations from scratch → time-consuming. Quasar bundles common animations → add a class → done.

**Where it's used:** Page load animations, notification appearances, card entrances, attention-grabbing effects.

**What goes wrong without it:**
- Animation loops infinitely → use `animated bounce` once, not `animated bounce infinite` unless intended.
- Animation on every render → distracting. Use for entrance only (on mount).
- Not testing performance → many animated elements → janky. Limit concurrent animations.

---

## Vue Transition Components

**What:** Vue's `<Transition>` and `<TransitionGroup>` for enter/leave animations.

```vue
<!-- Single element transition -->
<Transition name="fade">
    <div v-if="show" key="content">Content</div>
</Transition>

<!-- List transition -->
<TransitionGroup name="list" tag="ul">
    <li v-for="item in items" :key="item.id">{{ item.name }}</li>
</TransitionGroup>

<style>
.fade-enter-active, .fade-leave-active {
    transition: opacity 0.3s;
}
.fade-enter-from, .fade-leave-to {
    opacity: 0;
}

.list-enter-active, .list-leave-active {
    transition: all 0.5s;
}
.list-enter-from { opacity: 0; transform: translateX(-30px); }
.list-leave-to { opacity: 0; transform: translateX(30px); }
</style>
```

**Why it exists:** Vue's transition system hooks into `v-if`/`v-show` and `v-for` → automatic enter/leave animations → smooth list additions/removals.

**Where it's used:** Lists with add/remove, toggling content, route transitions.

**What goes wrong without it:**
- `key` missing on transitioned elements → Vue can't track them → animation doesn't work. Always use `:key`.
- `TransitionGroup` needs `tag` → the wrapper element type. Without it → renders a span (default).
- CSS class names must match: `name="fade"` → `.fade-enter-active`, `.fade-leave-active`, etc.

---

## QSlideTransition

**What:** Quasar component for expand/collapse animations.

```vue
<template>
    <div>
        <q-btn @click="show = !show" :label="show ? 'Collapse' : 'Expand'" />
        <q-slide-transition>
            <div v-show="show">
                <p>Hidden content that slides in and out</p>
                <p>Smooth height animation</p>
            </div>
        </q-slide-transition>
    </div>
</template>

<script setup>
import { ref } from 'vue'
const show = ref(false)
</script>
```

**Why it exists:** Animating height from 0 to auto is tricky in CSS (auto isn't animatable). QSlideTransition handles it → smooth expand/collapse → accordion, FAQ, details sections.

**Where it's used:** Accordions, FAQs, expandable cards, "show more" sections.

**What goes wrong without it:**
- Using `v-if` instead of `v-show` → element is removed from DOM → no transition. Use `v-show`.
- Content with dynamic height → QSlideTransition recalculates → should work, but test.
- Nested QSlideTransition → can cause height calculation issues. Avoid deep nesting.

---

## Scroll Animations

**What:** Animate elements when they come into view (on scroll).

```vue
<template>
    <div v-intersection="onIntersection" class="scroll-item">
        <p :class="{ 'animated fadeIn': isVisible }">Appears on scroll</p>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const isVisible = ref(false)

function onIntersection(entry) {
    isVisible.value = entry.isIntersecting
}
</script>

<style scoped>
.scroll-item {
    min-height: 200px;
    margin: 50px 0;
}
</style>
```

**Why it exists:** Animating everything on page load → overwhelming. Scroll animations reveal content as the user scrolls → engaging, paced experience.

**Where it's used:** Landing pages, portfolios, long content pages, storytelling.

**What goes wrong without it:**
- `v-intersection` directive → Quasar's IntersectionObserver wrapper. Must configure threshold.
- Animation only once → use a flag to prevent re-animating: `if (entry.isIntersecting && !animated.value)`.
- Content hidden before animation → if CSS hides it and animation doesn't fire (JS disabled) → invisible. Use progressive enhancement.

---

## Loading and Skeleton Animations

**What:** Show skeleton placeholders while data loads.

```vue
<template>
    <div v-if="loading">
        <q-skeleton type="rect" height="200px" />
        <q-skeleton type="text" width="50%" />
        <q-skeleton type="text" width="80%" />
    </div>
    <div v-else>
        <img :src="image" style="height: 200px" />
        <h3>{{ title }}</h3>
        <p>{{ description }}</p>
    </div>
</template>
```

**Why it exists:** Without skeletons, loading shows nothing or a spinner → user doesn't know what's coming. Skeletons show the layout → user expects content → less perceived wait time.

**Where it's used:** Card loading, list loading, image loading, any async content.

**What goes wrong without it:**
- Skeleton size doesn't match content → layout shifts when content loads → jarring. Match sizes.
- Too many skeletons → page looks broken. Use for above-the-fold content only.
- No animation on skeleton → looks static. Quasar skeletons have a shimmer animation by default.

---

## Animation Performance

**What:** Keep animations smooth (60fps) by following best practices.

```css
/* GOOD: animate transform and opacity (GPU-accelerated) */
.smooth {
    transition: transform 0.3s, opacity 0.3s;
}
.smooth:hover {
    transform: scale(1.05);
    opacity: 0.9;
}

/* BAD: animate width, height, margin (causes reflow) */
.janky {
    transition: width 0.3s, height 0.3s;
}
.janky:hover {
    width: 200px;  /* triggers reflow → janky */
}
```

**Why it exists:** Animating the wrong properties → browser recalculates layout → janky (stuttering). Transform and opacity are GPU-accelerated → smooth → 60fps.

**Where it's used:** Every animation — always use transform/opacity.

**What goes wrong without it:**
- Animating `width`/`height`/`margin` → reflow → janky on mobile → bad UX.
- Too many concurrent animations → GPU overload → janky. Limit to 3-5 at a time.
- Not using `will-change` for known animated elements → browser doesn't optimize. Add `will-change: transform` (sparingly).
