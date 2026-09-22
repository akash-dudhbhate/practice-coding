# Lesson 09 — Quasar Forms

## What you'll learn
- QForm and QInput (forms with validation)
- Validation rules (sync and async)
- QSelect, QToggle, QCheckbox, QRadio, QSlider
- Form submission and reset
- QEditor (rich text)
- QFile (file upload)
- Form layout best practices

## Lesson

### Basic form
```vue
<q-form @submit="onSubmit">
    <q-input v-model="name" :rules="[val => !!val || 'Required']" />
    <q-btn type="submit" label="Submit" />
</q-form>
```

### Select
```vue
<q-select v-model="country" :options="countries" emit-value map-options />
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.vue` — Create a login form with email and password fields. Add validation (email required + format, password required + min 6 chars). On submit, show a notification with the values.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------+
   |                      |   <- q-input email
   +----------------------+
   Email is required          <- red inline error
   +----------------------+
   | ***                  |   <- q-input password
   +----------------------+
   Min 6 characters           <- red inline error
   [ Login ]  -> toast "Logged in with email: X" when valid
   ```
2. `easy/p02-solve.vue` — Create a form with QSelect (country), QToggle (notifications), QCheckbox (terms), and QRadio (gender). Display the form state below the form.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Country       [ Canada     v ]        <- q-select
   Notifications        [ (o) ]          <- q-toggle
   [x] I accept the terms                <- q-checkbox
   ( ) Male   (*) Female   ( ) Other     <- q-radio group
   --------------------------------------
   { "country":"ca", "notifications":true,
     "terms":true, "gender":"f" }        <- live JSON state
   ```
3. `easy/p03-solve.vue` — Create a form with submit and reset buttons. On reset, clear all fields and validation errors. Use `formRef.resetValidation()`.

   WHAT IT SHOULD LOOK LIKE:
   ```
   INVALID SUBMIT:               AFTER RESET:
   +------------------+          +------------------+
   |                  |          |                  |
   +------------------+          +------------------+
   Required (red)                (no error styling)
   [ Submit ] [ Reset ]          [ Submit ] [ Reset ]
   ```

### Medium
4. `medium/p01-solve.vue` — Create a registration form with sections: Personal Info (name, email), Address (street, city, zip), Preferences (newsletter toggle, theme select). Use a 2-column layout on desktop, 1-column on mobile.

   WHAT IT SHOULD LOOK LIKE:
   ```
   PERSONAL INFO
   +----------------+ +----------------+
   | First name     | | Last name      |   <- side-by-side (wide)
   +----------------+ +----------------+
   ADDRESS
   +----------------+ +----------------+
   | City           | | Zip            |
   +----------------+ +----------------+
   PREFERENCES   [x] Newsletter   [Theme v]
   (fields stack vertically on narrow screens)
   ```
5. `medium/p02-solve.vue` — Create a form with async validation: username field that checks if the username is available (simulate API call with setTimeout). Show "checking..." while validating, "available" or "taken" as the result.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Username: [ admin________ ]  (o) checking...   <- spinner
             -> "Username is taken" (red)
   Username: [ neo_42_______ ]
             -> "Username available" (green)
   [ Submit ]  <- disabled until valid+available
   ```
6. `medium/p03-solve.vue` — Create a file upload form using QFile. Allow multiple images (jpg, png). Show file previews. Validate file size (max 5MB). Show a notification for rejected files.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------------------------+
   | [ Choose files...        ]   |   <- q-file
   +------------------------------+
   +----+ +----+ +----+
   |img | |img | |img |             <- thumbnail previews
   +----+ +----+ +----+
   (oversized/wrong-type -> red toast rejection)
   ```

### Hard
7. `hard/p01-solve.vue` — Build a multi-step form wizard: 3 steps (personal, contact, review). Each step has its own validation. Navigation: next (validates current step), back, and submit on the last step. Show a progress indicator.

   WHAT IT SHOULD LOOK LIKE:
   ```
   ( 1 ) Personal ---( 2 ) Contact ---( 3 ) Review   <- q-stepper
   ----------------------------------------------
   Step 1: Name [_______]  Email [___________]
                              [ Back ]  [ Next ]
   (Next blocked while current step is invalid;
    step 3 shows summary + Submit -> success toast)
   ```
8. `hard/p02-solve.vue` — Build a dynamic form: a form where users can add/remove fields (e.g., "add another phone number"). Each added field has validation. Submit collects all dynamic fields. Include add and remove buttons.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Phone 1: [ 555-0100_____ ]  [ - ]
   Phone 2: [ 555-0199_____ ]  [ - ]
   Phone 3: [ _____________ ]  [ - ]   <- Required if shown
   [ + Add phone ]                     [ Submit ]
   -> submit shows the collected array
   ```
9. `hard/p03-solve.vue` — Build a form with a rich text editor (QEditor) and live preview. User writes in the editor, preview shows the rendered HTML below. Include a save button that stores the content and a clear button that resets. Sanitize the HTML before display.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------------------+
   | B I U | link | ...               |  <- q-editor toolbar
   |----------------------------------|
   | Hello *world*                    |  <- editing area
   +----------------------------------+
   PREVIEW:
   Hello world                        <- rendered live below
   [ Save ] [ Clear ]   -> green "Saved" banner on save
   ```

### How to work
- Write your complete Vue/Quasar solution.
- Remove the TODO comment when done.
- Test by importing into a Quasar app.
