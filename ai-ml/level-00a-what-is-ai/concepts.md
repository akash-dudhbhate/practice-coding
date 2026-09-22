# Level 00A — Concepts (What IS AI, Really?)

> Zero math, zero code knowledge assumed. Every term explained
> like you're hearing it for the first time — because you are.
> Each concept explains: **What it is** · **Why it exists** ·
> **Where it's used** · **What goes wrong** without it · worked
> example · code · expected output (this level is code-free —
> the "output" is the picture in your head).

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

**Why it exists:** Some problems have rules too complex or too
fast-changing for a human to write — faces, speech, spam that
mutates daily. AI exists because "if-then by hand" doesn't scale
to those problems.

**Where it's used:** Spam filters, face unlock, recommendations,
fraud detection, autocorrect — anywhere the pattern is easier to
*show* than to *describe*.

**What goes wrong without it:** With hand-written rules, a spammer
changes "FREE" to "F R E E" and your filter dies overnight — you
play whack-a-mole forever. With learned rules, the model adapts
because the new emails are still *similar* to old spam.

---

## What is Machine Learning?

ML is how we BUILD AI. It's the "learning from examples" part.

- You give the program labeled examples: (email text → spam/ham)
- The program tries to find a pattern that separates them
- When it finds one, that pattern IS the model

**Why it exists:** Writing the pattern yourself requires already
knowing it. ML exists for the case where you have examples but no
formula — the data writes the formula.

**Where it's used:** Any time you have historical input→answer
pairs: past sales → future sales, past diagnoses → future
diagnoses, past clicks → future clicks.

**What goes wrong without it:** Without learning, you'd have to
manually encode "what a cat looks like" as pixels rules — an
impossible spec to write. Without *enough* examples, the learned
pattern memorizes noise instead of signal (that's overfitting —
you'll meet it in level-01).

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

**Why it exists:** "The model" gives you a reusable thing — once
the rules are learned, they're frozen into a function you can
call on new inputs forever, without re-showing the examples.

**Where it's used:** Everywhere: `model.fit(...)` learns,
`model.predict(...)` answers. scikit-learn models, PyTorch
networks, and GPT are all "a function + learned numbers."

**What goes wrong without it:** Without a model you re-derive the
answer from raw data every single time — no learned knowledge
persists between predictions.

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

**Why it exists:** You need *something* the learning process can
adjust. Weights are the adjustable part — they're what makes a
blank function into a trained model.

**Where it's used:** Every neural network layer, every linear
model, GPT's ~1.8 trillion parameters — all weights.

**What goes wrong without it:** Without weights there's nothing
to tune — the function can never change its behavior. A bad
weight (0.5 instead of 0.2) means every prediction is off by the
same systematic error — the whole point of training is finding
the right ones.

---

## What is "training"?

1. Show the model an example: input → correct answer
2. Model guesses (using current weights)
3. Compare guess to correct answer — measure the error
4. Nudge the weights slightly to reduce that error
5. Repeat millions of times

That's literally all "training a neural network" means.
Level-08 does this with real PyTorch code — you'll see the loop.

**Why it exists:** You can't set billions of weights by hand.
Training is the automatic process that finds good values —
it's the "learning" in machine learning.

**Where it's used:** `model.fit(X, y)`, `trainer.train()`,
every "epoch" and "loss curve" you'll ever see.

**What goes wrong without it:** Untrained weights are random —
the model outputs noise. And training done wrong explodes: too
big a learning rate and the weights diverge to infinity instead
of converging (level-00b shows this with real numbers).

---

## What is "predicting" (inference)?

Once trained, you freeze the weights and just USE them:
new input → model computes → output. No learning happens here.

**Why it exists:** Separating learning from using is what makes
models practical — you pay the training cost once, then run cheap
predictions millions of times.

**Where it's used:** `model.predict(X_new)` — the API call behind
every "the app recommended this" moment.

**What goes wrong without it:** If weights kept updating on live
traffic, one weird user could corrupt the model for everyone.
Freezing weights at inference is what makes the system stable.

---

## What is a "vector" / "embedding"?

A vector is just a **list of numbers**. That's all.

`[3.2, -1.0, 0.8]` is a vector with 3 numbers.

An **embedding** = turning something (a word, an image, a document)
into a vector so a computer can measure how similar two things are.

"The cat sat" → `[0.2, 0.9, -0.1]`
"The dog sat" → `[0.3, 0.8, -0.2]`  ← close vectors = similar meaning
"pizza recipe" → `[0.9, -0.5, 0.7]` ← far away = different meaning

**Why it exists:** Computers can't compare "cat" and "dog" as
text — but they can compare two lists of numbers with arithmetic.
Embeddings turn meaning into math.

**Where it's used:** Search engines, recommendations, RAG
(level-12/16), every LLM's first layer.

**What goes wrong without it:** Without embeddings, "similar
documents" means "share exact words" — a doc about "automobiles"
never matches a query about "cars." Bad embeddings put unrelated
things close together and search returns nonsense.

---

## What is cosine similarity?

A way to measure "how similar are two vectors" — gives a number
from -1 (opposite) to +1 (identical). 0 = unrelated.

You don't need the formula yet (level-16 covers it). Just know:
it compares the ANGLE between two arrows — pointing the same
direction = similar, regardless of length.

**Why it exists:** You need a similarity score that ignores SIZE
— a 10-word tweet and a 1000-word article can be about the same
thing. Angle captures direction (topic), not magnitude (length).

**Where it's used:** Semantic search, RAG retrieval,
recommendations, deduping near-identical documents.

**What goes wrong without it:** Using raw distance instead,
long documents look "far" from short ones even on the same topic
— your search ranks a long irrelevant doc above a short perfect
one.

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

**Why it exists:** LLMs only know their training data — they can't
see your docs, your database, or anything after their training
cutoff. RAG plugs private/fresh knowledge in at question time.

**Where it's used:** "Chat with your PDF," company knowledge
bots, customer-support assistants that cite real docs.

**What goes wrong without it:** Without retrieval the model
hallucinates — confidently invents policy numbers, prices,
procedures. With bad retrieval, the WRONG chunk gets stuffed
into context and the answer is confidently wrong *with a citation*.

---

## What is an "agent"?

An agent = a program that **decides what to do next on its own**.

Regular program: you call functions in order. Fixed script.
Agent: "I need to check the weather → use weather tool → got
sunny → now summarize." It picks the tool based on the situation.

**Why it exists:** Some tasks can't be scripted end-to-end —
you don't know which steps you'll need until you see intermediate
results. An agent handles branching logic you couldn't pre-write.

**Where it's used:** Research assistants, coding agents (like the
one writing this file), booking/trip planners, multi-tool
workflows. Level-13 teaches the loop.

**What goes wrong without it:** A fixed script breaks on the first
surprise (API down, empty results). But agents go wrong their own
way: an unconstrained agent can loop forever, call the wrong tool,
or rack up API bills — every real agent needs limits and
stop-conditions.

---

## What is the "singularity"?

The hypothetical point where AI becomes smarter than humans and
can improve itself without us. It hasn't happened. It's a topic
for sci-fi and philosophy — NOT something this curriculum covers
or needs.

**Why it exists:** As a speculation, not an engineering target.
It answers "what if AI compounds?" — interesting, but not a
dependency for anything you'll build here.

**What goes wrong without it (framed differently):** The real
failure mode is the opposite — people who *believe* it's imminent
skip learning the actual mechanics. What this curriculum teaches
is the real, working stuff: how models learn, how to build them,
how to deploy them, how to make them useful. That's actual
engineering, not speculation.

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
piece of it. Every agent loop: Think → Act → Observe → Think
again. That's ReAct (level-13 teaches it).

---

## Done? → Try `easy/p01-rules-vs-learning.py`
