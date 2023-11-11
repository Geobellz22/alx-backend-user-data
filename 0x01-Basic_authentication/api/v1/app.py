#!/usr/bin/env python3

"""
Route module for the API
"""

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None

AUTH_TYPE = getenv("AUTH_TYPE")
if AUTH_TYPE:  # Use truthiness to check if AUTH_TYPE is not empty
    from api.v1.auth.auth import Auth
    auth = Auth()

@app.before_request
def before_request():
    """Runs before request"""
    if auth is None:
        pass
    else:
        excluded_paths = [
            'api/v1/status/',
            'api/v1/unauthorized/',
            'api/v1/forbidden/'
        ]

        # Skip authorization checks for /api/v1/status
        if request.path == '/api/v1/status/':
            return

        if auth.require_auth(request.path, excluded_paths):
            if auth.authorization_header(request) is None:
                abort(401)
            if auth.current_user(request) is None:
                abort(403)

@app.errorhandler(404)
def not_found(error):
    """Not found handler"""
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(401)
def unauthorized(error):
    """Unauthorized handler"""
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def forbidden(error):
    """Forbidden handler"""
    return jsonify({"error": "Forbidden"}), 403

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))  # Ensure port is an integer
    app.run(host=host, port=port)
