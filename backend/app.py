import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='todo_db',
                            user=os.environ.get('DB_USERNAME'),
                            password=os.environ.get('DB_PASSWORD'))
    return conn

FAKE_USER_ID = 1

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM tasks WHERE user_id = {FAKE_USER_ID};')
    colnames = [desc[0] for desc in cur.description]
    # Result: ['task_id', 'user_id', 'title', 'notes', 'due_date', 'date_added']
    tasks = [dict(zip(colnames, row)) for row in cur.fetchall()]
    cur.close()
    conn.close()
    
    return jsonify(tasks)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        notes = request.form.get('notes')
        due_date = request.form.get('due_date')

        if not title:
            return jsonify({"error": "Title is required"}), 400

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO tasks (user_id, title, notes, due_date)'
                    'VALUES (%s, %s, %s, %s)',
                    (FAKE_USER_ID, title, notes, due_date))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    
    return jsonify({"message": "Send a POST request to create a task."}), 200
