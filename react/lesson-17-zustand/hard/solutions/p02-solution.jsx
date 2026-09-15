// Lesson 17 — Hard P02: Immer middleware for file system
import { create } from "zustand";
import { immer } from "zustand/middleware";
const useFileStore = create(immer((set) => ({
  root: { name: "root", type: "folder", children: [] },
  addFolder: (path, name) => set((state) => {
    state.root.children.push({ name, type: "folder", children: [] });
  }),
  addFile: (name) => set((state) => {
    state.root.children.push({ name, type: "file" });
  }),
  rename: (index, newName) => set((state) => {
    state.root.children[index].name = newName;
  }),
  delete: (index) => set((state) => {
    state.root.children.splice(index, 1);
  }),
})));
function FileManager() {
  const { root, addFolder, addFile, delete: del } = useFileStore();
  return (
    <div>
      <h3>{root.name}</h3>
      <button onClick={() => addFolder("New Folder")}>Add Folder</button>
      <button onClick={() => addFile("New File")}>Add File</button>
      <ul>{root.children.map((c, i) => <li key={i}>{c.type === "folder" ? "📁" : "📄"} {c.name} <button onClick={() => del(i)}>Delete</button></li>)}</ul>
    </div>
  );
}
export default FileManager;
