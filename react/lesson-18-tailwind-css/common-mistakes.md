# Lesson 18 — Common Mistakes

## Mistake 01: Missing shade numbers
```jsx
// WRONG
<div className="bg-blue text-white">
// CORRECT
<div className="bg-blue-500 text-white">
```

## Mistake 02: Too many classes
```jsx
// HARD TO READ
<div className="flex flex-col items-center justify-center gap-4 p-4 md:p-8 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow">
// EXTRACT to component or @apply
```

## Mistake 03: Not using config
```jsx
// WRONG — hardcoded colors
<div className="bg-[#007bff]">
// CORRECT — use config
<div className="bg-brand">
```

## Mistake 04: Fighting the framework
```jsx
// WRONG — custom CSS to override Tailwind
// CORRECT — use Tailwind's configuration
```

## Mistake 05: Not purging
```jsx
// Ensure content paths are set in config
// Otherwise CSS includes all utilities (huge file)
module.exports = { content: ["./src/**/*.{js,jsx}"] };
```
