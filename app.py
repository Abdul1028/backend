from flask import Flask, request, jsonify
from flask_cors import CORS
from routes.transaction import transaction_blueprint
from db import database

app = Flask(__name__)
CORS(app)

# Initialize the database with the Flask app instance
database.init_app(app)

app.register_blueprint(transaction_blueprint, url_prefix='/api/v1')

@app.route('/')
def index():
    return "Hello, this is your Flask app!"

if __name__ == "__main__":
    app.run(port=5000)
