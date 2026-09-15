# Lesson 16 — Common Mistakes

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
