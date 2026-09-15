"""SOLUTION: Flask app with 3 routes (Easy)"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Home Page!"

@app.route("/about")
def about():
    return "About Us"

@app.route("/contact")
def contact():
    return "Contact: hello@example.com"

if __name__ == "__main__":
    app.run(debug=True)
