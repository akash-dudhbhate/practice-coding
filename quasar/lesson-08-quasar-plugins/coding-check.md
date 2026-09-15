# Lesson 08 — Coding Check

## Easy

### p01-solve.vue — Notification types
- [ ] `useQuasar` imported
- [ ] 4 buttons for 4 notification types
- [ ] positive (green) notification
- [ ] negative (red) notification
- [ ] warning (orange) notification
- [ ] info (blue) notification

### p02-solve.vue — Dark mode toggle
- [ ] `useQuasar` imported
- [ ] Toggle button
- [ ] `$q.dark.toggle()` called
- [ ] Current state displayed (`$q.dark.isActive`)
- [ ] UI updates on toggle

### p03-solve.vue — Platform detection
- [ ] `$q.platform.is.mobile` displayed
- [ ] `$q.platform.is.desktop` displayed
- [ ] `$q.platform.is.ios` displayed
- [ ] `$q.platform.is.android` displayed
- [ ] Browser name displayed

## Medium

### p01-solve.vue — Delete confirmation
- [ ] Delete button triggers `$q.dialog`
- [ ] Dialog has title and message
- [ ] `cancel: true` set
- [ ] `onOk` shows "deleted" notification
- [ ] `onCancel` shows "cancelled" notification
- [ ] Flow is clear and user-friendly

### p02-solve.vue — Responsive grid
- [ ] `$q.screen` used for breakpoints
- [ ] 1 column on xs
- [ ] 2 columns on sm
- [ ] 3 columns on md+
- [ ] Current breakpoint displayed
- [ ] `q-card` used for items
- [ ] Grid adapts on resize

### p03-solve.vue — Form submission flow
- [ ] Submit button
- [ ] `$q.loading.show()` on submit
- [ ] 2-second async operation simulated
- [ ] Success notification on success
- [ ] Error notification on failure
- [ ] `$q.loading.hide()` in finally block
- [ ] Loading always hidden

## Hard

### p01-solve.vue — Notification system
- [ ] `useNotifications` composable created
- [ ] success preset (positive, check icon)
- [ ] error preset (negative, error icon)
- [ ] warning preset (warning, warning icon)
- [ ] info preset (info, info icon)
- [ ] Default timeout set
- [ ] Undo action for delete notifications
- [ ] Presets are reusable

### p02-solve.vue — Platform-aware component
- [ ] `$q.platform` used
- [ ] `$q.screen` used
- [ ] Mobile: bottom sheet menu
- [ ] Desktop: dropdown menu
- [ ] At least 4 menu items
- [ ] Correct menu shows on each platform
- [ ] Menu items work on both platforms

### p03-solve.vue — Settings panel
- [ ] Dark mode toggle (persisted)
- [ ] Notification position selector
- [ ] Loading spinner color picker
- [ ] All settings persisted to localStorage
- [ ] Settings loaded on app init
- [ ] Settings applied immediately
- [ ] Settings panel UI is clean
