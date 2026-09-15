# Multi-Page Blog (HTML/CSS/JS) — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
mini-07-multi-page-blog/
├── index.html, blog.html, post.html, styles.css, script.js, data/posts.js
└── README.md
```

---

## Implementation Steps

### Step 1: Data Structure

Create posts.js with array of post objects {id, title, date, author, excerpt, content, image}.

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: Home Page

index.html: hero, featured post, recent posts grid, newsletter signup.

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: Blog List Page

blog.html: all posts in a grid. Filter by category. Search bar.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: Single Post Page

post.html: full post content, author bio, related posts, comments section.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: Navigation

Shared header/footer across all pages. Active link highlighting.

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: JS: Dynamic Content

Load posts from data. Render cards. URL params for single post (?id=1).

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: JS: Search + Filter

Search by title. Filter by category. Real-time filtering.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: CSS Styling

Clean blog design: typography, spacing, card layout, responsive.

**Checkpoint:** Step 8 is complete when the described functionality works.

### Step 9: SEO Basics

Meta tags per page, semantic HTML, alt text on images, Open Graph tags.

**Checkpoint:** Step 9 is complete when the described functionality works.

---

## Final Checklist

- [ ] 3 pages (home, blog list, single post)
- [ ] Dynamic content from JS data
- [ ] Search functionality
- [ ] Category filter
- [ ] Responsive design
- [ ] SEO meta tags
- [ ] Related posts section
- [ ] Clean typography

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
