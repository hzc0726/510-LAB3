# 510-LAB3
Overview
The Streamlit Todo App is a streamlined task management application designed to help users organize and track their daily activities. Built with Python and Streamlit, and integrated with a SQLite database, this app provides a user-friendly platform for managing a wide range of tasks. It's perfect for personal use, work organization, or academic planning.

Features
Add Tasks: Users can effortlessly add new tasks, specifying details like the task name, description, and category.
View Tasks: All tasks are listed in an easily navigable format.
Update Task Status: Users can mark tasks as completed with a simple click.
Persistent Storage: Utilizing SQLite, tasks are stored persistently, ensuring no loss of data between sessions.
Intuitive UI: A clean, responsive user interface ensures a smooth user experience.
How to Run
Follow these steps to run the application locally:

Clone the Repository

sh
Copy code
git clone https://github.com/user/StreamlitTodoApp.git
cd StreamlitTodoApp
Environment Setup

Create and activate a virtual environment:
Windows:
sh
Copy code
python -m venv venv
venv\Scripts\activate
MacOS/Linux:
sh
Copy code
python3 -m venv venv
source venv/bin/activate
Install dependencies:
sh
Copy code
pip install -r requirements.txt
Start the App

sh
Copy code
streamlit run app.py
Access the App

The app will be running at http://localhost:8501.
Deployment
The app is deployed on Azure App Services and is accessible at http://streamlittodoapp.azurewebsites.net.

Lessons Learned
This project was an excellent opportunity to deepen my understanding of Streamlit and SQLite. I faced challenges in data persistence and state management, which were overcome by effectively utilizing SQLite. The project also enhanced my skills in building intuitive UIs with Streamlit and deploying Python apps to Azure.

Questions/Future Improvements
Exploring more advanced features in Streamlit for a richer UI experience.
Adding user authentication for personalized task management.
Implementing task prioritization and deadline reminders.
