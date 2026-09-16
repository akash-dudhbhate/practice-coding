"""Level 11 Llm Prompt — Medium P03 Solution"""

import json
import re

def solve():
    llm_output = '''
The answer is 42.
{"score": 0.95, "category": "positive"}
'''
    # Parse JSON from output
    json_match = re.search(r'\{.*\}', llm_output, re.DOTALL)
    if json_match:
        parsed = json.loads(json_match.group())
        print(f"Parsed: {parsed}")
    return parsed

if __name__ == "__main__":
    solve()