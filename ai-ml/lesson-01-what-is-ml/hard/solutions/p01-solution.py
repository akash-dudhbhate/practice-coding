"""
Lesson 01 - Hard P01
Design a full ML pipeline for diabetes prediction by answering 8 questions.

Solution:
  Q1. Problem type
  Q2. Data sources & features
  Q3. Data preprocessing steps
  Q4. Feature engineering
  Q5. Model choice
  Q6. Train/validation/test strategy
  Q7. Evaluation metrics
  Q8. Deployment & monitoring
"""

# ---------------------------------------------------------------------------
# Pipeline design answers
# ---------------------------------------------------------------------------
pipeline = {
    "Q1_problem_type": {
        "answer": "Binary classification",
        "detail": (
            "Predict whether a patient will develop diabetes (1) or not (0) "
            "within a given time window based on clinical and demographic features."
        ),
    },
    "Q2_data_and_features": {
        "answer": "Electronic health records (EHR) + lifestyle survey data",
        "features": [
            "age, sex, BMI",
            "blood_pressure",
            "glucose / HbA1c level",
            "insulin level",
            "family history of diabetes",
            "cholesterol (HDL, LDL, triglycerides)",
            "physical_activity_level",
            "smoking_status",
        ],
        "detail": "Combine lab results, demographics, and lifestyle factors for a rich feature set.",
    },
    "Q3_preprocessing": {
        "answer": [
            "Handle missing values (median imputation for numeric, mode for categorical).",
            "Encode categorical variables (one-hot for nominal, ordinal for ordered).",
            "Scale numeric features (StandardScaler).",
            "Remove or cap outliers (IQR or winsorization).",
            "Split data BEFORE fitting preprocessors to avoid leakage.",
        ],
        "detail": "Use sklearn Pipeline + ColumnTransformer so all preprocessing is fit on train data only.",
    },
    "Q4_feature_engineering": {
        "answer": [
            "Create BMI category (underweight/normal/overweight/obese).",
            "Age groups (young/middle/senior).",
            "Glucose-to-insulin ratio.",
            "Interaction terms (e.g., BMI x age).",
            "Polynomial features for key numeric variables (degree 2).",
        ],
        "detail": "Domain-informed features often improve predictive power beyond raw inputs.",
    },
    "Q5_model_choice": {
        "answer": "Gradient Boosted Trees (e.g., XGBoost / LightGBM)",
        "detail": (
            "Start with Logistic Regression as a baseline. Then use gradient boosting "
            "for higher accuracy, built-in handling of mixed feature types, and "
            "feature importance for interpretability. Random Forest is a good fallback."
        ),
    },
    "Q6_train_test_strategy": {
        "answer": "Stratified train/validation/test split + cross-validation",
        "detail": (
            "Split 70/15/15 with stratification on the target to preserve class balance. "
            "Use 5-fold stratified cross-validation on the training set for hyperparameter tuning. "
            "Keep the test set untouched until final evaluation."
        ),
    },
    "Q7_evaluation_metrics": {
        "answer": "ROC-AUC, precision, recall, F1-score, confusion matrix",
        "detail": (
            "Medical screening favors recall (don't miss true diabetes cases) while keeping "
            "precision acceptable. ROC-AUC summarizes discrimination across thresholds. "
            "Report a confusion matrix and, if costs are known, use a cost-sensitive threshold."
        ),
    },
    "Q8_deployment_monitoring": {
        "answer": "Deploy as a REST API; monitor for data drift and performance decay",
        "detail": (
            "Wrap the trained pipeline in a FastAPI/Flask endpoint. Log predictions and "
            "incoming feature distributions. Retrain periodically (e.g., quarterly) or when "
            "drift is detected (PSI > threshold). Track real-world precision/recall over time."
        ),
    },
}

# ---------------------------------------------------------------------------
# Print the pipeline design
# ---------------------------------------------------------------------------
for key, val in pipeline.items():
    label = key.replace("_", " ").title()
    print(f"{label}")
    print(f"  Answer: {val['answer']}")
    if "features" in val:
        print(f"  Features: {val['features']}")
    if "detail" in val:
        print(f"  Detail:   {val['detail']}")
    print()
