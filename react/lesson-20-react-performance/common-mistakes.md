# Lesson 20 — Common Mistakes

## Mistake 01: Premature optimization
```jsx
// Don't wrap everything in React.memo
// Measure first, optimize what's actually slow
```

## Mistake 02: memo without stable props
```jsx
// WRONG — new props every render
<MemoChild onClick={() => {}} style={{}} />
// CORRECT
const onClick = useCallback(() => {}, []);
const style = useMemo(() => ({}), []);
<MemoChild onClick={onClick} style={style} />
```

## Mistake 03: Importing entire libraries
```jsx
// WRONG — 70KB
import _ from "lodash";
// CORRECT — tree-shakeable
import debounce from "lodash/debounce";
```

## Mistake 04: Not code splitting
```jsx
// WRONG — one huge bundle
import Heavy from "./Heavy";
// CORRECT — load on demand
const Heavy = React.lazy(() => import("./Heavy"));
```

## Mistake 05: Rendering huge lists
```jsx
// WRONG — renders all 10,000 items
{items.map(item => <Row key={item.id} />)}
// CORRECT — virtualize
<FixedSizeList itemCount={items.length}>...</FixedSizeList>
```
