# Lesson 07 — Forms & Controlled Components

## What you'll learn
- How to make inputs "controlled" by React state.
- How to handle text inputs, textareas, selects, checkboxes, and radio buttons.
- How to manage multiple form fields with a single state object.
- How to validate and submit forms.

## Lesson

A controlled component is an input whose value comes from React state. Every keystroke updates state, and the input reflects state.

```jsx
function NameForm() {
  const [name, setName] = useState("");

  return (
    <form onSubmit={(e) => {
      e.preventDefault();
      console.log(name);
    }}>
      <input value={name} onChange={(e) => setName(e.target.value)} />
      <button type="submit">Submit</button>
    </form>
  );
}
```

### Key rules
- **Text inputs/textarea:** use `value` + `e.target.value`.
- **Checkboxes:** use `checked` + `e.target.checked`.
- **Radio buttons:** use `checked={value === "option"}` + `e.target.value`.
- **Select:** use `value` on `<select>` (not `selected` on `<option>`).
- **Multiple fields:** use one state object + `[e.target.name]: e.target.value`.
- **Always** call `e.preventDefault()` in `onSubmit`.
- **Always** give each input a `name` attribute when using the object pattern.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete component from scratch below** to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.jsx` — **Name Input:** A controlled text input. Display the typed name below in real time. Practice `value` + `onChange` + `e.target.value`.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------------+
   | Sam              |    <- controlled <input>
   +------------------+
   Hello, Sam!               <- <p> updates live
   ```
2. `easy/p02-solve.jsx` — **Checkbox Toggle:** A controlled checkbox that toggles a "Subscribe to newsletter" option. Show the current state below. Practice `checked` + `e.target.checked`.

   WHAT IT SHOULD LOOK LIKE:
   ```
   UNCHECKED:                 CHECKED:
   [ ] Subscribe to           [x] Subscribe to
       newsletter                 newsletter
   Not subscribed             Subscribed!
   ```
3. `easy/p03-solve.jsx` — **Select Dropdown:** A controlled `<select>` for choosing a color. Show the selected color name below. Practice `value` on `<select>`.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +-----------+
   | green   v |               <- <select>: red / green / blue
   +-----------+
   Selected: green             <- <p>
   ```

### Medium
4. `medium/p01-solve.jsx` — **Multi-Field Form:** A form with name, email, and message (textarea) fields. Use one state object with the `[e.target.name]` pattern. Display all values on submit.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------+
   | Ada                  |   <- name
   +----------------------+
   | ada@x.com            |   <- email
   +----------------------+
   | Hello there...       |   <- <textarea>
   +----------------------+
   [ Submit ]
   { "name": "Ada", "email": "ada@x.com",
     "message": "Hello there..." }    <- <pre> JSON on submit
   ```
5. `medium/p02-solve.jsx` — **Radio Button Group:** A size selector (Small/Medium/Large) using radio buttons. Show the selected size. Practice `checked={size === "value"}`.

   WHAT IT SHOULD LOOK LIKE:
   ```
   ( ) Small   (*) Medium   ( ) Large    <- radio group
   Selected size: medium                 <- <p>
   ```
6. `medium/p03-solve.jsx` — **Form with Validation:** A signup form with email and password. Validate on submit: email must contain "@", password must be 8+ characters. Show inline errors.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------+
   | bad-email            |
   +----------------------+
   Email must contain @         <- red error <span>
   +----------------------+
   | ***                  |
   +----------------------+
   Password must be 8+ chars    <- red error <span>
   [ Sign Up ]
   (errors clear as you fix each field)
   ```

### Hard
7. `hard/p01-solve.jsx` — **Registration Form with Validation:** Full registration form: name, email, password, confirm password. Validate all fields (required, email format, password match, length). Show errors inline and clear on fix.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------------+
   |                  |   Name is required        <- red
   +------------------+
   | a@b.com          |
   +------------------+
   | ********         |
   +------------------+
   | *******          |   Passwords do not match <- red
   +------------------+
   [ Register ]
   ```
8. `hard/p02-solve.jsx` — **Controlled Form with Reset:** A contact form that resets all fields after successful submission. Show a success message, then clear the form. Practice form reset pattern.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------------+      AFTER SUBMIT:
   |                  |      +------------------+
   +------------------+      |                  | <- cleared!
   |                  |      +------------------+
   +------------------+      Message sent successfully! <- green,
   |                  |         fades away after ~3s
   +------------------+
   [ Send ]
   ```
9. `hard/p03-solve.jsx` — **Dynamic Form Fields:** A form where users can add/remove multiple email inputs dynamically. Each email is validated. Collect all emails on submit. Practice dynamic form fields with array state.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------------+ +--------+
   | a@b.com          | | Remove |    <- keyed row per email
   +------------------+ +--------+
   | c@d.com          | | Remove |
   +------------------+ +--------+
   [ + Add Email ]  [ Submit ]
   ```

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete component from scratch** below the TODO marker.
- Remove the TODO line when done.
- When done, tell me and I'll review. Say **"give me next task"** to advance.
