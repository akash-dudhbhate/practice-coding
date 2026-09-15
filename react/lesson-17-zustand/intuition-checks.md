# Lesson 17 — Intuition Checks

## Check 01: Zustand vs Context
Why use Zustand over Context?
<details><summary>Answer</summary>
Zustand: no provider needed, selective subscriptions (only re-renders when selected value changes), simpler API. Context: built-in, no dependency, but all consumers re-render on any change.
</details>

## Check 02: create
```jsx
const useStore = create((set) => ({
  count: 0,
  increment: () => set(state => ({ count: state.count + 1 })),
}));
```
<details><summary>Answer</summary>
`create` returns a hook. `set` updates state (merges by default). Call `useStore()` in components.
</details>

## Check 03: Selectors
```jsx
const count = useStore(state => state.count);
const increment = useStore(state => state.increment);
```
<details><summary>Answer</summary>
Selector function picks specific state. Component only re-renders when selected value changes. Performance optimization.
</details>

## Check 04: set
```jsx
set({ count: 1 });              // merge
set(state => ({ count: state.count + 1 })); // functional
set({ count: 1 }, false);       // replace (not merge)
```
<details><summary>Answer</summary>
Default: merge new state into old. `false` as second arg: replace entire state.
</details>

## Check 05: Middleware
```jsx
const useStore = create(persist((set) => ({ ... }), { name: "storage" }));
```
<details><summary>Answer</summary>
Middleware wraps store. `persist` saves to localStorage. Other middleware: devtools, immer, subscribeWithSelector.
</details>
