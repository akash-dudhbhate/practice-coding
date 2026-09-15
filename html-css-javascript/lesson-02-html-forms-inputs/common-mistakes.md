# Lesson 02 — Common Mistakes

## Mistake 01: No label
```html
<!-- WRONG -->
<input type="text" placeholder="Username">

<!-- CORRECT -->
<label for="username">Username</label>
<input id="username" type="text" name="username">
```

## Mistake 02: Wrong input type
```html
<!-- WRONG -->
<input type="text" name="phone">
<input type="text" name="date">

<!-- CORRECT -->
<input type="tel" name="phone">
<input type="date" name="date">
```

## Mistake 03: No server-side validation
```html
<!-- WRONG — only client-side -->
<input type="email" required>
```
Always validate server-side too — client-side can be bypassed.

## Mistake 04: Forgetting name attribute
```html
<!-- WRONG — data not sent -->
<input type="text" id="username">

<!-- CORRECT -->
<input type="text" id="username" name="username">
```

## Mistake 05: Using placeholder as label
```html
<!-- WRONG -->
<input type="text" placeholder="Enter your name">

<!-- CORRECT -->
<label for="name">Name</label>
<input id="name" type="text" placeholder="John Doe">
```
