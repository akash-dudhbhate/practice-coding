# Lesson 02 — Refactoring Challenges

## Refactor 01 (Easy): Separate States for Related Data
### Before
```jsx
const [name, setName] = useState("");
const [email, setEmail] = useState("");
const [age, setAge] = useState(0);
```
### After
```jsx
const [form, setForm] = useState({ name: "", email: "", age: 0 });
```

## Refactor 02 (Medium): Object State Mutation
### Before
```jsx
setForm(form.name = "John"); // mutates directly
```
### After
```jsx
setForm(prev => ({ ...prev, name: "John" }));
```

## Refactor 03 (Hard): Derived State in useState
### Before
```jsx
const [items, setItems] = useState([]);
const [count, setCount] = useState(0);
useEffect(() => setCount(items.length), [items]);
```
### After
```jsx
const [items, setItems] = useState([]);
const count = items.length; // derived, no state
```
