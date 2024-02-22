import streamlit as st
from datetime import datetime
from models import Task
from db_handler import init_db, add_task, get_tasks, update_task
from pydantic import ValidationError

# Initialize the database
init_db()

# Streamlit app layout
st.title('Todo App')

# Task input form
with st.form(key='task_form'):
    name = st.text_input('Task Name')
    description = st.text_area('Description')
    created_by = st.text_input('Created By')
    category = st.selectbox('Category', ['Personal', 'Work', 'Other'], index=0)
    submit_button = st.form_submit_button('Submit')

if submit_button:
    try:
        # Manual data validation using Pydantic
        task_data = Task(
            name=name,
            description=description,
            is_done=False,  # default value
            created_at=datetime.now(),  # set current time as creation time
            created_by=created_by,
            category=category
        )
        add_task(task_data)
        st.success('Task added successfully!')
    except ValidationError as e:
        st.error('Task creation failed: ' + str(e))

# Display tasks
st.header('Tasks')
tasks = get_tasks()
for task in tasks:
    col1, col2 = st.columns([0.8, 0.2])
    col1.write(f'{task.name} - {task.description}')
    if col2.button('Done', key=str(task.id)):  # Convert task.id to string to use as key
        update_task(task.id, True)

