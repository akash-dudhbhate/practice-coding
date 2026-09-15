// Lesson 16 — Medium P01: Format price
function formatPrice(amount, currency) {
  const symbols = { USD: "$", EUR: "€", GBP: "£", INR: "₹" };
  const symbol = symbols[currency] || "";
  return `${symbol}${Number(amount).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`;
}
console.log(formatPrice(1234.5, "USD")); // $1,234.50
console.log(formatPrice(99.999, "EUR")); // €100.00
