# Lesson 18 — Intuition Checks

## Check 01: What is SSR?
<details><summary>Answer</summary>
Server-Side Rendering — HTML generated on server, sent to browser. Better SEO, faster first paint. Client then "hydrates" into interactive Vue app. Quasar: `quasar build -m ssr`.
</details>

## Check 02: process.env.CLIENT
```javascript
if (process.env.CLIENT) { /* browser only */ }
if (process.env.SERVER) { /* server only */ }
```
<details><summary>Answer</summary>
Quasar provides these flags. Use to guard browser-only APIs (window, document, localStorage). Code is tree-shaken for each build.
</details>

## Check 03: onMounted for browser code
```javascript
onMounted(() => {
  // runs only in browser, after hydration
  localStorage.getItem("key");
});
```
<details><summary>Answer</summary>
`onMounted` runs only in browser. Safe for browser APIs. `setup()` runs on both server and client.
</details>

## Check 04: PreFetch
```javascript
// routes.js
{
  path: "/",
  component: () => import("layouts/MainLayout"),
  preFetch: async ({ store, currentRoute }) => {
    await store.dispatch("fetchData");
  }
}
```
<details><summary>Answer</summary>
Fetch data on server before rendering. Data available in HTML immediately. Better SEO and UX.
</details>

## Check 05: Hydration
<details><summary>Answer</summary>
Server sends static HTML. Browser loads JS, Vue "hydrates" HTML into interactive app. If server and client render differently → hydration mismatch warning.
</details>
