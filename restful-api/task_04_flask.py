from flask import Flask, jsonify, request

app = Flask(__name__)

user_data = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_all_user():
    names = [user["username"] for user in user_data.values()]
    return jsonify(names)


@app.route("/status", methods=["GET"])
def status():
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user_info = user_data.get(username)
    if user_info:
        return jsonify(user_info)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    new_user = request.get_json()
    if not new_user:
        return jsonify(error="Invalid JSON"), 400
    if "username" not in new_user:
        return jsonify(error="Username is required"), 404
    if new_user["username"] in user_data:
        return jsonify(error="Username already exists"), 409
    username = new_user["username"]
    user_data[username] = {
        "username": username,
        "name": new_user.get("name", ""),
        "age": new_user.get("age", ""),
        "city": new_user.get("city", "")
    }
    return jsonify(message="User added", user=user_data[username]), 201


if __name__ == "__main__":
    app.run()
