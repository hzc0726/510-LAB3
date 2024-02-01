# app.py

import streamlit as st
from models import Task
from db_handler import init_db, add_task, get_tasks, update_task
from streamlit_pydantic import pydantic_form

# Initialize the database
init_db()

# Streamlit app layout
st.title('Todo App')

# Pydantic form for task input
with pydantic_form(key='task_form', model=Task):
    task_data = st.form_submit_button("Submit")

if task_data:
    add_task(task_data)
    st.success('Task added successfully!')

# Display tasks
st.header('Tasks')
tasks = get_tasks()
for task in tasks:
    col1, col2 = st.columns([0.8, 0.2])
    col1.write(f'{task.name} - {task.description}')
    if col2.button('Done', key=task.id):
        update_task(task.id, True)
