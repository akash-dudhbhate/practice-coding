#!/usr/bin/env python3
"""Generate TASK-BREAKDOWN.md files for all projects."""

import os

PROJECTS_DIR = "/home/akash-dev/workspace-personal/practice-coding/projects"

# Task breakdowns for each project
BREAKDOWNS = {
    "mini-02-flexbox-landing-page": {
        "title": "Landing Page with Flexbox",
        "files": "index.html, styles.css, script.js (smooth scroll)",
        "steps": [
            ("HTML Skeleton", "Create index.html with header, hero, features, testimonials, CTA, footer. Use semantic tags."),
            ("Header + Nav", "Sticky header with logo and navigation links. Use flexbox for layout."),
            ("Hero Section", "Full-width hero with headline, subtext, and CTA button. Flexbox centering."),
            ("Features Grid", "3-column flexbox grid with icons, titles, descriptions. Use flex-wrap for responsive."),
            ("Testimonials", "Row of 3 testimonial cards with quotes, names, avatars. Flexbox with gap."),
            ("CTA Section", "Centered call-to-action with button. Background color contrast."),
            ("Footer", "Multi-column footer with links, social icons, copyright."),
            ("CSS Styling", "Add colors, typography, spacing, hover effects. Use CSS variables for brand colors."),
            ("Responsive", "Media queries: mobile (1 column), tablet (2 columns), desktop (3 columns)."),
            ("Smooth Scroll", "JS for smooth scroll on nav link clicks. Active link highlighting."),
        ],
        "checklist": [
            "Hero section with headline + CTA",
            "Features section (3+ items) with flexbox",
            "Testimonials section",
            "CTA section",
            "Responsive (mobile, tablet, desktop)",
            "Smooth scroll navigation",
            "Hover effects on buttons and cards",
            "Consistent spacing and typography",
        ],
    },
    "mini-03-responsive-gallery": {
        "title": "Responsive Image Gallery",
        "files": "index.html, styles.css, script.js (lightbox)",
        "steps": [
            ("HTML Structure", "Grid container with image cards. Each card has image, caption, and data attributes."),
            ("CSS Grid Layout", "Use CSS Grid with auto-fit and minmax for responsive columns. No media queries needed."),
            ("Image Cards", "Style cards with border-radius, box-shadow, hover zoom effect."),
            ("Lightbox Modal", "Hidden modal that shows full-size image on click. Include close button and prev/next."),
            ("JS: Open Lightbox", "Click image → show modal with full image. Add keyboard support (Esc to close)."),
            ("JS: Navigation", "Prev/next buttons to cycle through images. Arrow key support."),
            ("CSS: Hover Effects", "Scale on hover, overlay caption, smooth transitions."),
            ("Responsive", "Grid auto-adjusts columns. Lightbox works on mobile (swipe optional)."),
        ],
        "checklist": [
            "CSS Grid with auto-fit/minmax",
            "6+ images with captions",
            "Lightbox modal on click",
            "Prev/next navigation in lightbox",
            "Keyboard support (Esc, arrows)",
            "Hover effects (zoom, overlay)",
            "Responsive (auto columns)",
            "Smooth transitions",
        ],
    },
    "mini-04-interactive-todo": {
        "title": "Interactive Todo List (Vanilla JS)",
        "files": "index.html, styles.css, script.js",
        "steps": [
            ("HTML Structure", "Input field, add button, todo list (ul), filter buttons (all/active/completed), count."),
            ("CSS Styling", "Clean card-based design. Checkbox styling, delete button hover, completed strikethrough."),
            ("JS: Add Todo", "Function to create todo object {id, text, done}. Render to DOM. Enter key + button."),
            ("JS: Toggle Todo", "Click checkbox → toggle done state. Update DOM + strikethrough."),
            ("JS: Delete Todo", "Delete button → remove from array + DOM. Confirmation for completed todos."),
            ("JS: Filter", "All/Active/Completed filter buttons. Show/hide todos based on filter."),
            ("JS: Counter", "Show remaining count: 'X items left'. Update on every change."),
            ("JS: Persistence", "Save todos to localStorage. Load on page refresh."),
            ("JS: Edit Todo", "Double-click to edit. Input field replaces text. Enter to save, Esc to cancel."),
        ],
        "checklist": [
            "Add todo (input + button + Enter key)",
            "Toggle complete (checkbox)",
            "Delete todo (button)",
            "Filter (all/active/completed)",
            "Item counter",
            "localStorage persistence",
            "Edit todo (double-click)",
            "Clean, responsive UI",
        ],
    },
    "mini-05-react-todo": {
        "title": "React Todo App",
        "files": "src/App.jsx, src/components/TodoInput.jsx, src/components/TodoList.jsx, src/components/TodoItem.jsx, src/components/Filters.jsx, src/hooks/useTodos.js",
        "steps": [
            ("Setup", "npx create-vite app --template react. Install. Clean App.jsx."),
            ("useTodos Hook", "Custom hook: todos state, addTodo, toggleTodo, deleteTodo, filter, localStorage sync."),
            ("TodoInput Component", "Input + button. useState for input. Call addTodo on submit. Enter key support."),
            ("TodoItem Component", "Props: todo, onToggle, onDelete, onEdit. Checkbox, text, delete button. Edit mode."),
            ("TodoList Component", "Map filtered todos to TodoItem. Empty state message."),
            ("Filters Component", "All/Active/Completed buttons. Active state styling."),
            ("App Component", "Compose all components. useTodos hook. Pass props down."),
            ("Styling", "CSS modules or Tailwind. Clean, modern design. Responsive."),
            ("Testing", "Write basic tests: add, toggle, delete, filter. Use vitest + testing-library."),
        ],
        "checklist": [
            "useTodos custom hook with localStorage",
            "Add todo (input + Enter)",
            "Toggle complete",
            "Delete todo",
            "Filter (all/active/completed)",
            "Edit todo (double-click)",
            "Item counter",
            "Responsive design",
            "Basic tests",
        ],
    },
    "mini-06-movie-search": {
        "title": "Movie Search App (React + API)",
        "files": "src/App.jsx, src/components/SearchBar.jsx, src/components/MovieCard.jsx, src/components/MovieList.jsx, src/components/MovieModal.jsx, src/hooks/useMovieSearch.js",
        "steps": [
            ("Setup", "create-vite react. Get OMDB API key from omdbapi.com."),
            ("useMovieSearch Hook", "State: query, results, loading, error, selected. Fetch from OMDB API. Debounce."),
            ("SearchBar Component", "Input with search icon. Debounced API call. Show loading spinner."),
            ("MovieCard Component", "Poster, title, year, type. Click to show details. Hover effect."),
            ("MovieList Component", "Grid of MovieCards. Loading skeleton. Empty state. Error state."),
            ("MovieModal Component", "Full details: plot, cast, ratings, runtime. Close button. Backdrop click to close."),
            ("App Component", "Compose. Manage state. Handle API errors gracefully."),
            ("Styling", "Grid layout, card shadows, modal overlay. Responsive."),
            ("Debouncing", "Use setTimeout or lodash debounce. Cancel old requests."),
        ],
        "checklist": [
            "Search bar with debounce",
            "Movie cards in a grid",
            "Movie detail modal",
            "Loading state (spinner or skeleton)",
            "Error state (message + retry)",
            "Empty state (no results)",
            "Responsive grid",
            "API key in env variable",
        ],
    },
    "mini-07-multi-page-blog": {
        "title": "Multi-Page Blog (HTML/CSS/JS)",
        "files": "index.html, blog.html, post.html, styles.css, script.js, data/posts.js",
        "steps": [
            ("Data Structure", "Create posts.js with array of post objects {id, title, date, author, excerpt, content, image}."),
            ("Home Page", "index.html: hero, featured post, recent posts grid, newsletter signup."),
            ("Blog List Page", "blog.html: all posts in a grid. Filter by category. Search bar."),
            ("Single Post Page", "post.html: full post content, author bio, related posts, comments section."),
            ("Navigation", "Shared header/footer across all pages. Active link highlighting."),
            ("JS: Dynamic Content", "Load posts from data. Render cards. URL params for single post (?id=1)."),
            ("JS: Search + Filter", "Search by title. Filter by category. Real-time filtering."),
            ("CSS Styling", "Clean blog design: typography, spacing, card layout, responsive."),
            ("SEO Basics", "Meta tags per page, semantic HTML, alt text on images, Open Graph tags."),
        ],
        "checklist": [
            "3 pages (home, blog list, single post)",
            "Dynamic content from JS data",
            "Search functionality",
            "Category filter",
            "Responsive design",
            "SEO meta tags",
            "Related posts section",
            "Clean typography",
        ],
    },
    "mini-08-ecommerce-product-page": {
        "title": "E-commerce Product Page (React)",
        "files": "src/App.jsx, src/components/ProductGallery.jsx, src/components/ProductInfo.jsx, src/components/SizeSelector.jsx, src/components/Reviews.jsx, src/components/AddToCart.jsx",
        "steps": [
            ("Product Data", "Create product object: images[], name, price, description, sizes[], reviews[]."),
            ("ProductGallery", "Main image + thumbnails. Click thumbnail to change main. Zoom on hover."),
            ("ProductInfo", "Name, price, description, rating stars, stock status."),
            ("SizeSelector", "Size buttons. Selected state. Out-of-stock sizes disabled."),
            ("QuantitySelector", "+/- buttons. Min 1, max stock. Input field."),
            ("AddToCart", "Button with loading state. Toast notification on add. Cart count badge."),
            ("Reviews", "List of reviews with rating, author, date, comment. Rating summary."),
            ("Styling", "Two-column layout (gallery + info). Responsive: stacks on mobile."),
        ],
        "checklist": [
            "Image gallery with thumbnails",
            "Product info (name, price, description)",
            "Size selector with states",
            "Quantity selector",
            "Add to cart with notification",
            "Reviews section with ratings",
            "Responsive (2-col → 1-col)",
            "Loading states",
        ],
    },
    "mini-09-cli-contact-book": {
        "title": "CLI Contact Book (Python)",
        "files": "contacts.py, storage.py, main.py",
        "steps": [
            ("Contact Class", "Contact dataclass: name, phone, email, address. __str__ method."),
            ("Storage Module", "Save/load contacts to JSON file. load_contacts(), save_contacts()."),
            ("Add Contact", "Prompt for fields. Validate phone (digits) and email (@). Add to list."),
            ("List Contacts", "Display all contacts in a table format. Sort by name."),
            ("Search Contacts", "Search by name, phone, or email. Case-insensitive. Partial match."),
            ("Edit Contact", "Select by index or name. Update fields. Keep old value if empty."),
            ("Delete Contact", "Select by index or name. Confirm before deletion."),
            ("Main Menu", "Loop with menu: add, list, search, edit, delete, exit. Handle invalid input."),
            ("Error Handling", "File not found, invalid input, duplicate contacts. Graceful messages."),
        ],
        "checklist": [
            "Add contact with validation",
            "List all contacts (sorted)",
            "Search contacts (partial match)",
            "Edit contact",
            "Delete contact (with confirm)",
            "JSON file persistence",
            "Clean CLI menu",
            "Error handling (graceful)",
        ],
    },
    "mini-10-file-organizer": {
        "title": "File Organizer (Python)",
        "files": "organizer.py, config.py, main.py",
        "steps": [
            ("Config", "Define file categories: images (.jpg, .png), docs (.pdf, .docx), videos (.mp4), etc."),
            ("Scan Directory", "Walk directory, list all files with extensions. Return file list."),
            ("Categorize Files", "Map each file to a category based on extension. Unknown → 'misc'."),
            ("Create Folders", "Create category folders if they don't exist. Handle permissions."),
            ("Move Files", "Move each file to its category folder. Handle name collisions (append number)."),
            ("Dry Run Mode", "--dry-run flag: show what would happen without moving. Log actions."),
            ("Undo Feature", "Log all moves. --undo flag reverses the last operation."),
            ("CLI Interface", "argparse: directory path, --dry-run, --undo, --verbose. Help text."),
            ("Logging", "Log all actions to file. Show summary at end (X files moved to Y categories)."),
        ],
        "checklist": [
            "Scan directory for files",
            "Categorize by extension",
            "Create category folders",
            "Move files to folders",
            "Handle name collisions",
            "Dry run mode",
            "Undo feature",
            "CLI with argparse",
            "Logging + summary",
        ],
    },
    "mini-11-web-scraper": {
        "title": "Web Scraper (Python)",
        "files": "scraper.py, parser.py, exporter.py, main.py",
        "steps": [
            ("Setup", "pip install requests beautifulsoup4. Test with a simple page."),
            ("Fetch Page", "requests.get with timeout, headers (User-Agent). Handle errors (404, timeout)."),
            ("Parse HTML", "BeautifulSoup: find titles, links, text. CSS selectors for specific elements."),
            ("Extract Data", "Extract structured data: title, price, rating, link. Store as list of dicts."),
            ("Pagination", "Follow 'next' links. Limit max pages. Rate limiting (time.sleep)."),
            ("Export to CSV", "Write data to CSV with csv module. Include headers. Handle special characters."),
            ("Export to JSON", "Optional: also export to JSON with json.dumps."),
            ("CLI Interface", "argparse: URL, output file, max pages, format (csv/json)."),
            ("Rate Limiting", "Respect robots.txt. Add delay between requests. Max retries."),
            ("Error Handling", "Network errors, parse errors, missing elements. Continue on error."),
        ],
        "checklist": [
            "Fetch page with requests",
            "Parse with BeautifulSoup",
            "Extract structured data",
            "Handle pagination",
            "Export to CSV",
            "Rate limiting (delays)",
            "CLI with argparse",
            "Error handling (graceful)",
            "Respects robots.txt",
        ],
    },
    "mini-12-fastapi-rest": {
        "title": "FastAPI REST API",
        "files": "main.py, models.py, database.py, schemas.py, crud.py",
        "steps": [
            ("Setup", "pip install fastapi uvicorn. Create main.py with FastAPI app."),
            ("Database", "SQLite with SQLAlchemy. Create engine, session, Base. models.py: Item model."),
            ("Schemas", "Pydantic models: ItemCreate, ItemResponse. Validation rules."),
            ("CRUD", "crud.py: get_items, get_item, create_item, update_item, delete_item."),
            ("Routes", "GET /items, GET /items/{id}, POST /items, PUT /items/{id}, DELETE /items/{id}."),
            ("Error Handling", "404 for missing items. 422 for validation errors. HTTPException."),
            ("Documentation", "Auto-docs at /docs. Add descriptions, tags, response models."),
            ("Testing", "pytest with TestClient. Test all endpoints. Test error cases."),
            ("CORS", "Add CORS middleware for frontend integration."),
        ],
        "checklist": [
            "SQLite database with SQLAlchemy",
            "Pydantic schemas with validation",
            "Full CRUD endpoints",
            "Proper HTTP status codes",
            "Error handling (404, 422)",
            "Auto-docs at /docs",
            "Tests with pytest",
            "CORS enabled",
        ],
    },
}

def generate_breakdown(project_name, data):
    project_dir = os.path.join(PROJECTS_DIR, project_name)
    filepath = os.path.join(project_dir, "TASK-BREAKDOWN.md")

    content = f"""# {data['title']} — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
{project_name}/
├── {data['files']}
└── README.md
```

---

## Implementation Steps

"""
    for i, (step_name, description) in enumerate(data['steps'], 1):
        content += f"### Step {i}: {step_name}\n\n{description}\n\n**Checkpoint:** Step {i} is complete when the described functionality works.\n\n"

    content += """---

## Final Checklist

"""
    for item in data['checklist']:
        content += f"- [ ] {item}\n"

    content += """
---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
"""
    with open(filepath, 'w') as f:
        f.write(content)
    return filepath

# Generate all breakdowns
for project_name, data in BREAKDOWNS.items():
    path = generate_breakdown(project_name, data)
    print(f"  Generated: {path}")

print(f"\nGenerated {len(BREAKDOWNS)} task breakdowns")
