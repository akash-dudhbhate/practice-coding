// Lesson 18 — Easy P01: Card with Tailwind
function Card() {
  return (
    <div className="bg-white rounded-lg shadow-md p-6 max-w-sm">
      <h3 className="text-lg font-bold mb-2">Card Title</h3>
      <p className="text-gray-600 mb-4">This is a card description using Tailwind CSS.</p>
      <button className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Click Me</button>
    </div>
  );
}
export default Card;
