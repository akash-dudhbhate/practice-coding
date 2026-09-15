// Lesson 19 — Medium P02: Test LoginForm
import { render, screen, fireEvent } from "@testing-library/react";
import LoginForm from "../LoginForm";

test("submit is disabled when fields are empty", () => {
  render(<LoginForm onSubmit={jest.fn()} />);
  expect(screen.getByRole("button", { name: /submit/i })).toBeDisabled();
});

test("submitting with valid data calls onSubmit", () => {
  const onSubmit = jest.fn();
  render(<LoginForm onSubmit={onSubmit} />);
  fireEvent.change(screen.getByPlaceholderText("Email"), { target: { value: "test@test.com" } });
  fireEvent.change(screen.getByPlaceholderText("Password"), { target: { value: "password123" } });
  fireEvent.click(screen.getByRole("button", { name: /submit/i }));
  expect(onSubmit).toHaveBeenCalledWith({ email: "test@test.com", password: "password123" });
});

test("shows error for invalid email", () => {
  render(<LoginForm onSubmit={jest.fn()} />);
  fireEvent.change(screen.getByPlaceholderText("Email"), { target: { value: "invalid" } });
  fireEvent.change(screen.getByPlaceholderText("Password"), { target: { value: "password123" } });
  fireEvent.click(screen.getByRole("button", { name: /submit/i }));
  expect(screen.getByText(/invalid email/i)).toBeInTheDocument();
});
