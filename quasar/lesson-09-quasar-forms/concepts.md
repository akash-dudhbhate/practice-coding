# Lesson 09 — Concepts Explained (Quasar Forms)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## QForm and QInput

**What:** Quasar provides form components with built-in validation.

```vue
<template>
    <q-form @submit="onSubmit" class="q-gutter-md">
        <q-input
            v-model="form.name"
            label="Name *"
            :rules="[val => !!val || 'Name is required']"
        />
        <q-input
            v-model="form.email"
            label="Email *"
            :rules="[
                val => !!val || 'Email is required',
                val => /.+@.+\..+/.test(val) || 'Invalid email'
            ]"
        />
        <q-btn type="submit" label="Submit" color="primary" />
    </q-form>
</template>

<script setup>
import { reactive } from 'vue'
const form = reactive({ name: '', email: '' })
function onSubmit() {
    console.log('Form submitted:', form)
}
</script>
```

**Why it exists:** Without QForm, you build forms manually — validation, error display, submit handling → tedious. QForm handles all of it → consistent, accessible, less code.

**Where it's used:** Every form — login, registration, contact, settings.

**What goes wrong without it:**
- `:rules` not set → no validation → user can submit empty form → bad data.
- `type="submit"` on the button → triggers `@submit` on the form. Without it, button does nothing.
- Not using `@submit.prevent` → page reloads on submit. QForm handles this automatically, but be aware.

---

## Validation Rules

**What:** Rules are functions that return `true` (valid) or a string (error message).

```vue
<q-input
    v-model="age"
    label="Age"
    :rules="[
        val => !!val || 'Age is required',
        val => val >= 18 || 'Must be 18+',
        val => val <= 120 || 'Invalid age'
    ]"
/>

<!-- Async validation -->
<q-input
    v-model="username"
    label="Username"
    :rules="[
        val => !!val || 'Required',
        async val => {
            const exists = await checkUsername(val)
            return !exists || 'Username taken'
        }
    ]"
/>
```

**Why it exists:** Without validation, users enter garbage → bad data → bugs, security issues. Rules validate input → catch errors early → data is clean.

**Where it's used:** Every form input that needs validation.

**What goes wrong without it:**
- Rule returns `false` instead of a string → no error message shown → user doesn't know what's wrong.
- Async rules without `await` → validation passes before the check completes → invalid data accepted.
- Too many rules → overwhelming error messages. Show one error at a time (Quasar does this by default).

---

## QSelect, QToggle, QCheckbox, QRadio

**What:** Other form input components.

```vue
<!-- Select dropdown -->
<q-select
    v-model="country"
    :options="countries"
    label="Country"
    emit-value
    map-options
/>

<!-- Toggle (on/off) -->
<q-toggle v-model="notifications" label="Enable notifications" />

<!-- Checkbox -->
<q-checkbox v-model="terms" label="I accept the terms" />

<!-- Radio group -->
<q-radio v-model="gender" val="male" label="Male" />
<q-radio v-model="gender" val="female" label="Female" />

<!-- Slider -->
<q-slider v-model="volume" :min="0" :max="100" label />
```

**Why it exists:** Different input types for different data. Quasar provides all of them with consistent API and styling → no need for external libraries.

**Where it's used:** Every form — selects for dropdowns, toggles for booleans, radios for single choice.

**What goes wrong without it:**
- `q-select` without `emit-value` → v-model gets the whole option object, not the value. Use `emit-value` + `map-options`.
- `q-checkbox` with array v-model → multi-select. With boolean v-model → single checkbox.
- `q-radio` → each radio needs the same v-model but different `val`. Forgetting `val` → all radios are the same.

---

## Form Submission and Reset

**What:** Handle form submit and reset.

```vue
<template>
    <q-form @submit="onSubmit" @reset="onReset" ref="formRef">
        <!-- inputs -->
        <q-btn type="submit" label="Submit" color="primary" />
        <q-btn type="reset" label="Reset" color="secondary" flat />
    </q-form>
</template>

<script setup>
import { ref, reactive } from 'vue'
const formRef = ref(null)
const form = reactive({ name: '', email: '' })

function onSubmit() {
    // Only called if all rules pass
    console.log('Valid form:', form)
}

function onReset() {
    form.name = ''
    form.email = ''
    formRef.value.resetValidation()  // clear error messages
}

// Programmatic validation
async function validate() {
    const valid = await formRef.value.validate()
    if (valid) {
        console.log('Form is valid')
    }
}
</script>
```

**Why it exists:** QForm manages validation state → submit only fires if valid. Reset clears inputs and errors → clean form for reuse.

**Where it's used:** Every form — submit, reset, programmatic validation.

**What goes wrong without it:**
- `@submit` only fires if all rules pass → if it doesn't fire, check your rules.
- `formRef.value.resetValidation()` → clears error messages. Without it, errors persist after reset.
- `validate()` returns a promise → must `await` it. Without await, you get a promise, not a boolean.

---

## QEditor (Rich Text)

**What:** A WYSIWYG rich text editor.

```vue
<q-editor
    v-model="content"
    :toolbar="[
        ['left', 'center', 'right', 'justify'],
        ['bold', 'italic', 'underline', 'strike'],
        ['undo', 'redo'],
        ['link', 'unlink'],
    ]"
    label="Write your post..."
/>
```

**Why it exists:** For content creation (blog posts, comments, messages), plain text isn't enough. QEditor provides formatting → bold, italic, links → rich content.

**Where it's used:** Blog editors, comment boxes, email composers.

**What goes wrong without it:**
- QEditor outputs HTML → must sanitize before displaying (XSS). Use DOMPurify.
- Toolbar too complex → overwhelming. Only include needed buttons.
- v-model contains HTML → storing in database → sanitize on server too.

---

## QFile (File Upload)

**What:** File upload component.

```vue
<q-file
    v-model="files"
    label="Upload files"
    multiple
    accept=".jpg,.png,.pdf"
    max-file-size="5242880"
    @rejected="onRejected"
>
    <template #prepend>
        <q-icon name="attach_file" />
    </template>
</q-file>

<script setup>
import { useQuasar } from 'quasar'
const $q = useQuasar()

function onRejected(rejectedEntries) {
    $q.notify({
        type: 'negative',
        message: `${rejectedEntries.length} file(s) rejected`
    })
}
</script>
```

**Why it exists:** File uploads are common — profile pictures, documents, images. QFile provides a consistent UI with validation (type, size) → better UX.

**Where it's used:** Profile pictures, document uploads, image galleries.

**What goes wrong without it:**
- `accept` doesn't prevent all invalid files → user can drag-drop anything. Validate on server too.
- `max-file-size` → rejected files trigger `@rejected` → notify the user.
- Large files → upload to server immediately or use chunked upload. Don't hold in memory.

---

## Form Layout Best Practices

**What:** Organize forms for good UX.

```vue
<q-form @submit="onSubmit" class="q-gutter-md">
    <!-- Section: Personal Info -->
    <div class="text-h6">Personal Information</div>
    <div class="row q-col-gutter-md">
        <div class="col-12 col-md-6">
            <q-input v-model="form.firstName" label="First Name" />
        </div>
        <div class="col-12 col-md-6">
            <q-input v-model="form.lastName" label="Last Name" />
        </div>
    </div>

    <!-- Section: Contact -->
    <div class="text-h6">Contact</div>
    <q-input v-model="form.email" label="Email" type="email" />
    <q-input v-model="form.phone" label="Phone" />

    <q-btn type="submit" label="Submit" color="primary" class="full-width" />
</q-form>
```

**Why it exists:** Long forms are overwhelming → users abandon them. Sections, columns, and spacing make forms scannable → higher completion rates.

**Where it's used:** Every form with 5+ fields.

**What goes wrong without it:**
- One long column of inputs → mobile users scroll forever → abandon. Use sections.
- Not using `q-gutter` → inputs touch each other → cramped. Use `q-gutter-md`.
- Submit button not visible → user can't find it. Place at the bottom, full width on mobile.
