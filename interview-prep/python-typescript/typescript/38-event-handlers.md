# 38 — Typing event handlers/callbacks — `React.MouseEvent`, `ChangeEvent<HTMLInputElement>`

> **Interview question:** "How do you type an `onClick` or `onChange` handler in React with TypeScript?"
> **What the interviewer is really testing:** Whether you know React events are *synthetic*, generic over the element type — and that inline handlers need no annotation at all.

## Theory — what it is

In plain JS, `el.addEventListener("click", e => ...)` gives you a DOM `Event`/`MouseEvent`. React wraps these in **synthetic events** — its own cross-browser event objects (`React.MouseEvent`, `React.ChangeEvent`, `React.KeyboardEvent`, `React.FormEvent`) that normalize browser differences but expose the familiar API: `preventDefault`, `stopPropagation`, `target`, `currentTarget`, `key`, `clientX`, etc.

Most React event types are **generic over the element type** — `React.MouseEvent<T = Element>` — where `T` is the element the handler is attached to. The generic matters because it fixes `currentTarget`:

- `React.MouseEvent<HTMLButtonElement>` — `e.currentTarget` is a `HTMLButtonElement` (has `.disabled`, `.name`, `.type`).
- `React.ChangeEvent<HTMLInputElement>` — `e.currentTarget.value` is a `string`; `e.currentTarget.checked` exists for checkboxes.
- `React.KeyboardEvent<HTMLInputElement>` — `e.key` plus the input's `.value`.
- `React.FormEvent<HTMLFormElement>` — for `onSubmit`; `e.preventDefault()` to stop a page reload.

Two rules of thumb:

1. **Inline handlers need no annotation.** `onClick={e => ...}` — TypeScript infers `e` from the JSX attribute's expected type. Hover it in your editor to see the inferred type, and copy that if you need it elsewhere.
2. **Extracted handlers need the annotation.** Pull the handler into a named function and you must write `React.MouseEvent<HTMLButtonElement>` yourself — and pick the right element or `currentTarget` will lie to you.

React also ships matching *handler* types if you'd rather type the whole function: `React.MouseEventHandler<HTMLButtonElement>`, `React.ChangeEventHandler<HTMLInputElement>` — handy when a handler is passed down as a prop.

## Why it was needed

Untyped, `e.target` is `EventTarget` — a nearly-empty interface with no `.value`. Code like `e.target.value` either fails to compile or forces an `as HTMLInputElement` cast at every use site. Casts are fragile: they claim `HTMLInputElement` even when a `<select>` fires the same handler, so the compiler stops protecting you exactly where the DOM is most ambiguous.

The generic element parameter exists because the *same* `onChange` prop can sit on `<input>`, `<textarea>`, or `<select>` — each with a different element type. Typing handlers also catches wiring mistakes like passing a `MouseEvent` handler to `onSubmit` (which expects `FormEvent`) or to `onKeyDown` (which expects `KeyboardEvent`).

## Where it's used in a real project

- **Forms:** `ChangeEvent<HTMLInputElement>` / `HTMLSelectElement` / `HTMLTextAreaElement` to read `.value` safely.
- **Buttons and menus:** `MouseEvent<HTMLButtonElement>` for `stopPropagation`, click coordinates, `currentTarget.disabled`.
- **Keyboard UX:** `KeyboardEvent<HTMLInputElement>` for Enter/Escape/submit-on-enter behavior.
- **Design systems:** a `<Button>` component accepting `onClick?: React.MouseEventHandler<HTMLButtonElement>` as a prop.

## Diagram

```
JSX:  <input onChange={handleChange} />
                  │ contextual typing infers `e`
                  v
        React.ChangeEvent<HTMLInputElement>
                  │
   ┌──────────────┴──────────────────────────────┐
   │ e.currentTarget: EventTarget & HTMLInputElement  ← the <input> itself
   │ e.target:        EventTarget                     ← whatever was hit
   │ e.currentTarget.value: string                    ← generic unlocks this
   └──────────────────────────────────────────────┘

Wrong generic -> wrong element type:
  onChange typed as ChangeEvent<HTMLSelectElement> on an <input>
  => compile error at the JSX prop — good, it caught a lie.
```

## Code — explained

```tsx
function SearchBox() {
  // named handler: annotate with the synthetic event type
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    console.log(e.currentTarget.value);   // string — no cast needed
  };

  const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();
    console.log(e.clientX, e.currentTarget.disabled);  // number, boolean
  };

  const handleKey = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") console.log("submit:", e.currentTarget.value);
  };

  return (
    <>
      <input onChange={handleChange} onKeyDown={handleKey} />
      {/* inline handler: `e` is inferred — no annotation needed */}
      <button onClick={(e) => console.log(e.currentTarget)}>Go</button>
      <button onClick={handleClick}>Also go</button>
    </>
  );
}
```

1. `React.ChangeEvent<HTMLInputElement>` — the generic says "this handler lives on an `<input>`," so `currentTarget` gets input members like `.value` and `.checked`.
2. `currentTarget` vs `target`: `currentTarget` is the element the handler is *bound* to (typed by the generic); `target` is what was actually hit — it can be a child element, so it's only `EventTarget`. Prefer `currentTarget` for reads.
3. `e.preventDefault()` and `e.clientX` come from the base synthetic event shape, shared by all React events.
4. The handler type must match the JSX prop: `onKeyDown` expects `KeyboardEvent`, so passing `handleChange` there is a compile error — on purpose.
5. Alternative: type the function — `const h: React.MouseEventHandler<HTMLButtonElement> = e => {...}` — useful for props.

## Problems

### Easy — read an input's value
**Problem:** Write a *named* `onChange` for `<input>` that logs the current value each keystroke. No `any`, no casts.
**Try this input:** user types `hi`
**Expected output:**
```
h
hi
```
**Solution:**
```tsx
const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
  console.log(e.currentTarget.value);
};

<input onChange={handleChange} />
// typing "hi" logs:  h   then   hi
```
**Logic explained:**
1. `ChangeEvent<HTMLInputElement>` makes `currentTarget` an `HTMLInputElement`, so `.value` is a `string`.
2. `onChange` fires once per keystroke with the *full current* value — "h", then "hi".
3. Without the generic, `currentTarget` is `EventTarget` and `.value` doesn't compile — that's why the element type is in the type.

### Medium — a typed callback prop
**Problem:** Build `<SearchInput onQueryChange={...}>`: the parent passes `onQueryChange: (q: string) => void`, and the component calls it with the input's value on every change.
**Try this input:** user types `cat` into the rendered input
**Expected output:** parent receives `"c"`, `"ca"`, `"cat"` in sequence
**Solution:**
```tsx
interface SearchInputProps {
  onQueryChange: (query: string) => void;
}

function SearchInput({ onQueryChange }: SearchInputProps) {
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    onQueryChange(e.currentTarget.value);
  };
  return <input onChange={handleChange} placeholder="search" />;
}

// parent:
<SearchInput onQueryChange={(q) => console.log(q)} />
// c
// ca
// cat
```
**Logic explained:**
1. The component's public API is a plain callback — `(q: string) => void` — so the parent never touches DOM events.
2. Inside, the DOM-facing handler is still typed `ChangeEvent<HTMLInputElement>`; the translation happens at the boundary.
3. This is the standard layering: DOM event types stay inside the component, clean data types cross the prop boundary.

### Hard — a typed event emitter
**Problem:** Implement `on`/`emit` for a small app event bus. Each event name has its own payload shape; subscribing with the wrong payload type — or emitting one — must be a compile error.
**Try this input:** `emit("search", { query: "cats", page: 2 })` after subscribing
**Expected output:** `q=cats page=2`; and `emit("search", { docId: "1" })` is a *compile error*.
**Solution:**
```typescript
type AppEvents = {
  save:   { docId: string };
  search: { query: string; page: number };
};

type Listener<K extends keyof AppEvents> = (payload: AppEvents[K]) => void;

const listeners: { [K in keyof AppEvents]: Listener<K>[] } = {
  save: [],
  search: [],
};

function on<K extends keyof AppEvents>(event: K, cb: Listener<K>): void {
  listeners[event].push(cb);
}

function emit<K extends keyof AppEvents>(event: K, payload: AppEvents[K]): void {
  for (const cb of listeners[event]) cb(payload);
}

on("search", (p) => console.log(`q=${p.query} page=${p.page}`));
on("save", (p) => console.log(`saved ${p.docId}`));

emit("search", { query: "cats", page: 2 });   // q=cats page=2
emit("save", { docId: "doc-9" });             // saved doc-9
// emit("search", { docId: "1" });            // ❌ compile error: wrong payload
// on("click", () => {});                     // ❌ compile error: unknown event
```
**Logic explained:**
1. `AppEvents` is the contract: event name → payload type. `keyof AppEvents` is `"save" | "search"`.
2. `Listener<K>` uses *indexed access* `AppEvents[K]` — the callback's payload type is looked up from the event name the caller chose.
3. The store is a mapped type `{ [K in keyof AppEvents]: Listener<K>[] }` — each key holds listeners for exactly its own payload.
4. Because `K` is generic, `on("search", cb)` fixes `K = "search"`, so `p` inside the callback is `{ query: string; page: number }` — fully typed, zero casts.
5. Same mechanics as DOM's `addEventListener("click", e => ...)`: the event name selects the event type. That's the interview-worthy insight.

## The 30-second interview answer

"React events are synthetic wrappers, and most are generic over the element: `ChangeEvent<HTMLInputElement>` makes `currentTarget.value` a `string`, `MouseEvent<HTMLButtonElement>` gives you button members like `disabled`. Inline handlers get this for free via contextual typing — I only annotate when I extract a named function, and I use `currentTarget` rather than `target` because the generic fixes its type. When passing handlers as props I use the `*Handler` aliases like `React.MouseEventHandler<HTMLButtonElement>`. The generic exists because the same `onChange` sits on input/select/textarea — the element parameter is what makes `e.currentTarget.value` type-check."

## Follow-up trap

**"Why does `e.target.value` error even though the event obviously came from the input?"** Because `target` is the element where the event *originated* — with event bubbling it can be a child of the element holding the handler — so it's typed `EventTarget`, which has no `value`. `currentTarget` is the element the handler is bound to, which React can type precisely from the generic. Second trap: *"Can you reuse one handler for input and select?"* — yes: `ChangeEvent<HTMLInputElement | HTMLSelectElement>` works, and `currentTarget.value` is `string` on both, but element-specific members then need a narrow (`if (e.currentTarget instanceof HTMLSelectElement)`).
