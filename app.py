from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def search():
    search_string = request.json.get('searchString', '')
    
    file_path = 'file.txt'

    result = []
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if search_string in line:
                result.append({
                    'line_number': line_number,
                    'line_content': line.strip()
                })
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
