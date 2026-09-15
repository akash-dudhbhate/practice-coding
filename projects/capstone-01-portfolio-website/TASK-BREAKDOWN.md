# Portfolio Website (React) — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
capstone-01-portfolio-website/
├── src/App.jsx, src/pages/Home.jsx, src/pages/Projects.jsx, src/pages/About.jsx, src/pages/Contact.jsx, src/components/ProjectCard.jsx, src/components/Skills.jsx, src/components/Navbar.jsx
└── README.md
```

---

## Implementation Steps

### Step 1: Design System

Define colors, typography, spacing. Create a theme. Use CSS variables or Tailwind.

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: Layout + Routing

React Router: /, /projects, /project/:id, /about, /contact. Shared layout.

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: Home/Hero

Name, title, tagline, CTA buttons (View Work, Contact). Animated entrance.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: Projects Page

Grid of project cards. Filter by tech stack. Search. Link to detail pages.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: Project Detail

Images, description, tech stack, live link, GitHub link. Markdown content.

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: About Page

Bio, skills (with icons), experience timeline, education. Download CV button.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: Contact Page

Contact form (name, email, message). Form validation. EmailJS or backend API.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: Navbar

Sticky, responsive. Mobile: hamburger menu. Active link highlight. Smooth scroll.

**Checkpoint:** Step 8 is complete when the described functionality works.

### Step 9: Animations

Scroll animations (fade in, slide up). Hover effects. Page transitions.

**Checkpoint:** Step 9 is complete when the described functionality works.

### Step 10: SEO + Performance

Meta tags, Open Graph, sitemap. Lazy load images. Lighthouse 90+.

**Checkpoint:** Step 10 is complete when the described functionality works.

### Step 11: Deploy

Deploy to Vercel/Netlify. Custom domain. HTTPS. Analytics (optional).

**Checkpoint:** Step 11 is complete when the described functionality works.

---

## Final Checklist

- [ ] React Router with 5 pages
- [ ] Hero section with CTA
- [ ] Projects grid with filters
- [ ] Project detail pages
- [ ] About page with skills + timeline
- [ ] Contact form with validation
- [ ] Responsive navbar (mobile menu)
- [ ] Scroll animations
- [ ] SEO meta tags + Open Graph
- [ ] Lighthouse score 90+
- [ ] Deployed to Vercel/Netlify

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
5. **Hardcoding values** — use environment variables for API keys, URLs, and configuration.
