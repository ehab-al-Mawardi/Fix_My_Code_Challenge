#!/usr/bin/python3
"""
Web server script using Flask.

This script creates a Flask web server that registers a blueprint (app_views)
for handling routes and includes a custom error handler for 404 errors.
"""

from api.v1.views import app_views
from flask import Flask, jsonify, make_response

app = Flask(__name__)
app.register_blueprint(app_views)

@app.errorhandler(404)
def not_found(error):
    """Custom error handler for 404 errors.

    Returns a JSON response with an error message.
    """
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    # Run the web server
    app.run(host="0.0.0.0", port=5000, debug=True)  # Set debug=True for development
