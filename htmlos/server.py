from flask import Flask, request, jsonify, send_from_directory
import json
import os

app = Flask(__name__, static_folder='')

JSON_PATH = "data/runningtasks.json"

@app.route('/')
def index():
    return send_from_directory('.', 'desktop.html')

@app.route('/data/runningtasks.json', methods=['GET', 'POST'])
def running_tasks():
    if request.method == 'GET':
        if os.path.exists(JSON_PATH):
            try:
                with open(JSON_PATH, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except json.JSONDecodeError:
                data = []
            return jsonify(data)
        else:
            return jsonify([])
    elif request.method == 'POST':
        data = request.get_json()
        with open(JSON_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return jsonify({"status": "success"})

@app.route('/apps/<path:filename>')
def serve_apps(filename):
    return send_from_directory('apps', filename)

@app.route('/data/<path:filename>')
def serve_data(filename):
    return send_from_directory('data', filename)

if __name__ == '__main__':
    app.run(debug=True)
