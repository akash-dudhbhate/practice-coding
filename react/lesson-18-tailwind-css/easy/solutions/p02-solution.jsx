// Lesson 18 — Easy P02: Responsive grid
function ResponsiveGrid() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 p-4">
      {[1, 2, 3, 4, 5, 6].map((n) => (
        <div key={n} className={`bg-${n % 2 === 0 ? "blue" : "purple"}-500 text-white p-8 rounded-lg text-center`}>
          Box {n}
        </div>
      ))}
    </div>
  );
}
export default ResponsiveGrid;
