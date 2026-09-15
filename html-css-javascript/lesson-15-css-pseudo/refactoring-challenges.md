# Lesson 15 — Refactoring Challenges

## Refactor 01 (Easy): Script Tags
### Before
```html
<script src="utils.js"></script>
<script src="api.js"></script>
<script src="app.js"></script>
```
### After
```html
<script type="module" src="app.js"></script>
<!-- app.js: import { utils } from "./utils.js"; -->
```

## Refactor 02 (Medium): Global Variables
### Before
```javascript
// utils.js
window.utils = { helper() { ... } };
// app.js
window.utils.helper();
```
### After
```javascript
// utils.js
export function helper() { ... }
// app.js
import { helper } from "./utils.js";
```

## Refactor 03 (Hard): Default Export Confusion
### Before
```javascript
export default { foo, bar, baz };
// import * as utils from "./utils"; utils.default.foo
```
### After
```javascript
export { foo, bar, baz };
// import { foo } from "./utils";
```
