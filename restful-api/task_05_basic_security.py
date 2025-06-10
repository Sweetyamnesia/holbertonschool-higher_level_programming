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
    "John": {"password": generate_password_hash("password"), "role": "user"},
    "Suzan": {"password": generate_password_hash("password"), "role": "admin"},
    "Peter": {"password": generate_password_hash("password"), "role": "admin"},
    "Lydia": {"password": generate_password_hash("password"), "role": "user"},
}

tokens = {
    "secret-token-1": "John",
    "secret-token-2": "Suzan",
    "secret-token-3": "Peter",
    "secret-token-4": "Lydia"
}


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def verify_password(username, password):
    if (username in users and
            check_password_hash(users.get(username)["password"], password)):
        return "Basic Auth: Access Granted"
    else:
        return 401


@app.route("/login", methods=["POST"])
@jwt_required()
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.route("/jwt-protected")
def protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
def admin():
    return "Admin Access: Granted"


get_jwt_identity()


if __name__ == '__main__':
    app.run(debug=True)
