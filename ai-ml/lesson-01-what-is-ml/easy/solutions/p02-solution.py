"""
Lesson 01 - Easy P02
Identify the features (X) and the label (y) for two scenarios.

Solution:
  Scenario 1 -> Features: square footage, bedrooms, age; Label: price
  Scenario 2 -> Features: age, blood pressure, cholesterol; Label: has disease
"""

# ---------------------------------------------------------------------------
# Scenario 1: House price prediction
# ---------------------------------------------------------------------------
scenario_1 = {
    "name": "House price prediction",
    "features_X": ["square_footage", "num_bedrooms", "house_age_years"],
    "label_y": "price",
    "note": "We use square footage, bedrooms, and age to predict the selling price (continuous).",
}

# ---------------------------------------------------------------------------
# Scenario 2: Disease diagnosis
# ---------------------------------------------------------------------------
scenario_2 = {
    "name": "Disease diagnosis",
    "features_X": ["patient_age", "blood_pressure", "cholesterol_level"],
    "label_y": "has_disease",
    "note": "We use patient age, blood pressure, and cholesterol to predict whether the patient has the disease (binary).",
}

# ---------------------------------------------------------------------------
# Print answers
# ---------------------------------------------------------------------------
for i, s in enumerate([scenario_1, scenario_2], start=1):
    print(f"Scenario {i}: {s['name']}")
    print(f"  Features (X): {s['features_X']}")
    print(f"  Label (y):    {s['label_y']}")
    print(f"  Note:         {s['note']}")
    print()
