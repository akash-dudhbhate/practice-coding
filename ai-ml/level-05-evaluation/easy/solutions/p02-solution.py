"""Level 05 Evaluation — Easy P02 Solution"""

def solve():
    y_true = [0, 0, 1, 1, 1, 0, 1, 0, 1, 1]
    y_pred = [0, 1, 1, 1, 0, 0, 1, 0, 1, 1]
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    tn = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 0)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)
    print(f"Confusion Matrix:")
    print(f"  TP={tp}  FN={fn}")
    print(f"  FP={fp}  TN={tn}")
    return {"TP": tp, "FP": fp, "TN": tn, "FN": fn}

if __name__ == "__main__":
    solve()