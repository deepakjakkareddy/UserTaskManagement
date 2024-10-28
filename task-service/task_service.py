from flask import Flask, request, jsonify
app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    updated_task = request.json
    tasks[task_id] = updated_task
    return jsonify(updated_task), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks.pop(task_id)
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
