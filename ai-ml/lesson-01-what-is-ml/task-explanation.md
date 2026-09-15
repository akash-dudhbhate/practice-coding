# Lesson 01 — What is ML? Supervised vs Unsupervised

## What you'll learn
- What machine learning actually is (vs traditional programming).
- The three main categories: supervised, unsupervised, reinforcement.
- How to recognize which category a problem belongs to.

## Lesson

### Traditional programming vs ML
- **Traditional:** You write rules (code) + data → answers.
- **ML:** You give data + answers → the algorithm learns the rules (a model).

Example: instead of hand-coding "if email contains 'free money' → spam", you feed the model thousands of labeled spam/non-spam emails and it learns the patterns itself.

### The three categories

| Category | Has labels? | Example |
|----------|-------------|---------|
| **Supervised** | Yes | Predict house price from size; classify email as spam/not-spam |
| **Unsupervised** | No | Group customers into segments; find topics in documents |
| **Reinforcement** | Learns from rewards | Game-playing AI, robot navigation |

### Supervised: two flavors
- **Regression** — predict a **number** (price, temperature, age).
- **Classification** — predict a **category** (spam/ham, dog/cat/bird).

### Key vocabulary
- **Features (X):** the inputs (e.g., house size, number of rooms).
- **Label/target (y):** what you're predicting (e.g., house price).
- **Training:** the process of the model learning from data.
- **Inference:** using the trained model to make new predictions.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. These are **concept questions** — answer in your own words by replacing the `TODO` strings in each file.

### Easy (start here)
1. `easy/p01-classify-problem-type.py` — classify 3 scenarios as regression/classification/unsupervised.
2. `easy/p02-identify-features-labels.py` — identify features (X) and label (y) for 2 scenarios.
3. `easy/p03-traditional-vs-ml.py` — decide traditional programming vs ML for 4 scenarios.

### Medium
4. `medium/p01-design-spam-classifier.py` — design a full spam classifier (5 questions).
5. `medium/p02-train-test-split.py` — explain train/test splits and overfitting.
6. `medium/p03-match-algorithm-to-problem.py` — match algorithms to problem types.

### Hard
7. `hard/p01-full-ml-pipeline-design.py` — design a full ML pipeline for diabetes prediction (8 questions).
8. `hard/p02-confusion-matrix-intuition.py` — calculate TP/FP/TN/FN and accuracy from a scenario.
9. `hard/p03-bias-variance-tradeoff.py` — explain bias, variance, and the tradeoff.

### How to work
- Open a problem file, read the questions in the header.
- Replace each `TODO` string with your answer (in your own words).
- Remove the TODO marker line when done.
- Run `python <filename>` to print your answers for review.
- When done, tell me and I'll review. Say **"give me next task"** to advance.
