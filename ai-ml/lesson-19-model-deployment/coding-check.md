# Lesson 19 — Coding Check

## Easy

### p01-solve.py — Save and load model
- [ ] Model trained on Iris
- [ ] `joblib.dump` used to save
- [ ] `joblib.load` used to load
- [ ] Predictions before saving printed
- [ ] Predictions after loading printed
- [ ] Both match

### p02-solve.py — Flask API
- [ ] Flask app created
- [ ] `/predict` POST endpoint defined
- [ ] Model loaded at startup
- [ ] JSON input parsed correctly
- [ ] JSON response returned
- [ ] Tested with a sample request

### p03-solve.py — FastAPI app
- [ ] FastAPI app created
- [ ] Pydantic model for input defined
- [ ] `/predict` endpoint defined
- [ ] Tested with a sample request
- [ ] Docs URL (`/docs`) mentioned

## Medium

### p01-solve.py — Complete serving pipeline
- [ ] Real dataset used
- [ ] sklearn Pipeline created (scaler + model)
- [ ] Pipeline saved with joblib
- [ ] FastAPI app loads the pipeline
- [ ] Raw input accepted (unscaled)
- [ ] Pipeline handles scaling internally
- [ ] Tested with 3 sample inputs
- [ ] Predictions are correct

### p02-solve.py — Dockerfile
- [ ] Python base image (slim)
- [ ] Working directory set
- [ ] requirements.txt copied and installed
- [ ] Model file copied
- [ ] App code copied
- [ ] Port exposed
- [ ] CMD with uvicorn
- [ ] requirements.txt written
- [ ] Build and run commands documented

### p03-solve.py — API tests
- [ ] Unit test: model produces valid output
- [ ] Integration test: API responds with 200
- [ ] Integration test: prediction in response
- [ ] Edge case: invalid input returns 422
- [ ] Edge case: missing field returns error
- [ ] `pytest` used
- [ ] `TestClient` from FastAPI used
- [ ] All tests pass

## Hard

### p01-solve.py — Complete deployment package
- [ ] Model trained and saved
- [ ] FastAPI app with `/predict` endpoint
- [ ] FastAPI app with `/health` endpoint
- [ ] Dockerfile written
- [ ] Tests written
- [ ] README.md with usage instructions
- [ ] client.py script for testing
- [ ] All files in one package
- [ ] Package is self-contained

### p02-solve.py — Batch prediction
- [ ] Saved model loaded
- [ ] CSV file read
- [ ] Predictions made on all rows
- [ ] Predictions saved to new CSV
- [ ] Batch prediction time measured
- [ ] Individual API call time measured
- [ ] Performance difference documented
- [ ] Batch is significantly faster

### p03-solve.py — Monitoring script
- [ ] Model loaded
- [ ] Predictions logged with timestamps
- [ ] Input statistics tracked (mean, std)
- [ ] Training stats recorded
- [ ] Current stats compared to training stats
- [ ] Data drift detected (threshold-based)
- [ ] Alert raised if drift detected
- [ ] Monitoring report printed
- [ ] Simulates time progression
