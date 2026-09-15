# Lesson 03 — Concepts Explained (HTML Tables & Data Display)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Table Structure (table, tr, th, td)

**What:** Tables display data in rows and columns, like a spreadsheet.

```html
<table>
  <tr>                 <!-- a row -->
    <th>Name</th>      <!-- header cell (bold, centered) -->
    <th>Age</th>
  </tr>
  <tr>
    <td>Akash</td>     <!-- data cell -->
    <td>25</td>
  </tr>
</table>
```

- `<table>` = the wrapper, `<tr>` = a row, `<th>` = header cell, `<td>` = data cell.

**Why it exists:** Some data is naturally tabular — financial reports, schedules, comparison charts. Tables give structure that makes this data readable and accessible.

**Where it's used:** Data dashboards, pricing tables, schedules, spreadsheets on web pages, email clients.

**What goes wrong without it:**
- Using `<div>` for tabular data → screen readers can't navigate rows/columns.
- Using tables for LAYOUT (not data) → terrible accessibility, hard to make responsive. This was common in the 1990s — don't do it today.
- Mismatched column counts per row → cells shift, data lands in wrong columns.

---

## Table Sections (thead, tbody, tfoot)

**What:** Tables are split into three sections: header, body, and footer.

```html
<table>
  <thead>
    <tr><th>Quarter</th><th>Revenue</th></tr>
  </thead>
  <tbody>
    <tr><td>Q1</td><td>$10,000</td></tr>
    <tr><td>Q2</td><td>$15,000</td></tr>
  </tbody>
  <tfoot>
    <tr><td>Total</td><td>$25,000</td></tr>
  </tfoot>
</table>
```

- `thead` = column headers (labels).
- `tbody` = the actual data rows.
- `tfoot` = summary/totals row.

**Why it exists:** Separating header, body, and footer lets the browser scroll the body independently of the header (useful for long tables), lets screen readers understand structure, and lets CSS style each section differently.

**Where it's used:** Financial tables, data reports, any table with a totals/summary row.

**What goes wrong without it:**
- All rows in one flat block → no structural distinction between headers and data.
- Header doesn't stay visible when body scrolls (in styled tables).
- Totals row mixes with data rows → screen readers can't tell it's a summary.
- `tfoot` must come AFTER `tbody` in HTML5 (older HTML4 put it before `tbody` — don't use the old order).

---

## Header Cell Scope (th scope)

**What:** The `scope` attribute on `<th>` tells screen readers whether the header labels a column or a row.

```html
<!-- Column headers -->
<tr>
  <th scope="col">Name</th>
  <th scope="col">Age</th>
</tr>

<!-- Row headers -->
<tr>
  <th scope="row">Q1</th>
  <td>$10,000</td>
</tr>
```

- `scope="col"` = this header labels the column below it.
- `scope="row"` = this header labels the row beside it.

**Why it exists:** Without `scope`, a screen reader reads cells in sequence ("Name, Age, Akash, 25") with no relationship. With `scope`, it reads "Name: Akash, Age: 25" — associating each data cell with its header.

**Where it's used:** Any accessible data table, especially tables with both column and row headers.

**What goes wrong without it:**
- Screen readers read cells as a flat list → blind users can't understand which header applies to which cell.
- Complex tables become incomprehensible without scope.
- For very complex tables with multiple headers per cell, use `headers`/`id` instead, but `scope` covers 95% of cases.

---

## Table Caption

**What:** The `<caption>` element gives a table a title. It must be the FIRST child of `<table>`.

```html
<table>
  <caption>Monthly Revenue Report — 2026</caption>
  <thead>
    <tr><th>Month</th><th>Revenue</th></tr>
  </thead>
  ...
</table>
```

**Why it exists:** A table without a title is just numbers. The caption gives context — what is this table about? — before a user reads any cells. Screen readers announce the caption first.

**Where it's used:** Data tables in reports, dashboards, documentation.

**What goes wrong without it:**
- Screen reader users hear cells with no context — "January, $10,000" — what is this?
- Sighted users see a table with no heading, must guess the topic.
- Putting the caption OUTSIDE the table (as a `<h3>` above it) → screen readers don't associate it with the table.

---

## Column Groups (colgroup, col)

**What:** `<colgroup>` and `<col>` let you style or set widths for entire columns at once, instead of repeating styles on every cell.

```html
<table>
  <colgroup>
    <col style="width: 200px; background: #eee;" />
    <col style="width: 100px;" />
    <col style="width: 100px;" />
  </colgroup>
  <thead>
    <tr><th>Name</th><th>Age</th><th>City</th></tr>
  </thead>
  <tbody>
    <tr><td>Akash</td><td>25</td><td>Delhi</td></tr>
  </tbody>
</table>
```

- `<colgroup>` wraps one or more `<col>` elements.
- Each `<col>` represents a column. Styles on `<col>` apply to the whole column.

**Why it exists:** Without colgroup, to set column widths you must add a class/style to every `<td>` and `<th>` in that column. For a 100-row table, that's 100 repetitions. Colgroup does it once.

**Where it's used:** Wide tables where columns need specific widths, tables with column-based coloring (e.g. highlighting a column).

**What goes wrong without it:**
- Setting width on individual cells → columns have inconsistent widths if any cell is missed.
- Much more repetitive CSS/HTML.
- Note: only a few CSS properties work on `<col>` (width, visibility, background, border). You can't set font-size or padding on a col — those must go on cells.

---

## Cell Spanning (colspan, rowspan)

**What:** `colspan` makes a cell span multiple columns; `rowspan` makes it span multiple rows.

```html
<!-- A cell spanning 2 columns -->
<tr>
  <td colspan="2">Merged cell</td>
</tr>

<!-- A cell spanning 2 rows -->
<tr>
  <td rowspan="2">Spans down</td>
  <td>Row 1</td>
</tr>
<tr>
  <td>Row 2</td>   <!-- the rowspan cell continues here, so only 1 td needed -->
</tr>
```

**Why it exists:** Real data isn't always a perfect grid. A summary row might need one wide cell. A category label might apply to multiple rows below it. Spanning handles these real-world layouts.

**Where it's used:** Summary/total rows, grouped headers, schedules with time blocks, comparison tables.

**What goes wrong without it:**
- Wrong `colspan` count → columns shift, data lands in wrong places. The total cell count per row must still equal the number of columns (accounting for spans).
- Forgetting to remove a `<td>` when using `rowspan` → extra cell pushes everything sideways.
- Overusing spans → tables become hard to maintain and inaccessible.

---

## Styling Tables (border-collapse, borders, padding)

**What:** By default, HTML tables have no borders and spaced-out cells. CSS controls the look.

```css
table {
  border-collapse: collapse;   /* removes gaps between cells */
  width: 100%;
}
th, td {
  border: 1px solid #ccc;
  padding: 8px;
  text-align: left;
}
th {
  background: #f4f4f4;
}
tbody tr:nth-child(even) {
  background: #fafafa;         /* zebra striping */
}
```

- `border-collapse: collapse` merges cell borders into single lines (vs `separate` which keeps gaps).
- Zebra striping (alternating row colors) improves readability.

**Why it exists:** Default table styling is ugly and inconsistent across browsers. CSS gives you control to make tables readable and professional.

**Where it's used:** Every styled data table.

**What goes wrong without it:**
- `border-collapse: separate` (default) → double borders between cells, looks messy.
- No padding → text touches borders, cramped and unreadable.
- No zebra striping → hard to follow a row across a wide table.
- Setting `border` on `<table>` only → inner cell borders missing; set borders on `th`/`td` too.

---

## Responsive Tables

**What:** Tables are wide by nature and overflow on small screens. Common fixes:

```css
/* Option 1: horizontal scroll */
.table-wrapper {
  overflow-x: auto;
}

/* Option 2: use CSS to reformat on mobile */
@media (max-width: 600px) {
  th, td { display: block; }  /* stack cells vertically */
}
```

```html
<div class="table-wrapper">
  <table>...</table>
</div>
```

**Why it exists:** A 6-column table doesn't fit on a 320px phone. Without a strategy, the table overflows or gets squished to unreadable widths.

**Where it's used:** Any table viewed on mobile — dashboards, reports, data-heavy sites.

**What goes wrong without it:**
- Table overflows the screen → horizontal scroll on the whole page, broken layout.
- Columns squished to 50px → text wraps every word, unreadable.
- No wrapper with `overflow-x: auto` → can't scroll just the table.
