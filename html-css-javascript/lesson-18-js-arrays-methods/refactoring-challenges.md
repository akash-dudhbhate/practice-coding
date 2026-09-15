# Lesson 18 — Refactoring Challenges

## Refactor 01 (Easy): No Error Handling
### Before
```javascript
const data = JSON.parse(str);
```
### After
```javascript
try { const data = JSON.parse(str); }
catch (e) { console.error("Invalid JSON"); }
```

## Refactor 02 (Medium): Generic Catch
### Before
```javascript
try { ... } catch (e) { console.log("Error"); }
```
### After
```javascript
try { ... } catch (e) {
  if (e instanceof SyntaxError) console.error("Parse error");
  else throw e;
}
```

## Refactor 03 (Hard): Repeated Try/Catch
### Before
```javascript
function safeA() { try { return a(); } catch { return null; } }
function safeB() { try { return b(); } catch { return null; } }
```
### After
```javascript
function safe(fn, fallback = null) {
  try { return fn(); } catch { return fallback; }
}
const safeA = () => safe(a);
```
