"""Level 11 — LLM & Prompt Engineering — Hard P02 Solution"""

def evaluate_response(response, criteria):
    result = {}
    if "max_length" in criteria:
        result["length"] = len(response) <= criteria["max_length"]
    if "format" in criteria:
        if criteria["format"] == "bullet":
            result["format"] = response.strip().startswith("- ") or response.strip().startswith("•")
        else:
            result["format"] = True
    if "contains" in criteria:
        result["accuracy"] = criteria["contains"].lower() in response.lower()
    return result

if __name__ == "__main__":
    r = evaluate_response("- Point one\n- Point two\n- Point three",
                          {"max_length": 100, "format": "bullet", "contains": "point"})
    print(r)
