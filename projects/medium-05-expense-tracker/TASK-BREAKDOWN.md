# Expense Tracker (React) — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
medium-05-expense-tracker/
├── src/App.jsx, src/components/Dashboard.jsx, src/components/AddExpense.jsx, src/components/ExpenseList.jsx, src/components/Charts.jsx, src/stores/expenses.js, src/hooks/useExpenses.js
└── README.md
```

---

## Implementation Steps

### Step 1: Expenses Store

Zustand: expenses, addExpense, deleteExpense, categories. localStorage.

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: AddExpense Form

Amount, category (select), date, description. Validation. Submit.

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: ExpenseList

Table/list of expenses. Sort by date/amount. Filter by category. Delete.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: Dashboard

Total balance, income vs expenses, recent transactions. Summary cards.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: Charts

Pie chart (by category), bar chart (by month). Use recharts or chart.js.

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: Categories

Custom categories. Color per category. Category management.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: Budget

Set monthly budget per category. Show progress bar. Alert when over budget.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: Responsive

Dashboard cards stack on mobile. Charts resize. Table → cards on mobile.

**Checkpoint:** Step 8 is complete when the described functionality works.

---

## Final Checklist

- [ ] Add expense with category
- [ ] Expense list with filters
- [ ] Dashboard with summary
- [ ] Pie chart by category
- [ ] Bar chart by month
- [ ] Budget tracking with alerts
- [ ] localStorage persistence
- [ ] Responsive design

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
5. **Hardcoding values** — use environment variables for API keys, URLs, and configuration.
