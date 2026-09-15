// Lesson 17 — Medium P03: Switch for day type
function getDayType(day) {
  switch (day.toLowerCase()) {
    case "saturday": case "sunday": return "Weekend";
    case "monday": case "tuesday": case "wednesday":
    case "thursday": case "friday": return "Weekday";
    default: return "Invalid";
  }
}
console.log(getDayType("Saturday")); // Weekend
console.log(getDayType("Monday"));   // Weekday
console.log(getDayType("Funday"));   // Invalid
