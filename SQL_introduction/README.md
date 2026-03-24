# 📂 SQL_introduction

This project introduces MySQL basics through standalone SQL scripts. It covers database creation, table definition, record insertion, filtering, aggregation, and ordered result sets.

## Files

| File | Description |
|------|-------------|
| `0-list_databases.sql` | List all databases |
| `1-create_database_if_missing.sql` | Create `hbtn_0c_0` if needed |
| `2-remove_database.sql` | Drop `hbtn_0c_0` if it exists |
| `3-list_tables.sql` | List all tables in the current database |
| `4-first_table.sql` | Create `first_table` |
| `5-full_table.sql` | Show the full structure of `first_table` |
| `6-list_values.sql` | Display every row from `first_table` |
| `7-insert_value.sql` | Insert one row into `first_table` |
| `8-count_89.sql` | Count rows where `id = 89` |
| `9-full_creation.sql` | Create and populate `second_table` |
| `10-top_score.sql` | List rows ordered by descending score |
| `11-best_score.sql` | Show rows with `score >= 10` |
| `12-no_cheating.sql` | Update Bob's score |
| `13-change_class.sql` | Delete rows where `score <= 5` |
| `14-average.sql` | Compute the average score |
| `15-groups.sql` | Count rows grouped by score |
| `16-no_link.sql` | Show rows with a non-null name |

## Running a script

```bash
mysql -u <user> -p <database> < <file>.sql
```
