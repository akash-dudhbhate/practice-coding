# Lesson 14 — Coding Check

## Easy

### p01-solve.vue — Notification types
- [ ] 4 buttons for 4 types
- [ ] positive (green, check icon)
- [ ] negative (red, error icon)
- [ ] warning (orange, warning icon)
- [ ] info (blue, info icon)
- [ ] Custom messages
- [ ] Different positions

### p02-solve.vue — Delete with undo
- [ ] Delete button opens dialog
- [ ] Dialog has confirm and cancel
- [ ] Confirm → "deleted" notification with Undo
- [ ] Undo action (5s timeout)
- [ ] Cancel → "cancelled" notification

### p03-solve.vue — Prompt dialog
- [ ] Button opens prompt dialog
- [ ] Text input in dialog
- [ ] Validation (not empty)
- [ ] On OK → notification with entered text
- [ ] On cancel → no action or notification

## Medium

### p01-solve.vue — Loading flow
- [ ] Button starts persistent notification
- [ ] `timeout: 0` for loading
- [ ] 3-second simulated operation
- [ ] Dismiss function used
- [ ] Loading dismissed after operation
- [ ] Success notification shown
- [ ] Dismiss in finally or after

### p02-solve.vue — Bottom sheet
- [ ] `$q.bottomSheet` used
- [ ] 4 actions (Share, Copy, Edit, Delete)
- [ ] Icons for each action
- [ ] On select → notification with action name
- [ ] Delete action styled as negative
- [ ] Mobile-friendly

### p03-solve.vue — Custom dialog component
- [ ] Custom dialog component created
- [ ] Form with name and email
- [ ] `$q.dialog({ component: ... })` used
- [ ] `componentProps` passed
- [ ] On OK → emits form data
- [ ] Caller shows notification with data
- [ ] Cancel handled

## Hard

### p01-solve.vue — CRUD notification system
- [ ] `useCrudNotifications` composable
- [ ] create → success notification
- [ ] update → success notification
- [ ] delete → notification with undo
- [ ] error → negative notification
- [ ] loading state for each
- [ ] Consistent API
- [ ] Reusable across components

### p02-solve.vue — Multi-step dialog wizard
- [ ] Custom dialog component
- [ ] 3 steps: form, review, confirm
- [ ] Navigation between steps
- [ ] Validation per step
- [ ] Can't proceed if invalid
- [ ] On finish → emits collected data
- [ ] Cancel closes dialog
- [ ] Step indicator

### p03-solve.vue — Notification center
- [ ] Bell icon with badge count
- [ ] Click opens dropdown
- [ ] All notifications listed
- [ ] Different types (info, warning, error)
- [ ] Mark as read functionality
- [ ] Read state persisted to localStorage
- [ ] Unread count on badge
- [ ] Clear all button
