"""Flask application for displaying products from JSON, CSV, or SQLite."""

import csv
import json
from pathlib import Path
import sqlite3

from flask import Flask, redirect, render_template_string, request, url_for

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / 'products.db'

app = Flask(__name__)


@app.route('/')
def home():
    """Redirect the home page to the products listing."""
    return redirect(url_for('products'))


def read_products_from_json():
    """Read and parse product data from the JSON file."""
    json_file = BASE_DIR / 'products.json'
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        return data.get('products', [])
    return []


def read_products_from_csv():
    """Read and parse product data from the CSV file."""
    csv_file = BASE_DIR / 'products.csv'
    with open(csv_file, 'r', encoding='utf-8', newline='') as file:
        rows = csv.DictReader(line.lstrip() for line in file)
        return [
            {
                'name': row.get('name', '').strip(),
                'category': row.get('category', '').strip(),
                'price': row.get('price', '').strip(),
            }
            for row in rows
        ]


def read_products_from_sql():
    """Read and parse product data from the SQLite database."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            'SELECT name, category, price FROM Products'
        ).fetchall()
    return [dict(row) for row in rows]


@app.route('/products')
def products():
    """Display products loaded from JSON, CSV, or SQLite."""
    source = request.args.get('source', 'json')
    error = None

    try:
        if source == 'json':
            products_list = read_products_from_json()
        elif source == 'csv':
            products_list = read_products_from_csv()
        elif source == 'sql':
            products_list = read_products_from_sql()
        else:
            products_list = []
            error = 'Wrong source'
    except sqlite3.Error:
        products_list = []
        error = 'Database error'

    template_path = BASE_DIR / 'product_display.html'
    with open(template_path, 'r', encoding='utf-8') as file:
        template = file.read()

    return render_template_string(
        template,
        products=products_list,
        error=error,
        selected_source=source
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
