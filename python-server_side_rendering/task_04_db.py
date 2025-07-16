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

import sqlite3

def setup_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Création de la table avec la structure demandée
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT NOT NULL
        )
    ''')

    # Insertion des données exemples, évite doublons grâce à OR IGNORE
    cursor.execute('''
        INSERT OR IGNORE INTO Products (id, name, price, category)
        VALUES
        (1, 'Laptop', 799.99, 'Electronics'),
        (2, 'Coffee Mug', 15.99, 'Home Goods')
    ''')

    conn.commit()
    conn.close()

def read_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()

    conn.close()

    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "category": row[3]
        })

    return products

# On lance la création / insertion
setup_database()

# Puis on récupère et affiche les données
products = read_products()
print(products)


@app.route('/source')
def products():
    source = request.args.get('source')
    prod_id = request.args.get('id')

    if source == "json":
        products = read_json_data()
    elif source == "csv":
        products = read_csv_data()
    elif source == "sql":
        products = read_products()
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
