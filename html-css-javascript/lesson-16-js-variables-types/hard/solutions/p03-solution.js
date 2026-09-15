// Lesson 16 — Hard P03: Analyze string
function analyzeString(str) {
  const reversed = str.split("").reverse().join("");
  const words = str.trim().split(/\s+/);
  const charCount = str.replace(/\s/g, "").length;
  const freq = {};
  for (const ch of str.replace(/\s/g, "")) freq[ch] = (freq[ch] || 0) + 1;
  const mostFreq = Object.entries(freq).sort((a, b) => b[1] - a[1])[0]?.[0];
  const cleanStr = str.toLowerCase().replace(/[^a-z0-9]/g, "");
  return {
    original: str,
    length: str.length,
    wordCount: words.length,
    charCount,
    reversed,
    isPalindrome: cleanStr === cleanStr.split("").reverse().join(""),
    mostFrequentChar: mostFreq,
    wordList: words,
  };
}
console.log(analyzeString("race car"));
