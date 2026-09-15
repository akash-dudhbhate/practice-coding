# Lesson 08 — Concepts Explained (useRef & DOM Access)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## useRef Basics

**What:** `useRef` creates a mutable reference that persists across renders. Unlike state, updating a ref does NOT trigger a re-render.

```jsx
import { useRef } from 'react';

function Component() {
    const countRef = useRef(0);

    function increment() {
        countRef.current++;     // updates the ref, NO re-render
        console.log(countRef.current);  // see the updated value
    }

    return <button onClick={increment}>Count: {countRef.current}</button>;
    // BUT: the displayed value won't update because no re-render happened
}
```

**Why it exists:** Sometimes you need to store a value that changes but should NOT trigger a re-render. State triggers re-renders → performance issues for rapidly changing values. Refs are for "background" data that the UI doesn't need to react to.

**Where it's used:** DOM element access, timers (setInterval IDs), previous values, any mutable data that doesn't affect rendering.

**What goes wrong without it:**
- Using state for a timer ID → every `setState` triggers a re-render → unnecessary renders.
- `countRef.current = 5` → updates the ref but the UI doesn't change → confused why the display doesn't update. Refs are NOT for display data — use state for that.
- Reading ref during render → unreliable (refs can change during render). Only read refs in event handlers and effects.

---

## Accessing DOM Elements

**What:** The most common use of `useRef` — getting a direct reference to a DOM element.

```jsx
function InputFocus() {
    const inputRef = useRef(null);

    function focusInput() {
        inputRef.current.focus();     // directly call DOM API
    }

    return (
        <>
            <input ref={inputRef} type="text" />
            <button onClick={focusInput}>Focus Input</button>
        </>
    );
}
```

**Why it exists:** React manages the DOM declaratively — you describe WHAT the UI should look like, React updates it. But some operations are imperative — focus, scroll, measure elements, integrate with non-React libraries. `useRef` gives you an escape hatch to the actual DOM.

**Where it's used:** Auto-focusing inputs, scrolling to elements, measuring element sizes, integrating with canvas/chart libraries, media playback (play/pause video).

**What goes wrong without it:**
- `inputRef.current` is `null` on first render → `inputRef.current.focus()` → `TypeError`. The ref is set AFTER the DOM is created. Only access in event handlers or `useEffect`.
- Using refs for things React should handle declaratively → anti-pattern. Don't use refs to set `value` or `className` — use state and props.
- Forgetting to attach the ref: `<input />` without `ref={inputRef}` → ref stays null.

---

## useRef for Timers

**What:** Store timer IDs in refs to clear them later.

```jsx
function Timer() {
    const timerRef = useRef(null);
    const [seconds, setSeconds] = useState(0);

    function start() {
        timerRef.current = setInterval(() => {
            setSeconds(s => s + 1);
        }, 1000);
    }

    function stop() {
        clearInterval(timerRef.current);
    }

    useEffect(() => {
        return () => clearInterval(timerRef.current);  // cleanup on unmount
    }, []);

    return (
        <>
            <p>{seconds}s</p>
            <button onClick={start}>Start</button>
            <button onClick={stop}>Stop</button>
        </>
    );
}
```

**Why it exists:** Without storing the timer ID, you can't clear the interval. State would work but triggers unnecessary re-renders every time you set the timer. Refs store the ID without re-rendering.

**Where it's used:** Timers, intervals, animation frames (requestAnimationFrame), debouncing, WebSocket connections.

**What goes wrong without it:**
- Storing timer ID in state → re-renders on set → unnecessary. Use ref.
- Forgetting cleanup → timer keeps running after component unmounts → memory leak, state updates on unmounted component → warnings.
- `setInterval` in render → creates a new interval every render → multiple intervals running. Always start timers in event handlers or `useEffect`.

---

## useRef for Previous Values

**What:** Track the previous value of a prop or state across renders.

```jsx
function usePrevious(value) {
    const ref = useRef();
    useEffect(() => {
        ref.current = value;    // update AFTER render
    }, [value]);
    return ref.current;         // returns the PREVIOUS value
}

function Counter({ count }) {
    const prevCount = usePrevious(count);
    return (
        <p>Now: {count}, Before: {prevCount}</p>
    );
}
```

**Why it exists:** React doesn't provide a built-in way to access previous values. Sometimes you need to compare current vs previous (e.g., animate on change, detect if value increased or decreased). `useRef` + `useEffect` is the standard pattern.

**Where it's used:** Change detection, animations on value change, undo functionality, debugging.

**What goes wrong without it:**
- Updating ref during render: `ref.current = value` in the component body → runs on every render → ref always has current value, never "previous". Must update in `useEffect` (runs after render).
- `useEffect` runs AFTER the render → `ref.current` still has the old value during render → that's why it returns "previous".
- Dependency array: `[value]` → effect only runs when value changes. Without it → runs every render → ref always current.

---

## useRef vs useState

**What:** When to use which:

| useRef | useState |
|-------|---------|
| Mutable, no re-render | Immutable, triggers re-render |
| For DOM access, timers, background data | For UI-visible data |
| `ref.current = newValue` | `setValue(newValue)` |
| Changes don't trigger updates | Changes trigger re-render |
| Reading during render is unreliable | Reading during render is safe |

```jsx
// WRONG: use ref for display data
const countRef = useRef(0);
return <p>{countRef.current}</p>;  // won't update on change!

// RIGHT: use state for display data
const [count, setCount] = useState(0);
return <p>{count}</p>;  // updates on change

// RIGHT: use ref for timer ID (not displayed)
const timerRef = useRef(null);
timerRef.current = setInterval(...);  // no re-render needed
```

**Why it exists:** Both serve different purposes. Understanding the difference prevents bugs — using state for non-UI data causes unnecessary renders; using ref for UI data causes stale displays.

**Where it's used:** Every component — choose the right hook for each piece of data.

**What goes wrong without it:**
- Ref for display data → UI doesn't update → "why isn't my component re-rendering?"
- State for timer ID → re-renders on set → unnecessary work → performance issues.
- Rule of thumb: if the value affects what's displayed, use state. If it's background data, use ref.

---

## forwardRef

**What:** Allow parent components to pass refs to child components.

```jsx
import { forwardRef, useRef } from 'react';

const CustomInput = forwardRef((props, ref) => {
    return <input ref={ref} {...props} />;
});

function Parent() {
    const inputRef = useRef(null);

    return (
        <>
            <CustomInput ref={inputRef} placeholder="Type here" />
            <button onClick={() => inputRef.current.focus()}>
                Focus Child Input
            </button>
        </>
    );
}
```

**Why it exists:** Without `forwardRef`, you can't pass `ref` to a custom component — React intercepts `ref` and it doesn't reach the DOM element. `forwardRef` forwards the ref through the component to its inner DOM element.

**Where it's used:** Reusable form components (CustomInput, CustomSelect), UI libraries (Material-UI, Chakra), any component that wraps a DOM element and needs ref forwarding.

**What goes wrong without it:**
- `<CustomInput ref={myRef} />` without `forwardRef` → React warning: "Function components cannot be given refs". Ref is `null`.
- Forgetting to spread `{...props}` → other props (className, onClick) are lost.
- `forwardRef` is being replaced by `ref` as a regular prop in React 19. But for older versions, `forwardRef` is required.

---

## Measuring Elements with useRef

**What:** Get the size or position of a DOM element.

```jsx
function MeasureBox() {
    const boxRef = useRef(null);
    const [size, setSize] = useState({ width: 0, height: 0 });

    useEffect(() => {
        if (boxRef.current) {
            const rect = boxRef.current.getBoundingClientRect();
            setSize({ width: rect.width, height: rect.height });
        }
    }, []);

    return (
        <>
            <div ref={boxRef} style={{ width: '50%', background: '#eee' }}>
                Resize the window and refresh
            </div>
            <p>Width: {size.width}px, Height: {size.height}px</p>
        </>
    );
}
```

**Why it exists:** Sometimes you need the actual rendered size of an element (for positioning tooltips, calculating layouts, responsive behavior). `getBoundingClientRect()` gives you the real dimensions.

**Where it's used:** Tooltips (position relative to element), drag-and-drop (element position), responsive layouts, scroll-based animations.

**What goes wrong without it:**
- Measuring in render → element might not be in the DOM yet → `getBoundingClientRect()` returns zeros. Measure in `useEffect`.
- Window resize → measurements are stale. Add a resize listener: `window.addEventListener('resize', updateSize)`.
- Forgetting cleanup → resize listener leaks. Remove in `useEffect` cleanup.

---

## useImperativeHandle

**What:** Customize what the parent can access via the ref — expose only specific methods instead of the entire DOM element.

```jsx
import { forwardRef, useImperativeHandle, useRef } from 'react';

const CustomInput = forwardRef((props, ref) => {
    const inputRef = useRef(null);

    useImperativeHandle(ref, () => ({
        focus: () => inputRef.current.focus(),
        clear: () => { inputRef.current.value = ''; },
        getValue: () => inputRef.current.value,
    }));

    return <input ref={inputRef} {...props} />;
});

// Parent can only call: ref.focus(), ref.clear(), ref.getValue()
// Cannot access the actual DOM element
```

**Why it exists:** Without `useImperativeHandle`, `forwardRef` exposes the entire DOM element → parent can do anything (change innerHTML, style, etc.) → breaks encapsulation. `useImperativeHandle` creates a controlled API.

**Where it's used:** Reusable components that expose specific imperative methods (focus, clear, validate) without exposing the DOM. UI libraries use this extensively.

**What goes wrong without it:**
- Exposing the entire DOM element → parent can modify it directly → breaks the component's internal state → bugs.
- Forgetting `forwardRef` → `useImperativeHandle` has no ref to attach to → warning.
- Overusing `useImperativeHandle` → imperative code in a declarative framework → anti-pattern. Prefer props/callbacks when possible.
