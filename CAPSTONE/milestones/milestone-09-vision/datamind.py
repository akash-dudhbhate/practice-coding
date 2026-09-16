"""
MILESTONE 09 — DataMind Vision Input
=====================================

Level-09 skill applied: accept images as input.

TASK:
  Implement `flatten_image(img)` — takes a 2D numpy array
  (grayscale image) and returns a normalized 1D vector:
    - flatten to 1D
    - divide by max possible pixel value (255 or 16)

  Implement `is_image_like(obj)` — True if obj is a 2D
  numpy array of numbers (so DataMind can route image
  vs tabular inputs automatically).

Run:  python3 datamind.py
Check: python3 check_milestone.py
"""

WEIGHTS = [0.5, 0.3, 0.2]
BIAS = 0.1


def predict(features):
    pass  # M00

def describe():
    pass  # M01

def load_records(raw):
    pass  # M02

def summarize(rows):
    pass  # M03

def auto_chart(rows, filename="chart.png"):
    pass  # M03

def train(X, y):
    pass  # M04

def model_predict(model, features):
    pass  # M04

def evaluate(model, X_test, y_test):
    pass  # M05

def full_report(X, y):
    pass  # M05

def add_features(rows):
    pass  # M06

def compare(X_basic, X_eng, y):
    pass  # M06

def segment(X, k=None):
    pass  # M07

def profile(X, labels):
    pass  # M07

def neural_fit(X, y, hidden=16, epochs=100):
    pass  # M08


def flatten_image(img):
    """2D array → normalized 1D vector."""
    # MILESTONE 09 — TODO
    pass


def is_image_like(obj):
    """True for 2D numeric arrays."""
    # MILESTONE 09 — TODO
    pass


if __name__ == "__main__":
    import numpy as np
    img = np.array([[0, 128, 255], [64, 32, 16], [200, 100, 50]])
    print(flatten_image(img))
    print(is_image_like(img), is_image_like([1, 2, 3]))
