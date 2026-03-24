# SQL_more_queries

Exercises about advanced MySQL queries, permissions, constraints, joins, and subqueries.

## Files

| File | Description |
|------|-------------|
| `0-privileges.sql` | Show privileges for MySQL users |
| `1-create_user.sql` | Create the `user_0d_1` user |
| `2-create_read_user.sql` | Create a read-only user on `hbtn_0d_2` |
| `3-force_name.sql` | Create a table with a non-null `name` column |
| `4-never_empty.sql` | Create a table with a default value |
| `5-unique_id.sql` | Create a table with a unique `id` |
| `6-states.sql` | Create the `states` table |
| `7-cities.sql` | Create the `cities` table with a foreign key |
| `8-cities_of_california_subquery.sql` | List California cities using a subquery |
| `9-cities_by_state_join.sql` | List cities with their state using a join |
| `10-genre_id_by_show.sql` | List shows with at least one genre |
| `11-genre_id_all_shows.sql` | List all shows and linked genres |
| `12-no_genre.sql` | List shows without a genre |
| `13-count_shows_by_genre.sql` | Count shows by genre |
| `14-my_genres.sql` | List genres linked to the show `Dexter` |
| `15-comedy_only.sql` | List comedy shows only |
| `16-shows_by_genre.sql` | List all shows and their genres |
| `hbtn_0d_tvshows.sql` | Sample database dump for TV shows exercises |

## Run

```bash
mysql -u root -p < 0-privileges.sql
mysql -u root -p hbtn_0d_usa < 9-cities_by_state_join.sql
```

## Topics

- user privileges
- table constraints
- foreign keys
- joins and subqueries
- aggregation with `COUNT`
