"""
Auto-Check System — Lesson 20: Quasar Deployment
=================================================
Solutions here include .js, .txt, .yml, and .md files. .js files get a
parse-only syntax check via `node --check` when available. Everything is
then verified STRUCTURALLY.

Usage:
    python3 check.py easy/p01     # check one problem
    python3 check.py all          # check all problems
"""

import glob
import os
import re
import shutil
import subprocess
import sys

LESSON_DIR = os.path.dirname(os.path.abspath(__file__))

NODE = "/home/akash-dev/.nvm/versions/node/v22.23.2/bin/node"
if not os.path.isfile(NODE):
    NODE = shutil.which("node")


def read_body(path):
    """Read a solution file, stripping the leading instructional comment so
    hint text in the problem description isn't mistaken for real code."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    content = re.sub(r"^\s*<!--.*?-->", "", content, count=1, flags=re.DOTALL)
    content = re.sub(r"^\s*/\*.*?\*/", "", content, count=1, flags=re.DOTALL)
    # For #-comment files (.yml, .txt), drop the leading instruction block
    if path.endswith((".yml", ".yaml", ".txt")):
        content = re.sub(r"^\s*(#.*\n)+", "", content)
    return content


def js_syntax_ok(path):
    """Parse-only syntax check via `node --check` (does NOT execute, so
    unresolved imports are fine). Skipped if node is missing."""
    if not NODE:
        return True, "node not found — skipped syntax check"
    try:
        result = subprocess.run(
            [NODE, "--check", path],
            capture_output=True, text=True, timeout=15,
        )
    except Exception as e:
        if "NoneType" in str(e):
            print(f"FAIL — a function returned None — write the body!")
        else:
            return True, f"syntax check skipped ({e})"
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip().splitlines()
        return False, "syntax error: " + (detail[0] if detail else "unknown")
    return True, "ok"


def require_all(path, checks, syntax=True):
    """checks: list of (label, regex). Returns (passed, message)."""
    if not os.path.isfile(path):
        return False, f"file not found: {path}"
    if syntax and path.endswith((".js", ".mjs", ".ts")):
        ok, msg = js_syntax_ok(path)
        if not ok:
            return False, msg
    body = read_body(path)
    if len(body.strip()) < 30:
        return False, "file looks empty — write your solution first"
    for label, pattern in checks:
        if not re.search(pattern, body):
            return False, f"missing {label} (expected pattern: {pattern})"
    return True, "All tests passed!"


def check_easy_p01(path):
    """SPA build config: publicPath, sourcemap off, gzip, env vars."""
    return require_all(path, [
        ("build section", r"build\s*[:{]"),
        ("publicPath", r"publicPath"),
        ("sourcemap disabled", r"sourcemap|sourceMap"),
        ("gzip enabled", r"gzip"),
        ("env vars", r"env\s*[:{]"),
        ("API_URL", r"API_URL"),
        ("dev/prod split", r"production|localhost|dev"),
        ("comments/docs", r"//|/\*"),
        ("export", r"export|module\.exports"),
    ])


def check_easy_p02(path):
    """_redirects + vercel.json both routing all paths to index.html."""
    return require_all(path, [
        ("netlify redirect rule", r"/\*"),
        ("index.html target", r"index\.html"),
        ("200 status", r"200"),
        ("vercel rewrites", r"rewrites|vercel\.json"),
        ("source/destination", r"source|destination"),
        ("explanation", r"#|//|SPA|routing|404"),
    ])


def check_easy_p03(path):
    """SPA deployment guide: prereqs, build, 3 platforms, issues."""
    return require_all(path, [
        ("prerequisites", r"[Pp]rerequisit|Node|CLI"),
        ("build command", r"quasar build|build -m spa"),
        ("output dir", r"dist/spa|dist"),
        ("Netlify", r"Netlify|netlify"),
        ("Vercel", r"Vercel|vercel"),
        ("GitHub Pages", r"GitHub Pages|gh-pages|github\.io"),
        ("deploy steps", r"deploy|Deploy"),
        ("common issues", r"[Ii]ssue|[Ff]ix|[Tt]roubleshoot|404"),
    ])


def check_medium_p01(path):
    """Dockerfile for SPA: nginx:alpine, dist/spa copy, try_files, port 80."""
    return require_all(path, [
        ("FROM base image", r"FROM"),
        ("nginx", r"nginx"),
        ("multi-stage build", r"AS build|--from="),
        ("copy dist/spa", r"dist/spa|/usr/share/nginx"),
        ("nginx config", r"server\s*\{|location"),
        ("try_files SPA fallback", r"try_files"),
        ("index.html fallback", r"index\.html"),
        ("expose port", r"EXPOSE|listen\s+80|:80"),
        ("CMD", r"CMD|daemon off"),
        ("build/run docs", r"docker build|docker run|//"),
    ])


def check_medium_p02(path):
    """Dockerfile for SSR: node:18-slim, dist/ssr, prod deps, compose."""
    return require_all(path, [
        ("FROM node", r"FROM\s+node"),
        ("slim image", r"slim|alpine|18"),
        ("ssr build", r"build -m ssr|dist/ssr"),
        ("prod deps only", r"omit=dev|production|--prod"),
        ("expose 3000", r"EXPOSE|3000"),
        ("CMD node", r"CMD.*node|node.*index\.js"),
        ("compose services", r"services:|docker-compose|compose"),
        ("restart policy", r"restart|unless-stopped|always"),
        ("environment vars", r"environment|NODE_ENV|API_URL"),
        ("healthcheck", r"healthcheck|health"),
    ])


def check_medium_p03(path):
    """GitHub Actions: push to main, install, lint, test, build, deploy."""
    return require_all(path, [
        ("workflow name", r"name:"),
        ("on push", r"on:|push:"),
        ("main branch", r"main"),
        ("jobs", r"jobs:"),
        ("checkout", r"checkout"),
        ("setup-node", r"setup-node|node-version"),
        ("npm install", r"npm ci|npm install"),
        ("lint step", r"lint"),
        ("test step", r"vitest|test"),
        ("build step", r"build"),
        ("deploy step", r"netlify|Netlify|deploy"),
        ("secrets usage", r"secrets\."),
        ("caching", r"cache"),
    ])


def check_hard_p01(path):
    """Full CI/CD: lint→test→build matrix→security→staging/prod→notify."""
    return require_all(path, [
        ("workflow triggers", r"on:|push:|release:"),
        ("multiple jobs", r"lint:|test:|build:"),
        ("job dependencies", r"needs:"),
        ("build matrix", r"matrix:|mode:|\[spa|pwa"),
        ("security scan", r"audit|snyk|security"),
        ("staging deploy", r"staging"),
        ("production deploy", r"production|release"),
        ("artifacts", r"upload-artifact|download-artifact|artifact"),
        ("secrets", r"secrets\."),
        ("slack notify", r"[Ss]lack|SLACK"),
        ("failure condition", r"failure|always\(\)"),
        ("env vars", r"env:|NODE_VERSION|API_URL"),
    ])


def check_hard_p02(path):
    """Deploy script: S3 upload, CloudFront invalidation, Slack, rollback."""
    return require_all(path, [
        ("config constants", r"BUILD_DIR|BUCKET|CLOUDFRONT|const"),
        ("file listing", r"readdirSync|listFiles|readdir"),
        ("S3 upload", r"S3|s3|upload"),
        ("versioned upload", r"version|versions/"),
        ("CloudFront invalidation", r"[Cc]loud[Ff]ront|invalidat"),
        ("Slack notify", r"[Ss]lack|webhook|notification"),
        ("rollback fn", r"rollback"),
        ("keep last N versions", r"MAX_VERSIONS|slice|keep|last 3|cleanup"),
        ("argv handling", r"process\.argv|--rollback|--env"),
        ("deploy main fn", r"deploy\(\)|async function deploy|function deploy"),
        ("process docs", r"//|/\*|Deploy"),
    ])


def check_hard_p03(path):
    """Deployment playbook: checklist, 3 platforms, verify, monitor, rollback."""
    return require_all(path, [
        ("checklist", r"- \[ \]|checklist|Checklist"),
        ("pre-deploy items", r"test|lint|env|sourcemap|gzip"),
        ("Netlify steps", r"Netlify|netlify"),
        ("Docker/AWS steps", r"Docker|docker|AWS|aws"),
        ("Vercel steps", r"Vercel|vercel"),
        ("post-deploy verification", r"[Vv]erification|smoke test|[Vv]erify"),
        ("monitoring", r"Sentry|monitoring|analytics|uptime"),
        ("rollback procedure", r"[Rr]ollback"),
        ("troubleshooting", r"[Tt]roubleshoot|Symptom|Cause|Fix"),
        ("substantial content", r"[\s\S]{500,}"),
    ])


CHECKS = {
    "easy/p01": check_easy_p01,
    "easy/p02": check_easy_p02,
    "easy/p03": check_easy_p03,
    "medium/p01": check_medium_p01,
    "medium/p02": check_medium_p02,
    "medium/p03": check_medium_p03,
    "hard/p01": check_hard_p01,
    "hard/p02": check_hard_p02,
    "hard/p03": check_hard_p03,
}


def find_problem_file(check_id):
    """Find the student's file for a check id like 'easy/p01'.
    Matches easy/p01-*.*, excluding solutions/."""
    level, num = check_id.split("/")
    pattern = os.path.join(LESSON_DIR, level, f"{num}-*")
    matches = [
        f for f in glob.glob(pattern)
        if os.path.isfile(f) and "solutions" not in f
    ]
    return matches[0] if matches else None


def run_one(check_id):
    if check_id not in CHECKS:
        print(f"ERROR — unknown problem '{check_id}'")
        print(f"Available: {', '.join(CHECKS)}")
        return False
    filepath = find_problem_file(check_id)
    if not filepath:
        print(f"ERROR — file not found: {check_id}-* (create it first)")
        return False
    try:
        passed, msg = CHECKS[check_id](filepath)
    except Exception as e:
        if "NoneType" in str(e):
            print(f"FAIL — a function returned None — write the body!")
        else:
            print(f"ERROR — {e}")
            return False
    if passed:
        print(f"PASS — {msg}")
        rel = os.path.relpath(filepath, LESSON_DIR)
        print(f"  Done? Add a DONE marker to the top of {rel}")
    else:
        print(f"FAIL — {msg}")
    return passed


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 check.py <level>/<problem>")
        print("Example: python3 check.py easy/p01")
        print("         python3 check.py all")
        sys.exit(1)

    target = sys.argv[1]

    if target == "all":
        print("=" * 60)
        print("  LESSON 20 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id in CHECKS:
            run_one(check_id)
        print("=" * 60)
        return

    run_one(target)


if __name__ == "__main__":
    main()
