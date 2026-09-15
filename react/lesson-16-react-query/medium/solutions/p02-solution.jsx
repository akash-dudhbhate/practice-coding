// Lesson 16 — Medium P02: Todo app with React Query
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { useState } from "react";
function TodoApp() {
  const qc = useQueryClient();
  const [input, setInput] = useState("");
  const { data: todos = [], isLoading } = useQuery({
    queryKey: ["todos"],
    queryFn: () => fetch("https://jsonplaceholder.typicode.com/todos?_limit=5").then((r) => r.json()),
  });
  const addMutation = useMutation({
    mutationFn: (todo) => fetch("https://jsonplaceholder.typicode.com/todos", { method: "POST", body: JSON.stringify(todo), headers: { "Content-Type": "application/json" } }).then((r) => r.json()),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["todos"] }),
  });
  const toggleMutation = useMutation({
    mutationFn: (id) => fetch(`https://jsonplaceholder.typicode.com/todos/${id}`, { method: "PATCH", body: JSON.stringify({ completed: true }), headers: { "Content-Type": "application/json" } }).then((r) => r.json()),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["todos"] }),
  });
  const deleteMutation = useMutation({
    mutationFn: (id) => fetch(`https://jsonplaceholder.typicode.com/todos/${id}`, { method: "DELETE" }).then((r) => r.json()),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["todos"] }),
  });
  if (isLoading) return <p>Loading...</p>;
  return (
    <div>
      <input value={input} onChange={(e) => setInput(e.target.value)} placeholder="Add todo" />
      <button onClick={() => { addMutation.mutate({ title: input, completed: false }); setInput(""); }}>Add</button>
      <ul>{todos.map((t) => <li key={t.id}>{t.completed ? "✓" : ""} {t.title} <button onClick={() => toggleMutation.mutate(t.id)}>Toggle</button> <button onClick={() => deleteMutation.mutate(t.id)}>Delete</button></li>)}</ul>
    </div>
  );
}
export default TodoApp;
