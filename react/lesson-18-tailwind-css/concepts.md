# Lesson 18 — Concepts Explained (Tailwind CSS with React)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What is Tailwind CSS?

**What:** Tailwind is a utility-first CSS framework. Instead of writing custom CSS classes, you compose styles using utility classes directly in JSX.

```jsx
// Traditional CSS: write a class, then style it in a .css file
<button className="btn-primary">Click me</button>
// .btn-primary { background: blue; color: white; padding: 8px 16px; border-radius: 4px; }

// Tailwind: compose utilities directly in JSX
<button className="bg-blue-500 text-white px-4 py-2 rounded">
    Click me
</button>
```

**Why it exists:** Without Tailwind, you switch between JSX and CSS files → context switching, naming classes (BEM, etc.), unused CSS accumulates. Tailwind keeps styles in the JSX → faster development, no naming, only used utilities are in the bundle.

**Where it's used:** Every React component — buttons, cards, layouts, forms, responsive design.

**What goes wrong without it:**
- Long className strings → hard to read. Use the `cn()` utility (clsx + tailwind-merge) to conditionally combine classes.
- Forgetting to configure the Tailwind config → custom colors/fonts don't work.
- Not purging in production → huge CSS file. Tailwind v3+ does this automatically based on content config.

---

## Utility Classes

**What:** Tailwind provides utilities for every CSS property.

```jsx
// Spacing: p (padding), m (margin), w (width), h (height)
<div className="p-4 m-2 w-full h-32">
    <p className="px-2 py-1">Padding X and Y</p>
</div>

// Colors: bg (background), text (color), border
<button className="bg-blue-500 hover:bg-blue-600 text-white border border-gray-300">
    Button
</button>

// Typography: font-size, font-weight, text-align
<h1 className="text-2xl font-bold text-center">Title</h1>
<p className="text-sm text-gray-600 leading-relaxed">Description</p>

// Flexbox and Grid
<div className="flex items-center justify-between gap-4">
    <div className="flex-1">Left</div>
    <div>Right</div>
</div>

<div className="grid grid-cols-3 gap-4">
    <div>1</div><div>2</div><div>3</div>
</div>

// Borders and Rounded
<div className="border-2 border-gray-200 rounded-lg shadow-md p-4">
    Card
</div>
```

**Why it exists:** Instead of memorizing CSS property names and values, Tailwind provides a constrained set of utilities → consistent design system → faster development.

**Where it's used:** Every element that needs styling.

**What goes wrong without it:**
- `px-4` = padding-left and padding-right: 1rem. `p-4` = all sides. Mixing them up → wrong spacing.
- `gap-4` only works with flex/grid. Using it on a block element → no effect.
- Color shades: `blue-500` is the default. `blue-400` is lighter, `blue-600` is darker. Know the scale (50, 100, 200, ..., 900, 950).

---

## Responsive Design

**What:** Tailwind uses mobile-first breakpoints. Base classes apply to all sizes, prefixed classes apply at larger sizes.

```jsx
// Mobile: 1 column. Tablet (md): 2 columns. Desktop (lg): 3 columns
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
    <Card /> <Card /> <Card />
</div>

// Responsive text size
<h1 className="text-xl md:text-2xl lg:text-4xl">Responsive Title</h1>

// Responsive flex direction
<div className="flex flex-col md:flex-row">
    <div>Sidebar</div>
    <div className="flex-1">Main</div>
</div>

// Hide/show at breakpoints
<div className="hidden md:block">Visible on tablet+</div>
<div className="block md:hidden">Visible on mobile only</div>
```

**Breakpoints:**
- `sm`: 640px
- `md`: 768px
- `lg`: 1024px
- `xl`: 1280px
- `2xl`: 1536px

**Why it exists:** Without responsive utilities, you write media queries in CSS → separate file, harder to see the responsive behavior. Tailwind puts it in the className → visible at a glance.

**Where it's used:** Every responsive layout — grids, navigation, sidebars, typography.

**What goes wrong without it:**
- Mobile-first means base (no prefix) = mobile. `md:` = 768px and UP. Forgetting this → styles apply to mobile when you meant desktop only.
- `hidden md:block` → hidden on mobile, visible on tablet+. `block md:hidden` → visible on mobile, hidden on tablet+. Easy to mix up.
- Too many breakpoints → className gets very long. Extract to a component for readability.

---

## Hover, Focus, and State Variants

**What:** Tailwind prefixes for interactive states.

```jsx
// Hover
<button className="bg-blue-500 hover:bg-blue-600 text-white transition-colors">
    Hover me
</button>

// Focus
<input className="border-2 border-gray-300 focus:border-blue-500 focus:outline-none" />

// Focus visible (keyboard only)
<button className="focus:visible:ring-2 focus:visible:ring-blue-500" />

// Active (pressed)
<button className="active:scale-95 transition-transform" />

// Disabled
<button className="disabled:opacity-50 disabled:cursor-not-allowed" disabled>
    Disabled
</button>

// Group hover (parent hover affects children)
<div className="group">
    <h3 className="group-hover:text-blue-500">Title</h3>
    <p className="group-hover:opacity-100 opacity-50">Description</p>
</div>
```

**Why it exists:** Without state variants, you write `:hover`, `:focus` in CSS → separate file. Tailwind puts it in the className → co-located with the element.

**Where it's used:** Every interactive element — buttons, inputs, links, cards with hover effects.

**What goes wrong without it:**
- `hover:` on mobile → touch devices don't have hover → styles don't apply. Use `active:` for touch.
- Forgetting `transition-colors` → hover change is instant → jarring. Add transitions for smooth changes.
- `group` + `group-hover:` → parent must have `group` class. Forgetting it → child `group-hover:` doesn't work.

---

## Conditional Classes (cn utility)

**What:** Combine class names conditionally using a utility function.

```jsx
import { clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

// cn = clsx + tailwind-merge
function cn(...inputs) {
    return twMerge(clsx(inputs));
}

function Button({ variant = 'primary', size = 'md', className, children }) {
    return (
        <button className={cn(
            'rounded font-medium transition-colors',
            {
                'bg-blue-500 hover:bg-blue-600 text-white': variant === 'primary',
                'bg-gray-200 hover:bg-gray-300 text-gray-800': variant === 'secondary',
                'bg-red-500 hover:bg-red-600 text-white': variant === 'danger',
            },
            {
                'px-2 py-1 text-sm': size === 'sm',
                'px-4 py-2': size === 'md',
                'px-6 py-3 text-lg': size === 'lg',
            },
            className  // allow override/additional classes
        )}>
            {children}
        </button>
    );
}
```

**Why it exists:** Without `cn`, conditional classes are string concatenation → messy, no conflict resolution. `clsx` handles conditionals, `tailwind-merge` resolves conflicts (e.g., `px-2 px-4` → `px-4`).

**Where it's used:** Every reusable component with variants — buttons, inputs, cards, badges.

**What goes wrong without it:**
- Without `tailwind-merge`: `cn('px-2', 'px-4')` → `px-2 px-4` → both applied → unpredictable (CSS specificity). With merge → `px-4` (last wins).
- Forgetting to spread `className` → can't customize component from outside → rigid. Always include `className` last in `cn()`.
- Object syntax: `{ 'class': condition }` → class applied when condition is truthy. Falsy → not applied.

---

## Tailwind Config (Customization)

**What:** Extend Tailwind with custom colors, fonts, spacing, etc.

```javascript
// tailwind.config.js
module.exports = {
    content: ['./src/**/*.{js,jsx,ts,tsx}'],
    theme: {
        extend: {
            colors: {
                brand: {
                    50: '#eff6ff',
                    500: '#3b82f6',
                    900: '#1e3a8a',
                },
            },
            fontFamily: {
                sans: ['Inter', 'system-ui', 'sans-serif'],
            },
            animation: {
                'fade-in': 'fadeIn 0.3s ease-in',
            },
            keyframes: {
                fadeIn: {
                    '0%': { opacity: '0' },
                    '100%': { opacity: '1' },
                },
            },
        },
    },
    plugins: [],
};

// Usage
<button className="bg-brand-500 hover:bg-brand-900 text-white font-sans animate-fade-in">
    Custom Button
</button>
```

**Why it exists:** Without config, you're limited to Tailwind's defaults. Config lets you match your brand colors, custom fonts, and project-specific design tokens → consistent design system.

**Where it's used:** Every project — set brand colors, fonts, and custom animations once.

**What goes wrong without it:**
- `content` config missing → Tailwind doesn't scan your files → no utilities generated → unstyled page. Always set `content`.
- Using `theme` (overwrite) vs `theme.extend` (add to) → `extend` preserves defaults. Using `theme` → loses all defaults.
- Custom colors need all shades (50-900) for hover/focus variants to work. Defining only `brand-500` → `hover:bg-brand-600` doesn't exist.

---

## Dark Mode

**What:** Tailwind supports dark mode with the `dark:` prefix.

```jsx
// Class-based dark mode (toggle via JS)
// tailwind.config.js: darkMode: 'class'

<div className="bg-white dark:bg-gray-900 text-gray-900 dark:text-white">
    <h1 className="text-2xl">Adapts to dark mode</h1>
</div>

// Toggle dark mode by adding 'dark' class to <html>
document.documentElement.classList.toggle('dark');
```

**Why it exists:** Without dark mode support, you write custom CSS media queries → separate from Tailwind. `dark:` prefix keeps it in the className → consistent with the rest of your styling.

**Where it's used:** Every app with dark mode — apply `dark:` variants to all colored elements.

**What goes wrong without it:**
- `darkMode: 'media'` (default) → follows OS setting. `darkMode: 'class'` → toggle via JS. If you want a manual toggle, use `'class'`.
- Forgetting `dark:` on some elements → inconsistent dark mode (some elements stay light). Audit all components.
- `dark:bg-gray-900` without `dark:text-white` → dark background with dark text → invisible. Always pair background and text colors.

---

## Component Patterns

**What:** Common React + Tailwind component patterns.

```jsx
// Card
function Card({ children, className }) {
    return (
        <div className={cn('bg-white rounded-lg shadow-md p-6', className)}>
            {children}
        </div>
    );
}

// Badge
function Badge({ children, color = 'blue' }) {
    const colors = {
        blue: 'bg-blue-100 text-blue-800',
        green: 'bg-green-100 text-green-800',
        red: 'bg-red-100 text-red-800',
    };
    return (
        <span className={cn('px-2 py-1 rounded text-sm font-medium', colors[color])}>
            {children}
        </span>
    );
}

// Input
function Input({ label, error, ...props }) {
    return (
        <div>
            {label && <label className="block text-sm font-medium mb-1">{label}</label>}
            <input
                className={cn(
                    'w-full px-3 py-2 border rounded',
                    error ? 'border-red-500' : 'border-gray-300',
                    'focus:outline-none focus:ring-2 focus:ring-blue-500'
                )}
                {...props}
            />
            {error && <p className="text-red-500 text-sm mt-1">{error}</p>}
        </div>
    );
}
```

**Why it exists:** Without reusable patterns, every component restyles from scratch → inconsistent design. Extracting common patterns (Card, Badge, Input) → consistent UI, faster development.

**Where it's used:** Every React + Tailwind project — build a component library early.

**What goes wrong without it:**
- Copy-pasting the same classes across components → inconsistent (one has `rounded-lg`, another `rounded-md`). Extract to a component.
- Not spreading `{...props}` on Input → can't pass `type`, `placeholder`, `onChange` → rigid. Always spread props.
- Hardcoding colors instead of using config → can't change brand color without finding all instances. Use config colors.
