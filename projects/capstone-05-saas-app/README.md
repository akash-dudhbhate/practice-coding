# Capstone Project 05 — Full SaaS App with Quasar

> **Type:** Capstone Project
> **Subject:** Quasar
> **Estimated sell price:** $1000–2000
> **Difficulty:** Advanced
> **Prerequisites:** All 20 Quasar lessons

## Project Brief

Build a complete SaaS (Software as a Service) application using Quasar that works as a web app, PWA, and desktop app. This is a high-value sellable product — SaaS apps are the most lucrative type of software product. The app is a project management tool with auth, multi-tenant workspaces, subscriptions, and an admin panel.

## What you'll build

A Quasar SaaS app with:
- **Authentication** — login, register, password reset, JWT tokens
- **Multi-tenant workspaces** — users can create/join organizations
- **Projects** — create projects within workspaces, assign team members
- **Tasks** — create tasks within projects, assign, set priority, due dates
- **Kanban board** — drag-and-drop task columns (todo, in_progress, done)
- **Team management** — invite users, assign roles (admin, member, viewer)
- **Settings** — profile, workspace settings, billing
- **Dark mode** — toggle with persistence
- **Notifications** — in-app notifications using Quasar Notify
- **Admin panel** — user management, workspace overview (admin role only)
- **PWA** — installable, works offline
- **Desktop** — Electron build for desktop app
- **Responsive** — works on mobile, tablet, desktop

## Skills you'll demonstrate

- Quasar framework (layout, components, plugins, forms)
- Vue 3 Composition API (ref, reactive, computed, watch)
- Pinia state management (auth, workspace, projects stores)
- Vue Router (protected routes, role-based access)
- API integration (axios with interceptors, auth headers)
- Quasar PWA mode
- Quasar Electron mode
- Quasar tables, dialogs, notifications
- Responsive design
- Role-based access control
- Drag-and-drop (Kanban board)

## Sellable pitch

> "I'll build you a complete SaaS project management application — like a mini Trello/Asana. Includes auth, multi-tenant workspaces, Kanban boards, team management, admin panel, and works as a web app, PWA, and desktop app. Built with Quasar (Vue 3) for cross-platform deployment from a single codebase."

## Requirements

- [ ] Auth: login, register, password reset pages
- [ ] JWT-based auth with Pinia store and axios interceptors
- [ ] Protected routes (redirect to login if not authenticated)
- [ ] Multi-tenant: users can create workspaces, invite others
- [ ] Projects: CRUD within workspaces
- [ ] Tasks: CRUD within projects, with priority, due date, assignee
- [ ] Kanban board: drag-and-drop between columns (Quasar + sortable.js)
- [ ] Team management: invite by email, roles (admin/member/viewer)
- [ ] Role-based UI (admin panel only visible to admins)
- [ ] Settings page: profile, workspace, billing (mock)
- [ ] Dark mode toggle (Quasar dark mode + localStorage)
- [ ] In-app notifications (Quasar Notify plugin)
- [ ] Quasar Layout with header, drawer, footer
- [ ] Responsive: drawer collapses on mobile, Kanban scrolls horizontally
- [ ] PWA: installable, service worker, offline indicator
- [ ] Electron: desktop build configuration
- [ ] Loading states (Quasar Loading plugin or q-skeleton)
- [ ] Error handling (Quasar Notify for errors)
- [ ] Form validation (Quasar q-input rules)
- [ ] README with setup, build (web/PWA/desktop), and deployment

## Getting started

1. Design the data model (users, workspaces, projects, tasks, roles)
2. Set up Quasar project with layout (header, drawer, footer)
3. Set up Pinia stores (auth, workspace, projects, tasks)
4. Set up Vue Router with protected routes
5. Build auth pages (login, register)
6. Build workspace selection/creation
7. Build project list and CRUD
8. Build task list and CRUD
9. Build Kanban board with drag-and-drop
10. Build team management
11. Build settings page
12. Build admin panel
13. Add dark mode, notifications, loading states
14. Configure PWA mode
15. Configure Electron mode
16. Test on web, mobile, and desktop
17. Write README

## Deliverables

- Complete Quasar project (organized src/ structure)
- Works as: web app, PWA, desktop (Electron)
- Pinia stores for state management
- API integration (mock with JSON Server or real backend)
- README with setup, build instructions for all 3 platforms
- Screenshots of all major pages
