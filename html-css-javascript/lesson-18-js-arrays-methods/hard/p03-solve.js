/**
LESSON 18 — JavaScript Arrays & Methods
========================================

PROBLEM: Pagination (Hard)
Write createPagination(items, page, pageSize) returning full info.

TRY THIS:
  - totalPages = Math.ceil(items.length / pageSize).
  - start = (page - 1) * pageSize; items = slice(start, start+pageSize).
  - Return { items, currentPage, totalPages, hasNext, hasPrev }.

EXPECTED OUTPUT:
  createPagination(1..25 array, 2, 10) ===
    { items: [11..20], currentPage: 2, totalPages: 3,
      hasNext: true, hasPrev: true }

TEST: node hard/p03-solve.js

CHECK: python3 check.py hard/p03
*/

// TODO: Write your complete solution from scratch below.
