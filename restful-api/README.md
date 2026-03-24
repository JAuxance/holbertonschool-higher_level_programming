# 📂 restful-api

This project introduces REST concepts through Python scripts and small Flask applications. It moves from consuming a public API to building custom HTTP endpoints and protecting routes with Basic Auth and JWT.

## Files

| File | Description |
|------|-------------|
| `task_02_requests.py` | Fetch posts from JSONPlaceholder and export them to CSV |
| `task_03_http_server.py` | Build a basic HTTP server with multiple endpoints |
| `task_04_flask.py` | Create a simple Flask API for in-memory user data |
| `task_05_basic_security.py` | Add Basic Auth and JWT-protected routes to the Flask API |

## Running a script

```bash
python3 <filename>.py
```

## Notes

- `task_02_requests.py` requires `requests`.
- `task_04_flask.py` requires `flask`.
- `task_05_basic_security.py` requires `flask`, `flask-httpauth`, and `flask-jwt-extended`.
