# Lesson 11 — Coding Check

## Easy

### p01-solve.vue — Basic table
- [ ] 5 users defined (id, name, email, age)
- [ ] Columns defined with labels
- [ ] `row-key="id"` set
- [ ] Sorting enabled on name
- [ ] Sorting enabled on age
- [ ] Table displays correctly

### p02-solve.vue — Search filter
- [ ] QInput with debounce
- [ ] `filter` ref bound to table
- [ ] Filter input above table
- [ ] Rows filter in real-time
- [ ] Empty state when no matches

### p03-solve.vue — Custom cells
- [ ] `body-cell-status` slot used
- [ ] Green badge for "active"
- [ ] Red badge for "inactive"
- [ ] `body-cell-actions` slot used
- [ ] Edit button
- [ ] Delete button
- [ ] `:props="props"` passed to q-td

## Medium

### p01-solve.vue — Pagination
- [ ] 50 sample rows generated
- [ ] 10 rows per page
- [ ] Page navigation shown
- [ ] Rows-per-page selector (5, 10, 20, 50)
- [ ] Pagination works correctly

### p02-solve.vue — Row selection
- [ ] `selection="multiple"` set
- [ ] `selected` ref bound
- [ ] "Delete Selected" button
- [ ] Button shows count of selected
- [ ] Confirm dialog on delete
- [ ] Selection cleared after delete

### p03-solve.vue — Server-side pagination
- [ ] 100 items in dataset
- [ ] `@request` handler
- [ ] Simulated API (setTimeout)
- [ ] 10 items per page
- [ ] Loading state shown
- [ ] Sorting handled server-side
- [ ] `rows-number` set to total

## Hard

### p01-solve.vue — Complete admin table
- [ ] 100 users
- [ ] Search filter
- [ ] Sortable columns
- [ ] Pagination (10/page)
- [ ] Row selection
- [ ] Bulk delete with confirmation
- [ ] Custom status badge cell
- [ ] Action buttons (edit/delete)
- [ ] CSV export button
- [ ] Loading state
- [ ] Empty state

### p02-solve.vue — Virtual scroll table
- [ ] 10,000 rows generated
- [ ] `virtual-scroll` enabled
- [ ] `rows-per-page-options="[0]"` set
- [ ] `virtual-scroll-item-size` set
- [ ] Smooth scrolling
- [ ] Search filter works
- [ ] Row count displayed

### p03-solve.vue — Editable table
- [ ] Double-click to edit cell
- [ ] QInput shown in edit mode
- [ ] Save on Enter
- [ ] Cancel on Escape
- [ ] Notification on save
- [ ] Add row button
- [ ] Delete row button
- [ ] Edit state tracked per cell
