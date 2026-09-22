/*
LESSON 04 — Conditional Rendering
HARD P03 — Permission-Based Dashboard
============================================
CONCEPT: Role checks compose: `role === "admin"` shows admin-only UI while `(admin || editor) &&` covers shared UI — stack several `&&` blocks for layered permissions.
PROBLEM: Build a `Dashboard` component with `role` state ("viewer" default) driven by a `<select>` (admin/editor/viewer). Everyone sees "View Content"; editors+admins see "Edit Tools"; only admins see the "Admin Panel" block. Show the current role in the heading.
TRY THIS: Render `<Dashboard />` and switch the select through all three roles.
EXPECTED OUTPUT: Viewer sees only content, editor gains Edit Tools, admin gains both Edit Tools and the Admin Panel.
CHECK: python3 check.py hard/p03
*/
// TODO: write your component from scratch
