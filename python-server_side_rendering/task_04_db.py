#!/usr/bin/python3
from flask import Flask, render_template, request
import json, csv, os, sqlite3

app = Flask(__name__)

# --- Fonctions lecture données ---

def read_json_data():
    with open('products.json') as f:
        return json.load(f)["products"]

def read_csv_data():
    with open("products.csv", newline='') as f:
        return list(csv.DictReader(f))

def setup_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT NOT NULL
        )
    ''')
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

# --- Routes statiques ---

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

# --- Route principale produits selon source ---

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
    else:
        return render_template("product_display.html", error="Wrong source")

    # Filtrage sur id si demandé
    if prod_id:
        filtered = [p for p in products if str(p["id"]) == prod_id]
        if not filtered:
            return render_template("product_display.html", error="Product not found")
        return render_template("product_display.html", products=filtered)

    return render_template("product_display.html", products=products)

# --- Lancement du serveur ---

if __name__ == '__main__':
    setup_database()  # Création base SQLite au lancement uniquement
    app.run(debug=True)
