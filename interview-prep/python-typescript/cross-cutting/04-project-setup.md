# 04 — Project setup to defend in an interview

> **Interview question:** "Walk me through how you'd set up tooling on a new Python or TypeScript project."
> **What the interviewer is really testing:** Whether you've owned project hygiene end-to-end — lint, format, test, type-check, CI — or just inherited whatever `create-*` scaffolded.

## Theory — what it is

A defensible setup has four layers, each with one job:

1. **Linter** — finds *bugs and bad patterns* (unused imports, `==` vs `===`, shadowed vars). Python: **ruff** (fast, replaces flake8+isort+pyupgrade). TypeScript: **eslint**.
2. **Formatter** — makes style *automatic and boring* so reviews never debate whitespace. Python: **black** (or `ruff format`). TypeScript: **prettier**. Rule: linter checks correctness, formatter owns style — configure them not to fight.
3. **Tests** — Python: **pytest**; TypeScript: **vitest** (or jest). Plus coverage thresholds so coverage can't silently rot.
4. **CI** — one pipeline that runs *all of the above* plus type-checking (`mypy`/`tsc --noEmit`) on every PR, blocking merge on failure. Locally the same checks run via **pre-commit** hooks so failures surface before push.

The principle that makes it defensible: **every check is automated, fast, and identical locally and in CI.** Nothing depends on a human remembering.

## Why it was needed

Without this, quality drifts: inconsistent formatting makes diffs noisy and reviews slow; bugs a linter would catch get found in production; "works on my machine" because there's no pinned toolchain; and tests get skipped when someone is in a hurry. Automating enforcement makes the *right* way the *easy* way — the codebase can't decay quietly.

It also signals seniority: juniors write code; engineers build systems where bad code can't land.

## Where it's used in a real project

1. **PR gate** — CI runs lint + format-check + type-check + tests; branch protection requires green before merge.
2. **Pre-commit hooks** — `pre-commit` (Python) or `husky`/`lint-staged` (TS) run the fast checks on staged files; commits can't skip them.
3. **Onboarding** — one `make setup` / `pnpm i` and one documented command (`make check`) runs everything; new devs are productive in minutes.
4. **Dependabot/renovate** — keep the toolchain itself patched; a stale linter is a false sense of security.

## Diagram

```
commit ──▶ pre-commit hooks (ruff/black | eslint/prettier on staged files)
             │ fast, local, auto-fixes
push ────▶ CI pipeline ──────────────────────────────────────────┐
             ├─ lint    : ruff check | eslint .                  │
             ├─ format  : ruff format --check | prettier --check │
             ├─ types   : mypy src/   | tsc --noEmit             │
             ├─ tests   : pytest --cov | vitest run --coverage   │
             └─ build   : python -m build | pnpm build           │
                          │                                      │
                    all green ──▶ merge allowed                  │
                    any red  ──▶ PR blocked ─────────────────────┘
```

## Code — explained

```toml
# ---------- PYTHON: pyproject.toml ----------
[project]
name = "myapp"
requires-python = ">=3.12"
dependencies = ["pydantic>=2", "fastapi"]

[dependency-groups]
dev = ["pytest", "pytest-cov", "ruff", "mypy", "pre-commit"]

[tool.ruff]
line-length = 100
[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B", "SIM"]  # errors, pyflakes, isort, pyupgrade, bugbear, simplify

[tool.mypy]
strict = true

[tool.pytest.ini_options]
addopts = "--cov=src --cov-fail-under=80"
testpaths = ["tests"]
```

```jsonc
// ---------- TYPESCRIPT: package.json ----------
{
  "scripts": {
    "lint": "eslint .",
    "format": "prettier --write .",
    "typecheck": "tsc --noEmit",
    "test": "vitest run --coverage",
    "check": "pnpm lint && pnpm typecheck && pnpm test"   // THE one command
  },
  "lint-staged": {
    "*.{ts,tsx}": ["eslint --fix", "prettier --write"]
  }
}
```

```yaml
# ---------- CI (GitHub Actions), same shape for both ----------
name: ci
on: [pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      # Python: setup-python + uv/pip install
      # TS:     setup-node + pnpm install --frozen-lockfile
      - run: ruff check . && ruff format --check .     # or: pnpm lint && prettier --check .
      - run: mypy src/                                  # or: pnpm typecheck
      - run: pytest                                     # or: pnpm test
```

Key choices to defend:

- **ruff over flake8** — one Rust binary replaces ~5 tools, runs in milliseconds, and `ruff format` is black-compatible so you can drop black entirely.
- **vitest over jest** — native ESM/TS, no transform config, jest-compatible API.
- **`--frozen-lockfile` in CI** — CI must install from the lockfile exactly, never re-resolve; that's how you prevent "works on my machine."
- **Coverage floor (`--cov-fail-under`)** — coverage can only go up.

## Problems

### Easy — Name the tool
**Problem:** For each task, name the right tool: (a) catch an unused import, (b) normalize quote style, (c) verify `divide(10,0)` raises, (d) block a PR on type errors.

**Try this input:** `divide(10, 0)` with `ZeroDivisionError` expected.
**Expected output:** (a) ruff/eslint (b) black/ruff-format/prettier (c) pytest `pytest.raises` / vitest `expect().toThrow` (d) mypy/tsc in CI.
**Solution:**

```python
import pytest
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
```

**Logic explained:**
1. Unused imports are a *correctness-adjacent* smell → linter, not formatter.
2. Quote style is pure style → formatter.
3. Exception behavior is a runtime assertion → test framework.
4. Type errors → checker in CI, enforced by branch protection.

### Medium — Order the pipeline
**Problem:** CI is flaky: lint auto-fixes in CI (`ruff check --fix`) and then tests run on modified code. Also, tests run before the type check so a trivial type error wastes 8 minutes of test time. Redesign the step order and explain why.

**Try this input:** a PR with a mypy error and 8-minute test suite.
**Expected output:** type/lint fail in <1 min, tests never start.
**Solution:**

```yaml
- run: ruff check .            # NO --fix in CI: CI verifies, it doesn't mutate
- run: ruff format --check .
- run: mypy src/
- run: pytest
```

**Logic explained:**
1. **CI must be read-only** — auto-fixing belongs in pre-commit locally; a mutating CI can pass while the committed code is still broken.
2. Order cheap→expensive: lint (seconds) → format (seconds) → types (~seconds–min) → tests (minutes). Fail fast on the cheapest signal.
3. Same principle locally: pre-commit runs fixers on staged files before you even push.

### Hard — Two languages, one repo
**Problem:** A monorepo has a Python service (`services/api/`) and a TS frontend (`apps/web/`). Design a single `make check` for CI that (a) only runs a side's checks when its files changed, (b) still runs a shared contract check always. Sketch it.

**Try this input:** a PR touching only `apps/web/`.
**Expected output:** Python checks skipped; eslint/tsc/vitest run; contract check runs.
**Solution:**

```makefile
check:
ifneq (,$(shell git diff --name-only origin/main...HEAD | grep '^services/api/'))
	cd services/api && ruff check . && mypy src/ && pytest
endif
ifneq (,$(shell git diff --name-only origin/main...HEAD | grep '^apps/web/'))
	cd apps/web && pnpm lint && pnpm typecheck && pnpm test
endif
	# always: contract check that pydantic models ↔ generated TS types match
	python scripts/check_contract.py
```

(In real GitHub Actions you'd use `paths-filter` or `dorny/paths-filter` instead of Makefile `grep` — same idea.)

**Logic explained:**
1. Path-based filtering keeps PRs fast — no 8-minute Python suite for a CSS change.
2. The shared contract check (e.g., regenerated OpenAPI types diffed against committed ones) must *always* run — it guards the seam between the two sides.
3. Interview gold: mention this is how you'd keep both ecosystems at equal strictness without one team's check slowing the other.

## The 30-second interview answer

"Four layers, each with one job: **ruff + black/ruff-format** and **eslint + prettier** for lint and format — linter owns correctness, formatter owns style, configured so they don't fight; **pytest** and **vitest** for tests with a coverage floor; **mypy/pyright** and **tsc --noEmit** for types. Pre-commit runs the fast fixers locally on staged files; CI runs everything read-only, ordered cheapest-first — lint, format-check, types, then tests — and branch protection blocks merge on red. I'd pin the toolchain via lockfile + `--frozen-lockfile` so CI is reproducible, and give the repo one entry point — `make check` / `pnpm check` — so the local loop and CI are identical."

## Follow-up trap

"Why not run eslint AND prettier on every file — don't they overlap?" — Strong answer: they do overlap on stylistic rules (indentation, semicolons), which causes infinite fix-loops where each tool undoes the other. The fix is `eslint-config-prettier` — it disables eslint's formatting rules so eslint only checks *bugs*, and prettier owns *style*. Same on Python: ruff's formatter-compatible lint rules, or run black for style and ruff with formatting rules off. One tool per concern.
