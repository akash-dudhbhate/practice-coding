# Capstone Project 04 — End-to-End ML Pipeline

> **Type:** Capstone Project
> **Subject:** AI/ML
> **Estimated sell price:** $1000–2000
> **Difficulty:** Advanced
> **Prerequisites:** All 20 AI/ML lessons

## Project Brief

Build a complete, production-ready ML pipeline from data collection to deployment. This is a high-value sellable product — companies pay $5,000–$50,000 for ML pipelines. You'll build a sentiment analysis model that classifies text as positive/negative/neutral, deploy it as an API, and wrap it in Docker.

## What you'll build

An end-to-end ML system with:
- **Data collection** — scrape or download a text dataset (reviews, tweets)
- **Data preprocessing** — clean text, handle missing values, tokenize
- **Feature engineering** — TF-IDF, word counts, text features
- **Model training** — train a classification model (logistic regression + XGBoost)
- **Model evaluation** — accuracy, precision, recall, F1, confusion matrix, ROC-AUC
- **Hyperparameter tuning** — GridSearchCV or RandomizedSearchCV
- **Model serialization** — save with joblib/pickle
- **API server** — FastAPI endpoint that accepts text and returns sentiment
- **Docker container** — Dockerfile for the entire system
- **Tests** — test the API endpoints and model predictions
- **Documentation** — README with full pipeline description

## Skills you'll demonstrate

- Data preprocessing and cleaning
- Feature engineering for text
- Model training (multiple algorithms)
- Model evaluation (multiple metrics)
- Cross-validation and hyperparameter tuning
- Model serialization and loading
- FastAPI for model serving
- Docker containerization
- Testing ML systems
- Full pipeline documentation

## Sellable pitch

> "I'll build you a complete sentiment analysis system — from data collection to a deployed API. The pipeline includes preprocessing, feature engineering, model training with hyperparameter tuning, evaluation, and deployment as a Dockerized FastAPI service. Production-ready with tests and documentation."

## Requirements

- [ ] Data: download or scrape 10,000+ text samples with labels
- [ ] Preprocessing: text cleaning, lowercasing, remove special chars, handle missing
- [ ] Feature engineering: TF-IDF vectorization, additional text features (length, word count)
- [ ] Train at least 2 models: logistic regression (baseline) + XGBoost (advanced)
- [ ] Evaluation: accuracy, precision, recall, F1, confusion matrix, ROC-AUC
- [ ] Cross-validation: 5-fold stratified cross-validation
- [ ] Hyperparameter tuning: GridSearchCV for best model
- [ ] Model comparison: document which model performs best and why
- [ ] Save best model with joblib/pickle
- [ ] FastAPI endpoint: POST /predict accepts {"text": "..."} returns {"sentiment": "positive", "confidence": 0.95}
- [ ] FastAPI endpoint: GET /health returns model status
- [ ] Input validation with Pydantic
- [ ] Error handling for invalid inputs
- [ ] Dockerfile for the API
- [ ] docker-compose.yml
- [ ] Tests: test API endpoints, test model predictions, test edge cases (empty text, very long text)
- [ ] README with: pipeline description, setup, training, deployment, API usage
- [ ] Requirements.txt with pinned versions

## Getting started

1. Find/download a labeled text dataset (IMDB reviews, Twitter sentiment, etc.)
2. Explore the data (EDA) — class distribution, text lengths, common words
3. Preprocess: clean, tokenize, handle missing values
4. Feature engineering: TF-IDF + custom features
5. Train baseline model (logistic regression)
6. Train advanced model (XGBoost)
7. Evaluate both models with multiple metrics
8. Tune the best model with GridSearchCV
9. Save the best model
10. Build FastAPI server with /predict and /health endpoints
11. Write tests
12. Create Dockerfile and docker-compose
13. Write comprehensive README
14. Test the full pipeline end-to-end

## Deliverables

- `data/` — raw and processed data
- `notebooks/` — EDA and experimentation notebooks
- `src/` — preprocessing, training, evaluation modules
- `models/` — saved model files
- `api/` — FastAPI server
- `tests/` — test suite
- `Dockerfile` + `docker-compose.yml`
- `requirements.txt`
- `README.md` with full documentation
