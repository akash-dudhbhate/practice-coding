# Lesson 03 — Coding Check

Use this to verify your solutions before asking me to review. Open each HTML file in a browser to check it renders correctly.

## Easy

### p01-solve.html (Basic 3-column table)
- [ ] Has `<table>`, `<tr>`, `<th>`, `<td>`.
- [ ] 3 columns: Name, Age, City.
- [ ] Header row with `<th>` for each column.
- [ ] 3 data rows with `<td>` cells.
- [ ] Each row has exactly 3 cells (no mismatched columns).

### p02-solve.html (Table with caption and sections)
- [ ] Has `<caption>` as the first child of `<table>`, titled "Student Grades".
- [ ] Has `<thead>` with header row.
- [ ] Has `<tbody>` with at least 2 data rows.
- [ ] Caption appears above the table in the browser.

### p03-solve.html (Table with CSS borders)
- [ ] Table has visible borders on cells.
- [ ] `border-collapse: collapse` applied (no double borders).
- [ ] Cells have padding (text doesn't touch borders).
- [ ] Borders applied to `th` and `td`, not just `table`.

## Medium

### p01-solve.html (Financial table with tfoot and scope)
- [ ] Has `<thead>`, `<tbody>`, `<tfoot>`.
- [ ] `<tfoot>` contains a totals/summary row.
- [ ] Column headers have `scope="col"`.
- [ ] Row headers (if any) have `scope="row"`.
- [ ] At least 3 data rows in `tbody`.

### p02-solve.html (Table with colgroup)
- [ ] Has `<colgroup>` with at least 2 `<col>` elements.
- [ ] Each `<col>` has a width set (via style or class).
- [ ] Has a `<caption>`.
- [ ] Column widths match the colgroup definitions in the browser.

### p03-solve.html (Table with colspan and rowspan)
- [ ] At least one cell uses `colspan` (spans 2+ columns).
- [ ] At least one cell uses `rowspan` (spans 2+ rows).
- [ ] Total cell count per row is correct (accounts for spans — no extra/missing cells).
- [ ] Table renders without shifted/misaligned columns.

## Hard

### p01-solve.html (Quarterly sales report)
- [ ] Has `<caption>` with a descriptive title.
- [ ] Has `<colgroup>` with `<col>` elements setting widths.
- [ ] Has `<thead>`, `<tbody>`, `<tfoot>`.
- [ ] All `<th>` have `scope` attributes.
- [ ] `tfoot` has a totals row with `scope="row"` on the label cell.
- [ ] Zebra striping: alternating row colors via CSS (`:nth-child(even)` or similar).
- [ ] Borders and padding applied for readability.

### p02-solve.html (Complex comparison table)
- [ ] Has merged header cells using `colspan` (e.g. "First Half" spanning 2 columns).
- [ ] Has row headers with `scope="row"`.
- [ ] All cells align correctly — no shifted columns.
- [ ] Borders and padding applied.
- [ ] Header cells are visually distinct (bold, background color).

### p03-solve.html (Responsive table)
- [ ] Table wrapped in a `<div>` with `overflow-x: auto`.
- [ ] Has `<caption>`, `<thead>`, `<tbody>`.
- [ ] All `<th>` have `scope`.
- [ ] Has a `<style>` block with table CSS (borders, padding).
- [ ] On narrow viewport, table scrolls horizontally within the wrapper (not the whole page).
- [ ] Wrapper prevents page-wide horizontal scroll.

## How to verify

Open each file in a browser:
```bash
xdg-open easy/p01-solve.html
```
- Check columns align — no cell is in the wrong column.
- For colspan/rowspan: verify no extra empty cells appear and rows aren't shifted.
- For responsive: resize the browser window narrow and confirm the table scrolls inside its wrapper, not the whole page.
- For zebra striping: confirm alternating rows have different background colors.
- For tfoot: confirm the totals row is visually at the bottom.
