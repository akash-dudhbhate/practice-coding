# Full Mastery Roadmap — 100 Lessons + 34 Sellable Projects

> **Goal:** Go from zero to job-ready in UI/Frontend, Backend, AI/ML, and cross-platform apps.
> Each lesson is small and incremental — one concept at a time, no skipping.
> Projects between lessons are **sellable** (freelance/portfolio pieces).

> **See also:** [STUDY-SCHEDULE.md](STUDY-SCHEDULE.md) — 12-week day-by-day study plan with milestones.

## How the roadmap is structured

- **5 subjects × 20 lessons = 100 lessons**
- Each lesson: `concepts.md` (WHY/WHERE/WHAT-GOES-WRONG) + `task-explanation.md` + `coding-check.md` + 9 problems (3 easy, 3 medium, 3 hard)
- **Reference solutions** in `solutions/` subdirectory per difficulty level
- **34 sellable projects** (19 mini, 10 medium, 5 capstone) — each with README + TASK-BREAKDOWN.md
- **900 practice problems** total (9 per lesson × 100 lessons)

## What's included per lesson

```
lesson-XX-name/
├── concepts.md          # Detailed explanations (WHAT/WHY/WHERE/WHAT-GOES-WRONG)
├── task-explanation.md  # Lesson content + 9 problem descriptions
├── coding-check.md      # Verification checklist for each problem
├── easy/
│   ├── p01-solve.*      # Problem with TODO (you write the solution)
│   ├── p02-solve.*
│   ├── p03-solve.*
│   └── solutions/       # Reference solutions (check your work)
├── medium/
│   ├── p01-solve.*
│   ├── p02-solve.*
│   ├── p03-solve.*
│   └── solutions/
└── hard/
    ├── p01-solve.*
    ├── p02-solve.*
    ├── p03-solve.*
    └── solutions/
```

## What's included per project

```
projects/XX-name/
├── README.md            # Project brief, requirements, sellable pitch
└── TASK-BREAKDOWN.md    # Step-by-step implementation guide with checkpoints
```

## Suggested order

Follow subjects in parallel or sequentially. If sequential:
1. HTML/CSS/JS → 2. React → 3. Python → 4. AI/ML → 5. Quasar

> **For a day-by-day plan**, see [STUDY-SCHEDULE.md](STUDY-SCHEDULE.md) — includes 12-week, 8-week accelerated, and 20-week relaxed schedules.

---

# 1. HTML / CSS / JavaScript (20 Lessons + 6 Projects)

## Phase 1: HTML Foundations (Lessons 1–5)

| # | Lesson | Key Concepts |
|---|--------|-------------|
| 1 | HTML Structure & Semantic Tags | elements, tags, nesting, semantic HTML5, accessibility |
| 2 | HTML Forms & Input Types | form, input types, label, select, textarea, validation |
| 3 | HTML Tables & Data Display | table, thead, tbody, tr, th, td, caption, colgroup |
| 4 | HTML Media & Embedding | img, video, audio, iframe, figure, picture, srcset |
| 5 | HTML Accessibility Deep Dive | ARIA, landmarks, alt text, keyboard nav, screen readers |

**Mini Project 1:** Accessible Contact Form Page ($50–100)
> Build a complete, accessible contact form with validation, labels, ARIA, and semantic structure.

## Phase 2: CSS Foundations (Lessons 6–10)

| # | Lesson | Key Concepts |
|---|--------|-------------|
| 6 | CSS Selectors & Specificity | element/class/id, combinators, specificity, cascade |
| 7 | Box Model & Spacing | margin, padding, border, box-sizing, width/height |
| 8 | CSS Text & Typography | font-family, font-size, line-height, text-align, color |
| 9 | CSS Colors & Backgrounds | hex, rgb, hsl, gradients, background-image, opacity |
| 10 | CSS Flexbox Layout | flex-direction, justify-content, align-items, flex-wrap, gap |

**Mini Project 2:** Landing Page with Flexbox ($100–200)
> Build a responsive landing page with hero, features grid, and footer using Flexbox.

**Medium Project 1:** Pricing Page with 3 Tiers ($200–400)
> Build a polished pricing page with toggle (monthly/yearly), 3 tiers, feature lists, responsive.

## Phase 3: CSS Advanced (Lessons 11–15)

| # | Lesson | Key Concepts |
|---|--------|-------------|
| 11 | CSS Grid Layout | grid-template, grid-area, repeat, minmax, auto-fit |
| 12 | CSS Responsive Design | media queries, breakpoints, mobile-first, viewport |
| 13 | CSS Animations & Transitions | transition, @keyframes, transform, animation properties |
| 14 | CSS Variables & Custom Properties | --var, :root, var(), theme switching, dark mode |
| 15 | CSS Pseudo-classes & Pseudo-elements | :hover, :focus, :nth-child, ::before, ::after, ::placeholder |

**Mini Project 3:** Responsive Image Gallery ($100–200)
> Grid-based gallery with hover effects, lightbox modal, responsive breakpoints.

## Phase 4: JavaScript Foundations (Lessons 16–20)

| # | Lesson | Key Concepts |
|---|--------|-------------|
| 16 | JS Variables, Types & Operators | let/const, number/string/boolean, arithmetic, comparison |
| 17 | JS Functions & Control Flow | function, arrow function, if/else, switch, ternary |
| 18 | JS Arrays & Array Methods | push, pop, map, filter, reduce, forEach, find, sort |
| 19 | JS Objects & DOM Manipulation | object literals, document.querySelector, innerHTML, classList |
| 20 | JS Events & Event Handling | addEventListener, click, submit, input, event object, delegation |

**Mini Project 4:** Interactive Todo List (vanilla JS) ($100–200)

**Medium Project 2:** Dynamic Calculator App ($200–400)
> Full calculator with keyboard support, history, and theme toggle.

**Capstone Project 1:** Personal Portfolio Website ($500–1000)
> Multi-section portfolio: hero, about, projects grid, contact form, dark mode, responsive, animated.

---

# 2. React (20 Lessons + 6 Projects)

## Phase 1: React Core (Lessons 1–5)

| # | Lesson | Key Concepts |
|---|--------|-------------|
| 1 | Components, JSX & Props | function components, JSX, props, children, fragments |
| 2 | State & useState | useState hook, state updates, immutable updates, batching |
| 3 | Event Handling in React | onClick, onChange, onSubmit, synthetic events, preventDefault |
| 4 | Conditional Rendering | &&, ternary, early return, loading/error states |
| 5 | Lists & Keys | .map(), key prop, dynamic lists, index as key pitfalls |

**Mini Project 5:** React Todo App ($100–200)

## Phase 2: React Hooks (Lessons 6–10)

| # | Lesson | Key Concepts |
|---|--------|-------------|
| 6 | useEffect & Side Effects | useEffect, dependency array, cleanup, fetch on mount |
| 7 | Forms & Controlled Components | controlled inputs, form state, validation, submit handling |
| 8 | useRef & DOM Access | useRef, accessing DOM, persisting values, timers |
| 9 | useMemo & useCallback | memoization, when to use, performance, dependency pitfalls |
| 10 | Custom Hooks | useFetch, useLocalStorage, useToggle, composing hooks |

**Mini Project 6:** Movie Search App ($100–200)
> Search movies via OMDB API, display results grid, loading states, debounced search.

**Medium Project 3:** Recipe Finder with Filters ($200–500)
> Search recipes, filter by cuisine/diet/intolerances, favorites with localStorage.

## Phase 3: React Architecture (Lessons 11–15)

| # | Lesson | Key Concepts |
|---|--------|-------------|
| 11 | Context API | createContext, useContext, provider/consumer, theme context |
| 12 | useReducer & Complex State | reducer, actions, dispatch, state machines |
| 13 | React Router | routes, Link, useParams, useNavigate, nested routes, layout |
| 14 | Error Boundaries & Suspense | ErrorBoundary, Suspense, lazy loading, fallbacks |
| 15 | Portals & Modals | createPortal, modal pattern, focus trapping, accessibility |

**Mini Project 7:** Multi-Page Blog ($100–200)

## Phase 4: React Production (Lessons 16–20)

| # | Lesson | Key Concepts |
|---|--------|-------------|
| 16 | API Integration with React Query | useQuery, useMutation, caching, invalidation, loading states |
| 17 | State Management with Zustand | store, actions, selectors, middleware, persistence |
| 18 | Styling: Tailwind CSS | utility classes, responsive, dark mode, composition, @apply |
| 19 | Testing React Components | React Testing Library, render, fireEvent, getByRole, assertions |
| 20 | React Performance & Profiling | React.memo, code splitting, lazy loading, profiler, bundle size |

**Mini Project 8:** E-commerce Product Page ($100–200)

**Medium Project 4:** Full E-commerce Store Front ($300–500)
> Product listing, cart, checkout flow, search, filters, localStorage persistence.

**Capstone Project 2:** Social Media Dashboard ($500–1500)
> Feed, post creation, likes, comments, user profiles, search, dark mode, responsive, tested.

---

# 3. Python (20 Lessons + 6 Projects)

## Phase 1: Python Basics (Lessons 1–5)

| # | Lesson | Key Concepts |
|---|--------|-------------|
| 1 | Variables, Types & Functions | variables, int/float/str/bool, def, return, parameters |
| 2 | Strings & String Methods | indexing, slicing, .upper/.lower/.strip/.split/.join, f-strings |
| 3 | Lists & Tuples | indexing, append, insert, pop, sort, reverse, list vs tuple |
| 4 | Dictionaries & Sets | key-value, .get/.keys/.values/.items, set operations, frozenset |
| 5 | Control Flow & Loops | if/elif/else, for, while, break, continue, range, enumerate |

**Mini Project 9:** CLI Contact Book ($50–100)
> Add, search, delete contacts in a CLI app using lists and dicts.

## Phase 2: Python Intermediate (Lessons 6–10)

| # | Lesson | Key Concepts |
|---|--------|-------------|
| 6 | Functions Deep Dive | *args, **kwargs, default params, lambda, scope, closures |
| 7 | File I/O & Error Handling | open, read/write, with, try/except/finally, custom exceptions |
| 8 | List Comprehensions & Generators | [x for x in], generator expressions, yield, itertools basics |
| 9 | OOP Basics | class, __init__, self, instance methods, class vs instance vars |
| 10 | OOP Advanced | inheritance, super(), polymorphism, @property, dunder methods |

**Mini Project 10:** File Organizer Script ($50–150)
> Script that organizes files in a directory by extension. Sellable as a utility.

**Medium Project 5:** Expense Tracker CLI ($200–400)
> Track expenses by category, generate monthly reports, save/load from JSON.

## Phase 3: Python Advanced (Lessons 11–15)

| # | Lesson | Key Concepts |
|---|--------|-------------|
| 11 | Modules & Packages | import, from, __init__.py, pip, virtualenv, requirements.txt |
| 12 | Decorators | function decorators, @wraps, class decorators, practical patterns |
| 13 | Iterators & Generators | __iter__, __next__, yield, generator pipelines, memory efficiency |
| 14 | Async/Await & Concurrency | async, await, asyncio, aiohttp, concurrent.futures, threading |
| 15 | Testing with pytest | test functions, fixtures, parametrize, coverage, mocks |

**Mini Project 11:** Web Scraper with Async ($100–200)

## Phase 4: Python Production (Lessons 16–20)

| # | Lesson | Key Concepts |
|---|--------|-------------|
| 16 | Working with REST APIs | requests, GET/POST/PUT/DELETE, headers, auth, JSON handling |
| 17 | Database Basics (SQLite) | sqlite3, CREATE/INSERT/SELECT/UPDATE/DELETE, ORM intro |
| 18 | Flask Web Server | routes, templates, request/response, Jinja2, session |
| 19 | FastAPI REST Server | FastAPI, Pydantic models, dependency injection, auto docs |
| 20 | Data Processing with Pandas | DataFrame, read_csv, filter, groupby, merge, export |

**Mini Project 12:** REST API with FastAPI ($100–200)

**Medium Project 6:** Full CRUD API with Auth ($300–500)
> FastAPI with SQLite, JWT auth, CRUD operations, validation, error handling.

**Capstone Project 3:** Full-Stack Task Management API ($500–1500)
> FastAPI + SQLite + JWT auth + tests + Docker + documentation. Production-ready.

---

# 4. AI / ML (14 Levels + 14 Projects + Capstone)

**NEW: Level-based structure.** Each `level-XX-*` has 9 auto-checked
problems (3 easy + 3 medium + 3 hard), a mini-project in `project/`,
and a `check.py`. The capstone `CAPSTONE/` grows one milestone per
level into a complete AI system ("DataMind").

## Phase 1: Foundations (Levels 00–03)

| # | Level | Key Concepts |
|---|-------|-------------|
| 00 | Setup & Math | env check, dot product, normalize, distance, gradient intuition |
| 01 | ML Foundations | supervised/unsupervised, features/labels, train/test, bias-variance |
| 02 | Python for ML | NumPy arrays, Pandas DataFrames, sklearn pipelines, data leakage |
| 03 | Visualization | matplotlib, seaborn, histograms, scatter, correlation, dashboards |

## Phase 2: Supervised Learning (Levels 04–05)

| # | Level | Key Concepts |
|---|-------|-------------|
| 04 | Supervised ML | linear/logistic regression, decision trees, RF, SVM, KNN, gradient descent |
| 05 | Model Evaluation | metrics, confusion matrix, k-fold CV, ROC-AUC, grid search, nested CV |

## Phase 3: Advanced ML (Levels 06–07)

| # | Level | Key Concepts |
|---|-------|-------------|
| 06 | Advanced ML | polynomial features, encoding, scaling, imbalance, class_weight, custom transformers |
| 07 | Unsupervised | K-Means, elbow, silhouette, DBSCAN, hierarchical, PCA, segmentation, anomalies |

## Phase 4: Deep Learning (Levels 08–09)

| # | Level | Key Concepts |
|---|-------|-------------|
| 08 | Neural Networks | perceptron, activations, XOR, PyTorch, backprop, MNIST |
| 09 | Deep Learning | convolution, pooling, CNNs, CIFAR-10, BatchNorm, dropout, transfer learning |

## Phase 5: Production AI (Levels 10–13)

| # | Level | Key Concepts |
|---|-------|-------------|
| 10 | Deployment | joblib, Flask/FastAPI, Docker, monitoring, versioning, A/B testing |
| 11 | LLM & Prompting | prompt styles, few-shot, CoT, temperature, personas, JSON output, evaluation |
| 12 | RAG | TF-IDF embeddings, retrieval, chunking, vector store, rerank, hybrid search |
| 13 | Agentic AI | tool registry, ReAct loop, tool calling, planning, memory, multi-agent, autonomy |

## Verification

```bash
cd ai-ml/level-XX-topic/
python3 check.py all            # check all 9 problems in the level
python3 verify_solutions.py     # from repo root: verify all reference solutions
```

---

# 5. Quasar / Vue 3 (20 Lessons + 6 Projects)

## Phase 1: Quasar Basics (Lessons 1–5)

| # | Lesson | Key Concepts |
|---|--------|-------------|
| 1 | Quasar Basics | q-page, SFC, q-btn, props, ref(), v-if, q-input, v-model |
| 2 | Quasar Layout System | q-layout, q-header, q-drawer, q-footer, q-page-container |
| 3 | Quasar Components Deep Dive | q-card, q-list, q-table, q-dialog, q-tabs, q-chip, q-badge |
| 4 | Vue 3 Composition API | script setup, ref, reactive, computed, watch, lifecycle hooks |
| 5 | Vue Reactivity System | ref vs reactive, deep reactivity, watchEffect, computed caching |

**Mini Project 16:** Quasar Settings Page ($50–150)

## Phase 2: Vue Ecosystem (Lessons 6–10)

| # | Lesson | Key Concepts |
|---|--------|-------------|
| 6 | Vue Router in Quasar | routes, lazy loading, navigation guards, route params, nested |
| 7 | Pinia State Management | defineStore, state, getters, actions, persistence, composition |
| 8 | Quasar Plugins | Dialog, Notify, Loading, BottomSheet, LocalStorage, AppVisibility |
| 9 | Quasar Form Components | q-input validation, q-select, q-date, q-time, q-slider, q-toggle |
| 10 | API Integration in Quasar | axios, fetch, useFetch pattern, loading/error states, interceptors |

**Mini Project 17:** Quasar Weather App ($100–200)
> Weather app with search, favorites (Pinia), 5-day forecast, responsive.

**Medium Project 9:** Quasar Admin Dashboard ($300–500)
> Dashboard with sidebar, data tables, charts, CRUD modals, auth, Pinia state.

## Phase 3: Quasar Advanced (Lessons 11–15)

| # | Lesson | Key Concepts |
|---|--------|-------------|
| 11 | Quasar Tables & Data | q-table, columns, pagination, sorting, filtering, server-side |
| 12 | Quasar Icons & Theming | Material Icons, FontAwesome, brand colors, dark mode, custom themes |
| 13 | Quasar Animations & Transitions | transitions, q-transition, CSS animations, scroll animations |
| 14 | Quasar Notifications & Dialogs | Notify patterns, dialog composition, confirm dialogs, custom dialogs |
| 15 | Quasar PWA Mode | manifest, service workers, offline, install prompt, push notifications |

**Mini Project 18:** PWA Notes App ($100–200)

## Phase 4: Quasar Production (Lessons 16–20)

| # | Lesson | Key Concepts |
|---|--------|-------------|
| 16 | Quasar Mobile (Capacitor) | iOS/Android build, plugins, permissions, native APIs, app store |
| 17 | Quasar Electron (Desktop) | Electron main/renderer, IPC, native menus, auto-update, packaging |
| 18 | Quasar SSR | server-side rendering, SEO, hydration, API pre-fetching, meta tags |
| 19 | Testing in Quasar | Vitest, component testing, E2E with Cypress/Playwright, mocking |
| 20 | Quasar App Deployment | Docker, CI/CD, Vercel/Netlify, app stores, environment config |

**Mini Project 19:** Desktop App with Electron ($150–300)

**Medium Project 10:** Cross-Platform Task Manager ($300–600)
> Build once, deploy as PWA + mobile + desktop. Sync, offline, notifications.

**Capstone Project 5:** Full SaaS App with Quasar ($1000–2000)
> Auth, multi-tenant, subscriptions, admin panel, API, mobile + web + desktop. Production SaaS.

---

# Project Summary

| Type | Count | Price Range | Total Potential |
|------|-------|-------------|-----------------|
| Mini | 19 | $50–200 | $950–3,800 |
| Medium | 10 | $200–600 | $2,000–6,000 |
| Capstone | 5 | $500–2,000 | $2,500–10,000 |
| **Total** | **34** | | **$5,450–19,800** |

# Lesson Summary

| Subject | Lessons | Problems | Projects |
|---------|---------|----------|----------|
| HTML/CSS/JS | 20 | 180 | 6 |
| React | 20 | 180 | 6 |
| Python | 20 | 180 | 6 |
| AI/ML | 20 | 180 | 6 |
| Quasar | 20 | 180 | 6 |
| **Total** | **100** | **900** | **34** |

# File Structure (per lesson)

```
subject/lesson-XX-topic/
├── concepts.md          # WHY/WHERE/WHAT-GOES-WRONG for every concept
├── task-explanation.md  # Lesson + problem list
├── coding-check.md      # Verification checklist
├── easy/
│   ├── p01-solve.*      # Problem with TODO (you write the solution)
│   ├── p02-solve.*
│   ├── p03-solve.*
│   └── solutions/       # Reference solutions (check your work)
├── medium/
│   ├── p01-solve.*
│   ├── p02-solve.*
│   ├── p03-solve.*
│   └── solutions/
└── hard/
    ├── p01-solve.*
    ├── p02-solve.*
    ├── p03-solve.*
    └── solutions/
```

# Project Structure (per project)

```
projects/
├── mini-XX-name/
│   ├── README.md            # Project brief, requirements, sellable pitch
│   └── TASK-BREAKDOWN.md    # Step-by-step guide with checkpoints
├── medium-XX-name/
│   ├── README.md
│   └── TASK-BREAKDOWN.md
└── capstone-XX-name/
    ├── README.md
    └── TASK-BREAKDOWN.md
```

# Complete Project List

## Mini Projects (19) — $50–200 each

| # | Project | Subject | Prerequisites |
|---|---------|---------|---------------|
| 1 | Accessible Contact Form | HTML/CSS/JS | Lessons 01–05 |
| 2 | Flexbox Landing Page | HTML/CSS/JS | Lessons 06–10 |
| 3 | Responsive Image Gallery | HTML/CSS/JS | Lessons 11–15 |
| 4 | Interactive Todo (Vanilla JS) | HTML/CSS/JS | Lessons 16–20 |
| 5 | React Todo App | React | Lessons 01–05 |
| 6 | Movie Search (React + API) | React | Lessons 06–10 |
| 7 | Multi-Page Blog | HTML/CSS/JS | Lessons 16–20 |
| 8 | E-commerce Product Page | React | Lessons 11–15 |
| 9 | CLI Contact Book | Python | Lessons 01–05 |
| 10 | File Organizer | Python | Lessons 06–10 |
| 11 | Web Scraper | Python | Lessons 11–15 |
| 12 | FastAPI REST API | Python | Lessons 16–20 |
| 13 | Data Cleaning Pipeline | AI/ML | Lessons 01–05 |
| 14 | House Price Predictor | AI/ML | Lessons 06–10 |
| 15 | Customer Segmentation | AI/ML | Lessons 11–15 |
| 16 | Quasar Settings Page | Quasar | Lessons 01–05 |
| 17 | Quasar Weather App | Quasar | Lessons 06–10 |
| 18 | PWA Notes App | Quasar | Lessons 11–15 |
| 19 | Electron Desktop App | Quasar | Lessons 16–20 |

## Medium Projects (10) — $200–600 each

| # | Project | Subject | Prerequisites |
|---|---------|---------|---------------|
| 1 | Pricing Page (3 Tiers) | HTML/CSS/JS | Lessons 01–10 |
| 2 | Calculator App | HTML/CSS/JS | Lessons 16–20 |
| 3 | Recipe Finder (React + API) | React | Lessons 06–10 |
| 4 | E-commerce Store | React | Lessons 01–20 |
| 5 | Expense Tracker | React | Lessons 01–20 |
| 6 | CRUD API with Auth | Python | Lessons 16–20 |
| 7 | Spam Classifier | AI/ML | Lessons 06–15 |
| 8 | Image Classifier API | AI/ML | Lessons 16–20 |
| 9 | Quasar Admin Dashboard | Quasar | Lessons 01–10 |
| 10 | Cross-Platform Task Manager | Quasar | Lessons 01–20 |

## Capstone Projects (5) — $500–2000 each

| # | Project | Subject | Description |
|---|---------|---------|-------------|
| 1 | Portfolio Website | React | Showcase all projects |
| 2 | Social Dashboard | React + FastAPI | Full-stack social app |
| 3 | Task Management API | Python | Production FastAPI with WebSocket |
| 4 | ML Pipeline | AI/ML | End-to-end MLOps pipeline |
| 5 | SaaS App | Quasar + FastAPI | Multi-tenant SaaS with billing |
