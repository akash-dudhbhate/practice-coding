// Lesson 19 — Medium P01: Merge configs with spread
function mergeConfigs(defaults, userPrefs) {
  return { ...defaults, ...userPrefs };
}
const defaults = { theme: "light", fontSize: 14, lang: "en" };
const userPrefs = { theme: "dark", fontSize: 16 };
console.log(mergeConfigs(defaults, userPrefs));
// { theme: "dark", fontSize: 16, lang: "en" }
