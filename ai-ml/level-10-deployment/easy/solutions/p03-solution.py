"""Level 10 Deployment — Easy P03 Solution"""

from flask import Flask, jsonify

def solve():
    app = Flask(__name__)
    model_info = {
        'name': 'LogisticRegression',
        'version': '1.0',
        'accuracy': 0.85,
        'features': ['age', 'income', 'score']
    }
    @app.route('/info', methods=['GET'])
    def info():
        return jsonify(model_info)
    print("Model info endpoint created")
    return app

if __name__ == "__main__":
    solve()