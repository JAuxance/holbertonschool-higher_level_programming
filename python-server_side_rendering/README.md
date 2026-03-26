# python-server_side_rendering Exercises

Practice project for rendering server-generated pages with Python and Flask.

## Files

| File | Description |
|------|-------------|
| `task_00_intro.py` | Generate invitation files from a text template and attendee data |
| `task_01_jinja.py` | Basic Flask app rendering static Jinja templates |
| `task_02_logic.py` | Flask app rendering a dynamic items page from JSON |
| `task_03_files.py` | Display products loaded from JSON or CSV |
| `task_04_db.py` | Display products loaded from JSON, CSV, or SQLite |
| `template.txt` | Invitation template used by `task_00_intro.py` |
| `products.json` | Product data source in JSON |
| `products.csv` | Product data source in CSV |
| `products.db` | SQLite database used for product rendering |
| `product_display.html` | HTML template used to show products |

## Run

```bash
python3 task_00_intro.py
python3 task_01_jinja.py
python3 task_04_db.py
```

Then open `http://127.0.0.1:5000/` or `http://127.0.0.1:5000/products?source=sql`.

## Topics

- string templating
- Flask routes
- Jinja templates
- JSON, CSV, and SQLite data sources
