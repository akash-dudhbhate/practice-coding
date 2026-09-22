# Level 00B — Weights & Training, Chapter by Chapter

> Read ONE chapter, do the matching problem, then continue.
> Every calculation is worked out with real numbers — check each
> one with a pencil. This is the real math of every neural
> network, just small enough to see whole.
>
> Each chapter explains: **What it is** · **Why it exists** ·
> **Where it's used** · **What goes wrong** without it · worked
> example · code · expected output.

Teaching methods here borrow from the best:
- **3Blue1Brown**: weights as *votes*, counting every knob
- **StatQuest**: tiny real datasets, every number in a table
- **Karpathy**: models as *circuits* of `×` and `+` gates — learn by coding

Our running example: predicting house price from size.
```
Real data we will learn from:
  1000 sqft → $200k
  2000 sqft → $400k
The "true" relationship: price = 0.2 × size   (the model must DISCOVER this)
```

---

## Chapter 1 — What IS a weight? (`easy/p01`)

Think of a neuron as **a thing that holds a number** (3Blue1Brown's
definition — that's all it is). The number it holds is computed as:

```
prediction = weight × input
```

The **weight** is a number the model stores — think of it as a
*volume knob* on the input. Multiply input by it → prediction.

**Watch it work.** weight = 0.2, input = 1000:
```
prediction = 0.2 × 1000 = 200   ✓ matches reality
```
weight = 0.5:
```
prediction = 0.5 × 1000 = 500   ✗ wrong — reality is 200
```

**The voting intuition:** when a model has several inputs, each
weight says "how loudly does this input vote?" Big positive
weight = loud "push the answer up". Negative = "push it down".
Zero = "this input gets no vote at all".

**Why it exists:** A model needs *something* stored inside it that
learning can adjust. The weight is that something — it's the
difference between a fixed formula and a trainable one.

**Where it's used:** Every neuron in every network — a
2-hidden-layer digit recognizer has 13,002 of these knobs, GPT
has ~1.8 trillion. Yours has 1. Same math, more knobs.

**What goes wrong without it:** Set the wrong weight and every
single prediction is systematically off (0.5 predicts 500 instead
of 200 — a 2.5× error on EVERY house). With no weight at all,
there's nothing to tune and the model can never improve.

**Vocabulary:**
- *parameter* — a fancier word for a weight
- *inference* — running `weight × input` after training is done

---

## Chapter 2 — Why bias? `w*x` is not enough (`easy/p02`)

Try this data:
```
0 sqft → $50k    (an empty plot still costs money!)
1000 sqft → $250k
```

Can `weight × size` produce BOTH rows? Try weight = 0.25:
```
0.25 × 1000 = 250   ✓
0.25 × 0    = 0     ✗ needs to be 50
```

**No single weight can do it** — anything × 0 is always 0.
We need a term that survives even when input is zero:

```
prediction = weight × input + bias
              0.2 × 1000 + 50 = 250   ✓
              0.2 × 0    + 50 =  50   ✓
```

**Bias** = the answer when all inputs are zero — the "default
mood" of the neuron (3Blue1Brown: "how active the neuron tends
to be" before any input arrives).

On a graph: weight = slope (tilt of the line), bias = intercept
(where the line crosses the y-axis). You learned this as
`y = mx + c` — `w` is `m`, `b` is `c`.

**Why it exists:** Reality has baselines — an empty plot still
costs money, a spam score isn't zero before words arrive. Bias
lets the model express "the default answer" independent of input.

**Where it's used:** Every neuron has one. In a big model, biases
are ~1% of the parameters but without them every layer is forced
through the origin.

**What goes wrong without it:** `w·x` alone *cannot* fit the data
above — no value of w outputs 50 when x is 0. On a graph, the
line is nailed to the origin: it can tilt but never shift up.
Any problem with a baseline (prices, temperatures, scores) is
unfittable without bias.

**Karpathy's circuit view:** values flow through gates:
```
x ──[× w]──┐
           ├──[+]──→ prediction
1 ──[× b]──┘        (bias is a weight whose input is always 1)
```
That picture — multiply gates feeding an add gate — IS a neuron.

---

## Chapter 3 — Measuring "wrong": residuals and loss (`easy/p03`)

StatQuest's method: put every example in a table, compute the
**residual** (prediction − truth) for each, square them, add up.

weight=0.3, bias=0 on our 2 examples:

| size | truth | pred = 0.3·size | residual | residual² |
|------|-------|------------------|----------|-----------|
| 1000 | 200   | 300              | +100     | 10000     |
| 2000 | 400   | 600              | +200     | 40000     |

**loss = 10000 + 40000 = 50000**  (sum of squared residuals)

weight=0.2, bias=0:

| size | truth | pred | residual | residual² |
|------|-------|------|----------|-----------|
| 1000 | 200   | 200  | 0        | 0         |
| 2000 | 400   | 400  | 0        | 0         |

**loss = 0** — the best possible score.

**Why square?** Two reasons:
1. A +100 and a −100 residual would cancel to 0 — hiding that
   BOTH were wrong. Squaring makes them add: 10000 + 10000.
2. Big mistakes get punished extra: a residual of 200 costs
   40000, not just "twice as bad" but *four times* as bad as 100.

**Why it exists:** "The model seems off" is not a number. Loss
compresses all errors into ONE number you can minimize — it's
the scoreboard training optimizes against.

**Where it's used:** Every training loop ever: MSE for
regression, cross-entropy for classification. `loss.backward()`
in PyTorch is this chapter.

**What goes wrong without it:** Without squaring, +100 and −100
cancel to loss=0 — the model looks perfect while being wrong on
both. Without any loss, you can't compare weight=0.3 to
weight=0.2 — you have no compass for which direction to nudge.

**The whole game of training:** find weights that make this sum
smallest. loss = 0 means perfect on the training data.

---

## Chapter 4 — One training step (`medium/p01`)

The residual's sign tells you which way to move the weight:
- residual **positive** → prediction too high → *decrease* weight
- residual **negative** → prediction too low → *increase* weight

The update rule (this IS gradient descent for one weight):

```
new_weight = weight − step × residual × input
```

**Why `× input`?** The input caused this much of the error, so
the correction should scale with it. (For the full math: the
derivative of `residual²` with respect to `w` is `2·residual·x` —
the `× input` comes from the chain rule. We fold the 2 into step.)

**Why minus?** We walk *downhill* on the loss. If the residual
is +100, subtracting makes weight smaller → prediction smaller.

weight=0.3, input=1000, truth=200, step=0.0000001:
```
residual   = 300 − 200 = +100
new_weight = 0.3 − 0.0000001 × 100 × 1000 = 0.3 − 0.01 = 0.29
```
Next prediction: `0.29 × 1000 = 290` — residual went +100 → +90.

Bias updates the same way, but its "input" is always 1:
```
new_bias = bias − step × residual
```

**Why it exists:** Guessing weights at random would take forever.
The update rule turns each example into a direction and a
distance — it's how "learning" becomes a mechanical procedure
instead of luck.

**Where it's used:** This one line — `w −= lr × gradient` — runs
trillions of times inside every model training job on Earth.
PyTorch's `optimizer.step()` is exactly this.

**What goes wrong without it:** Flip the minus to a plus and the
model walks UPHILL — every step makes the loss bigger, weights
rocket to infinity. Get the sign or the `× input` wrong and the
"correction" doesn't match which weight caused the error.

---

## Chapter 5 — Learning rate (`medium/p02`)

`step` is the **learning rate** — how far each nudge goes.

- **Too small** (0.0000000001): works, needs 1000s of steps.
- **Just right** (0.0000001): converges in ~20 steps.
- **Too big** (0.001): *overshoots* — watch it explode:

```
w=0.3, step=0.001, x=1000, truth=200:
step 1: residual +100 → w = 0.3 − 0.001·100·1000 = 0.3 − 100 = −99.7  (!!)
step 2: pred = −99700, residual = −99900
        → w = −99.7 − 0.001·(−99900)·1000 = −99.7 + 99900 = huge  (!!!)
```
Each step overcorrects worse than the last — the numbers explode
to infinity. This is a *divergent* training run. Real training
picks small rates (0.01–0.0001) and *normalizes* inputs (scales
them near 0-1) precisely to prevent this.

**Why it exists:** The update rule says *which way* and *how much*
proportional to error — but "how much" still needs a dial. The
learning rate is that dial: the only knob between "crawl forever"
and "explode."

**Where it's used:** It's the #1 hyperparameter in all of deep
learning — every optimizer (SGD, Adam) is built around it, and
level-05's grid search tunes it.

**What goes wrong without it:** This is THE concrete failure:
step too big → `w` goes 0.3 → −99.7 → +99900 → your loss reads
`nan` and the run is dead. Step too small → training takes
weeks of GPU time and still hasn't converged. No middle ground
exists without tuning it.

---

## Chapter 6 — Many examples (`medium/p03`)

One example can mislead you (noise, a typo). Real training looks
at ALL the data each round — average the corrections:

```
for each example:  residual_i = pred_i − truth_i
w −= step × average(residual_i × input_i)
b −= step × average(residual_i)
```

Data: (1000→200), (2000→400), (1500→300). w=0.1, b=0,
step=0.0000001:

| x    | truth | pred=0.1x | res  | res·x    |
|------|-------|-----------|------|----------|
| 1000 | 200   | 100       | −100 | −100000  |
| 2000 | 400   | 200       | −200 | −400000  |
| 1500 | 300   | 150       | −150 | −225000  |

```
avg(res·x) = (−100000−400000−225000)/3 = −241667
avg(res)   = (−100−200−150)/3 = −150
new_w = 0.1 − 0.0000001·(−241667) = 0.124
new_b = 0   − 0.0000001·(−150)    = 0.000015
```
Both went UP — every prediction was too low. Correct direction.

**Why it exists:** Any single example might be a fluke (a typo'd
price, a weird house). Averaging makes the update serve the
*whole dataset* — the majority's correction drowns out one bad
row's pull.

**Where it's used:** This is "batch gradient descent." Real
training uses mini-batches (e.g., 32–512 rows per step) — the
same averaging idea, chunked for GPU efficiency.

**What goes wrong without it:** Update on one example at a time
and a single outlier yanks the weight toward itself — the model
oscillates chasing each row instead of settling on the shared
pattern. A typo'd row can undo ten good steps.

---

## Chapter 7 — The real loop: gradient descent (`hard/p01`)

Put it all together — repeat until loss is tiny:

```
w, b = 0.0, 0.0
repeat N rounds:
    loss = 0
    for each (x, truth):  pred = w·x + b;  res = pred − truth;  loss += res²
    w −= step × mean(res·x over all examples)
    b −= step × mean(res over all examples)
return w, b
```

This is **gradient descent** — the algorithm inside PyTorch,
TensorFlow, everything. "Gradient" = direction the loss grows;
we step the opposite way. "Descent" = walking downhill on the
loss surface — picture a ball rolling into a valley.

Run it on our data: after ~500 rounds `w ≈ 0.2, b ≈ 0` — the
model **discovered** price = 0.2×size itself. Nobody told it.

**Why it exists:** You can't solve most models with a formula —
there's no closed-form answer for a billion weights. Iterating
"predict → measure → nudge" is the only way that scales.

**Where it's used:** Literally all of it — every `model.fit()`,
every epoch, every loss curve in this track is this loop.

**What goes wrong without it:** Stop the loop too early and the
model is half-trained (w stuck at 0.05, predictions all 4× low).
Loop forever without checking loss and you can't tell converged
(plateaued) from diverged (exploding) — the loss history IS your
dashboard.

---

## Chapter 8 — Two weights: the dot product (`hard/p02`)

Real inputs have many features: size AND rooms AND age.

```
prediction = w₁·size + w₂·rooms + w₃·age + b
```

The pattern `w₁x₁ + w₂x₂ + w₃x₃` — each input times its weight,
all added — is the **dot product**. In circuit terms (Karpathy):
three `×` gates feeding one big `+` gate.

```
dot([0.15, 5, −0.5], [1500, 3, 10])
  = 0.15·1500 + 5·3 + (−0.5)·10
  = 225 + 15 − 5 = 235
```

**Voting intuition again:** size votes +225 (loud), rooms vote
+15, age votes −5 (pushes price DOWN — older = cheaper). The
prediction is the sum of all votes plus the bias.

**Training rule extends mechanically:** each weight updates with
its own input — `wᵢ −= step · res · xᵢ`.

**Count the knobs** (3Blue1Brown's habit): a neuron with 3 inputs
has 3 weights + 1 bias = **4 parameters**. A layer of 10 such
neurons: 40. Always count — it builds the intuition for why big
models need so much data.

**Why it exists:** One feature rarely explains reality — price
depends on size AND rooms AND age. The dot product is the minimal
machine for "combine many clues into one number."

**Where it's used:** Every layer of every network is a batch of
dot products (`X @ W + b`). Attention in transformers is also
dot products — between queries and keys.

**What goes wrong without it:** Without per-input weights, all
features vote at equal volume — a useless feature (house color)
shouts as loud as size. And if you mix up which weight pairs
with which input (`w₁` on `rooms`), the model learns nonsense
correlations that never transfer.

---

## Chapter 9 — The full picture (`hard/p03`)

Train `price = w₁·size + w₂·rooms + b` on 4 examples, then
predict a house never seen in training:

```
data:
  (1200 sqft, 2 rooms) → 240k
  (1500 sqft, 3 rooms) → 300k
  (2000 sqft, 4 rooms) → 400k
  (1000 sqft, 2 rooms) → 200k
hidden truth: w₁=0.2, w₂=0, b=0   (rooms secretly don't matter)
```

After 500 rounds the model finds w₁≈0.2, w₂≈0 — including
learning that rooms are *irrelevant* (it zeroed that vote out
by itself!). Then predict (1800 sqft, 3 rooms) → ≈360.

**You just did what `LinearRegression().fit()` does.** Every
level after this adds pieces — nonlinear squashes, layers of
neurons — but the loop never changes:

```
predict → measure loss → nudge weights downhill → repeat
```

**Why it exists:** This chapter is the payoff — it proves the
machinery works end-to-end on data it hasn't memorized. Predicting
a *new* house correctly is the difference between a model and a
lookup table.

**Where it's used:** This IS `sklearn`'s LinearRegression,
PyTorch's training loop, and — with bigger matrices — the core
of how GPT was trained.

**What goes wrong without it:** Skip the "predict on unseen data"
step and you can't tell learned-the-pattern from memorized-the-
data. A model that nails the 4 training rows but predicts a new
1800sqft house at −50k has memorized, not learned — that's
overfitting, and it's why every later level holds out a test set.

---

## The map so far

```
Ch1:  pred = w·x                weight = the volume knob / vote
Ch2:  pred = w·x + b            bias = the default mood
Ch3:  loss = Σ residual²        how wrong, in one number
Ch4:  w −= step·res·x           one fix, scaled by its input
Ch5:  step size matters         too big explodes, too small crawls
Ch6:  average over examples     one example can lie
Ch7:  loop until loss ≈ 0       gradient descent — done
Ch8:  w₁x₁ + w₂x₂ + b           many features = dot product + votes
Ch9:  all of it on real data    you just trained a model
```

Now do the problems — **in order**.
