"""
LEVEL 05 PROJECT — Model Report Card
========================================

You're choosing between 3 models for a client. Build
`report_card(X_train, X_test, y_train, y_test)` that trains all
three and prints a comparison table — the deliverable you'd
actually show a stakeholder.

MODELS: LogisticRegression, RandomForestClassifier(42),
        GradientBoostingClassifier(42)

METRICS per model: accuracy, precision, recall, f1
                    + 5-fold CV mean accuracy on the training set

DATA: load_breast_cancer() — real, built into sklearn.

EXPECTED OUTPUT (yours should look like this table):
  ```
  Model               Acc   Prec  Rec   F1    CV-mean
  logistic            .973  .96x  .97x  .97x  .95x
  random_forest       .96x  .96x  .96x  .96x  .96x
  grad_boost          .95x  .95x  .96x  .95x  .94x

  Recommendation: logistic — best F1 + simplest model.
  ```

CONTRACT: return a dict {model_name: {"accuracy":..,"f1":..,"cv":..}}
so the checker can verify.

THEN ANSWER (in comments): which model wins and why — is highest
accuracy always the right choice? What would you check next?
"""

# === WRITE YOUR CODE BELOW ===

def report_card(X_train, X_test, y_train, y_test):
    # TODO: train 3 models, compute metrics, print table, return dict
    pass


if __name__ == "__main__":
    from sklearn.datasets import load_breast_cancer
    from sklearn.model_selection import train_test_split
    X, y = load_breast_cancer(return_X_y=True)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2,
                                            random_state=42, stratify=y)
    report_card(X_tr, X_te, y_tr, y_te)
