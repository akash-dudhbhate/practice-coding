# Level 00B — Weights & Training, Chapter by Chapter

> **Prerequisite: level-00a.** You know what AI is. Now we slow
> down and learn the ONE thing everything is built on: weights.
>
> Each problem = one chapter. Do them IN ORDER — each uses the
> idea from the one before. By hard/p03 you will have written
> real gradient descent, from scratch, and understood every line.

## The 9 chapters

| # | Problem | Chapter question it answers |
|---|---------|------------------------------|
| E1 | `p01-one-weight.py` | What IS a weight? What does it do? |
| E2 | `p02-why-bias.py` | Why is `w*x` alone not enough? What does `b` add? |
| E3 | `p03-error.py` | How do we MEASURE "wrong"? |
| M1 | `p01-training-step.py` | How does one training step fix the error? |
| M2 | `p02-learning-rate.py` | What if we nudge too much or too little? |
| M3 | `p03-many-examples.py` | How do we train on more than one example? |
| H1 | `p01-gradient-descent.py` | The real training loop — until the error is tiny |
| H2 | `p02-two-weights.py` | What happens with 2 inputs? (dot product!) |
| H3 | `p03-full-picture.py` | Train a real 2-weight model end to end |

## How to work each chapter

1. Read `concepts.md` — find the chapter matching the problem number.
   It has the full explanation WITH the arithmetic worked out.
2. Open the problem file — its docstring restates the idea briefly.
3. Write the function. Run `python3 check.py <level>/<num>`.
4. Only then move to the next chapter.

```bash
python3 check.py easy/p01    # check one
python3 check.py all         # check all 9
```

## After this level
Every "neural network" you'll ever see is this exact loop with
more weights. Level-08 adds the layer structure — the math is
already yours.