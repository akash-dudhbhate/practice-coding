# Lesson 05 — Common Mistakes

## Mistake 01: "Click here" links
```html
<!-- WRONG -->
<a href="/page">Click here</a>
<!-- CORRECT -->
<a href="/page">Read the documentation</a>
```

## Mistake 02: Div as button
```html
<!-- WRONG -->
<div onclick="submit()">Submit</div>
<!-- CORRECT -->
<button onclick="submit()">Submit</button>
```

## Mistake 03: Removing focus outline
```html
/* WRONG */
* { outline: none; }
/* CORRECT — provide alternative */
*:focus { outline: 2px solid blue; }
```

## Mistake 04: No skip link
```html
<!-- Add at top of body -->
<a href="#main" class="skip-link">Skip to main content</a>
```

## Mistake 05: Low contrast
```html
<!-- WRONG — light gray on white -->
<p style="color: #ccc;">Text</p>
<!-- CORRECT — sufficient contrast -->
<p style="color: #333;">Text</p>
```
