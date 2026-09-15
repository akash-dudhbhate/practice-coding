# Lesson 18 — Refactoring Challenges

## Refactor 01 (Easy): Inline Styles
### Before
```jsx
<div style={{ padding: '16px', margin: '8px', backgroundColor: 'red' }}>
```
### After
```jsx
<div className="p-4 m-2 bg-red-500">
```

## Refactor 02 (Medium): Repeated Class Strings
### Before
```jsx
<button className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">A</button>
<button className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">B</button>
```
### After
```jsx
const btnClass = "px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600";
<button className={btnClass}>A</button>
```

## Refactor 03 (Hard): Long Class Lists
### Before
```jsx
<div className="flex flex-col items-center justify-between p-4 m-2 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow cursor-pointer">
```
### After
```jsx
// Extract to component or @apply in CSS
.card { @apply flex flex-col items-center justify-between p-4 m-2 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow cursor-pointer; }
<div className="card">
```
