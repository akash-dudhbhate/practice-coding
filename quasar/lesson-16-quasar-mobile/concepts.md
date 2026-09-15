# Lesson 16 — Concepts Explained (Quasar Mobile - Capacitor/Cordova)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Quasar Mobile Overview

**What:** Quasar can build native mobile apps (iOS/Android) from the same codebase using Capacitor or Cordova.

```bash
# Add mobile mode
quasar mode add capacitor   # recommended (modern)
# or
quasar mode add cordova     # legacy

# Add platforms
cd src-capacitor
npx cap add android
npx cap add ios

# Build for mobile
quasar build -m capacitor -T android
quasar build -m capacitor -T ios
```

**Why it exists:** Building separate iOS (Swift) and Android (Kotlin) apps → 2 codebases, 2 teams. Quasar → one Vue codebase → deploys to web, iOS, and Android → 3x productivity.

**Where it's used:** Any web app that also needs to be in the App Store / Play Store.

**What goes wrong without it:**
- Not having Xcode (iOS) or Android Studio → can't build/test native. Install the IDE first.
- iOS builds require a Mac → can't build iOS on Linux/Windows. Use a Mac or CI.
- Capacitor vs Cordova → Capacitor is modern (maintained, better plugins). Cordova is legacy. Use Capacitor.

---

## Capacitor Integration

**What:** Capacitor wraps the web app in a native WebView → accesses native APIs.

```js
// Install Capacitor plugins
npm install @capacitor/camera @capacitor/geolocation @capacitor/storage

// Use in Vue component
import { Camera, CameraResultType } from '@capacitor/camera'

async function takePhoto() {
    const photo = await Camera.getPhoto({
        resultType: CameraResultType.Uri,
        quality: 80,
    })
    imageSrc.value = photo.webPath
}

import { Geolocation } from '@capacitor/geolocation'

async function getLocation() {
    const pos = await Geolocation.getCurrentPosition()
    console.log(pos.coords.latitude, pos.coords.longitude)
}
```

**Why it exists:** Web apps can't access the camera, GPS, contacts, etc. Capacitor provides a bridge → web code calls native APIs → full native capabilities.

**Where it's used:** Any mobile app that needs native features (camera, GPS, push, storage).

**What goes wrong without it:**
- Not requesting permissions → camera/GPS fails silently. Request permissions first.
- Testing in browser only → Capacitor plugins don't work in browser. Test on a device/emulator.
- Plugin not installed → import fails → error. Install before importing.

---

## Mobile-Specific Layouts

**What:** Adapt the layout for mobile (bottom tabs, no drawers, touch-friendly).

```vue
<q-layout>
    <!-- Desktop: left drawer -->
    <q-drawer v-if="$q.platform.is.desktop" side="left" v-model="drawer">
        <q-list>...</q-list>
    </q-drawer>

    <!-- Mobile: bottom tabs -->
    <q-tab-panels v-if="$q.platform.is.mobile">
        <!-- content -->
    </q-tab-panels>

    <!-- Mobile: bottom navigation -->
    <q-tabs v-if="$q.platform.is.mobile" class="absolute-bottom">
        <q-tab icon="home" label="Home" />
        <q-tab icon="search" label="Search" />
        <q-tab icon="person" label="Profile" />
    </q-tabs>
</q-layout>
```

**Why it exists:** Desktop layouts (left drawer, small buttons) don't work on mobile (thumb reach, small screen). Mobile layouts (bottom tabs, large buttons) → ergonomic → better UX.

**Where it's used:** Every app that runs on both mobile and desktop.

**What goes wrong without it:**
- Desktop drawer on mobile → hard to reach (top-left) → bad UX. Use bottom tabs on mobile.
- Small buttons on mobile → hard to tap → fat-finger errors. Use 44px minimum touch targets.
- Not testing on a real phone → layout looks fine on desktop but broken on mobile.

---

## Touch Events and Gestures

**What:** Handle touch-specific interactions (swipe, long-press, pinch).

```vue
<!-- Touch directives -->
<div
    v-touch:swipe.left="onSwipeLeft"
    v-touch:swipe.right="onSwipeRight"
    v-touch:hold="onLongPress"
>
    Swipe me
</div>

<!-- Pan gesture -->
<div v-touch-pan.horizontal="onPan">
    Drag horizontally
</div>

<script setup>
function onSwipeLeft() { console.log('Swiped left') }
function onSwipeRight() { console.log('Swiped right') }
function onLongPress() { console.log('Long pressed') }
function onPan({ offset }) { console.log('Pan offset:', offset) }
</script>
```

**Why it exists:** Mobile users use gestures (swipe, long-press) not just clicks. Quasar's touch directives → handle gestures declaratively → native-like feel.

**Where it's used:** Swipe to delete, swipe between tabs, long-press for context menu, drag to reorder.

**What goes wrong without it:**
- Swipe on desktop → no touch → doesn't trigger. Provide mouse alternatives.
- `v-touch:hold` → fires after a delay → might conflict with click. Use one or the other.
- Pan gesture on scrollable content → conflicts with scroll. Use `v-touch-pan.prevent` carefully.

---

## Native Device Features

**What:** Access device hardware via Capacitor plugins.

```js
// Camera
import { Camera } from '@capacitor/camera'

// Geolocation
import { Geolocation } from '@capacitor/geolocation'

// Device info
import { Device } from '@capacitor/device'
const info = await Device.getInfo()
console.log(info.platform)  // 'ios', 'android', 'web'
console.log(info.model)     // device model

// Haptics (vibration)
import { Haptics, ImpactStyle } from '@capacitor/haptics'
Haptics.impact({ style: ImpactStyle.Medium })

// Share
import { Share } from '@capacitor/share'
await Share.share({
    title: 'Check this out',
    text: 'Amazing app!',
    url: 'https://example.com',
})

// Clipboard
import { Clipboard } from '@capacitor/clipboard'
await Clipboard.write({ string: 'Copied text' })
```

**Why it exists:** Web apps are sandboxed → can't access hardware. Capacitor plugins bridge this → camera, GPS, vibration, sharing → native capabilities from web code.

**Where it's used:** Photo apps, location-based apps, sharing features, any app using device hardware.

**What goes wrong without it:**
- Not requesting permissions → `Camera.getPhoto()` fails → no error message. Request and handle denial.
- Web fallback → some plugins work in browser (geolocation, clipboard), others don't (haptics). Check.
- Plugin version mismatch → Capacitor 4 plugin with Capacitor 5 → might break. Match versions.

---

## Mobile App Configuration

**What:** Configure app metadata, permissions, and build settings.

```json
// src-capacitor/capacitor.config.json
{
    "appId": "com.example.myapp",
    "appName": "My App",
    "webDir": "dist",
    "server": {
        "androidScheme": "https"
    },
    "plugins": {
        "Camera": {
            "permissions": ["camera"]
        },
        "Geolocation": {
            "permissions": ["location"]
        }
    }
}
```

```xml
<!-- Android: src-android/app/src/main/AndroidManifest.xml -->
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />

<!-- iOS: src-ios/App/App/Info.plist -->
<key>NSCameraUsageDescription</key>
<string>We need camera access to take photos</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>We need location for maps</string>
```

**Why it exists:** Without proper configuration, the app can't access native features → camera/GPS fail. Permissions and descriptions → App Store / Play Store requirements → must be declared.

**Where it's used:** Every mobile app — configured once per platform.

**What goes wrong without it:**
- Missing permission in manifest → feature fails silently. Add all needed permissions.
- Missing usage description (iOS) → App Store rejects the app. Add `NS*UsageDescription` for every permission.
- Wrong `appId` → can't publish (must match App Store / Play Store). Set it correctly from the start.

---

## Testing on Devices

**What:** Test the app on real devices or emulators.

```bash
# Android
quasar build -m capacitor -T android
# Open in Android Studio
npx cap open android
# Run on emulator or device from Android Studio

# iOS
quasar build -m capacitor -T ios
# Open in Xcode
npx cap open ios
# Run on simulator or device from Xcode
```

**Why it exists:** Browser testing → can't test native features (camera, GPS, push). Device testing → real environment → catches issues that only appear on actual hardware.

**Where it's used:** Every mobile app — test on device before publishing.

**What goes wrong without it:**
- Only testing on emulator → some issues only appear on real devices (performance, network). Test on both.
- Not testing different screen sizes → layout breaks on small/large phones. Test multiple devices.
- iOS simulator → doesn't have all hardware (no camera on Mac simulator). Test on real iPhone for camera.
