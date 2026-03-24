# 📂 SQL_more_queries

This project expands on MySQL fundamentals with users, privileges, constraints, joins, subqueries, and many-to-many relationships. It also includes a sample TV shows database used by the later query exercises.

## Files

| File | Description |
|------|-------------|
| `0-privileges.sql` | Show privileges for two MySQL users |
| `1-create_user.sql` | Create a full-access local user |
| `2-create_read_user.sql` | Create a read-only user on `hbtn_0d_2` |
| `3-force_name.sql` | Create a table with a required `name` column |
| `4-never_empty.sql` | Create a table with a default `id` value |
| `5-unique_id.sql` | Create a table with a unique `id` column |
| `6-states.sql` | Create the `hbtn_0d_usa` database and `states` table |
| `7-cities.sql` | Create the `cities` table with a foreign key to `states` |
| `8-cities_of_california_subquery.sql` | List cities from California with a subquery |
| `9-cities_by_state_join.sql` | List cities with their state names using a join |
| `10-genre_id_by_show.sql` | List shows and their genre IDs |
| `11-genre_id_all_shows.sql` | List all shows, even without genres |
| `12-no_genre.sql` | List shows with no linked genre |
| `13-count_shows_by_genre.sql` | Count shows by genre |
| `14-my_genres.sql` | List every genre linked to `Dexter` |
| `15-comedy_only.sql` | List all comedy shows |
| `16-shows_by_genre.sql` | List all shows with all linked genres |
| `hbtn_0d_tvshows.sql` | Sample TV shows database dump |

## Running a script

```bash
mysql -u <user> -p <database> < <file>.sql
```
