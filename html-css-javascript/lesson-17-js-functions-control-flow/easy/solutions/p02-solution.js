// Lesson 17 — Easy P02: Destructuring in params
function formatName({ first, last }) {
  return `${first} ${last.toUpperCase()}`;
}
console.log(formatName({ first: "Akash", last: "dev" })); // "Akash DEV"
