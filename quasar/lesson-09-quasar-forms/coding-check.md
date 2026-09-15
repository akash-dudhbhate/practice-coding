# Lesson 09 — Coding Check

## Easy

### p01-solve.vue — Login form
- [ ] Email field with required + format validation
- [ ] Password field with required + min 6 chars
- [ ] Submit button (type="submit")
- [ ] `@submit` handler
- [ ] Notification shown on submit
- [ ] Form doesn't submit if invalid

### p02-solve.vue — Mixed form inputs
- [ ] QSelect for country
- [ ] QToggle for notifications
- [ ] QCheckbox for terms
- [ ] QRadio for gender
- [ ] Form state displayed below
- [ ] State updates reactively

### p03-solve.vue — Submit and reset
- [ ] Submit button (type="submit")
- [ ] Reset button (type="reset")
- [ ] `@reset` handler clears fields
- [ ] `formRef.value.resetValidation()` called
- [ ] Validation errors cleared on reset

## Medium

### p01-solve.vue — Registration form with sections
- [ ] Personal Info section (name, email)
- [ ] Address section (street, city, zip)
- [ ] Preferences section (newsletter, theme)
- [ ] 2-column layout on desktop
- [ ] 1-column layout on mobile
- [ ] `q-col-gutter` for spacing
- [ ] Section headers

### p02-solve.vue — Async validation
- [ ] Username field with async rule
- [ ] "checking..." indicator while validating
- [ ] Simulated API call (setTimeout)
- [ ] "available" result shown
- [ ] "taken" result shown
- [ ] Validation prevents submit if invalid

### p03-solve.vue — File upload
- [ ] QFile component used
- [ ] Multiple files allowed
- [ ] Accept filter (.jpg, .png)
- [ ] Max file size (5MB)
- [ ] `@rejected` handler
- [ ] Notification for rejected files
- [ ] File previews shown

## Hard

### p01-solve.vue — Multi-step wizard
- [ ] 3 steps: personal, contact, review
- [ ] Each step has validation
- [ ] Next button validates current step
- [ ] Back button navigates without validation
- [ ] Submit on last step
- [ ] Progress indicator
- [ ] Can't skip to next step if invalid

### p02-solve.vue — Dynamic form
- [ ] Add field button
- [ ] Remove field button (per field)
- [ ] Each field has validation
- [ ] Fields are reactive
- [ ] Submit collects all fields
- [ ] Empty state handled (no fields)

### p03-solve.vue — Rich text editor + preview
- [ ] QEditor used
- [ ] Live preview below editor
- [ ] Preview shows rendered HTML
- [ ] Save button stores content
- [ ] Clear button resets
- [ ] HTML sanitized before display
- [ ] Content persists (optional: localStorage)
