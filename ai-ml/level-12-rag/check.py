"""
Auto-Check System — Level 12 (RAG Systems)
============================================
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
    if not hasattr(module, 'similarity'):
        return False, "Function 'similarity' not found"
    s1 = module.similarity("machine learning is great", "deep learning uses neural nets")
    s2 = module.similarity("machine learning is great", "cooking recipes food")
    if not (0.1 < s1 < 0.3):
        return False, f"Similar docs should score ~0.1-0.3, got {s1:.4f}"
    if s2 > 0.05:
        return False, f"Different docs should score ~0, got {s2:.4f}"
    if s1 <= s2:
        return False, "Similar should score higher than different"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'retrieve'):
        return False, "Function 'retrieve' not found"
    docs = ["ML is a subset of AI", "Deep learning uses neural nets",
            "Cooking requires recipes", "NLP processes text"]
    r = module.retrieve("What is machine learning?", docs, top_k=2)
    if len(r) != 2:
        return False, f"Expected 2 results, got {len(r)}"
    if 'ML' not in r[0][0] and 'machine' not in r[0][0].lower():
        return False, f"Top result should be ML-related, got '{r[0][0]}'"
    if r[0][1] < r[1][1]:
        return False, "Results should be sorted by score descending"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'chunk_text'):
        return False, "Function 'chunk_text' not found"
    text = "a" * 200
    chunks = module.chunk_text(text, 50, 10)
    if len(chunks) != 5:
        return False, f"Expected 5 chunks, got {len(chunks)}"
    if len(chunks[0]) != 50:
        return False, f"First chunk should be 50 chars, got {len(chunks[0])}"
    if chunks[1][:10] != chunks[0][40:50]:
        return False, "Chunk overlap is wrong"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'vector_store'):
        return False, "Function 'vector_store' not found"
    docs = ["ML is great", "Python is a language", "Deep learning is fun"]
    r = module.vector_store(docs, "Tell me about machine learning", 2)
    if len(r) != 2:
        return False, f"Expected 2 results, got {len(r)}"
    if not isinstance(r[0], tuple):
        return False, "Each result should be (doc, score)"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'rerank'):
        return False, "Function 'rerank' not found"
    docs = [("Old doc about AI", 0.6), ("Recent ML advances", 0.5), ("Ancient history", 0.4)]
    r = module.rerank("machine learning advances", docs)
    if len(r) != 3:
        return False, f"Expected 3 results, got {len(r)}"
    if r[0][1] != 0.6:
        return False, f"Top score should be 0.6 (0.5+0.1), got {r[0][1]}"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'hybrid_search'):
        return False, "Function 'hybrid_search' not found"
    docs = ["Python is a programming language", "ML models learn patterns",
            "Cooking is an art", "AI and machine learning"]
    r = module.hybrid_search("machine learning", docs, 2)
    if len(r) != 2:
        return False, f"Expected 2 results, got {len(r)}"
    if 'machine learning' not in r[0][0].lower():
        return False, f"Top result should contain 'machine learning', got '{r[0][0]}'"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'rag'):
        return False, "Function 'rag' not found"
    doc, answer = module.rag("What is ML?", ["ML is a subset of AI", "Deep learning uses neural nets"])
    if 'ML' not in doc:
        return False, f"Should retrieve ML doc, got '{doc}'"
    if doc not in answer:
        return False, "Answer should reference the retrieved doc"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'evaluate_rag'):
        return False, "Function 'evaluate_rag' not found"
    questions = ["What is ML?", "What is deep learning?"]
    docs = ["ML is AI", "Deep learning uses neural nets"]
    answers = ["ML is AI", "Deep learning uses neural nets"]
    acc = module.evaluate_rag(questions, docs, answers)
    if acc < 0.5:
        return False, f"Accuracy should be 1.0 (easy matching), got {acc:.2f}"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'rewrite_query'):
        return False, "Function 'rewrite_query' not found"
    r1 = module.rewrite_query("What is ML?")
    if 'machine learning' not in r1.lower():
        return False, f"Should expand ML → 'machine learning', got '{r1}'"
    r2 = module.rewrite_query("Tell me about NLP")
    if 'natural language processing' not in r2.lower():
        return False, f"Should expand NLP, got '{r2}'"
    r3 = module.rewrite_query("Python is great")
    if r3 != "Python is great":
        return False, f"Should not change non-abbreviation text, got '{r3}'"
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
        print("  LEVEL 12 — AUTO-CHECK ALL")
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
