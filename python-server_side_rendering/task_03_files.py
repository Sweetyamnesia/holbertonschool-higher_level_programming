#!/usr/bin/python3
from flask import Flask, render_template, request
import json, csv, os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    json_path = os.path.join(os.path.dirname(__file__), 'items.json')
    with open(json_path, 'r') as file:
        data = json.load(file)
    return render_template('items.html', items=items)

@app.route('/flask')
def source():
    source = request.args.get('source')
    id = request.args.get('id')
    with open("data.csv", "w", newline="") as fichier_csv:
        data
    with open("data.json", "r") as fichier:
    	data = json.load(fichier)


if __name__ == '__main__':
    app.run(debug=True, port=5000)