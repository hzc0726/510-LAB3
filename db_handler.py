# db_handler.py

import sqlite3
from models import Task

def init_db():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            is_done BOOLEAN,
            created_at TIMESTAMP,
            created_by TEXT,
            category TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_task(task_data: Task):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('INSERT INTO tasks (name, description, is_done, created_at, created_by, category) VALUES (?, ?, ?, ?, ?, ?)', 
              (task_data.name, task_data.description, task_data.is_done, task_data.created_at, task_data.created_by, task_data.category))
    conn.commit()
    conn.close()

def get_tasks():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    tasks = c.fetchall()
    conn.close()
    return [Task(id=row[0], name=row[1], description=row[2], is_done=row[3], created_at=row[4], created_by=row[5], category=row[6]) for row in tasks]

def update_task(task_id, is_done):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('UPDATE tasks SET is_done = ? WHERE id = ?', (is_done, task_id))
    conn.commit()
    conn.close()
