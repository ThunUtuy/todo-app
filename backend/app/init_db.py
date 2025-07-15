import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

conn = psycopg2.connect(
        host="localhost",
        database="todo_db",
        user=os.environ.get('DB_USERNAME'),
        password=os.environ.get('DB_PASSWORD'))

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('CREATE TABLE users (user_id serial PRIMARY KEY,'
                                 'first_name varchar (50) NOT NULL,'
                                 'last_name varchar (50) NOT NULL,'
                                 'password varchar (128) NOT NULL,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

cur.execute('DROP TABLE IF EXISTS tasks;')
cur.execute('CREATE TABLE tasks (task_id serial PRIMARY KEY,'
                                 'user_id integer NOT NULL,'
                                 'title varchar (50) NOT NULL,'
                                 'notes text,'
                                 'due_date date,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP,'
                                 'CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES users(user_id));'
                                 )

conn.commit()

cur.close()
conn.close()
