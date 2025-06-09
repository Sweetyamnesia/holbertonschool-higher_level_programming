#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    data = {"username": "john", "name": "John", "age": 30, "city": "New York"}
    return jsonify(data)


@app.route("/status")
def status():
    return jsonify("OK")


@app.route("/users/<username>")
def get_user(username):
    return jsonify(username)


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data["username"]
    users[username] = data
    return jsonify(data)


if __name__ == "__main__":
    app.run()
