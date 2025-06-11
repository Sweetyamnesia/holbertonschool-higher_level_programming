#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request

"""Initialize the Flask application"""
app = Flask(__name__)

"""A simple in-memory data store with one predefined user"""
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

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
    """Check if the user exists in the dictionary"""
    if username in users:
        return jsonify(users[username])
    else:
        """Return an error if the user is not found"""
        return jsonify({"error": "User not found"}), 404


"""Route to add a new user via POST request"""


@app.route("/add_user", methods=["POST"])
def add_user():
    """Get the JSON data sent in the request body"""
    data = request.get_json()

    """Validate that the required field 'username' exists"""
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    """Add the new user to the users dictionary"""
    users[username] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    """Return a confirmation response"""
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


"""Run the Flask application if this file is executed directly"""
if __name__ == "__main__":
    app.run(debug=True)
