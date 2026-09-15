# Lesson 17 — Approach Comparison

## Problem: Global State

### Approach 1: Context + useReducer
```jsx
const AppContext = createContext();
const [state, dispatch] = useReducer(reducer, initial);
<AppContext.Provider value={{ state, dispatch }}>
```

### Approach 2: Zustand
```jsx
const useStore = create((set) => ({ count: 0, increment: () => set(s => ({ count: s.count + 1 })) }));
```

**Winner:** Approach 2 — simpler, no provider, better performance.

---

## Problem: Persisted State

### Approach 1: Manual localStorage
```jsx
const [count, setCount] = useState(() => Number(localStorage.getItem("count")) || 0);
useEffect(() => { localStorage.setItem("count", count); }, [count]);
```

### Approach 2: Zustand persist
```jsx
const useStore = create(persist((set) => ({ count: 0 }), { name: "my-storage" }));
```

**Winner:** Approach 2 — automatic, cleaner.
