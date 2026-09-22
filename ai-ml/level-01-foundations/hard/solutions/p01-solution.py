"""
LEVEL 01 — ML Foundations
HARD P01 — Full ML Pipeline Design (Solution)
==============================================
"""

def design_pipeline():
    """Design a complete ML pipeline for diabetes prediction."""
    return {
        "problem": "classification (diabetic / not-diabetic)",
        "data": "patient records: age, BMI, blood pressure, glucose, family history",
        "preprocessing": "handle missing values, normalize numeric features, encode categories",
        "split": "80/20",
        "model": "logistic regression or decision tree (simple, interpretable)",
        "training": "model.fit(X_train, y_train) on the training set",
        "evaluation": "recall — missing a disease is worse than a false alarm",
        "deployment": "API endpoint that takes patient data and returns risk score"
    }


if __name__ == "__main__":
    result = design_pipeline()
    for key, value in result.items():
        print(f"{key}: {value}")
