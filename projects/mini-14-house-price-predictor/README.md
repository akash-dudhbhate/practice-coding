# Mini Project 14 — House Price Predictor

> **Type:** Mini Project
> **Subject:** AI/ML
> **Estimated sell price:** $100–200
> **Difficulty:** Beginner–Intermediate
> **Prerequisites:** Lessons 01–10 (ML Foundations through Cross-Validation)

## Project Brief

Build a house price prediction model using linear regression. Train on a housing dataset, evaluate the model, and create a simple function that predicts prices for new inputs. This is a classic ML portfolio project that demonstrates the full ML workflow.

## What you'll build

A Python script/notebook that:
- Loads a housing dataset (use sklearn's California Housing or Boston dataset)
- Preprocesses the data (scaling, train/test split)
- Trains a linear regression model
- Evaluates with R², MAE, and RMSE
- Predicts prices for new inputs
- Visualizes actual vs predicted prices

## Skills you'll demonstrate

- Data loading and preprocessing
- Train/test split
- Linear regression (sklearn)
- Model evaluation (R², MAE, RMSE)
- Data visualization (matplotlib)
- Making predictions with new data

## Requirements

- [ ] Load housing dataset (sklearn datasets or CSV)
- [ ] Explore data: print shape, feature names, basic stats
- [ ] Split into train (80%) and test (20%)
- [ ] Scale features (StandardScaler)
- [ ] Train LinearRegression model
- [ ] Evaluate: print R², MAE, RMSE on test set
- [ ] Scatter plot: actual vs predicted prices (matplotlib)
- [ ] Function `predict_price(features)` that takes a dict/array and returns predicted price
- [ ] Print example predictions for 3 sample houses
- [ ] Document which features are most important (coefficients)

## Deliverables

- `house_predictor.py` or Jupyter notebook
- Trained model saved (joblib)
- Visualization plot
- README with setup and usage
