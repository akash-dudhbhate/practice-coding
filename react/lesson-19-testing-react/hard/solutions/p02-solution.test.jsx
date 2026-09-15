// Lesson 19 — Hard P02: Test useFetch hook with renderHook
import { renderHook, waitFor } from "@testing-library/react";
import { useFetch } from "../useFetch";

afterEach(() => jest.restoreAllMocks());

test("initial loading state", () => {
  jest.spyOn(global, "fetch").mockImplementation(() => new Promise(() => {}));
  const { result } = renderHook(() => useFetch("https://api.example.com"));
  expect(result.current.loading).toBe(true);
  expect(result.current.data).toBe(null);
});

test("data is set after fetch", async () => {
  jest.spyOn(global, "fetch").mockResolvedValue({ ok: true, json: async () => ({ name: "Alice" }) });
  const { result } = renderHook(() => useFetch("https://api.example.com"));
  await waitFor(() => expect(result.current.loading).toBe(false));
  expect(result.current.data).toEqual({ name: "Alice" });
});

test("error state on fetch failure", async () => {
  jest.spyOn(global, "fetch").mockRejectedValue(new Error("Failed"));
  const { result } = renderHook(() => useFetch("https://api.example.com"));
  await waitFor(() => expect(result.current.loading).toBe(false));
  expect(result.current.error).toBe("Failed");
});

test("refetch works", async () => {
  jest.spyOn(global, "fetch").mockResolvedValue({ ok: true, json: async () => ({ name: "Bob" }) });
  const { result, rerender } = renderHook(({ url }) => useFetch(url), { initialProps: { url: "https://api.example.com" } });
  await waitFor(() => expect(result.current.data).toEqual({ name: "Bob" }));
  jest.spyOn(global, "fetch").mockResolvedValue({ ok: true, json: async () => ({ name: "Charlie" }) });
  rerender({ url: "https://api.example.com/v2" });
  await waitFor(() => expect(result.current.data).toEqual({ name: "Charlie" }));
});
