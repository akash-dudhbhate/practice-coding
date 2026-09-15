# Quasar Framework — Curriculum

Master the Quasar Framework (Vue 3 based) for building cross-platform apps (SPA, PWA, SSR, mobile, desktop) from a single codebase.

## Prerequisites
Comfortable with HTML, CSS, JavaScript, and ideally Vue.js basics.

## Setup (Docker)

A `Dockerfile` is provided in this folder to install all Quasar dependencies
(Node.js, Quasar CLI) in an isolated container.

### Build the image
```bash
cd quasar
docker build -t quasar-dev .
```

### Run a Quasar dev server inside the container
```bash
docker run -it --rm -p 8080:8080 -v "$(pwd)":/app quasar-dev
```
Then open http://localhost:8080 in your browser.

### Create a new Quasar project (inside the container)
```bash
quasar create my-app
cd my-app
quasar dev
```

## Progress Tracker

| Lesson | Topic | Status | Completed On |
|--------|-------|--------|--------------|
| 01 | Quasar basics: layout, pages & components | Not started | — |

> New lessons are added as you complete tasks. Say **"give me next task"** to advance.

## Lesson roadmap (planned)

1. Quasar basics: layout, pages & components
2. Quasar components (QBtn, QInput, QCard, QTable)
3. Routing & layouts (QLayout, QDrawer, QHeader)
4. State management (Pinia)
5. Forms & validation
6. API calls & Axios
7. Theming & dark mode
8. PWA & mobile build (Capacitor)
9. SSR mode
10. Mini-project: full Quasar app

(These are planned — you unlock them one at a time by completing tasks.)
