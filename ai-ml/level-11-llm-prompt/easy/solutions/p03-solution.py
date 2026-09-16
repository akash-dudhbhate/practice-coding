"""Level 11 — LLM & Prompt Engineering — Easy P03 Solution"""

def explain_temperature(temp):
    if temp <= 0.2:
        return "Deterministic — same output every time"
    elif temp <= 0.7:
        return "Balanced — some variety but coherent"
    elif temp <= 1.2:
        return "Creative — more random, diverse outputs"
    else:
        return "Very creative — may be incoherent"

if __name__ == "__main__":
    for t in [0.0, 0.5, 1.0, 1.5]:
        print(f"Temperature {t}: {explain_temperature(t)}")
