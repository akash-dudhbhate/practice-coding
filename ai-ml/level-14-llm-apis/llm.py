"""
LEVEL 14 — Real LLM APIs
=========================

Levels 11-13 simulated LLMs. This level uses the SAME code shape
but calls a real model. One env var switches backends:

    LLM_BACKEND=simulated   # default — offline, no key needed
    LLM_BACKEND=ollama      # local Ollama (free, needs install)
    LLM_BACKEND=openai      # OpenAI API (needs OPENAI_API_KEY)

THE PATTERN — one `chat()` function, three backends. This is how
production apps work: your code calls chat(), the backend is
config. You NEVER sprinkle openai/ollama calls through your code.

Run:  python3 easy/p01-*.py
Check: python3 check.py easy/p01
"""

import os
import json

BACKEND = os.environ.get("LLM_BACKEND", "simulated")


def chat(prompt, system="", temperature=0.0):
    """Single function to call ANY LLM backend.

    Returns a string — the model's reply.

    - simulated: rule-based mock that returns canned responses
      (lets all exercises run offline, same code path)
    - ollama: calls http://localhost:11434/api/generate
    - openai: calls the OpenAI chat completions API
    """
    if BACKEND == "ollama":
        return _chat_ollama(prompt, system, temperature)
    if BACKEND == "openai":
        return _chat_openai(prompt, system, temperature)
    return _chat_simulated(prompt, system, temperature)


# --- backends ---

def _chat_simulated(prompt, system, temperature):
    """Mock LLM — deterministic canned replies for offline work.

    Gives DIFFERENT plausible outputs per prompt type so exercises
    still feel real: echo structure, extraction, summarization.
    """
    p = prompt.lower()
    if "json" in p or "extract" in p:
        return json.dumps({"name": "Alice", "age": 30, "city": "Paris"})
    if "summar" in p:
        return "• Key point one\n• Key point two\n• Key point three"
    if "classify" in p or "sentiment" in p:
        return "positive" if "good" in p or "love" in p else "neutral"
    if "weather" in p:
        return "I cannot check live weather — connect a real API key."
    if "step" in p or "think" in p:
        return "Step 1: restate problem\nStep 2: solve\nStep 3: verify"
    # default: parrot-back style reply
    return f"[simulated-llm] Response to: {prompt[:80]}"


def _chat_ollama(prompt, system, temperature):
    """Ollama local API — http://localhost:11434/api/generate"""
    import urllib.request
    body = json.dumps({
        "model": os.environ.get("OLLAMA_MODEL", "llama3.2"),
        "prompt": (system + "\n\n" if system else "") + prompt,
        "stream": False,
        "options": {"temperature": temperature},
    }).encode()
    req = urllib.request.Request(
        "http://localhost:11434/api/generate",
        data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())["response"]


def _chat_openai(prompt, system, temperature):
    """OpenAI chat completions — needs OPENAI_API_KEY env var."""
    import openai
    client = openai.OpenAI()
    msgs = ([{"role": "system", "content": system}] if system else [])
    msgs.append({"role": "user", "content": prompt})
    r = client.chat.completions.create(
        model=os.environ.get("OPENAI_MODEL", "gpt-4o-mini"),
        messages=msgs, temperature=temperature)
    return r.choices[0].message.content
