/**
LESSON 19 — JavaScript Objects & DOM
=====================================

PROBLEM: Merge Configs (Medium)
Write mergeConfigs(defaults, userPrefs) with spread — prefs win.

TRY THIS:
  - return { ...defaults, ...userPrefs }.
  - Test with defaults {theme, fontSize, lang} and prefs overriding
    two of them.

EXPECTED OUTPUT:
  mergeConfigs({theme:"light",fontSize:14,lang:"en"},
               {theme:"dark",fontSize:16})
    -> { theme: "dark", fontSize: 16, lang: "en" }

TEST: node medium/p01-solve.js

CHECK: python3 check.py medium/p01
*/

// TODO: Write your complete solution from scratch below.
