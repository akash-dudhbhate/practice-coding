"""Level 11 Llm Prompt — Medium P01 Solution"""

def solve():
    cot_prompt = '''
Solve this step by step:

Problem: If a store sells 3 apples for $2, how much do 12 apples cost?

Step 1: Find the cost per apple.
$2 / 3 = $0.67 per apple

Step 2: Multiply by the number of apples.
$0.67 × 12 = $8.00

Answer: $8.00

Problem: A train travels 60 mph for 2.5 hours. How far does it go?

Step 1: Use the formula distance = speed × time.
Step 2: distance = 60 × 2.5 = 150 miles

Answer: 150 miles
'''
    print(cot_prompt)
    return cot_prompt

if __name__ == "__main__":
    solve()