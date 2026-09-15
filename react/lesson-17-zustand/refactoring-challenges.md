# Lesson 17 — Refactoring Challenges

## Refactor 01 (Easy): Prop Drilling for Global State
### Before
```jsx
<App user={user} setUser={setUser} />
  <Header user={user} setUser={setUser} />
```
### After
```jsx
const useStore = create((set) => ({ user: null, setUser: (u) => set({ user: u }) }));
const user = useStore(s => s.user);
```

## Refactor 02 (Medium): Redux Boilerplate
### Before
```jsx
// actions, reducers, types, dispatch
const mapStateToProps = (state) => ({ user: state.user });
connect(mapStateToProps)(Component);
```
### After
```jsx
const user = useStore(s => s.user);
```

## Refactor 03 (Hard: No Selector
### Before
```jsx
const state = useStore(); // re-renders on ANY state change
```
### After
```jsx
const user = useStore(s => s.user); // only re-renders when user changes
```
