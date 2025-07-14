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

fake_user_id = 1

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM tasks WHERE user_id = {fake_user_id};')
    colnames = [desc[0] for desc in cur.description]
    # Result: ['task_id', 'user_id', 'title', 'notes', 'due_date', 'date_added']
    tasks = [dict(zip(colnames, row)) for row in cur.fetchall()]
    cur.close()
    conn.close()
    
    return jsonify(tasks)
