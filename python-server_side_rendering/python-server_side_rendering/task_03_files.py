"""Flask application for displaying products loaded from files."""

import csv
import json
from pathlib import Path

from flask import Flask, redirect, render_template_string, request, url_for

BASE_DIR = Path(__file__).resolve().parent

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


@app.route('/products')
def products():
    """Display products loaded from either a JSON or CSV source."""
    source = request.args.get('source', 'json')

    if source == 'json':
        products_list = read_products_from_json()
    elif source == 'csv':
        products_list = read_products_from_csv()
    else:
        products_list = []

    template_path = BASE_DIR / 'product_display.html'
    with open(template_path, 'r', encoding='utf-8') as file:
        template = file.read()

    return render_template_string(template, products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
