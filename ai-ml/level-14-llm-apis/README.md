# Level 14 — Real LLM APIs

> **Math level:** 10th grade is enough. See [MATH-YOU-NEED.md](../MATH-YOU-NEED.md) — it explains every symbol used here.

> Level-11 taught prompt patterns on a *simulated* LLM.
> Level-14 uses the **same prompts but real API calls** — one env var
> flips between simulated (offline), Ollama (local, free), and OpenAI.

## The pattern that matters

Every exercise imports `chat()` from `llm.py`. Your code NEVER calls
OpenAI/Ollama directly — it calls `chat(prompt, system, temperature)`
and the backend is config. That's how production LLM apps are built.

```python
import sys; sys.path.insert(0, "..")   # so exercises can import llm.py
from llm import chat

reply = chat("Summarize this in 3 bullets", temperature=0.0)
```

Set backend: `LLM_BACKEND=ollama python3 easy/p01-*.py`

## Problems

### Easy — basic calls
| # | File | You build |
|---|------|-----------|
| 1 | `p01-first-call.py` | `ask_llm(question)` — call chat(), return reply |
| 2 | `p02-system-prompt.py` | `ask_with_persona(q, persona)` — system param |
| 3 | `p03-temperature.py` | `creative_vs_precise(prompt)` — same prompt, temp 0 vs 1 |

### Medium — structured work
| # | File | You build |
|---|------|-----------|
| 1 | `p01-json-extract.py` | `extract(text)` → dict via "return JSON" prompt |
| 2 | `p02-retry-parse.py` | `parse_or_retry(text)` — malformed JSON → retry once |
| 3 | `p03-batch-call.py` | `classify_batch(texts)` — one prompt → list of labels |

### Hard — real patterns
| # | File | You build |
|---|------|-----------|
| 1 | `p01-stream-tokens.py` | `stream(prompt)` — yield chunks (simulated splits words) |
| 2 | `p02-tool-call.py` | `agent_decide(task)` → {"tool":..,"args":..} via JSON prompt |
| 3 | `p03-cost-tracker.py` | `TrackedLLM` class — count calls/est. tokens per prompt |

## Mini-project
`project/chatbot.py` — multi-turn chat with system prompt + history.

## Check your work
```bash
python3 check.py easy/p01
python3 check.py all
```
