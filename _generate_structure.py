#!/usr/bin/env python3
"""
Generate the full folder structure + problem file stubs for all 100 lessons
and 34 sellable projects. Does NOT write content — just creates the skeleton.
Content (concepts.md, task-explanation.md, coding-check.md) is added separately.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# ─── Lesson definitions for all 5 subjects ───────────────────────────────

LESSONS = {
    "html-css-javascript": [
        ("html-structure", "HTML Structure & Semantic Tags", "html"),
        ("html-forms-inputs", "HTML Forms & Input Types", "html"),
        ("html-tables-data", "HTML Tables & Data Display", "html"),
        ("html-media-embedding", "HTML Media & Embedding", "html"),
        ("html-accessibility", "HTML Accessibility Deep Dive", "html"),
        ("css-selectors-specificity", "CSS Selectors & Specificity", "css"),
        ("css-box-model", "Box Model & Spacing", "css"),
        ("css-typography", "CSS Text & Typography", "css"),
        ("css-colors-backgrounds", "CSS Colors & Backgrounds", "css"),
        ("css-flexbox", "CSS Flexbox Layout", "css"),
        ("css-grid", "CSS Grid Layout", "css"),
        ("css-responsive", "CSS Responsive Design", "css"),
        ("css-animations", "CSS Animations & Transitions", "css"),
        ("css-variables", "CSS Variables & Custom Properties", "css"),
        ("css-pseudo", "CSS Pseudo-classes & Pseudo-elements", "css"),
        ("js-variables-types", "JS Variables, Types & Operators", "js"),
        ("js-functions-control-flow", "JS Functions & Control Flow", "js"),
        ("js-arrays-methods", "JS Arrays & Array Methods", "js"),
        ("js-objects-dom", "JS Objects & DOM Manipulation", "js"),
        ("js-events", "JS Events & Event Handling", "js"),
    ],
    "react": [
        ("components-jsx-props", "Components, JSX & Props", "jsx"),
        ("state-usestate", "State & useState", "jsx"),
        ("event-handling", "Event Handling in React", "jsx"),
        ("conditional-rendering", "Conditional Rendering", "jsx"),
        ("lists-keys", "Lists & Keys", "jsx"),
        ("useeffect-side-effects", "useEffect & Side Effects", "jsx"),
        ("forms-controlled", "Forms & Controlled Components", "jsx"),
        ("useref-dom", "useRef & DOM Access", "jsx"),
        ("usememo-usecallback", "useMemo & useCallback", "jsx"),
        ("custom-hooks", "Custom Hooks", "jsx"),
        ("context-api", "Context API", "jsx"),
        ("usereducer", "useReducer & Complex State", "jsx"),
        ("react-router", "React Router", "jsx"),
        ("error-boundaries-suspense", "Error Boundaries & Suspense", "jsx"),
        ("portals-modals", "Portals & Modals", "jsx"),
        ("react-query", "API Integration with React Query", "jsx"),
        ("zustand", "State Management with Zustand", "jsx"),
        ("tailwind-css", "Styling: Tailwind CSS", "jsx"),
        ("testing-react", "Testing React Components", "jsx"),
        ("react-performance", "React Performance & Profiling", "jsx"),
    ],
    "python": [
        ("variables-types-functions", "Variables, Types & Functions", "py"),
        ("strings-methods", "Strings & String Methods", "py"),
        ("lists-tuples", "Lists & Tuples", "py"),
        ("dicts-sets", "Dictionaries & Sets", "py"),
        ("control-flow-loops", "Control Flow & Loops", "py"),
        ("functions-deep-dive", "Functions Deep Dive", "py"),
        ("file-io-error-handling", "File I/O & Error Handling", "py"),
        ("comprehensions-generators", "List Comprehensions & Generators", "py"),
        ("oop-basics", "OOP Basics", "py"),
        ("oop-advanced", "OOP Advanced", "py"),
        ("modules-packages", "Modules & Packages", "py"),
        ("decorators", "Decorators", "py"),
        ("iterators-generators", "Iterators & Generators", "py"),
        ("async-concurrency", "Async/Await & Concurrency", "py"),
        ("testing-pytest", "Testing with pytest", "py"),
        ("rest-apis", "Working with REST APIs", "py"),
        ("database-sqlite", "Database Basics (SQLite)", "py"),
        ("flask-server", "Flask Web Server", "py"),
        ("fastapi-server", "FastAPI REST Server", "py"),
        ("pandas-data", "Data Processing with Pandas", "py"),
    ],
    "ai-ml": [
        ("what-is-ml", "What is ML?", "py"),
        ("data-preprocessing", "Data Preprocessing", "py"),
        ("numpy-fundamentals", "NumPy Fundamentals", "py"),
        ("pandas-for-ml", "Pandas for ML", "py"),
        ("data-visualization", "Data Visualization", "py"),
        ("linear-regression", "Linear Regression", "py"),
        ("logistic-regression", "Logistic Regression", "py"),
        ("decision-trees-forests", "Decision Trees & Random Forests", "py"),
        ("evaluation-metrics", "Model Evaluation Deep Dive", "py"),
        ("cross-validation-tuning", "Cross-Validation & Tuning", "py"),
        ("feature-engineering", "Feature Engineering", "py"),
        ("imbalanced-data", "Handling Imbalanced Data", "py"),
        ("svm-knn", "SVM & KNN", "py"),
        ("gradient-boosting", "Gradient Boosting (XGBoost)", "py"),
        ("unsupervised-learning", "Unsupervised Learning", "py"),
        ("neural-networks", "Neural Networks Basics", "py"),
        ("pytorch-fundamentals", "PyTorch Fundamentals", "py"),
        ("cnn-image-classification", "CNNs for Image Classification", "py"),
        ("model-deployment", "Model Deployment", "py"),
        ("llm-prompt-engineering", "LLMs & Prompt Engineering", "py"),
    ],
    "quasar": [
        ("quasar-basics", "Quasar Basics", "vue"),
        ("quasar-layout", "Quasar Layout System", "vue"),
        ("quasar-components", "Quasar Components Deep Dive", "vue"),
        ("vue-composition-api", "Vue 3 Composition API", "vue"),
        ("vue-reactivity", "Vue Reactivity System", "vue"),
        ("vue-router-quasar", "Vue Router in Quasar", "vue"),
        ("pinia-state", "Pinia State Management", "vue"),
        ("quasar-plugins", "Quasar Plugins", "vue"),
        ("quasar-forms", "Quasar Form Components", "vue"),
        ("api-integration-quasar", "API Integration in Quasar", "vue"),
        ("quasar-tables-data", "Quasar Tables & Data", "vue"),
        ("quasar-icons-theming", "Quasar Icons & Theming", "vue"),
        ("quasar-animations", "Quasar Animations & Transitions", "vue"),
        ("quasar-notifications-dialogs", "Quasar Notifications & Dialogs", "vue"),
        ("quasar-pwa", "Quasar PWA Mode", "vue"),
        ("quasar-mobile", "Quasar Mobile (Capacitor)", "vue"),
        ("quasar-electron", "Quasar Electron (Desktop)", "vue"),
        ("quasar-ssr", "Quasar SSR", "vue"),
        ("testing-quasar", "Testing in Quasar", "vue"),
        ("quasar-deployment", "Quasar App Deployment", "vue"),
    ],
}

# ─── Problem definitions per difficulty ──────────────────────────────────
# Each lesson gets 3 easy, 3 medium, 3 hard problems.
# Problem names are generic — actual content is filled in later.

EASY_PROBLEMS = ["p01", "p02", "p03"]
MEDIUM_PROBLEMS = ["p01", "p02", "p03"]
HARD_PROBLEMS = ["p01", "p02", "p03"]

# ─── Comment styles per file extension ───────────────────────────────────

COMMENT_STYLES = {
    "py":   ('"""', '"""', '# '),
    "js":   ('/*', '*/', '// '),
    "jsx":  ('/*', '*/', '// '),
    "html": ('<!--', '-->', '<!-- '),
    "css":  ('/*', '*/', '/* '),
    "vue":  ('<!--', '-->', '<!-- '),
}

# ─── Project definitions ─────────────────────────────────────────────────

PROJECTS = [
    # Mini projects (after every 5 lessons per subject)
    ("mini", "mini-01-accessible-contact-form", "HTML/CSS/JS", "Accessible Contact Form Page", "$50-100"),
    ("mini", "mini-02-flexbox-landing-page", "HTML/CSS/JS", "Landing Page with Flexbox", "$100-200"),
    ("mini", "mini-03-responsive-gallery", "HTML/CSS/JS", "Responsive Image Gallery", "$100-200"),
    ("mini", "mini-04-interactive-todo", "HTML/CSS/JS", "Interactive Todo List (vanilla JS)", "$100-200"),
    ("mini", "mini-05-react-todo", "React", "React Todo App", "$100-200"),
    ("mini", "mini-06-movie-search", "React", "Movie Search App", "$100-200"),
    ("mini", "mini-07-multi-page-blog", "React", "Multi-Page Blog", "$100-200"),
    ("mini", "mini-08-ecommerce-product-page", "React", "E-commerce Product Page", "$100-200"),
    ("mini", "mini-09-cli-contact-book", "Python", "CLI Contact Book", "$50-100"),
    ("mini", "mini-10-file-organizer", "Python", "File Organizer Script", "$50-150"),
    ("mini", "mini-11-web-scraper", "Python", "Web Scraper with Async", "$100-200"),
    ("mini", "mini-12-fastapi-rest", "Python", "REST API with FastAPI", "$100-200"),
    ("mini", "mini-13-data-cleaning-pipeline", "AI/ML", "Data Cleaning Pipeline", "$50-150"),
    ("mini", "mini-14-house-price-predictor", "AI/ML", "House Price Predictor", "$100-200"),
    ("mini", "mini-15-customer-segmentation", "AI/ML", "Customer Segmentation", "$100-200"),
    ("mini", "mini-16-quasar-settings-page", "Quasar", "Quasar Settings Page", "$50-150"),
    ("mini", "mini-17-quasar-weather-app", "Quasar", "Quasar Weather App", "$100-200"),
    ("mini", "mini-18-pwa-notes-app", "Quasar", "PWA Notes App", "$100-200"),
    ("mini", "mini-19-electron-desktop-app", "Quasar", "Desktop App with Electron", "$150-300"),
    # Medium projects (after every 10 lessons per subject)
    ("medium", "medium-01-pricing-page", "HTML/CSS/JS", "Pricing Page with 3 Tiers", "$200-400"),
    ("medium", "medium-02-calculator-app", "HTML/CSS/JS", "Dynamic Calculator App", "$200-400"),
    ("medium", "medium-03-recipe-finder", "React", "Recipe Finder with Filters", "$200-500"),
    ("medium", "medium-04-ecommerce-store", "React", "Full E-commerce Store Front", "$300-500"),
    ("medium", "medium-05-expense-tracker", "Python", "Expense Tracker CLI", "$200-400"),
    ("medium", "medium-06-crud-api-auth", "Python", "Full CRUD API with Auth", "$300-500"),
    ("medium", "medium-07-spam-classifier", "AI/ML", "Spam Classifier", "$200-500"),
    ("medium", "medium-08-image-classifier-api", "AI/ML", "Image Classifier API", "$300-500"),
    ("medium", "medium-09-quasar-admin-dashboard", "Quasar", "Quasar Admin Dashboard", "$300-500"),
    ("medium", "medium-10-cross-platform-task-manager", "Quasar", "Cross-Platform Task Manager", "$300-600"),
    # Capstone projects (end of each subject)
    ("capstone", "capstone-01-portfolio-website", "HTML/CSS/JS", "Personal Portfolio Website", "$500-1000"),
    ("capstone", "capstone-02-social-dashboard", "React", "Social Media Dashboard", "$500-1500"),
    ("capstone", "capstone-03-task-api", "Python", "Full-Stack Task Management API", "$500-1500"),
    ("capstone", "capstone-04-ml-pipeline", "AI/ML", "End-to-End ML Pipeline", "$1000-2000"),
    ("capstone", "capstone-05-saas-app", "Quasar", "Full SaaS App with Quasar", "$1000-2000"),
]


def make_problem_file(filepath, ext, lesson_num, lesson_name, difficulty, prob_num):
    """Create a problem file stub with TODO marker."""
    open_comment, close_comment, line_comment = COMMENT_STYLES[ext]

    title = f"PROBLEM: {lesson_name} — {difficulty.title()} P{prob_num[1:]}"
    concept_line = f"CONCEPT: See concepts.md for the full list of concepts in this lesson."

    if ext in ("py",):
        content = f'''{open_comment}
{title}
{"=" * len(title)}

{concept_line}

# See concepts.md in this lesson folder for detailed explanations (WHY/WHERE/WHAT-GOES-WRONG).

{close_comment}

# TODO: Write your complete solution from scratch below (function signature + body).
#       Remove this TODO line when done.
'''
    elif ext in ("js", "jsx"):
        content = f'''{open_comment}
{title}
{"=" * len(title)}

{concept_line}

// See concepts.md in this lesson folder for detailed explanations (WHY/WHERE/WHAT-GOES-WRONG).

{close_comment}

// TODO: Write your complete solution from scratch below.
//       Remove this TODO line when done.
'''
    elif ext in ("html", "css"):
        content = f'''{open_comment}
{title}
{"=" * len(title)}

{concept_line}

See concepts.md in this lesson folder for detailed explanations (WHY/WHERE/WHAT-GOES-WRONG).
{close_comment}

<!-- TODO: Write your complete solution from scratch below. -->
<!--       Remove this TODO comment when done. -->
'''
    elif ext == "vue":
        content = f'''{open_comment}
{title}
{"=" * len(title)}

{concept_line}

See concepts.md in this lesson folder for detailed explanations (WHY/WHERE/WHAT-GOES-WRONG).
{close_comment}

<template>
  <!-- TODO: Write your complete solution from scratch below. -->
  <!--       Remove this TODO comment when done. -->
</template>

<script setup>
// TODO: Add your script logic here.
</script>

<style scoped>
/* TODO: Add your styles here. */
</style>
'''
    else:
        content = f"{line_comment} TODO: Write your solution here.\n"

    with open(filepath, "w") as f:
        f.write(content)


def make_project_readme(project_dir, ptype, name, subject, title, price):
    """Create a project README with brief, requirements, and sellable pitch."""
    content = f'''# {title}

> **Type:** {ptype.title()} Project
> **Subject:** {subject}
> **Estimated sell price:** {price}
> **Difficulty:** {"Beginner" if ptype == "mini" else "Intermediate" if ptype == "medium" else "Advanced"}

## Project Brief

{title} — a {ptype} project you can build, polish, and sell to clients or use in your portfolio.

## What you'll build

(Detailed requirements will be filled in per project.)

## Skills you'll demonstrate

- (Filled in per project)

## Sellable pitch

(Draft pitch for selling this to a client or showcasing in your portfolio.)

## Requirements

- [ ] (Filled in per project)

## Getting started

1. Read the requirements above.
2. Plan your architecture before coding.
3. Build incrementally — get a working version first, then polish.
4. Test with real inputs.
5. Document your code and write a README for the end product.

## Deliverables

- Working code
- README with setup instructions
- Screenshots/demo
- (If applicable) live deployment link
'''
    with open(os.path.join(project_dir, "README.md"), "w") as f:
        f.write(content)


def main():
    lessons_created = 0
    problems_created = 0
    projects_created = 0

    # ─── Create lesson folders + problem stubs ───────────────────────────
    for subject, lesson_list in LESSONS.items():
        for idx, (slug, name, ext) in enumerate(lesson_list, 1):
            lesson_num = f"{idx:02d}"
            lesson_dir_name = f"lesson-{lesson_num}-{slug}"
            lesson_path = os.path.join(ROOT, subject, lesson_dir_name)

            # Skip if lesson 01 already exists (it has content)
            is_lesson_01 = (idx == 1)

            # Create difficulty subfolders
            for difficulty, problems in [("easy", EASY_PROBLEMS),
                                          ("medium", MEDIUM_PROBLEMS),
                                          ("hard", HARD_PROBLEMS)]:
                diff_path = os.path.join(lesson_path, difficulty)
                os.makedirs(diff_path, exist_ok=True)

                # Create problem file stubs
                for prob in problems:
                    filename = f"{prob}-solve.{ext}"
                    filepath = os.path.join(diff_path, filename)

                    # Only create if doesn't exist (don't overwrite lesson 01)
                    if not os.path.exists(filepath):
                        make_problem_file(filepath, ext, lesson_num, name, difficulty, prob)
                        problems_created += 1

            # Create placeholder content files if they don't exist
            for content_file in ["concepts.md", "task-explanation.md", "coding-check.md"]:
                fpath = os.path.join(lesson_path, content_file)
                if not os.path.exists(fpath):
                    with open(fpath, "w") as f:
                        f.write(f"# Lesson {lesson_num} — {name}\n\n> Content to be filled in.\n")

            lessons_created += 1

    # ─── Create project folders + READMEs ────────────────────────────────
    projects_root = os.path.join(ROOT, "projects")
    os.makedirs(projects_root, exist_ok=True)

    for ptype, slug, subject, title, price in PROJECTS:
        project_dir = os.path.join(projects_root, slug)
        os.makedirs(project_dir, exist_ok=True)

        readme_path = os.path.join(project_dir, "README.md")
        if not os.path.exists(readme_path):
            make_project_readme(project_dir, ptype, slug, subject, title, price)
            projects_created += 1

    print(f"Created {lessons_created} lessons, {problems_created} problem stubs, {projects_created} projects")


if __name__ == "__main__":
    main()
