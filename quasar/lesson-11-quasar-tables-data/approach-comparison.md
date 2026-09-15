# Lesson 11 — Approach Comparison

## Problem: Large Dataset Table

### Approach 1: Client-side
```vue
<q-table :rows="allRows" :rows-per-page-options="[10,25,50]" />
```
**Cons:** Loads all data upfront.

### Approach 2: Server-side
```javascript
async function onRequest(props) {
  const { page, rowsPerPage } = props.pagination;
  const res = await api.get(`/users?page=${page}&limit=${rowsPerPage}`);
  rows.value = res.data.items;
  pagination.value.rowsNumber = res.data.total;
}
```

**Winner:** Approach 2 for 1000+ rows. Approach 1 for small data.
