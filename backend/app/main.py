import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect, jsonify, Blueprint
from flask_login import login_required, current_user

#app = Flask(__name__)
#app.secret_key = os.environ.get("SECRET_KEY", "dev")

main = Blueprint('main', __name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='todo_db',
                            user=os.environ.get('DB_USERNAME'),
                            password=os.environ.get('DB_PASSWORD'))
    return conn

FAKE_USER_ID = 1

@main.route('/')
def start():
    return redirect(url_for("auth.login"))

@main.route('/index')
@login_required
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM tasks WHERE user_id = {current_user.user_id};')
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', tasks = tasks, name=(current_user.username).capitalize())

@login_required
@main.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        notes = request.form.get('notes')
        due_date = request.form.get('due_date')

        if not title:
            return render_template('create.html')

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO tasks (user_id, title, notes, due_date)'
                    'VALUES (%s, %s, %s, %s)',
                    (current_user.user_id, title, notes, due_date))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('main.index'))
    
    return render_template('create.html')
