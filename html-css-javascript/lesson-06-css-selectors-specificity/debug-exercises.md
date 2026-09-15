# Lesson 06 — Debug Exercises

## Debug 01 (Easy): Wrong Selector
```css
p .text { color: red; }
```
**Hint:** Space means descendant. No space means something else.
<details><summary>Answer</summary>
**Bug:** `p .text` selects elements with class "text" INSIDE `<p>`. If you want `<p class="text">`, use `p.text` (no space).
</details>

## Debug 02 (Medium): Specificity War
```css
#header .title { color: blue; }
.title { color: red; }
```
Which wins for `<div id="header"><h1 class="title">Hi</h1></div>`?
<details><summary>Answer</summary>
Blue wins — `#header .title` has specificity (1,1,0) vs `.title` (0,1,0). ID beats class.
</details>

## Debug 03 (Hard): !important Overuse
```css
.text { color: red !important; }
#header .text { color: blue; }
```
<details><summary>Answer</summary>
Red wins — `!important` overrides specificity. This is why `!important` is a code smell. Avoid it.
</details>
