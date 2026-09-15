# Lesson 05 — Refactoring Challenges

## Refactor 01 (Easy): Index as Key
### Before
```jsx
{items.map((item, index) => <li key={index}>{item.name}</li>)}
```
### After
```jsx
{items.map(item => <li key={item.id}>{item.name}</li>)}
```

## Refactor 02 (Medium): No Key
### Before
```jsx
{items.map(item => <li>{item.name}</li>)}
```
### After
```jsx
{items.map(item => <li key={item.id}>{item.name}</li>)}
```

## Refactor 03 (Hard): Inline Map
### Before
```jsx
function List({ items }) {
  return <ul>{items.map(item => <li key={item.id}>{item.name} - {item.price}</li>)}</ul>;
}
```
### After
```jsx
const ListItem = ({ item }) => <li>{item.name} - {item.price}</li>;
function List({ items }) {
  return <ul>{items.map(item => <ListItem key={item.id} item={item} />)}</ul>;
}
```
