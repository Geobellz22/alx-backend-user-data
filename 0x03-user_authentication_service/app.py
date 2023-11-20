#!/usr/bin/env python3
"""Setting up a basic flask app"""

from flask import Flask, jsonify
from auth import Auth


app = Flask(__name__)
AUTH = AUTH()


@app.route("/")
def index() -> str:
    message = {"message": "Bienvenue"}
    return jsonify(message)


@app.route("/users", methods=["POST"])
def user() -> str:
    """register new user"""
    email = register.form.get('email')
    paswword = register.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
