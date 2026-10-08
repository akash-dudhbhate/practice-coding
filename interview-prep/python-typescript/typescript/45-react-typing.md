# 45 — TypeScript + React: props, `children`, `useState<T>`, `useRef`, generic components

> **Interview question:** "How do you type React components in TypeScript — props, children, hooks?"
> **What the interviewer is really testing:** Whether you know the *idioms*: props as an interface, `children` as `React.ReactNode`, `useState<T>` only when inference fails, `useRef`'s two meanings (DOM ref vs mutable box), and how to write a generic component. Not `React.FC` dogma — the practical patterns.

## Theory — what it is

**Props — an interface (or `type`), nothing fancy:**

```tsx
interface ButtonProps {
  label: string;
  disabled?: boolean;                 // optional
  onClick: () => void;                // callback prop
  children: React.ReactNode;          // anything renderable
}

function Button({ label, disabled, onClick, children }: ButtonProps) {
  return <button disabled={disabled} onClick={onClick}>{label}{children}</button>;
}
```

Rules that matter:

- **`React.ReactNode` for children** — the widest "renderable" type: elements, strings, numbers, fragments, arrays of those, `null`/`undefined`. (`React.ReactElement` is narrower — a single `<jsx/>` element; `ReactNode` is what `children` actually accepts.)
- **`useState<T>`** — usually *infer*: `useState("")` → `string`. Only pass `<T>` when inference fails: empty/nullable initial (`useState<User | null>(null)`), or widening a literal/union.
- **`useRef` has two jobs with two typings:**
  - DOM ref: `useRef<HTMLInputElement>(null)` — read `ref.current?.focus()`; `current` is readonly-ish conceptually but you never assign it (React does).
  - Mutable box: `useRef<number>(0)` — a `.current` you *do* assign (timers, previous values) — changes don't re-render.
- **Generic components:** `function List<T>({ items, render }: { items: T[]; render: (item: T) => ReactNode })` — `T` inferred from usage; `<List items={users} render={u => ...}/>` makes `u` typed `User`.
- **`React.FC`** — the old helper (`React.FC<Props>`) — mostly discouraged now: it added implicit `children`, can't be generic, makes return type `JSX.Element | null` — plain function declarations are the modern idiom.
- **Event handlers** — covered in file 38 (`ChangeEvent<HTMLInputElement>` etc.).

## Why it was needed

React's API is plain functions — TypeScript just has to describe them. The friction points were specific: `children` needed a type broad enough for "anything JSX can render" (`ReactNode`); `useState`'s generic needed inference smart enough to not require annotations on every call; `useRef` overloaded one hook for two purposes (DOM handle vs mutable cell) so the generic parameterization differs — `useRef<T>(null)` (read-only-ish) vs `useRef<T>(init)` (writable box); and components needed to be generic (`List<T>`) which arrow-function syntax (`<T,>` hack in `.tsx`) makes awkward — hence function declarations.

## Where it's used in a real project

- **Every component file:** props interface at top, destructured params, `ReactNode` children.
- **Forms:** `useState` for controlled inputs, `useRef` for focus/`e.currentTarget` (file 38 covers the event types).
- **Design systems:** generic `List<T>`/`Select<T>` components, `onSelect: (item: T) => void` callbacks.
- **`useRef` patterns:** storing `setTimeout` ids, previous-value tracking (`usePrevious`), DOM measurements (`scrollHeight`, `focus()`).
- **`ComponentProps<typeof X>`** to extend a component's props in wrappers.

## Diagram

```
interface ButtonProps {
  label: string;
  onClick: () => void;
  children: React.ReactNode;   <- "anything renderable"
}

<Button label="Go" onClick={...}>Click <b>me</b></Button>
                                   │
                                   └─ children = text + element + ...
                                      ReactNode accepts all of it

useState — inference vs explicit:
  const [q, setQ] = useState("");          q: string      ✅ inferred
  const [u, setU] = useState<User | null>(null);          ✅ explicit needed
  const [n, setN] = useState<number>();    n: number|undefined ✅

useRef — two different typings for two purposes:
  const inputRef = useRef<HTMLInputElement>(null);   DOM handle — React writes it
  const countRef = useRef(0);                        mutable box — YOU write it
  countRef.current++;                                ✅ assignable
  inputRef.current?.focus();                         read via ?.

Generic component — T flows from props to callbacks:
  function List<T>(p: { items: T[]; render: (t: T) => ReactNode })
  <List items={users} render={u => <li>{u.name}</li>} />
                         │
                         u: User — inferred, not any
```

## Code — explained

```tsx
import { useState, useRef } from "react";
import type { ReactNode } from "react";

// 1. Props as an interface — the bread and butter
interface CardProps {
  title: string;
  footer?: ReactNode;              // optional ReactNode prop
  children: ReactNode;             // required children
  onClose?: () => void;
}

function Card({ title, footer, children, onClose }: CardProps) {
  return (
    <div className="card">
      <h2>{title}</h2>
      {children}
      {footer && <footer>{footer}</footer>}
      {onClose && <button onClick={onClose}>x</button>}
    </div>
  );
}

// 2. useState — infer when possible, annotate when inference fails
function SearchBox() {
  const [query, setQuery] = useState("");                    // string — inferred
  const [user, setUser] = useState<User | null>(null);       // explicit needed
  const [count, setCount] = useState<number>();              // number | undefined
  const inputRef = useRef<HTMLInputElement>(null);           // DOM ref

  const submit = () => {
    inputRef.current?.focus();      // (3) ?. because ref is null until mounted
    setUser({ id: "1", name: query });
  };

  return <input ref={inputRef} value={query}
               onChange={(e) => setQuery(e.currentTarget.value)} />;
}

// 4. useRef as a mutable box — NOT a DOM ref
function Timer() {
  const tickRef = useRef(0);              // MutableRefObject<number>
  tickRef.current += 1;                   // assignable — doesn't re-render
  return <div>{tickRef.current}</div>;
}

// 5. Generic component — T inferred from items
interface ListProps<T> {
  items: T[];
  render: (item: T) => ReactNode;
}
function List<T>({ items, render }: ListProps<T>) {
  return <ul>{items.map((it, i) => <li key={i}>{render(it)}</li>)}</ul>;
}

interface User { id: string; name: string }
const users: User[] = [{ id: "1", name: "Ana" }];

// usage — u inside render is typed User, inferred from items
const el = <List items={users} render={(u) => <span>{u.name}</span>} />;
```

1. `CardProps` — required `title`/`children`, optional `footer`/`onClose`. `children: ReactNode` accepts elements, strings, fragments, arrays — the widest "renderable" type.
2. `useState("")` infers `string` — annotate only when the initial value can't carry the type: `null` (`User | null`), empty (`useState<number>()`), or a union you're widening into.
3. `inputRef.current?.focus()` — `useRef<HTMLInputElement>(null)` types `current` as `HTMLInputElement | null` — it's `null` until React attaches the DOM node, so `?.` is mandatory, not optional style.
4. `useRef(0)` for a mutable box — `.current` is writable and changes don't trigger re-render (vs `useState` which does). Two jobs, two typings.
5. `List<T>` — the generic lives on the props interface; callers pass `items={users}` and `T` = `User` is inferred, so `u` in `render` is fully typed. Arrow-function generics in `.tsx` need `<T,>` or `<T extends unknown>` to dodge the JSX parse ambiguity — `function` declarations avoid it.

## Problems

### Easy — type a component's props
**Problem:** Write `Alert({ kind, message, onDismiss })` where `kind` is `"info" | "warn" | "error"`, `message` a `string`, `onDismiss` optional callback. Show a use with `onDismiss` omitted.
**Try this input:** `<Alert kind="error" message="boom" />`.
**Expected output:** compiles; passing `kind="fatal"` errors.
**Solution:**
```tsx
interface AlertProps {
  kind: "info" | "warn" | "error";
  message: string;
  onDismiss?: () => void;
}

function Alert({ kind, message, onDismiss }: AlertProps) {
  return (
    <div className={`alert-${kind}`}>
      {message}
      {onDismiss && <button onClick={onDismiss}>×</button>}
    </div>
  );
}

const a = <Alert kind="error" message="boom" />;          // ✅ onDismiss optional
// const b = <Alert kind="fatal" message="x" />;          // ❌ "fatal" not in union
```
**Logic explained:**
1. `kind` as a string-literal union — the variant prop — restricts styling to known classes and fails typos like `"fatal"` at compile time.
2. `onDismiss?: () => void` — optional callback prop; the `&&` guard means the button only renders when a handler was passed.
3. Plain interface + destructured params — no `React.FC`, no magic — that's the modern idiom.

### Medium — `useState` and `useRef` together
**Problem:** Build a `SearchInput` that keeps a `query` in state and focuses its `<input>` via a ref when `onSearch` fires. Show the `null`-safe ref use.
**Try this input:** typing "cats", then clicking Search → input refocuses.
**Expected output:** `searching: cats` logged; `inputRef.current?.focus()` safe before mount.
**Solution:**
```tsx
import { useRef, useState } from "react";

function SearchInput() {
  const [query, setQuery] = useState("");
  const inputRef = useRef<HTMLInputElement>(null);   // HTMLInputElement | null

  const onSearch = () => {
    console.log(`searching: ${query}`);
    inputRef.current?.focus();        // ?. — null until mounted
  };

  return (
    <>
      <input
        ref={inputRef}
        value={query}
        onChange={(e) => setQuery(e.currentTarget.value)}
      />
      <button onClick={onSearch}>Search</button>
    </>
  );
}
```
**Logic explained:**
1. `useState("")` — inference gives `string`; `setQuery` is typed `(s: string) => void`.
2. `useRef<HTMLInputElement>(null)` — the DOM-ref use: `current` is `HTMLInputElement | null` (React fills it on mount, clears on unmount).
3. `inputRef.current?.focus()` — the `?.` isn't style: before mount / after unmount, `current` is genuinely `null`; the type forces the guard.
4. `ref={inputRef}` wires it — React does the assignment, you only read.

### Hard — generic `Select<T>` component
**Problem:** Write `Select<T>` taking `options: T[]`, `getLabel: (t: T) => string`, `onSelect: (t: T) => void`. Show `T` inferred as `User` and `onSelect`'s arg typed correctly.
**Try this input:** `<Select options={users} getLabel={u => u.name} onSelect={u => console.log(u.id)} />`.
**Expected output:** `u` inside both callbacks typed `User`; `onSelect={(x: string) => ...}` errors.
**Solution:**
```tsx
import type { ReactNode } from "react";

interface SelectProps<T> {
  options: T[];
  getLabel: (item: T) => string;
  onSelect: (item: T) => void;
}

function Select<T>({ options, getLabel, onSelect }: SelectProps<T>) {
  return (
    <ul>
      {options.map((opt, i) => (
        <li key={i} onClick={() => onSelect(opt)}>
          {getLabel(opt)}
        </li>
      ))}
    </ul>
  );
}

interface User { id: string; name: string }
const users: User[] = [{ id: "1", name: "Ana" }, { id: "2", name: "Bo" }];

const el = (
  <Select
    options={users}                          // T inferred = User
    getLabel={(u) => u.name}                 // u: User
    onSelect={(u) => console.log(u.id)}      // u: User — fully typed
  />
);
// <Select options={users} getLabel={u=>u.name} onSelect={(x: string)=>{}} />
//   ❌ Error: User not assignable to string
```
**Logic explained:**
1. `SelectProps<T>` — the generic lives on the props; `T` appears in `options`, `getLabel`, and `onSelect`, so all three stay correlated to the same type.
2. `function Select<T>` — the function-declaration generic works cleanly in `.tsx`; an arrow version needs `const Select = <T,>(props: SelectProps<T>) => ...` (the trailing comma stops `<T` parsing as JSX).
3. Inference flows from `options={users}` — `T` becomes `User`, so `u.name`/`u.id` autocomplete and `onSelect` args are `User`, not `any`.
4. This is the design-system pattern — `Table<T>`, `List<T>`, `Combobox<T>` — the component is shape-agnostic; `getLabel`/`render` props bridge `T` to what's displayed.

## The 30-second interview answer

"Props are just an interface — `interface Props { label: string; onClick: () => void; children: React.ReactNode }` — `ReactNode` is the broad 'anything renderable' type for children. For hooks: `useState` usually infers — `useState('')` is `string` — I only annotate when inference fails, like `useState<User | null>(null)` or `useState<number>()` for optional. `useRef` has two typings for its two jobs: `useRef<HTMLInputElement>(null)` is a DOM handle — `current` is `HTMLInputElement | null`, so `?.` — and `useRef(0)` is a mutable box you assign `.current` on without re-rendering. Generic components put `<T>` on the props interface — `List<T>` with `items: T[]` and `render: (t: T) => ReactNode` — so `T` is inferred from `items` and callbacks get real types. I write components as plain function declarations — `React.FC` is discouraged; it can't be generic and forced implicit children."

## Follow-up trap

**"Why not `React.FC`?"** — Three reasons: it implicitly added `children` to props (pre-18) so every component accepted children even when it shouldn't; it can't express generics (`const List: FC<ListProps<T>>` doesn't work — `FC` fixes the type too early); and it changes the return type signature. Plain `function C(props: Props)` is clearer and strictly more capable. Second trap: **"`useRef<HTMLInputElement>(null)` vs `useRef<HTMLInputElement | null>(null)` — same?"** — No: the former gives `RefObject` (`.current` readonly — meant for React to write); the latter gives `MutableRefObject` (`.current` writable). Passing `null` with just `<HTMLInputElement>` is the DOM-ref idiom; for a mutable box you want the writable version. Third: **"`React.ReactNode` vs `React.ReactElement` vs `JSX.Element`?"** — `ReactNode` is everything renderable (elements, strings, numbers, fragments, arrays, null); `ReactElement`/`JSX.Element` is a single `<jsx/>` element only. `children` should be `ReactNode`; `ReactElement` for props that must be exactly one element. Bonus: **generic arrow components need `<T,>` or `<T extends unknown>`** in `.tsx` — `<T>` alone parses as JSX.
