# lesson-16-quasar-mobile — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Capacitor vs Cordova
<details><summary>Answer</summary>
Capacitor — modern, Ionic team, better plugin ecosystem, native project control. Cordova — older, legacy. Quasar supports both. Prefer Capacitor.
</details>

## Check 02: Platform detection
```javascript
$q.platform.is.mobile  // boolean
$q.platform.is.ios
$q.platform.is.android
$q.platform.is.desktop
```
<details><summary>Answer</summary>
Detect platform at runtime. Show/hide features based on platform. Different UI for mobile vs desktop.
</details>

## Check 03: Build commands
```bash
quasar build -m capacitor -T android
quasar build -m capacitor -T ios
```
<details><summary>Answer</summary>
Builds for specific platform. Requires Android Studio / Xcode. Outputs native project for deployment.
</details>

## Check 04: Native plugins
```javascript
import { Camera } from "@capacitor/camera";
const photo = await Camera.getPhoto();
```
<details><summary>Answer</summary>
Access native features: camera, geolocation, push notifications, haptics. Install Capacitor plugins, use in Vue components.
</details>

## Check 05: Responsive design
<details><summary>Answer</summary>
Use Quasar's responsive classes: `q-pa-md`, `q-gutter-sm`. Breakpoints: xs, sm, md, lg, xl. `$q.screen` for programmatic access.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01: Missing Capacitor
```bash
quasar build -m capacitor
# Error: capacitor not installed
```
<details><summary>Answer</summary>
**Bug:** Capacitor not installed.
**Fix:** `npm i @capacitor/core @capacitor/cli` and `quasar mode add capacitor`.
</details>

## Debug 02: No Platform Check
```javascript
if (showDesktop) { /* desktop only */ }
// runs on mobile too
```
<details><summary>Answer</summary>
**Bug:** No platform check — desktop code runs on mobile.
**Fix:** `if ($q.platform.is.mobile) { /* mobile only */ }`.
</details>

## Debug 03: Touch Targets Too Small
```css
.btn { padding: 4px; } /* too small for touch */
```
<details><summary>Answer</summary>
**Bug:** Touch target too small — hard to tap on mobile.
**Fix:** Minimum 44x44px touch targets. Use Quasar components (sized appropriately).
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Not installing Capacitor
```bash
npm i @capacitor/core @capacitor/cli
quasar mode add capacitor
```

## Mistake 02: No platform checks
```javascript
// Check platform before platform-specific code
if ($q.platform.is.mobile) { /* mobile */ }
```

## Mistake 03: Small touch targets
```css
/* Minimum 44x44px for touch */
/* Use Quasar components — already sized */
```

## Mistake 04: Not testing on device
```bash
# Test on real device, not just browser
# Emulators are better than nothing
```

## Mistake 05: Ignoring safe areas
```css
/* Use safe-area-inset for notches */
padding-top: env(safe-area-inset-top);
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): No Platform Check
### Before
```javascript
if (showDesktop) { /* runs on mobile too */ }
```
### After
```javascript
if ($q.platform.is.mobile) { /* mobile only */ }
```

## Refactor 02 (Medium): Small Touch Targets
### Before
```css
.btn { padding: 4px; }
```
### After
```vue
<q-btn padding="md" />
```

## Refactor 03 (Hard: Responsive Web for Native Features
### Before
```bash
quasar build -m spa
```
### After
```bash
quasar build -m capacitor -T android
```

---

## Approach Comparison — different ways to solve it

## Problem: Mobile App

### Approach 1: Responsive web
```bash
quasar build -m spa
```
**Cons:** No native features, no app store.

### Approach 2: Capacitor
```bash
quasar build -m capacitor -T android
```

**Winner:** Approach 2 for native features/app store. Approach 1 for web-only.

---

## Problem: Platform-Specific UI

### Approach 1: CSS media queries
```css
@media (max-width: 600px) { ... }
```

### Approach 2: $q.platform
```javascript
:class="{ 'mobile-layout': $q.platform.is.mobile }"
```

**Winner:** Use both. CSS for styling, $q for logic.
