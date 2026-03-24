# 📂 SQL_introduction

SQL exercises introducing MySQL basics: listing databases, creating tables, querying and manipulating data.

## Files

| File | Description |
|------|-------------|
| `0-list_databases.sql` | List all databases on the server |
| `1-create_database_if_missing.sql` | Create database `hbtn_0c_0` if it does not exist |
| `2-remove_database.sql` | Drop database `hbtn_0c_0` if it exists |
| `3-list_tables.sql` | List all tables in the current database |
| `4-first_table.sql` | Create table `first_table` if it does not exist |
| `5-full_table.sql` | Show the full definition of `first_table` |
| `6-list_values.sql` | List all rows in `first_table` |
| `7-insert_value.sql` | Insert a row `(89, 'Best School')` into `first_table` |
| `8-count_89.sql` | Count rows with `id = 89` in `first_table` |
| `9-full_creation.sql` | Create `second_table` and insert multiple records |
| `10-top_score.sql` | List all records ordered by score descending |
| `11-best_score.sql` | List records with `score >= 10` ordered by score descending |
| `12-no_cheating.sql` | Update Bob's score to 10 in `second_table` |
| `13-change_class.sql` | Delete all records with `score <= 5` from `second_table` |
| `14-average.sql` | Compute the average score in `second_table` |
| `15-groups.sql` | Count records grouped by score, ordered by count descending |
| `16-no_link.sql` | List records with a non-null name, ordered by score descending |

## Running .sql files

```bash
mysql -u root -p hbtn_0c_0 < 0-list_databases.sql
```
