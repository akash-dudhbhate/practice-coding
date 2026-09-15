"""
Lesson 02 - Hard P02
ColumnTransformer for mixed data types:
  - numeric columns: impute (median) + scale (StandardScaler)
  - categorical columns: impute (most_frequent) + one-hot encode
Combined with a RandomForestClassifier in a Pipeline.

Solution:
  1. Create a mixed-type dataset with missing values.
  2. Define numeric and categorical column lists.
  3. Build a ColumnTransformer with separate pipelines per type.
  4. Wrap in a Pipeline with RandomForestClassifier.
  5. Split, fit, predict, evaluate.
"""

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# ---------------------------------------------------------------------------
# 1. Create a mixed-type dataset with missing values
# ---------------------------------------------------------------------------
np.random.seed(42)
n = 300
df = pd.DataFrame({
    "age": np.random.randint(25, 65, size=n).astype(float),
    "income": np.random.randint(30000, 120000, size=n).astype(float),
    "credit_score": np.random.randint(300, 850, size=n).astype(float),
    "education": np.random.choice(["HighSchool", "Bachelors", "Masters", "PhD"], size=n),
    "employment": np.random.choice(["Employed", "SelfEmployed", "Unemployed"], size=n),
})
# Inject missing values
for col in ["age", "income", "credit_score"]:
    df.loc[df.sample(frac=0.08, random_state=42).index, col] = np.nan
for col in ["education", "employment"]:
    df.loc[df.sample(frac=0.05, random_state=42).index, col] = np.nan

# Create a binary target: approved if income > 60000 and credit_score > 600
y = ((df["income"].fillna(df["income"].median()) > 60000) &
     (df["credit_score"].fillna(df["credit_score"].median()) > 600)).astype(int)

print(f"Dataset shape: {df.shape}")
print(f"Missing values:\n{df.isnull().sum()}\n")

# ---------------------------------------------------------------------------
# 2. Define column groups
# ---------------------------------------------------------------------------
numeric_features = ["age", "income", "credit_score"]
categorical_features = ["education", "employment"]

# ---------------------------------------------------------------------------
# 3. Build the ColumnTransformer
# ---------------------------------------------------------------------------
# Solution: ColumnTransformer applies different preprocessing to different
# column subsets, all within a single object that prevents data leakage.
numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])

categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ],
    remainder="drop",
)

# ---------------------------------------------------------------------------
# 4. Full pipeline: preprocessing + model
# ---------------------------------------------------------------------------
full_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42)),
])

# ---------------------------------------------------------------------------
# 5. Split, fit, predict, evaluate
# ---------------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    df, y, test_size=0.2, random_state=42, stratify=y
)

full_pipeline.fit(X_train, y_train)
y_pred = full_pipeline.predict(X_test)

print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.4f}\n")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# ---------------------------------------------------------------------------
# 6. Inspect feature names after transformation
# ---------------------------------------------------------------------------
fitted_preprocessor = full_pipeline.named_steps["preprocessor"]
cat_encoder = fitted_preprocessor.named_transformers_["cat"].named_steps["onehot"]
cat_feature_names = cat_encoder.get_feature_names_out(categorical_features)
all_feature_names = numeric_features + cat_feature_names.tolist()
print(f"Total features after preprocessing: {len(all_feature_names)}")
print(f"Feature names: {all_feature_names}")

# Feature importances from the random forest
importances = full_pipeline.named_steps["classifier"].feature_importances_
print("\nFeature Importances:")
for name, imp in sorted(zip(all_feature_names, importances), key=lambda x: -x[1]):
    print(f"  {name:<25} {imp:.4f}")
