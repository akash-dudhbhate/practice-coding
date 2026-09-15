// Lesson 16 — Hard P02: Optimistic updates
import { useState } from "react";
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
function OptimisticTodos() {
  const qc = useQueryClient();
  const [simulateError, setSimulateError] = useState(false);
  const { data: todos = [] } = useQuery({
    queryKey: ["todos-optimistic"],
    queryFn: () => fetch("https://jsonplaceholder.typicode.com/todos?_limit=5").then((r) => r.json()),
  });
  const addMutation = useMutation({
    mutationFn: async (newTodo) => {
      if (simulateError) throw new Error("Simulated error");
      return fetch("https://jsonplaceholder.typicode.com/todos", { method: "POST", body: JSON.stringify(newTodo), headers: { "Content-Type": "application/json" } }).then((r) => r.json());
    },
    onMutate: async (newTodo) => {
      await qc.cancelQueries({ queryKey: ["todos-optimistic"] });
      const prev = qc.getQueryData(["todos-optimistic"]);
      qc.setQueryData(["todos-optimistic"], (old) => [...old, { ...newTodo, id: Date.now() }]);
      return { prev };
    },
    onError: (err, newTodo, context) => qc.setQueryData(["todos-optimistic"], context.prev),
    onSettled: () => qc.invalidateQueries({ queryKey: ["todos-optimistic"] }),
  });
  return (
    <div>
      <label><input type="checkbox" checked={simulateError} onChange={(e) => setSimulateError(e.target.checked)} /> Simulate Error</label>
      <button onClick={() => addMutation.mutate({ title: "New todo", completed: false })}>Add Todo</button>
      <ul>{todos.map((t) => <li key={t.id}>{t.title}</li>)}</ul>
    </div>
  );
}
export default OptimisticTodos;
