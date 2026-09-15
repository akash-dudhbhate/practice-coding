# Lesson 16 — Intuition Checks

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
