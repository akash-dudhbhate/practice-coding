// Lesson 19 — Easy P03: Test Button with label prop
import { render, screen } from "@testing-library/react";
import Button from "../Button";

test("renders button with correct label", () => {
  render(<Button label="Submit" />);
  expect(screen.getByRole("button", { name: "Submit" })).toBeInTheDocument();
});

test("renders different label", () => {
  render(<Button label="Cancel" />);
  expect(screen.getByRole("button", { name: "Cancel" })).toBeInTheDocument();
});
