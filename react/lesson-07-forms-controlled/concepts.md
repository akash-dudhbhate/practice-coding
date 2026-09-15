# Lesson 07 — Concepts Explained (Forms & Controlled Components)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Controlled Components

**What:** A controlled component is an input whose value is controlled by React state. The input's `value` comes from state, and every change updates state.

```jsx
function NameForm() {
  const [name, setName] = useState("");

  return (
    <form>
      <input
        type="text"
        value={name}              // value comes FROM state
        onChange={(e) => setName(e.target.value)}  // changes go TO state
      />
      <p>You typed: {name}</p>
    </form>
  );
}
```

The input is "controlled" because React state is the single source of truth. The input can't change without React updating state.

**Why it exists:** Without controlled inputs, the DOM manages the input value — React doesn't know what's in it. Controlled components make React the single source of truth, so you can validate, transform, and track input values in real time.

**Where it's used:** Every form in React — login, signup, search, contact, checkout, settings.

**What goes wrong without it:**
- Setting `value` without `onChange` → React warns: input is read-only. You can't type.
- Using `defaultValue` instead of `value` → uncontrolled input. React can't track or validate the value.
- Mixing controlled and uncontrolled → inconsistent behavior, hard to debug.

---

## Controlled Text Input

**What:** A text input bound to state. Every keystroke updates state, and the input reflects state.

```jsx
function SearchBar() {
  const [query, setQuery] = useState("");

  return (
    <input
      type="text"
      value={query}
      onChange={(e) => setQuery(e.target.value)}
      placeholder="Search..."
    />
  );
}
```

**Why it exists:** Text inputs are the most common form element. Controlling them with state lets you validate as the user types, show live previews, enable/disable submit buttons, and transform input (e.g., uppercase).

**Where it's used:** Search bars, name fields, email fields, textareas, any text entry.

**What goes wrong without it:**
- No `onChange` → input is read-only (React controls the value but can't update it).
- `e.target.value` vs `e.value` → `e.value` is `undefined`. Must be `e.target.value`.
- Forgetting `value={state}` → uncontrolled input. React doesn't track changes. You type but React doesn't know.

---

## Controlled Textarea

**What:** In React, `<textarea>` uses `value` (not `defaultValue` or inner text like HTML).

```jsx
function MessageForm() {
  const [message, setMessage] = useState("");

  return (
    <textarea
      value={message}
      onChange={(e) => setMessage(e.target.value)}
      rows={5}
      placeholder="Write a message..."
    />
  );
}
```

**Why it exists:** In HTML, `<textarea>` uses inner text (`<textarea>Default text</textarea>`). React normalizes this to use `value`, making it consistent with `<input>` — one pattern for all text inputs.

**Where it's used:** Message forms, comments, descriptions, reviews, any multi-line text input.

**What goes wrong without it:**
- Using children: `<textarea>{message}</textarea>` → doesn't work in React. Use `value={message}`.
- Forgetting `onChange` → textarea is read-only.
- Not setting `rows` → defaults to a small box. Set `rows` for height or use CSS.

---

## Controlled Select

**What:** In React, `<select>` uses `value` on the `<select>` element (not `selected` on `<option>` like HTML).

```jsx
function CountrySelector() {
  const [country, setCountry] = useState("us");

  return (
    <select value={country} onChange={(e) => setCountry(e.target.value)}>
      <option value="us">United States</option>
      <option value="uk">United Kingdom</option>
      <option value="in">India</option>
    </select>
  );
}
```

**Why it exists:** In HTML, you mark the selected option with `selected` attribute. React simplifies this — set `value` on `<select>` and it automatically highlights the matching `<option>`. One source of truth, consistent with other inputs.

**Where it's used:** Country/state selectors, category dropdowns, quantity selectors, filter options.

**What goes wrong without it:**
- Using `selected` on `<option>` → React ignores it (use `value` on `<select>`).
- Forgetting `onChange` → select is read-only, can't change selection.
- Value doesn't match any option → nothing appears selected. Ensure the state value matches an option value.

---

## Controlled Checkbox

**What:** Checkboxes use `checked` (not `value`) and read `e.target.checked` in the onChange handler.

```jsx
function PreferencesForm() {
  const [preferences, setPreferences] = useState({
    newsletter: true,
    notifications: false,
    darkMode: true,
  });

  const handleChange = (e) => {
    setPreferences({
      ...preferences,
      [e.target.name]: e.target.checked,  // checked, not value!
    });
  };

  return (
    <form>
      <label>
        <input
          type="checkbox"
          name="newsletter"
          checked={preferences.newsletter}
          onChange={handleChange}
        />
        Subscribe to newsletter
      </label>
    </form>
  );
}
```

**Why it exists:** Checkboxes are boolean (checked/unchecked), not text values. Using `checked` and `e.target.checked` correctly handles this boolean nature.

**Where it's used:** Terms acceptance, newsletter opt-in, preference toggles, multi-select filters.

**What goes wrong without it:**
- Using `value` instead of `checked` → checkbox doesn't reflect state correctly.
- Using `e.target.value` → always "on" regardless of checked state. Must use `e.target.checked`.
- Forgetting `name` attribute → can't use computed property `[e.target.name]` to update the right field.

---

## Controlled Radio Buttons

**What:** Radio buttons share a `name` and use `checked` to indicate the selected option.

```jsx
function SizeSelector() {
  const [size, setSize] = useState("medium");

  return (
    <div>
      <label>
        <input
          type="radio"
          name="size"
          value="small"
          checked={size === "small"}
          onChange={(e) => setSize(e.target.value)}
        />
        Small
      </label>
      <label>
        <input
          type="radio"
          name="size"
          value="medium"
          checked={size === "medium"}
          onChange={(e) => setSize(e.target.value)}
        />
        Medium
      </label>
      <label>
        <input
          type="radio"
          name="size"
          value="large"
          checked={size === "large"}
          onChange={(e) => setSize(e.target.value)}
        />
        Large
      </label>
    </div>
  );
}
```

**Why it exists:** Radio buttons are for selecting ONE option from many. They share a `name` (so the browser groups them), and `checked` reflects which one is selected. State tracks the selected value.

**Where it's used:** Size/color selectors, gender selection, payment method, plan selection.

**What goes wrong without it:**
- Missing `name` → radio buttons aren't grouped → multiple can be selected.
- Using `value` instead of `checked` → React doesn't know which is selected.
- All radios set to `checked={true}` → all appear selected. Use `checked={size === "small"}` to select only the matching one.

---

## Form State Object Pattern

**What:** Instead of separate `useState` for each field, use one state object and update fields with computed property names.

```jsx
function RegistrationForm() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,  // dynamic key from input's name
    });
  };

  return (
    <form>
      <input name="name" value={formData.name} onChange={handleChange} />
      <input name="email" value={formData.email} onChange={handleChange} />
      <input name="password" type="password" value={formData.password} onChange={handleChange} />
    </form>
  );
}
```

**Why it exists:** One handler works for all fields — no need for 5 separate `onChange` functions. The `name` attribute on each input maps to the state key. This scales to forms with many fields.

**Where it's used:** Registration forms, settings panels, checkout forms, any form with 3+ fields.

**What goes wrong without it:**
- Forgetting `name` attribute → `[e.target.name]` is `undefined` → `formData[undefined]` → state breaks.
- Forgetting to spread: `setFormData({ [e.target.name]: e.target.value })` → loses all other fields! Must spread: `setFormData({ ...formData, [e.target.name]: e.target.value })`.
- Using `formData[e.target.name]` without brackets in the object → doesn't work. Must use computed property: `[e.target.name]: e.target.value`.

---

## Form Submission

**What:** Handle form submission with `onSubmit` on the `<form>` element. Always call `e.preventDefault()` first.

```jsx
function ContactForm() {
  const [formData, setFormData] = useState({ name: "", email: "", message: "" });

  const handleSubmit = (e) => {
    e.preventDefault();  // CRITICAL — stops page reload
    console.log("Form submitted:", formData);
    // Send to API, show success message, etc.
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="name" value={formData.name} onChange={handleChange} />
      <input name="email" value={formData.email} onChange={handleChange} />
      <textarea name="message" value={formData.message} onChange={handleChange} />
      <button type="submit">Send</button>
    </form>
  );
}
```

**Why it exists:** The `<form>` `onSubmit` event fires on both button click AND Enter key press. This gives a consistent submission experience. `preventDefault` stops the browser from reloading the page.

**Where it's used:** Every form that submits data — login, signup, contact, checkout.

**What goes wrong without it:**
- Missing `e.preventDefault()` → page reloads → all state lost → blank page. #1 form bug.
- `onClick` on button instead of `onSubmit` on form → Enter key doesn't submit.
- Button without `type="submit"` → may not trigger form submission. Inside a `<form>`, `<button>` defaults to `type="submit"`, but be explicit.
- Button with `type="button"` → doesn't submit. Use this for non-submit buttons inside forms.

---

## Form Validation

**What:** Validate form fields before submission. Show error messages for invalid fields.

```jsx
function SignupForm() {
  const [formData, setFormData] = useState({ email: "", password: "" });
  const [errors, setErrors] = useState({});

  const validate = () => {
    const newErrors = {};
    if (!formData.email) {
      newErrors.email = "Email is required";
    } else if (!formData.email.includes("@")) {
      newErrors.email = "Invalid email format";
    }
    if (!formData.password) {
      newErrors.password = "Password is required";
    } else if (formData.password.length < 8) {
      newErrors.password = "Password must be at least 8 characters";
    }
    return newErrors;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const validationErrors = validate();
    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
      return;  // don't submit if errors
    }
    setErrors({});
    console.log("Form is valid!", formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="email" value={formData.email} onChange={handleChange} />
      {errors.email && <span className="error">{errors.email}</span>}
      <input name="password" type="password" value={formData.password} onChange={handleChange} />
      {errors.password && <span className="error">{errors.password}</span>}
      <button type="submit">Sign Up</button>
    </form>
  );
}
```

**Why it exists:** Users make mistakes — empty fields, invalid emails, short passwords. Validation catches these before submission, giving immediate feedback. Without it, bad data goes to the server.

**Where it's used:** Registration forms, checkout forms, contact forms, any form that needs correct data.

**What goes wrong without it:**
- No validation → empty/invalid data submitted → server errors or corrupted data.
- Validating only on submit → user fills entire form, then sees all errors at once. Better to validate on blur or change for instant feedback.
- Not clearing errors when fixed → error message stays even after user corrects the field. Re-validate on change or clear errors on submit.

---

## Form Reset

**What:** Clear all form fields after submission by resetting state to initial values.

```jsx
function ContactForm() {
  const initialForm = { name: "", email: "", message: "" };
  const [formData, setFormData] = useState(initialForm);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Submitted:", formData);
    setFormData(initialForm);  // reset to initial values
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="name" value={formData.name} onChange={handleChange} />
      <input name="email" value={formData.email} onChange={handleChange} />
      <textarea name="message" value={formData.message} onChange={handleChange} />
      <button type="submit">Send</button>
    </form>
  );
}
```

**Why it exists:** After submitting a form (especially for multi-entry forms like contact or admin panels), users expect the fields to clear. Resetting state clears all controlled inputs at once.

**Where it's used:** Contact forms, admin data entry, message forms, any form where users submit multiple entries.

**What goes wrong without it:**
- Not resetting → form keeps old data → user submits the same data twice by mistake.
- Using `e.target.reset()` → works for uncontrolled forms, but with controlled inputs you must reset state. The inputs show what state says, not what the DOM says.
- Resetting to `""` for each field individually → verbose. Store initial values in a constant and reset to it.
