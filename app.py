import streamlit as st
import sqlite3
import datetime
from pydantic import BaseModel

# Database setup
conn = sqlite3.connect('todos.db', check_same_thread=False)
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT,
        is_done BOOLEAN,
        created_at TEXT,
        created_by TEXT,
        category TEXT
    )
''')
conn.commit()

# Pydantic model for the task
class Task(BaseModel):
    name: str
    description: str
    created_by: str
    category: str

# Streamlit app layout
st.title("Todo App")

# Task form
with st.form("task_form", clear_on_submit=True):
    st.subheader("Create a new task")
    name = st.text_input("Task name")
    description = st.text_area("Task description")
    created_by = st.text_input("Created by")
    category = st.selectbox("Category", options=["Personal", "Work", "School"])
    submitted = st.form_submit_button("Submit")

    if submitted:
        c.execute('''
            INSERT INTO tasks (name, description, is_done, created_at, created_by, category)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, description, False, datetime.datetime.now(), created_by, category))
        conn.commit()
        st.success("Task added successfully!")

# Display tasks
st.subheader("Your Tasks")
tasks = c.execute('SELECT id, name, description, is_done FROM tasks').fetchall()
for task in tasks:
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        st.markdown(f"**{task[1]}**")
        st.caption(task[2])
    with col2:
        if st.checkbox("Done", task[3], key=task[0]):
            c.execute('UPDATE tasks SET is_done = ? WHERE id = ?', (True, task[0]))
            conn.commit()
