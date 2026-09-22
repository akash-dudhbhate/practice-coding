/**
LESSON 16 — JavaScript Variables & Types
=========================================

PROBLEM: Format a Price (Medium)
Write formatPrice(amount, currency) -> "$1,234.50" style strings.

TRY THIS:
  - Map currency codes to symbols ({ USD: "$", EUR: "€", ... }).
  - Number(amount).toFixed(2), then insert thousands separators
    (regex or toLocaleString-style logic).
  - Template literal for the final string.

EXPECTED OUTPUT:
  formatPrice(1234.5, "USD") === "$1,234.50"
  formatPrice(99.999, "EUR") === "€100.00"

TEST: node medium/p01-solve.js

CHECK: python3 check.py medium/p01
*/

// TODO: Write your complete solution from scratch below.
