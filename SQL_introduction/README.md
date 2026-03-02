# 📂 SQL_introduction

SQL exercises introducing MySQL basics: listing databases, creating tables, querying and manipulating data.

## Files

| File | Description |
|------|-------------|
| `0-list_databases.sql` | List all databases on the server using `INFORMATION_SCHEMA.SCHEMATA` |

## Python example

Run the Python helper to list databases using SQLAlchemy:

```bash
# SQLite (default, no setup required)
.venv/bin/python example_list_databases.py

# MySQL (replace credentials as needed)
export DATABASE_URL="mysql+pymysql://user:pass@localhost:3306/"
.venv/bin/python example_list_databases.py
```

> Requires the virtual environment set up at the root of the repo.
> Install dependencies: `pip install -r ../requirements.txt`

## Running .sql files directly

```bash
mysql -u root -p < 0-list_databases.sql
```
