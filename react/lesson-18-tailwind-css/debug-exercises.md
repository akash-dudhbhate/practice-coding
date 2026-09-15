# Lesson 18 — Debug Exercises

## Debug 01 (Easy: Wrong Class Name
```jsx
<div className="bg-blue">Box</div>
```
<details><summary>Answer</summary>
**Bug:** `bg-blue` is not valid. Tailwind needs shade: `bg-blue-500`.
**Fix:** `className="bg-blue-500"`.
</details>

## Debug 02 (Medium): Arbitrary Value Syntax
```jsx
<div className="w-[500]">Box</div>
```
<details><summary>Answer</summary>
**Bug:** Arbitrary values need units: `w-[500px]`.
**Fix:** `className="w-[500px]"`.
</details>

## Debug 03 (Hard): Responsive Prefix Order
```jsx
<div className="md:sm:flex">Box</div>
```
<details><summary>Answer</summary>
**Bug:** Can't stack responsive prefixes. Only one per property.
**Fix:** `className="sm:flex md:block"` — different breakpoints for different properties.
</details>
