# Lesson 03 — HTML Tables & Data Display

## What you'll learn
- How to build tables with `<table>`, `<thead>`, `<tbody>`, `<tfoot>`, `<tr>`, `<th>`, `<td>`.
- How to use `<caption>`, `<colgroup>`, `scope`, `colspan`, and `rowspan`.
- How to style tables with CSS (borders, padding, zebra striping).
- How to make tables responsive on mobile.

## Lesson

Tables display tabular data — data that belongs in rows and columns, like a spreadsheet.

### Basic table
```html
<table>
  <thead>
    <tr><th scope="col">Name</th><th scope="col">Age</th></tr>
  </thead>
  <tbody>
    <tr><td>Akash</td><td>25</td></tr>
  </tbody>
</table>
```

### Sections
- `thead` = headers, `tbody` = data, `tfoot` = totals/summary.
- `<caption>` = table title (first child of `<table>`).

### Accessibility
- `scope="col"` on column headers, `scope="row"` on row headers.
- This lets screen readers associate each cell with its header.

### Column widths
```html
<colgroup>
  <col style="width: 200px;" />
  <col style="width: 100px;" />
</colgroup>
```

### Cell spanning
- `colspan="2"` = cell spans 2 columns.
- `rowspan="2"` = cell spans 2 rows.

### Styling
```css
table { border-collapse: collapse; }
th, td { border: 1px solid #ccc; padding: 8px; }
```

### Key rules
- Use tables for DATA, not for page layout.
- Always include `<thead>` and `<tbody>`.
- Use `scope` on `<th>` for accessibility.
- Wrap wide tables in a scrollable container for mobile.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete HTML from scratch below** to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.html` — A 3-column table (Name, Age, City) with header row and 3 data rows.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +-------+-----+-------+
   | Name  | Age | City  |   <- bold header row
   +-------+-----+-------+
   | ...   | ... | ...   |
   | ...   | ... | ...   |   <- 3 data rows
   | ...   | ... | ...   |
   +-------+-----+-------+
   ```
2. `easy/p02-solve.html` — A table with `thead`, `tbody`, and a `<caption>` titled "Student Grades".

   ```
   WHAT IT SHOULD LOOK LIKE:
             Student Grades            <- <caption> sits above table
   +---------+---------+-------+
   | Student | Subject | Grade |   <- <thead> header row
   +---------+---------+-------+
   | ...     | ...     | ...   |   <- <tbody> data rows
   | ...     | ...     | ...   |
   +---------+---------+-------+
   ```
3. `easy/p03-solve.html` — A table with basic CSS borders and padding (inline or `<style>` block).

   ```
   WHAT IT SHOULD LOOK LIKE:
   +-----------+-----------+   <- single merged lines
   |  cell     |  cell     |      (border-collapse: collapse)
   +-----------+-----------+
   |  cell     |  cell     |   <- breathing room around text
   +-----------+-----------+      (padding inside each cell)
   ```

### Medium
4. `medium/p01-solve.html` — A financial table with `thead`, `tbody`, `tfoot` (totals row), and `scope` on all headers.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +---------+--------+---------+
   | Item    | Cost   | Profit  |   <- <thead>
   +---------+--------+---------+
   | ...     | ...    | ...     |   <- <tbody> rows
   | ...     | ...    | ...     |
   +---------+--------+---------+
   | Total   |  ...   |  ...    |   <- <tfoot> renders at the BOTTOM
   +---------+--------+---------+
   ```
5. `medium/p02-solve.html` — A table using `colgroup` to set 3 column widths, with a caption.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +----------------------+---------+---------+
   | wide column (~50%)   |  col 2  |  col 3  |   <- widths set by
   +----------------------+---------+---------+      <colgroup>, not cells
   | ...                  |  ...    |  ...    |
   +----------------------+---------+---------+
   ```
6. `medium/p03-solve.html` — A table with `colspan` (merged header) and `rowspan` (a cell spanning 2 rows).

   ```
   WHAT IT SHOULD LOOK LIKE:
   +-------+-------+-----+
   |       Name    | Age |   <- "Name" stretches over 2 cols (colspan)
   +-------+-------+     |
   | John  | Doe   |     |   <- "Age" stretches down 2 rows (rowspan)
   +-------+-------+-----+
   | Jane  | Smith |  30 |
   +-------+-------+-----+
   ```

### Hard
7. `hard/p01-solve.html` — A full quarterly sales report: caption, colgroup, thead/tbody/tfoot, scope, zebra-striped rows with CSS.

   ```
   WHAT IT SHOULD LOOK LIKE:
   Q1 Sales Report                              <- <caption>
   +---------+-----+-----+-----+--------+
   | Product | Jan | Feb | Mar | Total  |   <- <thead>
   +---------+-----+-----+-----+--------+
   | Widget  |  .. |  .. |  .. |   ..   |   ~~ shaded row (zebra)
   | Gadget  |  .. |  .. |  .. |   ..   |
   | Gizmo   |  .. |  .. |  .. |   ..   |   ~~ shaded row
   +---------+-----+-----+-----+--------+
   | Total   |  .. |  .. |  .. |   ..   |   <- bold <tfoot>
   +---------+-----+-----+-----+--------+
   ```
8. `hard/p02-solve.html` — A complex comparison table with merged headers (colspan), row headers (scope="row"), and styled with borders.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +---------+-------+-----+
   |         |    Plan     |   <- "Plan" spans Basic+Pro (colspan)
   | Feature +-------+-----+
   |         | Basic | Pro |
   +---------+-------+-----+
   | Storage | 10GB  | 1TB |   <- row headers (scope="row")
   | Users   |   1   |  10 |
   | Support | Email | 24/7|
   +---------+-------+-----+
   ```
9. `hard/p03-solve.html` — A responsive table wrapped in a scrollable container, with caption, proper sections, scope, and a `<style>` block for mobile.

   ```
   WHAT IT SHOULD LOOK LIKE:
   DESKTOP (wide):                 MOBILE (narrow):
   +---+---+---+---+---+           +------------+--+
   | a | b | c | d | e |           | a | b | c  | >|  <- wrapper scrolls
   +---+---+---+---+---+           +------------+--+    sideways; table
                                      keeps its shape
   ```

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete HTML from scratch** below the TODO marker.
- Remove the TODO comment when done.
- Open the file in a browser to check it renders correctly.
- When done, tell me and I'll review. Say **"give me next task"** to advance.
