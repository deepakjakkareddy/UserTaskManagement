from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Database configuration
DB_HOST = "postgres-service"
DB_NAME = "tasks_db"  # Replace with actual DB name if different
DB_USER = "admin"
DB_PASSWORD = "password"

# Establish a database connection
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

# Ensure the 'users' table exists
def create_users_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table 'users' ensured in database.")

@app.route('/users', methods=['POST'])
def create_user():
    user = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, email, password) VALUES (%s, %s, %s) RETURNING id",
        (user['username'], user['email'], user['password'])  # Match these keys with the payload
    )
    user_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    user['id'] = user_id
    return jsonify(user), 201

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    updated_user = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET name = %s, email = %s WHERE id = %s",
        (updated_user['name'], updated_user['email'], user_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_user), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return '', 204

if __name__ == '__main__':
    create_users_table()  # Ensure table exists at startup
    app.run(host='0.0.0.0', port=5002)
