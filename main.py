from flask import Flask, jsonify, request
from flask_cors import CORS  # Install with: pip install flask-cors
import json

app = Flask(__name__)
CORS(app)  # Allow all origins

@app.route("/hello")
def home():
    return jsonify({"user": "Jaine", "id": 1})

@app.route("/api/data")
def get_data():
    try:
        with open("data.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON"}), 500

    # return jsonify({"user": "Jaine", "id": 1})


@app.route("/api/data", methods=["POST"])
def add_data():
    try:
        # Get JSON data from request
        new_data = request.get_json()
        if not new_data:
            return jsonify({'error': 'No data provided'}), 400

        # Load existing data or initialize empty list
        try:
            with open("data.json", 'r') as f:
                existing_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = {"content":[]}

        arr = existing_data["content"]
        arr.append(new_data)
        # Append new data (or modify as needed)
        # if isinstance(existing_data, list):
        #     existing_data.append(new_data)
        # elif isinstance(existing_data, dict):
        #     existing_data.update(new_data)

        # Write back to file
        with open("data.json", 'w') as f:
            json.dump(existing_data, f, indent=4)

        return jsonify({
            'message': 'Ok'
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
if __name__ == "__main__":
    app.run(debug=True)