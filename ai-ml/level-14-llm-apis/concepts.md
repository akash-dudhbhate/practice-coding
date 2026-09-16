# Level 14 — Concepts

## 1. The chat() abstraction
**WHAT:** One function that calls any LLM. `chat(prompt, system, temp) → str`.
**WHY:** Swapping backends should be a config change, not a rewrite.
Production apps wrap the API — never call `openai.chat.completions.create()`
scattered through your code.
**GOES WRONG:** hard-coding OpenAI calls everywhere → can't test offline,
can't switch providers, vendor lock-in.

## 2. System prompts
**WHAT:** Instructions that shape the model's persona/behavior, sent
before the user message.
**WHY:** A system prompt like "You are a concise technical writer" makes
every response follow that style without repeating it in each prompt.
**GOES WRONG:** forgetting to pass it — model drifts to generic answers.

## 3. Temperature
**WHAT:** Sampling randomness. 0.0 = deterministic, 1.0+ = creative.
**WHY:** Same prompt, different jobs: extraction wants 0, brainstorming
wants 0.8.
**GOES WRONG:** using temp=0 for creative writing (boring) or temp=1
for JSON extraction (breaks parsing).

## 4. Structured output (JSON)
**WHAT:** Asking the model to return parseable JSON instead of prose.
**WHY:** LLMs are functions — JSON output lets code consume them.
**GOES WRONG:** model adds "Here's the JSON:" wrapper → `json.loads` fails.
Fix: tell it "return ONLY valid JSON, no preamble" + retry on parse error.

## 5. Streaming
**WHAT:** Receiving tokens as they're generated, not one big response.
**WHY:** User sees output immediately — feels 10× faster.
**GOES WRONG:** forgetting it's a generator; treating it like a string
breaks.

## 6. Tool calling (function calling)
**WHAT:** Model returns `{"tool": "calc", "args": {"a": 6}}` — you run it,
feed result back.
**WHY:** LLMs can't compute/fetch — they DECIDE, code EXECUTES.
**GOES WRONG:** trusting model output blindly → always validate tool name
and arg types before calling.

## 7. Cost tracking
**WHAT:** Tokens = billing unit. ~4 chars ≈ 1 token.
**WHY:** A chatbot making 50 calls/user at 2000 tokens each gets expensive
fast. Track it.
**GOES WRONG:** no tracking → surprise bill. Estimate tokens before
sending, log after.

## 8. Retry & validation
**WHAT:** LLM output is unreliable — parse may fail, answer may be wrong.
**WHY:** Production code wraps LLM calls with retry + schema validation.
**GOES WRONG:** assuming output is valid → crashes on the one malformed
response in 1000.
