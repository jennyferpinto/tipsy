"""
model.py
"""
import sqlite3
import datetime

def connect_db():
    return sqlite3.connect("tipsy.db")

def new_user(db, email, password, name):          
    c = db.cursor()                                     
    query = """INSERT INTO Users VALUES (NULL, ?, ?, ?)"""                                                           
    result = c.execute(query, (email, password, name))          
    db.commit()
    return result.lastrowid

def authenticate(db, email, password):
    c = db.cursor()
    query = """SELECT * from Users WHERE email=? AND password=?"""
    c.execute(query, (email, password))
    result = c.fetchone()
    if result:
        fields = ["id", "email", "password", "username"]
        return dict(zip(fields, result))

    return None

def get_user(db, user_id):
    """Gets a user dictionary out of the database given an id"""
    c = db.cursor()
    query = """SELECT * from Users WHERE id = ?"""
    c.execute(query, (user_id))
    result = c.fetchone()
    if result:
        fields = ["id", "email", "password", "username"]
        return dict(zip(fields,result))

def new_task(db, title, user_id):
    """Given a title and a user_id, create a new task belonging to that user. Return the id of the created task"""
    c = db.cursor()
    time_created = datetime.datetime.today()
    query = """INSERT INTO Tasks VALUES (NULL, ?, ?, NULL, ?)"""
    result = c.execute(query,(title, time_created, user_id))
    db.commit()
    return result.lastrowid


def complete_task(db, task_id):
    """Mark the task with the given task_id as being complete."""
    c = db.cursor()
    time_completed = datetime.datetime.now()
    query = """UPDATE Tasks SET completed_at=? WHERE id = ?"""
    result = c.execute(query,(time_completed, task_id))
    db.commit()


def get_tasks(db, user_id):
    """Get all the tasks matching the user_id, getting all the tasks in the system if the user_id is not provided. Returns the results as a list of dictionaries."""
    c = db.cursor()
    tasks = []
    if user_id == None:
        query = """SELECT * FROM Tasks"""
        c.execute(query,())
    else:
        query = """SELECT * FROM Tasks WHERE user_id = ?"""
        c.execute(query, (user_id))
    
    result = c.fetchall()  
    
    #if result:
        #for row in result:
            #new_dict = {}
            #new_dict ['id'] = row[0]
            #new_dict ['title'] = row[1]
            #new_dict ['created_at'] = row[2]
            #new_dict ['completed_at'] = row[3]
            #new_dict ['user_id'] = row[4]
            #tasks.append(new_dict)
        #return tasks
    #else:
        #print "No tasks exist"
    
    if result:
        fields = ['id','title','created_at', 'completed_at', 'user_id']
        tasks = []
        for rows in result:
            task = dict(zip(fields, rows)) # makes each row in the results a dictionary
            tasks.append(task) # appends the new dict to the empty list tasks
        return tasks
    else:
        print "No tasks exist"
        

def get_task(db, task_id):
    """Gets a single task, given its id. Returns a dictionary of the task data."""
    c = db.cursor()
    query = """SELECT * FROM Tasks WHERE id = ?"""
    c.execute(query,(task_id))
    result = c.fetchone()
    if result:
        fields = ["id", "title", "created_at", "completed_at", "user_id"]
        return dict(zip(fields, result))
