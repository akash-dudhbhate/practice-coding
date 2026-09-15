# Lesson 08 — Concepts Explained (Quasar Plugins)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What are Quasar Plugins?

**What:** Quasar plugins are built-in utilities accessed via `$q` — available globally in components.

```js
// In any component:
export default {
    mounted() {
        this.$q.notify('Hello!')  // notification plugin
    }
}

// In <script setup>:
import { useQuasar } from 'quasar'
const $q = useQuasar()
$q.notify('Hello!')
```

**Why it exists:** Common features (notifications, dialogs, dark mode, platform detection) are needed in every app. Quasar bundles them as plugins → consistent API → no need for external libraries.

**Where it's used:** Every Quasar app — notifications, dialogs, dark mode, screen size, platform info.

**What goes wrong without it:**
- Forgetting to register a plugin in `quasar.config.js` → `$q.notify` is undefined → error.
- Using `this.$q` in `<script setup>` → `this` is undefined. Use `useQuasar()`.
- Not importing the plugin in `quasar.config.js` → plugin not available → silent failure.

---

## Notify Plugin (Notifications)

**What:** Display toast notifications to the user.

```js
// Basic notification
this.$q.notify('Item saved!')

// With options
this.$q.notify({
    message: 'Profile updated',
    type: 'positive',        // 'positive', 'negative', 'warning', 'info'
    position: 'top',         // 'top', 'bottom', 'top-right', etc.
    timeout: 3000,           // ms (0 = persistent)
    actions: [
        { label: 'Undo', color: 'white', handler: () => this.undo() }
    ]
})

// In <script setup>:
import { useQuasar } from 'quasar'
const $q = useQuasar()
$q.notify({ message: 'Done!', type: 'positive' })
```

**Why it exists:** User feedback is essential — "saved", "error", "deleted". Without notifications, users don't know if their action worked → bad UX. Notify provides a consistent, non-intrusive way to give feedback.

**Where it's used:** After CRUD operations, form submissions, errors, confirmations.

**What goes wrong without it:**
- `timeout: 0` without a dismiss button → notification stays forever → user can't dismiss.
- Too many notifications → spam → user ignores them. Batch or use a single summary.
- Not using `type` → all notifications look the same → user can't distinguish success from error.

---

## Dialog Plugin

**What:** Display modal dialogs for confirmations and prompts.

```js
// Confirmation dialog
this.$q.dialog({
    title: 'Confirm',
    message: 'Delete this item?',
    cancel: true,
    persistent: true,
}).onOk(() => {
    this.deleteItem()
}).onCancel(() => {
    console.log('Cancelled')
})

// Prompt dialog
this.$q.dialog({
    title: 'Enter name',
    message: 'What is your name?',
    prompt: {
        model: '',
        type: 'text',
    },
    cancel: true,
}).onOk(name => {
    console.log('Name:', name)
})
```

**Why it exists:** Destructive actions (delete, reset) need confirmation → prevents accidents. Prompts collect quick input without a full form. Dialog plugin provides these without custom components.

**Where it's used:** Delete confirmations, prompts, alerts, custom dialogs.

**What goes wrong without it:**
- `persistent: true` → can't close by clicking outside or pressing Escape → user is forced to choose.
- Not handling `onCancel` → user cancels but code assumes they confirmed → bug.
- Dialog inside dialog → can be confusing. Avoid nesting.

---

## Dark Mode Plugin

**What:** Toggle between light and dark themes.

```js
// Toggle dark mode
this.$q.dark.toggle()

// Set explicitly
this.$q.dark.set(true)   // dark
this.$q.dark.set(false)  // light

// Check current state
console.log(this.$q.dark.isActive)  // true/false

// With Pinia:
import { useQuasar } from 'quasar'
const $q = useQuasar()
const toggleDark = () => $q.dark.toggle()
```

**Why it exists:** Dark mode is a common user preference. Quasar handles all the CSS automatically → components, colors, and layouts adapt → no manual styling needed.

**Where it's used:** Settings page, theme toggle button, respecting system preference.

**What goes wrong without it:**
- Not persisting dark mode → resets on refresh. Save to localStorage and restore on init.
- Setting dark mode before app is ready → might not apply. Use `$q.dark.set()` in `mounted()` or later.
- Custom components not using Quasar CSS variables → don't adapt to dark mode. Use `var(--q-color)` or Quasar classes.

---

## Platform Plugin

**What:** Detect the user's platform (OS, browser, mobile/desktop).

```js
// Platform info
console.log(this.$q.platform.is.desktop)  // true on desktop
console.log(this.$q.platform.is.mobile)   // true on mobile
console.log(this.$q.platform.is.ios)      // true on iOS
console.log(this.$q.platform.is.android)  // true on Android
console.log(this.$q.platform.is.safari)   // true on Safari

// Conditional rendering
<template>
    <div v-if="$q.platform.is.mobile">
        Mobile-specific content
    </div>
    <div v-else>
        Desktop content
    </div>
</template>
```

**Why it exists:** Different platforms need different UI — mobile needs bigger buttons, desktop can show more content. Platform detection lets you adapt → better UX on each device.

**Where it's used:** Responsive layouts, platform-specific features, conditional rendering.

**What goes wrong without it:**
- Using platform detection for responsive design → use CSS breakpoints instead (more reliable, handles window resize).
- `$q.platform.is.mobile` → detects by user agent → tablets might report as desktop. Test on real devices.
- Assuming platform never changes → user can resize desktop window to mobile width → use `screen` plugin for responsive behavior.

---

## Screen Plugin

**What:** Responsive breakpoints and screen size info.

```js
// Screen sizes
console.log(this.$q.screen.width)    // current width in px
console.log(this.$q.screen.height)   // current height

// Breakpoints (boolean)
console.log(this.$q.screen.xs)   // < 600px
console.log(this.$q.screen.sm)   // 600-1024px
console.log(this.$q.screen.md)   // 1024-1440px
console.log(this.$q.screen.lg)   // 1440-1920px
console.log(this.$q.screen.xl)   // > 1920px

// In template:
<q-grid :cols="$q.screen.xs ? 1 : $q.screen.sm ? 2 : 3">
```

**Why it exists:** CSS breakpoints handle most responsive design, but sometimes you need JS logic (different columns, different data per breakpoint). Screen plugin provides reactive breakpoint info → adapts on resize.

**Where it's used:** Grid layouts, conditional rendering, responsive component props.

**What goes wrong without it:**
- Using screen plugin for simple responsive design → CSS is more efficient. Use screen plugin only when JS logic is needed.
- Not handling all breakpoints → what happens at xl? What about xs? Cover all cases.
- Screen size changes → re-renders → can cause performance issues with heavy components. Debounce if needed.

---

## Loading Plugin

**What:** Show a loading spinner overlay.

```js
// Show loading
this.$q.loading.show({
    message: 'Saving data...',
    spinnerColor: 'primary',
})

// Hide loading
this.$q.loading.hide()

// With async operation:
this.$q.loading.show()
try {
    await this.saveData()
    this.$q.notify('Saved!')
} catch (error) {
    this.$q.notify({ type: 'negative', message: 'Error!' })
} finally {
    this.$q.loading.hide()
}
```

**Why it exists:** Async operations (API calls, file uploads) take time → user needs feedback. Loading overlay blocks interaction → prevents double-submits → shows progress.

**Where it's used:** Form submissions, data fetching, file uploads, any async operation.

**What goes wrong without it:**
- Forgetting to hide loading → spinner stays forever → user stuck. Always use `finally`.
- Multiple `loading.show()` calls → only one spinner shows, but you need multiple `hide()` calls. Use a counter or `loading.hide()` carefully.
- Loading on fast operations → flashes briefly → jarring. Only show for operations > 300ms.

---

## AppFullscreen Plugin

**What:** Toggle fullscreen mode.

```js
// Enter fullscreen
this.$q.fullscreen.request()

// Exit fullscreen
this.$q.fullscreen.exit()

// Toggle
this.$q.fullscreen.toggle()

// Check state
console.log(this.$q.fullscreen.isActive)
```

**Why it exists:** Video players, image viewers, and presentations benefit from fullscreen. Quasar handles the browser API differences → consistent behavior.

**Where it's used:** Media viewers, presentations, immersive experiences.

**What goes wrong without it:**
- Fullscreen requires user interaction → can't enter fullscreen automatically (browser security). Must be triggered by a click.
- Not handling fullscreen exit (Esc key) → UI doesn't update. Watch `$q.fullscreen.isActive`.
- iOS Safari → doesn't support fullscreen API. Detect and provide alternative.
