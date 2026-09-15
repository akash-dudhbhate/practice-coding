# Lesson 01 — Coding Check

Use this to verify your solutions before asking me to review.

## Easy

### p01-greeting-component.jsx
- [ ] `Greeting` is a function component (capital G).
- [ ] Accepts `name` prop, renders `<h1>Hello, {name}!</h1>`.
- [ ] Default export.

### p02-button-component.jsx
- [ ] Accepts `label` and `color` props.
- [ ] Uses inline style `{{ backgroundColor: color }}`.
- [ ] Button text shows `{label}`.

### p03-badge-component.jsx
- [ ] Accepts `text` and `variant` props.
- [ ] Color maps: success→green, warning→orange, error→red, default→gray.
- [ ] Renders a `<span>` with inline style.

## Medium

### p01-user-card.jsx
- [ ] `UserCard` accepts `name`, `email`, `role` props.
- [ ] Renders `<h2>` (name), `<p>` (role), `<p>` (email).
- [ ] `App` renders 3 `UserCard` components with different data.
- [ ] `App` is default export.

### p02-price-list.jsx
- [ ] Accepts `items` array prop.
- [ ] Uses `.map()` to render `<li>` elements.
- [ ] Each `<li>` has a `key` prop.
- [ ] Format: "{name}: ${price}".

### p03-alert-component.jsx
- [ ] `type` defaults to "info", `show` defaults to true.
- [ ] Returns `null` when `show` is false.
- [ ] Uses template string for className: `alert alert-${type}`.
- [ ] Has `role="alert"`.

## Hard

### p01-reusable-table.jsx
- [ ] Accepts `columns` and `rows` props.
- [ ] `<thead>` uses `.map()` on columns, each `<th>` has `key`.
- [ ] `<tbody>` uses `.map()` on rows, each `<tr>` has `key`.
- [ ] Cell content accessed via `row[column.key]`.

### p02-nested-comment-tree.jsx
- [ ] `Comment` accepts `author`, `text`, `replies` props.
- [ ] `replies` defaults to `[]`.
- [ ] Renders nested `<Comment>` components recursively.
- [ ] Each reply has a `key`.

### p03-layout-composition.jsx
- [ ] `Layout` accepts `children` prop.
- [ ] `Header` and `Footer` are separate components.
- [ ] `Layout` renders Header, `<main>{children}</main>`, Footer.
- [ ] `App` uses `<Layout>` with children content.
- [ ] `App` is default export.
