from flask import Flask, request, jsonify
import psycopg2

# Flask app initialization
app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = psycopg2.connect(
        host="postgres-service",  # Update with your Postgres service hostname
        database="tasks_db",
        user="admin",
        password="password"
    )
    return conn

# Ensure the tasks table exists
def create_tasks_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        description TEXT
    );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table 'tasks' ensured in database.")

@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description) VALUES (%s, %s) RETURNING id;",
        (task['title'], task['description'])
    )
    task_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    task['id'] = task_id
    return jsonify(task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description FROM tasks;")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    task_list = [{'id': t[0], 'title': t[1], 'description': t[2]} for t in tasks]
    return jsonify(task_list), 200

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    updated_task = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET title = %s, description = %s WHERE id = %s;",
        (updated_task['title'], updated_task['description'], task_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_task), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s;", (task_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return '', 204

if __name__ == '__main__':
    create_tasks_table()  # Ensure table exists
    app.run(host='0.0.0.0', port=5001)
