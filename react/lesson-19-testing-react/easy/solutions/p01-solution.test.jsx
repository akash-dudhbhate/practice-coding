// Lesson 19 — Easy P01: Test Greeting component
import { render, screen } from "@testing-library/react";
import Greeting from "../Greeting";

test("renders greeting with name", () => {
  render(<Greeting name="Akash" />);
  expect(screen.getByText("Hello, Akash!")).toBeInTheDocument();
});
