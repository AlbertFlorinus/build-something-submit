from flask import Flask, request, jsonify
import logging
app = Flask(__name__)

@app.route("/auth", methods=["POST"])
def add_book():
    """Add a new book."""
    data = request.json
    if not data.get("password"):
        return {"error": "password required"}, 400
    if data.get("password") == "byggarebob":
        #inte säkert jag vet
        return data, 201
    return data, 401

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True, host='0.0.0.0', port=4000)