"""
tipsy.py -- A flask-based to-do list!
"""

from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html", first_name = "Jen")

@app.route("/tasks")
def list_tasks():
  db = model.connect_db()
  # use the get_tasks function because you want to pass it NO user_id
  # and get it to return you the list of dictionaries, which are formatted by html template
  tasks_from_db = model.get_tasks(db, None)
  return render_template("list_tasks.html", tasks = tasks_from_db)

# renders the html from the template and stores the data inputted into form
@app.route("/new_task")
def new_tasks():
  return render_template("new_task.html")

# Takes the info saved in a dictionary (from the form) and assigns it to variables
# that are then passed into the model.new_task() function from model.py
# Connects to db and uses the new_task function to input the form info to a new task
# Returns a redirect to the list of tasks page (/tasks url)
@app.route("/save_task", methods=["POST"])
def save_task():
  task_title = request.form['task_title']
  user_id = request.form['user_id']
  db = model.connect_db()
  task_id = model.new_task(db, task_title, user_id)
  return redirect("/tasks")

if __name__ == "__main__":
  app.run(debug=True)
