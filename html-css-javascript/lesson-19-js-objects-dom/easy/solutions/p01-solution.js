// Lesson 19 — Easy P01: Object with method using this
const car = {
  brand: "Toyota",
  model: "Camry",
  year: 2024,
  getInfo() {
    return `${this.brand} ${this.model} (${this.year})`;
  },
};
console.log(car.getInfo()); // Toyota Camry (2024)
