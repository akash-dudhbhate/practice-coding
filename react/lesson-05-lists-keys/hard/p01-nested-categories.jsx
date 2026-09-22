/*
LESSON 05 — Lists & Keys
HARD P01 — Nested Category List
============================================
CONCEPT: Objects containing arrays need nested .map(): an outer map for categories, an inner map for items — each level needs its own keys.
PROBLEM: Build a `NestedList` component. Define `categories` where each has `{ id, name, items: [{id, name}] }`. Map categories to a `<div key={cat.id}>` with an `<h3>` and an inner `<ul>` mapping `cat.items` to `<li key={item.id}>`.
TRY THIS: Render `<NestedList />`.
EXPECTED OUTPUT: "Fruits" heading over Apple/Banana and "Vegetables" over Carrot/Spinach.
CHECK: python3 check.py hard/p01
*/
// TODO: write your component from scratch
