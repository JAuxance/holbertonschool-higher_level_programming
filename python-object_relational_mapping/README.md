# 📂 python-object_relational_mapping

This project bridges SQL and Python by querying MySQL from scripts and then introducing SQLAlchemy models. It covers raw SQL execution with `MySQLdb`, safe parameter binding, joins, and ORM-based table mapping.

## Files

| File | Description |
|------|-------------|
| `0-select_states.sql` | List all states ordered by `id` |
| `0-select_states.py` | Query and print all states from MySQL |
| `1-filter_states.py` | Print states whose names start with `N` |
| `2-my_filter_states.py` | Filter states from raw string formatting input |
| `3-my_safe_filter_states.py` | Filter states safely with parameterized queries |
| `4-cities_by_state.sql` | Join cities and states in SQL |
| `4-cities_by_state.py` | Print cities with their state names |
| `5-filter_cities.py` | Print all cities for a given state |
| `6-model_state.sql` | Create the `states` table for the ORM tasks |
| `6-model_state.py` | Create mapped tables with SQLAlchemy |
| `7-model_state_fetch_all.py` | Query all `State` objects with SQLAlchemy |
| `model_state.py` | Define the SQLAlchemy `State` model |

## Running a script

```bash
python3 <script>.py <mysql_user> <mysql_password> <database>
```
