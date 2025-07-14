import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='todo_db',
                            user=os.environ.get('DB_USERNAME'),
                            password=os.environ.get('DB_PASSWORD'))
    return conn