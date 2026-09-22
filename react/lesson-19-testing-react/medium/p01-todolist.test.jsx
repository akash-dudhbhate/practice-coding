/*
LESSON 19 — Testing React
MEDIUM P01 — Test a TodoList (Render, Add, Toggle)
============================================
CONCEPT: Multi-step interactions chain fireEvents: `fireEvent.change` types into an input (set `target.value`), `fireEvent.click` presses buttons — then assert the resulting DOM with getByText / toHaveClass.
PROBLEM: For `TodoList` (import "../TodoList") accepting `initialTodos`, write THREE tests: (1) renders "Learn React" from `initialTodos`; (2) typing "New task" into the "Add todo" placeholder input + clicking the add button makes the text appear; (3) clicking an initial "Task" todo gives it the `done` class (`toHaveClass("done")`).
TRY THIS: Run the suite — covers read, create, and update paths.
EXPECTED OUTPUT: 3 passing tests for initial render, add flow, and toggle flow.
CHECK: python3 check.py medium/p01
*/
// TODO: write your test from scratch
