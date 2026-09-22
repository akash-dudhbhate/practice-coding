"""Level 11 — LLM & Prompt Engineering — Medium P03 Solution"""

import json

def parse_llm_output(text):
    start = text.find('{')
    end = text.rfind('}')
    if start == -1 or end == -1:
        return None
    try:
        return json.loads(text[start:end+1])
    except json.JSONDecodeError:
        return None

if __name__ == "__main__":
    t = 'The sentiment is: {"score": 0.95, "category": "positive"}'
    print(parse_llm_output(t))
