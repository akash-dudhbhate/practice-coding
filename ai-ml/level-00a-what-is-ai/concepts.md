# Level 00A — Concepts (What IS AI, Really?)

> Zero math, zero code knowledge assumed. Every term explained
> like you're hearing it for the first time — because you are.

---

## What is AI?

**AI = a program that makes decisions or predictions instead of
following fixed rules.**

Regular program: "If email contains 'FREE!!!', mark spam."
Someone wrote that rule by hand.

AI program: "Here are 10,000 spam and 10,000 normal emails —
figure out the rules yourself." The program finds that spam emails
say "free", "prize", "click now" — patterns no human wrote down.

**That's the whole difference:** rules written by a human vs
rules learned from examples.

---

## What is Machine Learning?

ML is how we BUILD AI. It's the "learning from examples" part.

- You give the program labeled examples: (email text → spam/ham)
- The program tries to find a pattern that separates them
- When it finds one, that pattern IS the model

---

## What is a "model"?

A model is just a **function that learned its own rules**.

Example: predicting house price from size.
```
You show it:  1000sqft → $200k,  1500sqft → $300k,  2000sqft → $400k
The model learns:  price = 0.2 × size   (roughly)
```

That `0.2` — the number it discovered — is a **weight**.

A "big" model like GPT has billions of weights. Same idea,
just more knobs to tune.

---

## What are "weights"?

Think of a recipe: "2 cups flour, 1 cup sugar, 3 eggs."
The weights are those numbers — how much of each ingredient.

In a model: `prediction = weight1×input1 + weight2×input2 + bias`
- weight1 decides how much input1 matters
- If weight1 is big, input1 drives the answer
- If weight1 is 0, input1 is ignored entirely

**Training** = adjusting the weights until the predictions match
reality. That's it. No magic — just numbers getting tuned.

---

## What is "training"?

1. Show the model an example: input → correct answer
2. Model guesses (using current weights)
3. Compare guess to correct answer — measure the error
4. Nudge the weights slightly to reduce that error
5. Repeat millions of times

That's literally all "training a neural network" means.
Level-08 does this with real PyTorch code — you'll see the loop.

---

## What is "predicting" (inference)?

Once trained, you freeze the weights and just USE them:
new input → model computes → output. No learning happens here.

---

## What is a "vector" / "embedding"?

A vector is just a **list of numbers**. That's all.

`[3.2, -1.0, 0.8]` is a vector with 3 numbers.

An **embedding** = turning something (a word, an image, a document)
into a vector so a computer can measure how similar two things are.

"The cat sat" → `[0.2, 0.9, -0.1]`
"The dog sat" → `[0.3, 0.8, -0.2]`  ← close vectors = similar meaning
"pizza recipe" → `[0.9, -0.5, 0.7]` ← far away = different meaning

---

## What is cosine similarity?

A way to measure "how similar are two vectors" — gives a number
from -1 (opposite) to +1 (identical). 0 = unrelated.

You don't need the formula yet (level-16 covers it). Just know:
it compares the ANGLE between two arrows — pointing the same
direction = similar, regardless of length.

---

## What is RAG?

**RAG = Retrieval-Augmented Generation.** Fancy words for:

1. User asks a question
2. Search your documents for the most similar chunk (retrieval)
3. Give that chunk to the LLM as context
4. LLM answers using YOUR data, not just its training

It's "open-book exam" for AI. Without RAG, the model answers from
memory only. With RAG, it looks up your notes first.

Level-12 teaches RAG. Level-16 makes it production-real.

---

## What is an "agent"?

An agent = a program that **decides what to do next on its own**.

Regular program: you call functions in order. Fixed script.
Agent: "I need to check the weather → use weather tool → got
sunny → now summarize." It picks the tool based on the situation.

The loop: Think → Act → Observe → Think again. That's ReAct
(level-13 teaches it).

---

## What is the "singularity"?

The hypothetical point where AI becomes smarter than humans and
can improve itself without us. It hasn't happened. It's a topic
for sci-fi and philosophy — NOT something this curriculum covers
or needs.

What this curriculum teaches is the real, working stuff:
how models learn, how to build them, how to deploy them, how to
make them useful. That's actual engineering, not speculation.

---

## The Big Picture

```
You ──give──> data ──to──> training ──produces──> weights (the model)
                                                     │
You ──ask──> new input ──to──> model.predict() ──> answer
                                                     │
                    (optional: search docs first ──> RAG)
                    (optional: model picks a tool ──> agent)
```

That's the whole pipeline. Every level in this track teaches one
piece of it.

---

## Done? → Try `easy/p01-rules-vs-learning.py`
