// Lesson 18 — Hard P03: Pagination
function createPagination(items, page, pageSize) {
  const totalPages = Math.ceil(items.length / pageSize);
  const start = (page - 1) * pageSize;
  const pageItems = items.slice(start, start + pageSize);
  return {
    items: pageItems,
    currentPage: page,
    totalPages,
    hasNext: page < totalPages,
    hasPrev: page > 1,
  };
}
const data = Array.from({ length: 25 }, (_, i) => i + 1);
console.log(createPagination(data, 2, 10));
// { items: [11..20], currentPage: 2, totalPages: 3, hasNext: true, hasPrev: true }
