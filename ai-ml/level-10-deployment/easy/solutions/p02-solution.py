"""Level 10 Deployment — Easy P02 Solution"""

from flask import Flask, request, jsonify
import numpy as np

def solve():
    app = Flask(__name__)
    @app.route('/predict', methods=['POST'])
    def predict():
        data = request.get_json()
        features = np.array(data['features'])
        # Dummy prediction
        prediction = 1 if features.sum() > 0 else 0
        return jsonify({'prediction': int(prediction)})
    print("Flask API created. Run with: app.run(debug=True)")
    return app

if __name__ == "__main__":
    app = solve()
    # app.run(debug=True)  # Uncomment to run