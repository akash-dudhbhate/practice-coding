# Mini Project 01 — Task Breakdown: Accessible Contact Form

> **Step-by-step implementation guide.** Follow each step in order. Don't skip steps.

---

## File Structure

```
mini-01-accessible-contact-form/
├── index.html      # Main HTML page
├── styles.css      # All styling
├── script.js       # Form validation + submission
└── README.md       # Project documentation
```

---

## Step 1: HTML Skeleton (15 min)

Create `index.html` with semantic structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us — [Business Name]</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Skip link for keyboard users -->
    <a href="#main-content" class="skip-link">Skip to main content</a>

    <header>
        <nav><!-- Navigation --></nav>
    </header>

    <main id="main-content">
        <!-- Contact form goes here -->
    </main>

    <footer><!-- Footer --></footer>

    <script src="script.js"></script>
</body>
</html>
```

**Checkpoint:** Open in browser. You should see a blank page with no errors in console.

---

## Step 2: Header + Navigation (10 min)

Add a simple header with business name and nav:

```html
<header role="banner">
    <h1>[Business Name]</h1>
    <nav aria-label="Main navigation">
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact" aria-current="page">Contact</a></li>
        </ul>
    </nav>
</header>
```

**Checkpoint:** Header is visible. Tab through links — focus order is logical.

---

## Step 3: Contact Form (20 min)

Build the form with proper labels and ARIA:

```html
<section aria-labelledby="contact-heading">
    <h2 id="contact-heading">Get in Touch</h2>
    <p>Fill out the form below and we'll get back to you within 24 hours.</p>

    <form id="contact-form" novalidate>
        <!-- Name -->
        <div class="form-group">
            <label for="name">Full Name <span class="required" aria-hidden="true">*</span></label>
            <input type="text" id="name" name="name" required
                   aria-required="true" aria-describedby="name-error"
                   autocomplete="name">
            <span id="name-error" class="error-message" role="alert" aria-live="assertive"></span>
        </div>

        <!-- Email -->
        <div class="form-group">
            <label for="email">Email Address <span class="required" aria-hidden="true">*</span></label>
            <input type="email" id="email" name="email" required
                   aria-required="true" aria-describedby="email-error"
                   autocomplete="email">
            <span id="email-error" class="error-message" role="alert" aria-live="assertive"></span>
        </div>

        <!-- Subject dropdown -->
        <div class="form-group">
            <label for="subject">Subject</label>
            <select id="subject" name="subject">
                <option value="">Choose a topic...</option>
                <option value="general">General Inquiry</option>
                <option value="support">Technical Support</option>
                <option value="billing">Billing Question</option>
            </select>
        </div>

        <!-- Message -->
        <div class="form-group">
            <label for="message">Your Message <span class="required" aria-hidden="true">*</span></label>
            <textarea id="message" name="message" rows="5" required
                      aria-required="true" aria-describedby="message-error"></textarea>
            <span id="message-error" class="error-message" role="alert" aria-live="assertive"></span>
        </div>

        <button type="submit">Send Message</button>
    </form>

    <!-- Success message (hidden initially) -->
    <div id="success-message" class="success-message" role="status" aria-live="polite" hidden>
        <h3>✓ Message Sent!</h3>
        <p>Thank you for reaching out. We'll respond within 24 hours.</p>
    </div>
</section>
```

**Checkpoint:** Form renders with all fields. Each label is linked to its input (click label → input focuses).

---

## Step 4: Footer (5 min)

```html
<footer role="contentinfo">
    <p>&copy; 2024 [Business Name]. All rights reserved.</p>
    <address>
        Email: <a href="mailto:info@business.com">info@business.com</a>
        Phone: <a href="tel:+1234567890">(123) 456-7890</a>
    </address>
</footer>
```

**Checkpoint:** Footer is visible with contact info.

---

## Step 5: CSS Styling (30 min)

Create `styles.css`:

```css
/* Reset + base */
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: system-ui, sans-serif; line-height: 1.6; color: #333; }
a { color: #0066cc; }

/* Skip link — visible only on focus */
.skip-link {
    position: absolute; top: -40px; left: 0;
    background: #0066cc; color: white; padding: 8px 16px;
    z-index: 100; text-decoration: none;
}
.skip-link:focus { top: 0; }

/* Header */
header { padding: 1rem 2rem; border-bottom: 1px solid #ddd; }
nav ul { list-style: none; display: flex; gap: 1rem; margin-top: 0.5rem; }

/* Main */
main { max-width: 600px; margin: 2rem auto; padding: 0 1rem; }

/* Form */
.form-group { margin-bottom: 1.5rem; }
label { display: block; margin-bottom: 0.25rem; font-weight: 600; }
.required { color: #c10015; }
input, select, textarea {
    width: 100%; padding: 0.75rem; border: 1px solid #ccc;
    border-radius: 4px; font-size: 1rem;
}
input:focus, select:focus, textarea:focus {
    outline: 2px solid #0066cc; border-color: #0066cc;
}
button {
    background: #0066cc; color: white; border: none;
    padding: 0.75rem 2rem; font-size: 1rem; border-radius: 4px;
    cursor: pointer; width: 100%;
}
button:hover { background: #0052a3; }

/* Error + success messages */
.error-message { color: #c10015; font-size: 0.875rem; display: block; margin-top: 0.25rem; }
.success-message { background: #d4edda; border: 1px solid #c3e6cb; padding: 1rem; border-radius: 4px; margin-top: 1rem; }

/* Footer */
footer { padding: 1rem 2rem; border-top: 1px solid #ddd; text-align: center; margin-top: 2rem; }

/* Responsive */
@media (max-width: 600px) {
    header, footer { padding: 1rem; }
    nav ul { flex-direction: column; }
}
```

**Checkpoint:** Form looks clean and professional. Responsive on mobile (narrow browser).

---

## Step 6: JavaScript Validation (25 min)

Create `script.js`:

```javascript
const form = document.getElementById('contact-form');
const successMessage = document.getElementById('success-message');

form.addEventListener('submit', function(e) {
    e.preventDefault();
    let valid = true;

    // Clear previous errors
    document.querySelectorAll('.error-message').forEach(el => el.textContent = '');

    // Validate name
    const name = document.getElementById('name');
    if (!name.value.trim()) {
        document.getElementById('name-error').textContent = 'Name is required';
        valid = false;
    }

    // Validate email
    const email = document.getElementById('email');
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email.value.trim()) {
        document.getElementById('email-error').textContent = 'Email is required';
        valid = false;
    } else if (!emailRegex.test(email.value)) {
        document.getElementById('email-error').textContent = 'Please enter a valid email';
        valid = false;
    }

    // Validate message
    const message = document.getElementById('message');
    if (!message.value.trim()) {
        document.getElementById('message-error').textContent = 'Message is required';
        valid = false;
    }

    if (valid) {
        form.hidden = true;
        successMessage.hidden = false;
    }
});
```

**Checkpoint:** Submit empty form → errors appear. Fill valid data → success message shows.

---

## Step 7: Accessibility Testing (15 min)

Test the following:
1. **Keyboard navigation:** Tab through the entire page. Order should be: skip link → nav links → form fields → submit button → footer links.
2. **Screen reader:** Use VoiceOver/NVDA or Chrome's accessibility inspector. Every input should announce its label.
3. **Error announcements:** Submit empty form → errors should be announced (role="alert").
4. **Lighthouse audit:** Run Chrome DevTools → Lighthouse → Accessibility. Score should be 90+.
5. **Color contrast:** Ensure text is readable (use WebAIM contrast checker).

**Checkpoint:** All accessibility tests pass. Lighthouse accessibility score ≥ 90.

---

## Step 8: Polish (10 min)

- Add a subtle box-shadow to the form container
- Add transition on focus (border color change)
- Add a character counter for the message field (optional)
- Test on mobile device (or responsive mode)

---

## Final Checklist

- [ ] Semantic HTML5 structure (header, main, footer, nav)
- [ ] Skip-to-content link
- [ ] All inputs have labels with for/id
- [ ] Required fields marked with `required` + `aria-required`
- [ ] Error messages have `role="alert"` + `aria-live`
- [ ] Success message has `role="status"` + `aria-live`
- [ ] Email validation (HTML + JS)
- [ ] Responsive (mobile + desktop)
- [ ] Keyboard accessible (logical tab order)
- [ ] Lighthouse accessibility score ≥ 90
- [ ] Clean, professional styling

## Common Pitfalls

1. **Forgetting `novalidate` on form** → browser's built-in validation interferes with custom JS validation.
2. **`aria-hidden="true"` on required asterisk** → screen readers announce "required" from the `aria-required` attribute, the asterisk is visual only.
3. **Not clearing errors on resubmit** → old errors persist → confusing.
4. **Hiding the form on success** → use `hidden` attribute, not `display: none` (screen readers skip display:none but announce hidden).
