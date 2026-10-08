# 48 — Config & secrets: env vars, pydantic-settings, never hardcode

> **Interview question:** "How do you handle configuration and secrets in a Python app?"
> **What the interviewer is really testing:** Whether a leaked `AWS_SECRET = "AKIA..."` in your git history would be your fault — and whether your app fails *fast* on missing config.

## Theory — what it is

**Configuration** = values that change between environments (dev/staging/prod): database URL, feature flags, timeouts, log level. **Secrets** = config that must stay private: API keys, DB passwords, JWT signing keys.

The standard answer: the **12-factor app** rule — *store config in environment variables*. The same code runs everywhere; only the env differs. `os.environ["DATABASE_URL"]` reads them, but raw env vars are all strings and give late, cryptic failures.

**`pydantic-settings`** (`pip install pydantic-settings`, a separate package from pydantic v2) gives you a `BaseSettings` class: declare fields with types, and it automatically reads env vars, casts types (`"5432"` → `int`), applies defaults, reads `.env` files, and raises a clear `ValidationError` at startup if anything's missing — instead of a `KeyError` deep in a request handler at 3 AM.

## Why it was needed

Hardcoded secrets end up in git history, in logs, in screenshots, in Docker image layers. Rotating a leaked key means a code change + redeploy instead of a config change. Bots scan GitHub for `AKIA` keys within minutes of a push.

Non-secret config has the same shape: a dev DB URL, a staging DB URL, a prod DB URL — if it's in code, you need per-environment builds or `if` branches. Env vars keep ONE build artifact that runs everywhere — critical for containers and CI.

And scattered `os.environ.get("X")` calls fail lazily: the app boots fine, then crashes on the first request that touches the missing key. Centralized settings fail *at startup*, where it's visible.

## Where it's used in a real project

- **`settings.py`**: one `Settings(BaseSettings)` class, instantiated once, imported everywhere — the single source of truth.
- **`.env` files for dev only**: developers keep `DATABASE_URL=postgres://localhost/dev` locally; `.env` is in `.gitignore`. Prod injects real env vars via the platform (Kubernetes secrets, AWS Secrets Manager, GitHub Actions secrets).
- **Startup validation**: `settings = Settings()` at module import — a missing `SECRET_KEY` crashes deploy immediately, not at first login.
- **Tests**: override settings via `dependency_overrides` or construct `Settings(_env_file="test.env")`.

## Diagram

```
        dev laptop                CI / prod
        ----------                ---------
   .env file (gitignored)    real env vars injected by
        |                      platform / secrets manager
        v                            |
   +-----------------------------------------+
   |   pydantic-settings BaseSettings        |
   |   reads env -> casts types -> validates |
   +-----------------------------------------+
        |  settings = Settings()  (once, at startup)
        v
   rest of app imports `settings`:
   settings.database_url  settings.debug  settings.api_key
        |
        +-- missing/invalid var -> ValidationError NOW (fail fast)
            never: KeyError mid-request
```

## Code — explained

```python
# settings.py
from pydantic_settings import BaseSettings, SettingsConfigDict  # 1

class Settings(BaseSettings):                              # 2
    model_config = SettingsConfigDict(env_file=".env")     # 3

    database_url: str                                      # 4
    api_key: str                                           # 5
    debug: bool = False                                    # 6
    port: int = 8000                                       # 7
    allowed_hosts: list[str] = ["localhost"]               # 8

settings = Settings()                                      # 9

# app code: from settings import settings
# db = create_engine(settings.database_url)               # 10
```

1. `pydantic-settings` is a separate install on pydantic v2 — `BaseSettings` moved out of the core package.
2. Declaring a class = declaring your app's *entire* config contract in one readable place.
3. `env_file=".env"` — for local dev, read a `.env` file too. Real env vars still win if both exist (env > .env > default).
4. `database_url: str` with NO default = **required**. pydantic reads `DATABASE_URL` (field names match env vars case-insensitively).
5. Same for `api_key` — if `API_KEY` isn't set, app won't start. The secret is never in code.
6. `debug: bool = False` — env `DEBUG=true`/`1`/`yes` all cast to `True`; missing → `False`. Safe default: debug off.
7. `port: int` — env `PORT=8080` becomes the *integer* 8080. With raw `os.environ` you'd get `"8080"` and a subtle bug.
8. Complex types work: `ALLOWED_HOSTS='["a.com","b.com"]'` parses as JSON into a list.
9. Instantiate once at startup — if anything's missing, you get `ValidationError: database_url field required` **right now**, not later.
10. Everywhere else imports the object — no scattered `os.environ.get` calls, one place to see every knob.

Anti-pattern to name in interviews:

```python
# NEVER this:
API_KEY = "sk_live_51abc..."        # in git forever
DB = os.environ["DB_URL"]           # fine, but scattered + KeyError at random time
```

## Problems

### Easy — env var with default
**Problem:** Read `LOG_LEVEL` from env with default `"INFO"`, uppercase it, and return it. Handle the unset case without crashing.
**Try this input:** env unset; then `LOG_LEVEL=debug`
**Expected output:** `INFO` then `DEBUG`
**Solution:**
```python
import os

def log_level() -> str:
    return os.environ.get("LOG_LEVEL", "INFO").upper()

os.environ.pop("LOG_LEVEL", None)
print(log_level())                    # INFO
os.environ["LOG_LEVEL"] = "debug"
print(log_level())                    # DEBUG
```
**Logic explained:**
1. `os.environ.get(key, default)` — never `os.environ[key]` for optional config, or you get `KeyError`.
2. `.upper()` normalizes input — env vars are strings, users write `debug`, `Debug`, `DEBUG`.
3. Pattern rule: optional config → `.get` with a safe default; required config → fail loudly at startup (see Hard).

### Medium — cast env vars safely
**Problem:** Env vars are always strings. Write `get_int_env(name, default)` that returns the int value or the default — and raises `ValueError` with a *helpful* message if the var is set but not an integer.
**Try this input:** `RETRIES=3`, `RETRIES=abc`, unset
**Expected output:** `3`, `ValueError: RETRIES must be an int, got 'abc'`, `5` (default)
**Solution:**
```python
import os

def get_int_env(name: str, default: int) -> int:
    raw = os.environ.get(name)
    if raw is None:
        return default
    try:
        return int(raw)
    except ValueError:
        raise ValueError(f"{name} must be an int, got {raw!r}")

os.environ["RETRIES"] = "3"
print(get_int_env("RETRIES", 5))      # 3
os.environ["RETRIES"] = "abc"
try:
    get_int_env("RETRIES", 5)
except ValueError as e:
    print("ValueError:", e)           # RETRIES must be an int, got 'abc'
del os.environ["RETRIES"]
print(get_int_env("RETRIES", 5))      # 5
```
**Logic explained:**
1. `int("abc")` raises a bare `ValueError: invalid literal` — useless at 3 AM. Wrap it with the *variable name* so ops knows which env var to fix.
2. `raw is None` distinguishes "unset" (use default) from `""` (probably a mistake — `int("")` also raises, which is correct).
3. This is exactly the type-casting work pydantic-settings does for you; doing it manually shows you understand what the library replaces.

### Hard — a mini settings loader
**Problem:** Build `Settings` that loads required + optional keys from a dict (simulating env), casts types, and collects ALL errors before raising — so one startup failure lists every missing var.
**Try this input:** `{"DB_URL": "postgres://x", "PORT": "abc"}` with spec `{DB_URL: str required, PORT: int default 8000, DEBUG: bool default False}`
**Expected output:** raises listing `PORT: 'abc' is not a valid int` — and with `PORT=8080` prints `{'db_url': 'postgres://x', 'port': 8080, 'debug': False}`
**Solution:**
```python
class SettingsError(Exception):
    pass

SPEC = {                              # name -> (type, required, default)
    "DB_URL": (str,  True,  None),
    "PORT":   (int,  False, 8000),
    "DEBUG":  (bool, False, False),
}

def load_settings(env: dict) -> dict:
    out, errors = {}, []
    for name, (typ, required, default) in SPEC.items():
        raw = env.get(name)
        if raw is None:
            if required:
                errors.append(f"{name}: required but not set")
            else:
                out[name.lower()] = default
            continue
        try:
            if typ is bool:
                out[name.lower()] = raw.lower() in ("1", "true", "yes")
            else:
                out[name.lower()] = typ(raw)
        except ValueError:
            errors.append(f"{name}: {raw!r} is not a valid {typ.__name__}")
    if errors:
        raise SettingsError("; ".join(errors))
    return out

try:
    load_settings({"DB_URL": "postgres://x", "PORT": "abc"})
except SettingsError as e:
    print("SettingsError:", e)
# SettingsError: PORT: 'abc' is not a valid int

print(load_settings({"DB_URL": "postgres://x", "PORT": "8080"}))
# {'db_url': 'postgres://x', 'port': 8080, 'debug': False}
```
**Logic explained:**
1. `SPEC` is the schema — same idea as pydantic field declarations. One place defines every config knob, its type, and whether it's required.
2. Loop collects errors into a list instead of raising on the first — operators see *all* missing vars in one deploy log.
3. Booleans need special-casing: `bool("false")` is `True` (non-empty string!) — the classic env-var bug. Parse `"1"/"true"/"yes"` explicitly.
4. Raise once with the full error list; the dict returned uses lowercase keys like attribute names (`settings.db_url`).

## The 30-second interview answer

"All config comes from environment variables — 12-factor style — so the same build runs in dev, CI, and prod. Secrets are never in code or git: they live in env vars injected by the platform or a secrets manager; `.env` files are dev-only and gitignored. I centralize everything in a `pydantic-settings` `BaseSettings` class: it reads env vars, casts types, applies defaults, and — most importantly — validates at startup, so a missing `DATABASE_URL` fails the deploy immediately instead of throwing `KeyError` mid-request. Tests override the settings object or use a separate env file."

## Follow-up trap

**"A secret got committed — what do you do?"** The trap is answering "delete it and commit again." Wrong: git history keeps it, and bots likely scraped it already. Correct order: **(1) rotate the key immediately** — assume it's compromised; (2) then scrub history (`git filter-repo`/BFG) if you control the repo; (3) add a pre-commit scanner like `gitleaks`/`detect-secrets` so it can't recur. Deleting without rotating leaves a live key public. Second trap: "**Where do prod secrets actually come from?**" — a secrets manager (AWS Secrets Manager, Vault, Kubernetes `Secret` → env var at pod start), not `.env` files on servers.
