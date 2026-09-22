"""
Auto-Check System — Level 11 (LLM & Prompt Engineering)
=========================================================
Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import os
import sys
import glob
import importlib.util


def load_module(filepath):
    spec = importlib.util.spec_from_file_location("solution", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _find_file(level_dir, level, num):
    num_clean = num.lstrip("p")
    filepath = os.path.join(level_dir, level, f"p{num_clean}-solve.py")
    if not os.path.exists(filepath):
        pattern = os.path.join(level_dir, level, f"p{num_clean}-*.py")
        matches = [f for f in glob.glob(pattern) if "solutions" not in f]
        if matches:
            filepath = matches[0]
    return filepath


def check_easy_p01(module):
    if not hasattr(module, 'make_prompts'):
        return False, "Function 'make_prompts' not found"
    p = module.make_prompts("test text")
    if not isinstance(p, dict):
        return False, f"Expected dict, got {type(p)}"
    for key in ['simple', 'detailed', 'structured']:
        if key not in p:
            return False, f"Missing key: {key}"
    if 'bullet' not in p['detailed'] or '3' not in p['detailed']:
        return False, "Detailed prompt should mention '3 bullet points'"
    if 'json' not in p['structured'].lower() or 'main_point' not in p['structured']:
        return False, "Structured prompt should mention JSON and keys"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'few_shot_prompt'):
        return False, "Function 'few_shot_prompt' not found"
    ex = [("I love it", "Positive"), ("Terrible", "Negative"), ("Meh", "Neutral")]
    p = module.few_shot_prompt(ex, "This is amazing!")
    if 'I love it' not in p or 'Positive' not in p:
        return False, "Prompt should include examples"
    if 'This is amazing!' not in p:
        return False, "Prompt should include the query"
    if p.strip().endswith('→') or p.strip().endswith('→ '):
        pass  # good — query has empty label for model to fill
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'explain_temperature'):
        return False, "Function 'explain_temperature' not found"
    cases = [
        (0.0, "Deterministic"), (0.5, "Balanced"),
        (1.0, "Creative"), (1.5, "Very creative")
    ]
    for temp, expected in cases:
        r = module.explain_temperature(temp)
        if expected.lower() not in r.lower():
            return False, f"temp={temp}: expected '{expected}', got '{r}'"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'chain_of_thought'):
        return False, "Function 'chain_of_thought' not found"
    p = module.chain_of_thought("test problem")
    if 'step by step' not in p.lower():
        return False, "Should mention 'step by step'"
    if 'test problem' not in p:
        return False, "Should include the problem text"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'structured_prompt'):
        return False, "Function 'structured_prompt' not found"
    p = module.structured_prompt("data scientist", "ML", "bullets", "What is X?")
    if 'data scientist' not in p:
        return False, "Missing persona"
    if 'ML' not in p:
        return False, "Missing context"
    if 'bullets' not in p:
        return False, "Missing format"
    if 'What is X?' not in p:
        return False, "Missing question"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'parse_llm_output'):
        return False, "Function 'parse_llm_output' not found"
    r = module.parse_llm_output('Result: {"score": 0.9, "cat": "good"}')
    if not isinstance(r, dict):
        return False, f"Expected dict, got {type(r)}"
    if r.get('score') != 0.9:
        return False, f"Expected score=0.9, got {r}"
    r2 = module.parse_llm_output('no json here')
    if r2 is not None:
        return False, f"Should return None for no JSON, got {r2}"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'iterate_prompts'):
        return False, "Function 'iterate_prompts' not found"
    result = module.iterate_prompts("summarize")
    if not isinstance(result, list) or len(result) < 3:
        return False, f"Expected ≥3 prompt versions, got {len(result)}"
    prompts = [p for p, s in result]
    scores = [s for p, s in result]
    if scores != sorted(scores):
        return False, "Scores should be increasing (v3 > v2 > v1)"
    if 'bullet' not in prompts[1]:
        return False, "v2 should mention bullet points"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'evaluate_response'):
        return False, "Function 'evaluate_response' not found"
    r = module.evaluate_response("- a\n- b", {"max_length": 50, "format": "bullet", "contains": "a"})
    if not isinstance(r, dict):
        return False, f"Expected dict, got {type(r)}"
    if r.get('length') is not True:
        return False, f"Expected length=True, got {r}"
    if r.get('format') is not True:
        return False, f"Expected format=True, got {r}"
    r2 = module.evaluate_response("very long " * 100, {"max_length": 10})
    if r2.get('length') is not False:
        return False, "Should detect too-long response"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'get_personas'):
        return False, "Function 'get_personas' not found"
    p = module.get_personas()
    if len(p) != 4:
        return False, f"Expected 4 personas, got {len(p)}"
    for key in ['helpful', 'expert', 'creative', 'critical']:
        if key not in p:
            return False, f"Missing persona: {key}"
    if 'data scientist' not in p['expert'].lower():
        return False, "Expert persona should mention data scientist"
    return True, "All tests passed!"


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


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 check.py <level>/<problem>")
        sys.exit(1)

    target = sys.argv[1]
    level_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(level_dir)

    if target == "all":
        print("=" * 60)
        print("  LEVEL 11 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id, check_func in CHECKS.items():
            level, num = check_id.split("/")
            filepath = _find_file(level_dir, level, num)
            if not os.path.exists(filepath):
                print(f"  {check_id}: FILE NOT FOUND")
                continue
            try:
                module = load_module(filepath)
                passed, msg = check_func(module)
                status = "PASS" if passed else "FAIL"
                print(f"  {check_id}: {status} — {msg}")
            except Exception as e:
                if "NoneType" in str(e):
                    print(f"  {check_id}: FAIL — a function returned None — write the body!")
                else:
                    print(f"  {check_id}: ERROR — {e}")
        print("=" * 60)
        return

    level, num = target.split("/")
    check_id = f"{level}/{num}"
    if check_id not in CHECKS:
        print(f"Error: unknown problem '{check_id}'")
        sys.exit(1)

    filepath = _find_file(level_dir, level, num)
    if not os.path.exists(filepath):
        print(f"Error: file not found: {filepath}")
        sys.exit(1)

    try:
        module = load_module(filepath)
        passed, msg = CHECKS[check_id](module)
        if passed:
            print(f"PASS — {msg}")
            print(f"  Add '# DONE' to the first line of {filepath}")
        else:
            print(f"FAIL — {msg}")
    except Exception as e:
        if "NoneType" in str(e):
            print(f"FAIL — a function returned None — write the body!")
        else:
            print(f"ERROR — {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
