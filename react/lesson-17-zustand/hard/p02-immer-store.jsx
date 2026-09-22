/*
LESSON 17 — Zustand
HARD P02 — Immer Middleware (Nested State)
============================================
CONCEPT: The `immer` middleware wraps `set` so you write MUTATING code (`state.root.children.push(...)`) and Immer produces the immutable update for you — no deep spread gymnastics on nested trees.
PROBLEM: Create `useFileStore = create(immer((set) => ({root: {name:"root", type:"folder", children: []}, ...})))` with actions `addFolder(path, name)` (push a folder), `addFile(name)` (push a file), `rename(index, newName)` (assign `.name`), `delete(index)` (`splice`) — all via direct mutation. Build `FileManager` rendering the root name, Add Folder / Add File buttons, and a `<ul>` of children (📁/📄 icon by type, Delete per row).
TRY THIS: Render `<FileManager />`, add a folder and a file, rename one via `rename`, delete one.
EXPECTED OUTPUT: Nested children mutate cleanly with push/splice/assign — no spread operators needed.
CHECK: python3 check.py hard/p02
*/
// TODO: write your component from scratch
