// Lesson 19 — Easy P02: Test Counter component
import { render, screen, fireEvent } from "@testing-library/react";
import Counter from "../Counter";

test("initial count is 0", () => {
  render(<Counter />);
  expect(screen.getByText(/count: 0/i)).toBeInTheDocument();
});

test("increments count on button click", () => {
  render(<Counter />);
  const button = screen.getByRole("button", { name: /increment/i });
  fireEvent.click(button);
  expect(screen.getByText(/count: 1/i)).toBeInTheDocument();
});
