"""Level 11 Llm Prompt — Easy P03 Solution"""

def solve():
    temperatures = {
        0.0: 'Deterministic — same output every time',
        0.5: 'Balanced — some variety but coherent',
        1.0: 'Creative — more random, diverse outputs',
        1.5: 'Very creative — may be incoherent'
    }
    for temp, desc in temperatures.items():
        print(f"Temperature {temp}: {desc}")
    return temperatures

if __name__ == "__main__":
    solve()