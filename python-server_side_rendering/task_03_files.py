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
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get("items", [])
    except Exception as e:
        print(f"{e}")
        items_list = []
    return render_template('items.html', items=items_list)


def read_json_data():
    try:
        with open('products.json') as f:
            return json.load(f)["products"]
    except FileNotFoundError:
        return {"error": "Fichier products.json introuvable."}

def read_csv_data():
    try:
        with open("products.csv", newline='') as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return {"error": "Fichier products.csv introuvable."}


@app.route('/source')
def products():
    source = request.args.get('source')
    prod_id = request.args.get('id')

    if source == "json":
        products = read_json_data()
    elif source == "csv":
        products = read_csv_data()
    else:
        return render_template("product_display.html", error="Wrong source")

    # Si id est fourni, on filtre
    if prod_id:
        filtered = [p for p in products if str(p["id"]) == prod_id]
        if not filtered:
            return render_template("product_display.html", error="Product not found")
        return render_template("product_display.html", products=filtered)

    return render_template("product_display.html", products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)