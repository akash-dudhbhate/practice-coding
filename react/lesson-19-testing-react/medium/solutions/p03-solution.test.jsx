// Lesson 19 — Medium P03: Test async UserProfile
import { render, screen, waitFor } from "@testing-library/react";
import UserProfile from "../UserProfile";

afterEach(() => jest.restoreAllMocks());

test("shows loading state", () => {
  jest.spyOn(global, "fetch").mockImplementation(() => new Promise(() => {}));
  render(<UserProfile userId={1} />);
  expect(screen.getByText(/loading/i)).toBeInTheDocument();
});

test("shows user data after fetch", async () => {
  jest.spyOn(global, "fetch").mockResolvedValue({ ok: true, json: async () => ({ id: 1, name: "Alice" }) });
  render(<UserProfile userId={1} />);
  await waitFor(() => expect(screen.getByText("Alice")).toBeInTheDocument());
});

test("shows error on fetch failure", async () => {
  jest.spyOn(global, "fetch").mockRejectedValue(new Error("Network error"));
  render(<UserProfile userId={1} />);
  await waitFor(() => expect(screen.getByText(/error/i)).toBeInTheDocument());
});
