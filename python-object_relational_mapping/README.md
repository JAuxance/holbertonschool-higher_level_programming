# python-object_relational_mapping

Python and MySQL exercises about database access with both raw SQL and SQLAlchemy ORM.

## Files

| File | Description |
|------|-------------|
| `0-select_states.sql` | SQL script to create the `states` table |
| `0-select_states.py` | List all states from the database |
| `1-filter_states.py` | List states starting with `N` |
| `2-my_filter_states.py` | Search states by name from command-line input |
| `3-my_safe_filter_states.py` | Safe state search using parameterized queries |
| `4-cities_by_state.sql` | SQL script to create the `cities` table |
| `4-cities_by_state.py` | List all cities with their state names |
| `5-filter_cities.py` | List cities that belong to a given state |
| `6-model_state.py` | Create the `states` table through SQLAlchemy metadata |
| `6-model_state.sql` | SQL reference file for ORM setup |
| `7-model_state_fetch_all.py` | List all `State` objects using SQLAlchemy |
| `model_state.py` | SQLAlchemy `Base` and `State` model definition |

## Requirements

- Python 3
- MySQL server
- `mysqlclient`
- `SQLAlchemy`

## Run

```bash
python3 0-select_states.py <mysql_user> <mysql_password> <database_name>
python3 7-model_state_fetch_all.py <mysql_user> <mysql_password> <database_name>
```

## Topics

- MySQLdb queries
- SQL injection prevention
- joins and filters
- SQLAlchemy models and sessions
