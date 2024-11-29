from flask import Flask, request, jsonify
import requests
from db_con import LocalConnectionPool
import logging
app = Flask(__name__)
AUTH_SERVICE_URL = "http://auth-service:4000/auth"

@app.route("/")
def hello():
    return """(/books", methods=["POST"]), (/books", methods=["GET"])"""


@app.route("/books", methods=["GET"])
def get_books():
    """Fetch all books."""
    con = LocalConnectionPool()
    books = con.read_query("SELECT * FROM books;")
    return jsonify(books), 200

#example: curl -X POST -H "Content-Type: application/json" -d '{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}' http://127.0.0.1:5000/books
@app.route("/books", methods=["POST"])
def add_book():
    """Add a new book."""
    data = request.json
    if not data.get("title") or not data.get("author"):
        return {"error": "Title and author are required"}, 400
    auth_payload = {"password": data.get("password")}
    auth_response = requests.post(AUTH_SERVICE_URL, json=auth_payload)

    # Check auth response
    if auth_response.status_code != 201:  # Auth failed
        return {"error": f"Unauthorized, code. {auth_response.status_code}"}, 401
    
    #call add_book auth route with http post from the request.json here
    con = LocalConnectionPool()
    con.execute_query(f"insert into books (title, author) values ('{data['title']}', '{data['author']}');")
    return data, 201

@app.route("/reset", methods=["POST"])
def delete_books():
    """Add a new book."""
    data = request.json
    auth_payload = {"password": data.get("password")}
    auth_response = requests.post(AUTH_SERVICE_URL, json=auth_payload)

    if auth_response.status_code != 201:  # Auth failed
        return {"error": f"Unauthorized, code. {auth_response.status_code}"}, 401
    
    con = LocalConnectionPool()
    con.execute_query("delete from books;")
    return data, 201

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True, host='0.0.0.0', port=5000)
