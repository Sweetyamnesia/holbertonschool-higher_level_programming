#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_jwt_extended.exceptions import (
    NoAuthorizationError,
    InvalidHeaderError,
)
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)


# Custom handler for missing or invalid JWT token
@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return jsonify({"error": "Missing or invalid JWT token"}), 401


# Custom handler for invalid JWT tokens
@jwt.invalid_token_loader
def invalid_token_callback(callback):
    return jsonify({"error": "Invalid token"}), 401


# Custom handler for expired JWT tokens
@jwt.expired_token_loader
def expired_token_callback(callback, payload):
    return jsonify({"error": "Token has expired"}), 401


# In-memory user data store with hashed passwords and roles
users = {
    "John": {
        "password": generate_password_hash(
            "password", method="pbkdf2:sha256"
        ),
        "role": "user",
    },
    "Suzan": {
        "password": generate_password_hash(
            "password", method="pbkdf2:sha256"
        ),
        "role": "admin",
    },
    "Peter": {
        "password": generate_password_hash(
            "password", method="pbkdf2:sha256"
        ),
        "role": "admin",
    },
    "Lydia": {
        "password": generate_password_hash(
            "password", method="pbkdf2:sha256"
        ),
        "role": "user",
    },
}


# Verify username and password for Basic Auth
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


# Basic Auth protected route example
@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"})


# Login endpoint to authenticate user and provide JWT token
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data.get("username")
    password = data.get("password")
    user = users.get(username)

    # Verify user credentials
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Bad username or password"}), 401

    # Create JWT access token embedding username and role
    access_token = create_access_token(
                                       identity={
                                                 "username": username,
                                                 "role": user["role"],
                                                }
                                        )

    # Return the JWT token
    return jsonify(access_token=access_token), 200


# JWT protected route example
@app.route("/jwt-protected")
@jwt_required()
def protected():
    identity = get_jwt_identity()
    return jsonify({"message": "JWT Auth: Access Granted", "user": identity})


# Role-based access control: admin-only route
@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Access forbidden: Admins only"}), 403
    return jsonify({"message": "Admin Access: Granted"}), 200


# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
