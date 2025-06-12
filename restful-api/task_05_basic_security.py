#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

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


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"})


@app.route("/login", methods=["POST"])
def login():
    username = request.get_json("username")
    password = request.get_json("password")
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Bad username or password"}), 401

    access_token = create_access_token(identity={"username": username,
                                                 "role": user["role"]})
    return jsonify(access_token=access_token)


@app.route("/jwt-protected")
@jwt_required()
def protected():
    identity = get_jwt_identity()
    return jsonify({"message": "JWT Auth: Access Granted", "user": identity})


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Access forbidden: Admins only"}), 403
    return jsonify({"message": "Admin Access: Granted"}), 200



if __name__ == '__main__':
    app.run(debug=True)
