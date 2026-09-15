// Lesson 19 — Medium P01: Test TodoList
import { render, screen, fireEvent } from "@testing-library/react";
import TodoList from "../TodoList";

test("renders initial todos", () => {
  render(<TodoList initialTodos={[{ id: 1, text: "Learn React", done: false }]} />);
  expect(screen.getByText("Learn React")).toBeInTheDocument();
});

test("adds a new todo", () => {
  render(<TodoList />);
  fireEvent.change(screen.getByPlaceholderText("Add todo"), { target: { value: "New task" } });
  fireEvent.click(screen.getByRole("button", { name: /add/i }));
  expect(screen.getByText("New task")).toBeInTheDocument();
});

test("toggles todo done state", () => {
  render(<TodoList initialTodos={[{ id: 1, text: "Task", done: false }]} />);
  const todo = screen.getByText("Task");
  fireEvent.click(todo);
  expect(todo).toHaveClass("done");
});
