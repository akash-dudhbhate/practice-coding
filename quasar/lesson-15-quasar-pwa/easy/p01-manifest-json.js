/**
 * LESSON 15 — Quasar PWA
 * EASY P01 — manifest.json
 * ============================================
 * CONCEPT: The web app manifest tells the OS how to install your PWA:
 * name/short_name for the title bar and icon label, display: standalone
 * for an app-like window, theme/background colors, and icons for the home
 * screen. (Write the JSON object directly in this file.)
 *
 * PROBLEM: Write a manifest object with name, short_name, description,
 * start_url '/', display 'standalone', theme_color, background_color, and
 * an icons array with at least 128x128 and 512x512 entries (src, sizes,
 * type, purpose).
 *
 * TRY THIS: { "name": "My Quasar PWA App", "short_name": "QuasarApp",
 *   "display": "standalone", "icons": [{ "src": "icons/icon-128.png",
 *   "sizes": "128x128", "type": "image/png" }, ...] }
 *
 * EXPECTED OUTPUT: A valid manifest that a browser would accept for "Add to
 * Home Screen" — this file's content is copied to manifest.json.
 *
 * CHECK: python3 check.py easy/p01
 */
// TODO: write your manifest object below (plain JSON)
