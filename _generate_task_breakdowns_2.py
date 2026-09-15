#!/usr/bin/env python3
"""Generate TASK-BREAKDOWN.md for remaining projects (mini 13-19, medium 1-10, capstone 1-5)."""

import os

PROJECTS_DIR = "/home/akash-dev/workspace-personal/practice-coding/projects"

BREAKDOWNS = {
    "mini-13-data-cleaning-pipeline": {
        "title": "Data Cleaning Pipeline (Python)",
        "files": "cleaner.py, pipeline.py, main.py, sample_data.csv",
        "steps": [
            ("Load Data", "pd.read_csv with error handling. Show shape, columns, dtypes."),
            ("Inspect Data", "Show missing values, duplicates, outliers, data types. Summary stats."),
            ("Handle Missing Values", "Drop rows with too many NaN. Fill numeric with median, categorical with mode."),
            ("Remove Duplicates", "Identify and drop duplicate rows. Log count before/after."),
            ("Fix Data Types", "Convert date strings to datetime. Convert numeric columns. Category for low-cardinality."),
            ("Handle Outliers", "IQR method: identify, cap (winsorize) or remove. Log count."),
            ("Standardize Text", "Strip whitespace, normalize case, fix encoding issues in string columns."),
            ("Export Clean Data", "Save to CSV. Generate cleaning report (what was changed, counts)."),
            ("CLI Interface", "argparse: input file, output file, --report. Configurable cleaning options."),
        ],
        "checklist": [
            "Load CSV with pandas",
            "Handle missing values (median/mode)",
            "Remove duplicates",
            "Fix data types (dates, numbers)",
            "Handle outliers (IQR)",
            "Standardize text columns",
            "Export cleaned CSV",
            "Cleaning report generated",
            "CLI with argparse",
        ],
    },
    "mini-14-house-price-predictor": {
        "title": "House Price Predictor (ML)",
        "files": "data_loader.py, model.py, predict.py, train.py, app.py",
        "steps": [
            ("Load Dataset", "Use California Housing or Ames dataset. Split into X (features) and y (target)."),
            ("EDA", "Correlation heatmap, distribution plots, feature vs target scatter plots."),
            ("Feature Engineering", "Create new features (rooms_per_household, bedrooms_per_room). Scale features."),
            ("Train Model", "LinearRegression baseline. Then RandomForest. Cross-validation for both."),
            ("Evaluate", "RMSE, MAE, R². Compare models. Feature importance plot."),
            ("Hyperparameter Tuning", "GridSearchCV on RandomForest: n_estimators, max_depth, min_samples_split."),
            ("Save Model", "joblib.dump the best model + scaler. Save feature names."),
            ("Prediction Script", "predict.py: load model, take input (CLI or JSON), output prediction."),
            ("Simple API", "FastAPI endpoint: POST /predict with feature values → price prediction."),
        ],
        "checklist": [
            "Dataset loaded and explored",
            "Feature engineering (new features)",
            "Feature scaling",
            "LinearRegression baseline",
            "RandomForest with tuning",
            "Cross-validation",
            "RMSE/MAE/R² metrics",
            "Model saved with joblib",
            "Prediction CLI",
            "FastAPI prediction endpoint",
        ],
    },
    "mini-15-customer-segmentation": {
        "title": "Customer Segmentation (Unsupervised ML)",
        "files": "data_loader.py, segmentation.py, visualize.py, main.py",
        "steps": [
            ("Load Data", "Mall customers or e-commerce data. Features: age, income, spending score."),
            ("EDA", "Distributions, correlations, pair plots. Understand the data."),
            ("Feature Scaling", "StandardScaler for KMeans (distance-based). Fit and transform."),
            ("Find Optimal K", "Elbow method (inertia vs K). Silhouette score for each K. Plot both."),
            ("Train KMeans", "Fit KMeans with optimal K. Get cluster labels. Cluster centers."),
            ("Analyze Clusters", "Mean values per cluster. Name clusters (e.g., 'High Value', 'Budget')."),
            ("Visualize", "Scatter plot with cluster colors. 3D plot if 3+ features. PCA for visualization."),
            ("DBSCAN Comparison", "Train DBSCAN. Compare clusters. When is DBSCAN better?"),
            ("Export Results", "Save customer data with cluster labels. Generate segment summary report."),
        ],
        "checklist": [
            "Data loaded and explored",
            "Feature scaling",
            "Elbow method for optimal K",
            "Silhouette score",
            "KMeans trained",
            "Clusters analyzed and named",
            "Visualization (scatter, 3D or PCA)",
            "DBSCAN comparison",
            "Results exported with labels",
        ],
    },
    "mini-16-quasar-settings-page": {
        "title": "Quasar Settings Page",
        "files": "src/pages/Settings.vue, src/components/ThemeToggle.vue, src/components/NotificationSettings.vue, src/stores/settings.js",
        "steps": [
            ("Quasar Setup", "quasar create app. Add Settings page route."),
            ("Settings Store", "Pinia store: theme (dark/light), notifications, language. localStorage persistence."),
            ("ThemeToggle Component", "Toggle dark/light. Use $q.dark.set(). Persist choice."),
            ("Notification Settings", "Toggles for email, push, sound. Each saved to store."),
            ("Language Selector", "QSelect with languages. Use vue-i18n (optional) or just store value."),
            ("Profile Section", "Display user info. Edit name/avatar. Save to store."),
            ("Layout", "QPage with QCard sections. QToggle, QSelect, QInput components."),
            ("Responsive", "Works on mobile (stacked) and desktop (side-by-side)."),
        ],
        "checklist": [
            "Pinia settings store with localStorage",
            "Dark/light theme toggle",
            "Notification toggles",
            "Language selector",
            "Profile edit section",
            "Quasar components (QToggle, QSelect)",
            "Responsive layout",
            "Settings persist on refresh",
        ],
    },
    "mini-17-quasar-weather-app": {
        "title": "Quasar Weather App",
        "files": "src/pages/Weather.vue, src/components/WeatherCard.vue, src/components/SearchBar.vue, src/composables/useWeather.js",
        "steps": [
            ("API Setup", "Get OpenWeatherMap API key. Create useWeather composable."),
            ("SearchBar", "QInput with debounce. Search by city name. Show suggestions."),
            ("WeatherCard", "Current weather: temp, condition, icon, humidity, wind. Styled card."),
            ("Forecast", "5-day forecast section. Horizontal scroll on mobile."),
            ("useWeather Composable", "fetchWeather(city), loading, error, data. Handle API errors."),
            ("Geolocation", "Use navigator.geolocation for 'current location' button."),
            ("Unit Toggle", "Celsius/Fahrenheit toggle. Convert values. Persist preference."),
            ("Styling", "Weather-appropriate colors. Icons for conditions. Responsive."),
        ],
        "checklist": [
            "City search with debounce",
            "Current weather display",
            "5-day forecast",
            "Geolocation support",
            "Celsius/Fahrenheit toggle",
            "Loading and error states",
            "Weather icons",
            "Responsive design",
        ],
    },
    "mini-18-pwa-notes-app": {
        "title": "PWA Notes App (Quasar)",
        "files": "src/pages/Notes.vue, src/components/NoteEditor.vue, src/stores/notes.js, src-pwa/...",
        "steps": [
            ("Quasar PWA Setup", "quasar create app --kit pwa. Configure manifest.json."),
            ("Notes Store", "Pinia: notes array, addNote, editNote, deleteNote. localStorage persistence."),
            ("Notes List Page", "QList of notes with title, preview, date. Search bar. FAB to add."),
            ("NoteEditor Component", "QInput for title, QTextarea for content. Auto-save. Back button."),
            ("Offline Support", "Workbox config: cache app shell. Notes work offline (localStorage)."),
            ("Install Prompt", "beforeinstallprompt event. Custom install button in settings."),
            ("Manifest", "name, icons, theme_color, display: standalone. Test install."),
            ("Responsive", "Mobile-first. Desktop: list + editor side-by-side (master-detail)."),
        ],
        "checklist": [
            "Notes store with localStorage",
            "Notes list with search",
            "Note editor with auto-save",
            "Works offline (PWA)",
            "Installable (manifest + prompt)",
            "App icons configured",
            "Responsive (master-detail on desktop)",
            "Create/edit/delete notes",
        ],
    },
    "mini-19-electron-desktop-app": {
        "title": "Electron Desktop App (Quasar)",
        "files": "src/pages/Main.vue, src-electron/electron-main.js, src-electron/electron-preload.js, src/stores/app.js",
        "steps": [
            ("Quasar Electron Setup", "quasar mode add electron. Configure electron-main.js."),
            ("Main Process", "Create BrowserWindow. Set min/max size. Handle close (minimize to tray)."),
            ("Preload Bridge", "Expose file operations: readFile, saveFile, onMenuAction."),
            ("IPC Handlers", "File open/save dialogs. Read/write files. Recent files list."),
            ("App Menu", "File (New, Open, Save, Quit), Edit (Undo, Redo), View (Toggle DevTools)."),
            ("System Tray", "Tray icon with context menu (Show, Quit). Minimize to tray on close."),
            ("Main Page", "Simple text editor or note app. Uses IPC for file operations."),
            ("Auto-Update", "electron-updater setup. Check for updates on startup. Notify user."),
        ],
        "checklist": [
            "Electron main process configured",
            "Preload bridge (contextBridge)",
            "IPC handlers for file operations",
            "Application menu",
            "System tray with context menu",
            "Minimize to tray on close",
            "Main page with file operations",
            "Auto-update configured",
        ],
    },
    "medium-01-pricing-page": {
        "title": "Pricing Page with 3 Tiers",
        "files": "index.html, styles.css, script.js",
        "steps": [
            ("HTML Structure", "Header, pricing section with 3 cards, FAQ section, footer."),
            ("Pricing Cards", "3 tiers: Basic, Pro, Enterprise. Price, features list, CTA button."),
            ("Monthly/Yearly Toggle", "Toggle switch. JS updates prices. Save 20% on yearly badge."),
            ("Feature Comparison", "Feature list per tier. Checkmarks/X marks. Highlight popular tier."),
            ("FAQ Section", "Accordion FAQ. Click to expand/collapse. 5+ common questions."),
            ("CSS Styling", "Clean SaaS pricing design. Gradient on popular tier. Hover effects."),
            ("Responsive", "Cards stack on mobile. Side-by-side on desktop. Toggle works on both."),
            ("Animations", "Price change animation. Card hover lift. FAQ smooth expand."),
        ],
        "checklist": [
            "3 pricing tiers",
            "Monthly/yearly toggle",
            "Feature comparison per tier",
            "Popular tier highlighted",
            "FAQ accordion",
            "Responsive (stack on mobile)",
            "Hover effects",
            "Price change animation",
        ],
    },
    "medium-02-calculator-app": {
        "title": "Calculator App (Vanilla JS)",
        "files": "index.html, styles.css, script.js",
        "steps": [
            ("HTML Structure", "Display, number pad (0-9), operators (+, -, *, /), functions (C, =, +/-, %)."),
            ("CSS Grid Layout", "Grid for button layout. Display at top. Responsive sizing."),
            ("JS: Input Handling", "Click button → update display. Handle numbers, operators, decimals."),
            ("JS: Calculation", "Evaluate expression. Handle order of operations. Prevent invalid input."),
            ("Keyboard Support", "Map keys: 0-9, +, -, *, /, Enter (=), Escape (C), Backspace."),
            ("History", "Store last 10 calculations. Show in a dropdown or side panel. Click to reuse."),
            ("Theme Toggle", "Light/dark theme. CSS variables. Persist to localStorage."),
            ("Edge Cases", "Division by zero, max digits, consecutive operators, leading zeros."),
        ],
        "checklist": [
            "Number pad (0-9)",
            "Operators (+, -, *, /)",
            "Clear and equals",
            "Keyboard support",
            "Calculation history",
            "Light/dark theme",
            "Division by zero handling",
            "Responsive design",
        ],
    },
    "medium-03-recipe-finder": {
        "title": "Recipe Finder (React + API)",
        "files": "src/App.jsx, src/components/SearchBar.jsx, src/components/RecipeCard.jsx, src/components/RecipeModal.jsx, src/components/Favorites.jsx, src/hooks/useRecipes.js, src/hooks/useFavorites.js",
        "steps": [
            ("API Setup", "Use TheMealDB API (free, no key). useRecipes composable."),
            ("SearchBar", "Search by ingredient or dish name. Debounced. Recent searches dropdown."),
            ("RecipeCard", "Image, name, category, area. Click to view details. Favorite button (heart)."),
            ("RecipeModal", "Full recipe: ingredients with measurements, instructions, video link."),
            ("Favorites", "useFavorites hook with localStorage. Favorites page/tab. Remove favorite."),
            ("Filters", "Filter by category (dessert, main, etc.) and area (Italian, Mexican, etc.)."),
            ("Loading/Empty States", "Skeleton loading, no results message, error state with retry."),
            ("Responsive", "Grid of cards. Modal scrollable. Mobile-friendly."),
        ],
        "checklist": [
            "Search by name/ingredient",
            "Recipe cards in grid",
            "Recipe detail modal",
            "Favorites with localStorage",
            "Category and area filters",
            "Loading skeleton",
            "Empty and error states",
            "Responsive grid",
        ],
    },
    "medium-04-ecommerce-store": {
        "title": "E-commerce Store (React)",
        "files": "src/App.jsx, src/pages/Home.jsx, src/pages/ProductDetail.jsx, src/pages/Cart.jsx, src/pages/Checkout.jsx, src/stores/cart.js, src/components/ProductCard.jsx, src/components/Header.jsx",
        "steps": [
            ("Router Setup", "React Router: /, /product/:id, /cart, /checkout. Layout with header."),
            ("Product Data", "Mock product data (10+ products): id, name, price, image, category, description, stock."),
            ("Home Page", "Product grid with filters (category, price range). Sort (price, name). Search."),
            ("ProductCard", "Image, name, price, rating. Add to cart button. Hover effect. Link to detail."),
            ("ProductDetail", "Gallery, info, quantity selector, add to cart, reviews, related products."),
            ("Cart Store", "Zustand: items, addItem, removeItem, updateQty, total, clear. localStorage."),
            ("Cart Page", "List items with qty controls, remove button, subtotal, shipping, total. Checkout button."),
            ("Checkout Page", "Form: shipping address, payment (mock). Order summary. Place order → success page."),
            ("Header", "Logo, nav, search, cart icon with count badge. Responsive menu."),
            ("Responsive", "Grid adjusts columns. Cart stacks on mobile. Mobile nav menu."),
        ],
        "checklist": [
            "React Router with 4 pages",
            "Product grid with filters + sort",
            "Product detail page",
            "Cart with Zustand store",
            "Quantity controls in cart",
            "Checkout form (mock)",
            "Order success page",
            "Header with cart badge",
            "Responsive (mobile + desktop)",
            "localStorage cart persistence",
        ],
    },
    "medium-05-expense-tracker": {
        "title": "Expense Tracker (React)",
        "files": "src/App.jsx, src/components/Dashboard.jsx, src/components/AddExpense.jsx, src/components/ExpenseList.jsx, src/components/Charts.jsx, src/stores/expenses.js, src/hooks/useExpenses.js",
        "steps": [
            ("Expenses Store", "Zustand: expenses, addExpense, deleteExpense, categories. localStorage."),
            ("AddExpense Form", "Amount, category (select), date, description. Validation. Submit."),
            ("ExpenseList", "Table/list of expenses. Sort by date/amount. Filter by category. Delete."),
            ("Dashboard", "Total balance, income vs expenses, recent transactions. Summary cards."),
            ("Charts", "Pie chart (by category), bar chart (by month). Use recharts or chart.js."),
            ("Categories", "Custom categories. Color per category. Category management."),
            ("Budget", "Set monthly budget per category. Show progress bar. Alert when over budget."),
            ("Responsive", "Dashboard cards stack on mobile. Charts resize. Table → cards on mobile."),
        ],
        "checklist": [
            "Add expense with category",
            "Expense list with filters",
            "Dashboard with summary",
            "Pie chart by category",
            "Bar chart by month",
            "Budget tracking with alerts",
            "localStorage persistence",
            "Responsive design",
        ],
    },
    "medium-06-crud-api-auth": {
        "title": "CRUD API with Auth (FastAPI)",
        "files": "main.py, models.py, schemas.py, database.py, auth.py, crud.py, dependencies.py",
        "steps": [
            ("Database Setup", "SQLAlchemy + SQLite. User model, Item model. Relationship (user → items)."),
            ("Auth System", "JWT tokens. register, login endpoints. Password hashing (bcrypt)."),
            ("Dependencies", "get_current_user: decode JWT, fetch user. Optional vs required auth."),
            ("User Endpoints", "POST /register, POST /login, GET /me, PUT /me (update profile)."),
            ("Item CRUD", "POST /items (auth required), GET /items (public), GET /items/{id}, PUT, DELETE (owner only)."),
            ("Validation", "Pydantic schemas. Email validation, password strength, item fields."),
            ("Rate Limiting", "SlowAPI or custom: limit requests per IP. Prevent abuse."),
            ("Testing", "pytest: test auth flow, CRUD operations, unauthorized access, owner checks."),
            ("Documentation", "OpenAPI docs. Security scheme (Bearer JWT). Examples in descriptions."),
        ],
        "checklist": [
            "JWT authentication",
            "Password hashing (bcrypt)",
            "Register + login endpoints",
            "User profile endpoints",
            "Item CRUD (owner-only edit/delete)",
            "Pydantic validation",
            "Rate limiting",
            "Tests with pytest",
            "OpenAPI docs with security",
        ],
    },
    "medium-07-spam-classifier": {
        "title": "Spam Classifier (ML)",
        "files": "data_loader.py, preprocess.py, model.py, train.py, predict.py, app.py",
        "steps": [
            ("Dataset", "Use SMS Spam Collection or Enron dataset. Load, explore class distribution."),
            ("Text Preprocessing", "Lowercase, remove punctuation, tokenize, remove stopwords, lemmatize."),
            ("Vectorization", "TF-IDF vectorizer. Fit on training data. ngram_range=(1,2)."),
            ("Train Models", "Naive Bayes baseline. Logistic Regression. Compare with cross-validation."),
            ("Evaluate", "Accuracy, precision, recall, F1, confusion matrix. ROC curve. Class imbalance handling."),
            ("Hyperparameter Tuning", "GridSearchCV: alpha for NB, C for LR. Tune TF-IDF params."),
            ("Save Pipeline", "joblib: save vectorizer + model as a pipeline. Load for prediction."),
            ("Prediction API", "FastAPI: POST /classify with text → {is_spam, probability}. Test with examples."),
            ("Testing", "Test with real spam/ham examples. Edge cases: empty, very long, emoji-only."),
        ],
        "checklist": [
            "Dataset loaded and explored",
            "Text preprocessing pipeline",
            "TF-IDF vectorization",
            "Naive Bayes + Logistic Regression",
            "Cross-validation",
            "Precision/recall/F1/confusion matrix",
            "Hyperparameter tuning",
            "Model saved as pipeline",
            "FastAPI classification endpoint",
            "Tested with real examples",
        ],
    },
    "medium-08-image-classifier-api": {
        "title": "Image Classifier API (PyTorch)",
        "files": "model.py, dataset.py, train.py, predict.py, app.py",
        "steps": [
            ("Dataset", "Use CIFAR-10 or a custom dataset. Train/val/test split. DataLoaders."),
            ("Model Architecture", "Simple CNN: conv layers, pooling, FC. Or use transfer learning (ResNet18)."),
            ("Training Loop", "Forward, loss, backward, step. Track loss and accuracy per epoch. Save best."),
            ("Data Augmentation", "Random crop, flip, rotation, color jitter. Improve generalization."),
            ("Evaluation", "Accuracy, per-class precision/recall, confusion matrix. Visualize predictions."),
            ("Save Model", "torch.save model state_dict. Save class names. Load function."),
            ("Prediction Function", "Load model, preprocess image, predict, return class + confidence."),
            ("FastAPI Endpoint", "POST /classify accepts image file → {class, confidence, all_probs}."),
            ("Testing", "Test with real images. Handle different formats, sizes, invalid inputs."),
        ],
        "checklist": [
            "Dataset with DataLoaders",
            "CNN model (or transfer learning)",
            "Training loop with tracking",
            "Data augmentation",
            "Evaluation (accuracy, per-class)",
            "Confusion matrix",
            "Model saved and loadable",
            "FastAPI image classification endpoint",
            "Handles various image formats",
            "Tested with real images",
        ],
    },
    "medium-09-quasar-admin-dashboard": {
        "title": "Quasar Admin Dashboard",
        "files": "src/layouts/AdminLayout.vue, src/pages/Dashboard.vue, src/pages/Users.vue, src/pages/Products.vue, src/pages/Settings.vue, src/stores/...",
        "steps": [
            ("Layout", "QLayout with QDrawer (sidebar), QHeader (topbar), QPageContainer. Responsive."),
            ("Sidebar Navigation", "QList with QItems. Routes: Dashboard, Users, Products, Settings. Active state."),
            ("Dashboard Page", "Stat cards (users, revenue, orders). Charts (line, bar, pie). Recent activity table."),
            ("Users Page", "QTable with server-side pagination, search, sort. CRUD with dialogs. Role badges."),
            ("Products Page", "QTable with image thumbnails, price, stock. Add/edit dialog with image upload."),
            ("Settings Page", "Theme toggle, notification prefs, API settings. Persist to Pinia + localStorage."),
            ("Auth", "Login page. JWT in localStorage. Route guards. Logout. Protected routes."),
            ("API Integration", "Axios instance with interceptors. Services for users, products, stats."),
            ("Responsive", "Sidebar collapses on mobile (mini mode or overlay). Tables scroll. Cards stack."),
        ],
        "checklist": [
            "Admin layout with sidebar",
            "Dashboard with stat cards + charts",
            "Users page with QTable (server-side)",
            "Products page with CRUD",
            "Settings page",
            "Login + auth + route guards",
            "Axios with interceptors",
            "Responsive (sidebar collapses)",
            "Notifications on CRUD actions",
        ],
    },
    "medium-10-cross-platform-task-manager": {
        "title": "Cross-Platform Task Manager (Quasar)",
        "files": "src/pages/Tasks.vue, src/pages/Projects.vue, src/pages/Calendar.vue, src/stores/tasks.js, src/stores/projects.js",
        "steps": [
            ("Quasar Setup", "Create app with PWA + Capacitor + Electron modes. Configure all three."),
            ("Task Store", "Pinia: tasks, projects, addTask, updateTask, deleteTask, toggleComplete. localStorage + sync."),
            ("Tasks Page", "Kanban board (todo, in-progress, done). Drag between columns. Or list view toggle."),
            ("Projects Page", "List of projects. Each with task count, progress bar. Create/edit/delete."),
            ("Calendar Page", "Monthly calendar with tasks on due dates. Click date to see tasks. QCalendar or custom."),
            ("Notifications", "Notify when task due. Push notifications (PWA/Capacitor). Reminders."),
            ("Offline Sync", "Work offline. Queue changes. Sync when online. Conflict resolution."),
            ("Mobile Features", "Swipe to complete/delete. Long-press for options. Bottom sheet actions."),
            ("Desktop Features", "Keyboard shortcuts. System tray. Window menu. Minimize to tray."),
            ("Responsive", "Kanban → list on mobile. Sidebar → bottom tabs. Touch-friendly on mobile."),
        ],
        "checklist": [
            "Works on web, mobile (Capacitor), desktop (Electron)",
            "Kanban board with drag-and-drop",
            "Projects with progress tracking",
            "Calendar view with due dates",
            "Task notifications/reminders",
            "Offline support with sync",
            "Mobile gestures (swipe, long-press)",
            "Desktop features (tray, shortcuts)",
            "Responsive across all platforms",
        ],
    },
    "capstone-01-portfolio-website": {
        "title": "Portfolio Website (React)",
        "files": "src/App.jsx, src/pages/Home.jsx, src/pages/Projects.jsx, src/pages/About.jsx, src/pages/Contact.jsx, src/components/ProjectCard.jsx, src/components/Skills.jsx, src/components/Navbar.jsx",
        "steps": [
            ("Design System", "Define colors, typography, spacing. Create a theme. Use CSS variables or Tailwind."),
            ("Layout + Routing", "React Router: /, /projects, /project/:id, /about, /contact. Shared layout."),
            ("Home/Hero", "Name, title, tagline, CTA buttons (View Work, Contact). Animated entrance."),
            ("Projects Page", "Grid of project cards. Filter by tech stack. Search. Link to detail pages."),
            ("Project Detail", "Images, description, tech stack, live link, GitHub link. Markdown content."),
            ("About Page", "Bio, skills (with icons), experience timeline, education. Download CV button."),
            ("Contact Page", "Contact form (name, email, message). Form validation. EmailJS or backend API."),
            ("Navbar", "Sticky, responsive. Mobile: hamburger menu. Active link highlight. Smooth scroll."),
            ("Animations", "Scroll animations (fade in, slide up). Hover effects. Page transitions."),
            ("SEO + Performance", "Meta tags, Open Graph, sitemap. Lazy load images. Lighthouse 90+."),
            ("Deploy", "Deploy to Vercel/Netlify. Custom domain. HTTPS. Analytics (optional)."),
        ],
        "checklist": [
            "React Router with 5 pages",
            "Hero section with CTA",
            "Projects grid with filters",
            "Project detail pages",
            "About page with skills + timeline",
            "Contact form with validation",
            "Responsive navbar (mobile menu)",
            "Scroll animations",
            "SEO meta tags + Open Graph",
            "Lighthouse score 90+",
            "Deployed to Vercel/Netlify",
        ],
    },
    "capstone-02-social-dashboard": {
        "title": "Social Dashboard (React + FastAPI)",
        "files": "frontend/src/..., backend/main.py, backend/models.py, backend/auth.py",
        "steps": [
            ("Backend Setup", "FastAPI + SQLAlchemy + PostgreSQL/SQLite. User, Post, Comment, Like models."),
            ("Auth Backend", "JWT auth. Register, login, get current user. Password hashing. Rate limiting."),
            ("Posts API", "CRUD for posts. Pagination. Like/unlike. Comments. Feed (following's posts)."),
            ("Frontend Setup", "React + Router + Zustand. Axios instance with auth interceptor."),
            ("Auth Frontend", "Login/register pages. Protected routes. Auth context/store. Token refresh."),
            ("Feed Page", "Infinite scroll feed. Post cards with like, comment, share. Create post."),
            ("Profile Page", "User info, posts grid, edit profile, follow/unfollow. Avatar upload."),
            ("Notifications", "Real-time notifications (WebSocket or polling). Like/comment notifications."),
            ("Search", "Search users and posts. Hashtag support. Trending posts."),
            ("Responsive", "Mobile: bottom nav, single column. Desktop: sidebar + feed + suggestions."),
            ("Deploy", "Backend: Railway/Render. Frontend: Vercel. Environment variables. CORS configured."),
        ],
        "checklist": [
            "FastAPI backend with auth",
            "Posts CRUD with likes + comments",
            "React frontend with auth",
            "Infinite scroll feed",
            "Profile pages with follow",
            "Real-time notifications",
            "Search + hashtags",
            "Responsive (mobile + desktop)",
            "Deployed (backend + frontend)",
            "CORS + environment variables",
        ],
    },
    "capstone-03-task-api": {
        "title": "Task Management API (FastAPI)",
        "files": "main.py, models.py, schemas.py, database.py, auth.py, tasks.py, projects.py, websockets.py, tests/",
        "steps": [
            ("Database Design", "Users, Projects, Tasks, Comments, Tags. Relationships. Migrations with Alembic."),
            ("Auth System", "JWT + refresh tokens. Role-based access (admin, member). OAuth2 password flow."),
            ("Project Endpoints", "CRUD projects. Members. Roles. Invite by email. Leave project."),
            ("Task Endpoints", "CRUD tasks. Assign to user. Status (todo/in-progress/done). Priority. Due date."),
            ("Comments + Tags", "Comments on tasks. Tags for categorization. Filter by tag. @mentions."),
            ("WebSocket", "Real-time task updates. Notify on assign, status change, comment. Connected clients."),
            ("File Uploads", "Attach files to tasks. Upload to S3 or local. Download endpoint."),
            ("Search + Filter", "Search tasks by name/description. Filter by status, assignee, priority, due date."),
            ("Pagination + Sorting", "Cursor or offset pagination. Sort by any field. Include total count."),
            ("Testing", "pytest: unit tests, integration tests, auth tests, WebSocket tests. 80%+ coverage."),
            ("Documentation", "OpenAPI with examples. WebSocket docs. Postman collection. README with setup."),
            ("Deploy", "Docker + docker-compose. PostgreSQL. Gunicorn + uvicorn workers. CI/CD pipeline."),
        ],
        "checklist": [
            "Database with 5+ models and relationships",
            "JWT auth with refresh tokens",
            "Role-based access control",
            "Project CRUD with members",
            "Task CRUD with assign/status/priority",
            "Comments and tags",
            "WebSocket real-time updates",
            "File uploads",
            "Search + filter + pagination",
            "Tests with 80%+ coverage",
            "Docker deployment",
            "CI/CD pipeline",
        ],
    },
    "capstone-04-ml-pipeline": {
        "title": "End-to-End ML Pipeline",
        "files": "pipeline/, data/, models/, tests/, config.yaml, Dockerfile",
        "steps": [
            ("Project Structure", "Modular: data/, features/, models/, evaluation/, deployment/. Config.yaml."),
            ("Data Ingestion", "Download from S3/API/DB. Validate schema. Version with DVC. Train/test split."),
            ("Data Processing", "Clean, handle missing values, feature engineering. Save processed data. Reproducible."),
            ("Feature Store", "Create features. Save to feature store (Feast or simple parquet). Reuse across models."),
            ("Model Training", "Train multiple models (LR, RF, XGBoost). Track with MLflow. Hyperparameter tuning."),
            ("Evaluation", "Cross-validation. Multiple metrics. Compare models. Select best. Feature importance."),
            ("Model Registry", "Register model with MLflow. Versioning. Stage (staging/production). Approval workflow."),
            ("Deployment", "FastAPI app serving the model. Batch prediction endpoint. Health check."),
            ("Monitoring", "Track predictions, data drift, model performance. Alert on degradation."),
            ("CI/CD", "GitHub Actions: run tests, train model, register, deploy. DVC for data versioning."),
            ("Docker", "Dockerfile for API. docker-compose for full stack (API + MLflow + DB)."),
            ("Documentation", "README with architecture diagram. API docs. Run instructions. Model card."),
        ],
        "checklist": [
            "Modular project structure",
            "Data ingestion + validation",
            "Data processing pipeline",
            "Feature engineering + store",
            "Multiple models trained",
            "MLflow experiment tracking",
            "Hyperparameter tuning",
            "Model evaluation + comparison",
            "Model registry + versioning",
            "FastAPI serving endpoint",
            "Monitoring (drift, performance)",
            "CI/CD pipeline",
            "Docker deployment",
            "Documentation + model card",
        ],
    },
    "capstone-05-saas-app": {
        "title": "SaaS App (Quasar + FastAPI)",
        "files": "frontend/src/..., backend/main.py, backend/models.py, backend/auth.py, backend/billing.py",
        "steps": [
            ("Backend Setup", "FastAPI + PostgreSQL + SQLAlchemy + Alembic. Multi-tenant architecture."),
            ("Auth System", "JWT + refresh. Email verification. Password reset. OAuth (Google/GitHub)."),
            ("Subscription/Billing", "Stripe integration. Plans (Free, Pro, Enterprise). Webhooks. Usage limits."),
            ("Tenant Management", "Organizations. Members. Roles (owner/admin/member). Invitations."),
            ("Core Feature", "Pick one: task manager, CRM, or analytics dashboard. Full CRUD + business logic."),
            ("Frontend Setup", "Quasar + Vue 3 + Pinia + Vue Router. Axios with interceptors. Auth guard."),
            ("Auth Frontend", "Login, register, forgot password, email verify. Protected routes. Token refresh."),
            ("Dashboard", "Overview with stats, charts, recent activity. Role-based content."),
            ("Settings", "Profile, organization, billing, team members, API keys, notifications."),
            ("Pricing Page", "Public pricing page. Stripe checkout. Plan upgrade/downgrade. Usage display."),
            ("Responsive + Cross-Platform", "Works on web, PWA, mobile (Capacitor). Responsive layout."),
            ("Deploy", "Backend: Railway/Render. Frontend: Vercel/Netlify. DB: managed PostgreSQL. CI/CD."),
        ],
        "checklist": [
            "Multi-tenant backend (FastAPI + PostgreSQL)",
            "JWT auth + email verification + OAuth",
            "Stripe billing + subscriptions",
            "Organization + members + roles",
            "Core SaaS feature (full CRUD)",
            "Quasar frontend with auth",
            "Dashboard with charts",
            "Settings page (profile, billing, team)",
            "Public pricing page + checkout",
            "Responsive + PWA + mobile-ready",
            "Deployed (backend + frontend + DB)",
            "CI/CD pipeline",
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
5. **Hardcoding values** — use environment variables for API keys, URLs, and configuration.
"""
    with open(filepath, 'w') as f:
        f.write(content)
    return filepath

# Generate all breakdowns
for project_name, data in BREAKDOWNS.items():
    path = generate_breakdown(project_name, data)
    print(f"  Generated: {os.path.basename(path)}")

print(f"\nGenerated {len(BREAKDOWNS)} task breakdowns")
