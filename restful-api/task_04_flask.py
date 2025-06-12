#!/usr/bin/python3
from flask import Flask, jsonify, request

"""Initialize the Flask application"""
app = Flask(__name__)

"""A simple in-memory data store"""
users = {}

"""Root route that returns a welcome message"""
@app.route("/")
def home():
    return "Welcome to the Flask API!"

"""Route to return a list of usernames"""
@app.route("/data")
def data():
    return jsonify(list(users.keys()))

"""Route to return the API status"""
@app.route("/status")
def status():
    return jsonify({"status": "OK"})

"""Route to get user details by username"""
@app.route("/users/<username>")
def get_user(username):
    if username in users:
        user_data = users[username].copy()
        user_data["username"] = username
        return jsonify(user_data)
    else:
        return jsonify({"error": "User not found"}), 404

"""Route to add a new user via POST request"""
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    """Validate required fields"""
    required_fields = ["username", "name", "age", "city"]
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"error": f"{field} is required"}), 400

    username = data["username"]

    """Check for duplicate usernames"""
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = {
        "username": username,
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

"""Run the Flask application if this file is executed directly"""
if __name__ == "__main__":
    app.run(debug=True)
