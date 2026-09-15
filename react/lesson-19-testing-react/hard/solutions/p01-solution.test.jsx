// Lesson 19 — Hard P01: Test Modal component
import { render, screen, fireEvent } from "@testing-library/react";
import Modal from "../Modal";

test("does not render when closed", () => {
  render(<Modal open={false} onClose={jest.fn()}><p>Content</p></Modal>);
  expect(screen.queryByText("Content")).not.toBeInTheDocument();
});

test("renders when open", () => {
  render(<Modal open={true} onClose={jest.fn()}><p>Content</p></Modal>);
  expect(screen.getByText("Content")).toBeInTheDocument();
});

test("close button works", () => {
  const onClose = jest.fn();
  render(<Modal open={true} onClose={onClose}><p>Content</p></Modal>);
  fireEvent.click(screen.getByRole("button", { name: /close/i }));
  expect(onClose).toHaveBeenCalled();
});

test("overlay click closes", () => {
  const onClose = jest.fn();
  render(<Modal open={true} onClose={onClose}><p>Content</p></Modal>);
  fireEvent.click(screen.getByTestId("modal-overlay"));
  expect(onClose).toHaveBeenCalled();
});

test("Escape key closes", () => {
  const onClose = jest.fn();
  render(<Modal open={true} onClose={onClose}><p>Content</p></Modal>);
  fireEvent.keyDown(document, { key: "Escape" });
  expect(onClose).toHaveBeenCalled();
});

test("body scroll is locked when open", () => {
  render(<Modal open={true} onClose={jest.fn()}><p>Content</p></Modal>);
  expect(document.body.style.overflow).toBe("hidden");
});
