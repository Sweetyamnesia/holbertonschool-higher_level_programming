#!/usr/bin/python3
from flask import Flask, render_template, request
import json, csv, os, sqlite3

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
    return render_template('items.html', items=data["items"])

def read_json_data():
    with open('products.json') as f:
        return json.load(f)["products"]

def read_csv_data():
    with open("products.csv", newline='') as f:
        return list(csv.DictReader(f))

def read_sql_data():
    try:
        connexion = sqlite3.connect('products.db')
        cursor = connexion.cursor()
        
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        
        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })

        connexion.close()
        return products
    except Exception as e:
        return None

@app.route('/source')
def products():
    source = request.args.get('source')
    prod_id = request.args.get('id')

    if source == "json":
        products = read_json_data()
    elif source == "csv":
        products = read_csv_data()
    elif source == "sql":
        products = read_sql_data()
        if products is None:
            return render_template("product_display.html", error="Database error")
    else:
        return render_template("product_display.html", error="Wrong source")

    # Si id est fourni, on filtre
    if prod_id:
        filtered = [p for p in products if str(p["id"]) == prod_id]
        if not filtered:
            return render_template("product_display.html", error="Product not found")
        return render_template("product_display.html", products=filtered)

    return render_template("product_display.html", products=products)
