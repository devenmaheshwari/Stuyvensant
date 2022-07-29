# Sports! - Sean Ging and Deven Maheshwari
# SoftDev
# K16 - All About Databse/Skeleton stub/SQLITE3 BASICS
# Oct 21 2021 


import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) # open if file exists, otherwise create
c = db.cursor()               # facilitate db ops -- you will use cursor to trigger db events
#==========================================================

try:
    command = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER);"          # test SQL stmt in sqlite3 shell, save as string
    c.execute(command)    # run SQL statement

    # < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

    # Table: courses
    with open('courses.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            command = 'INSERT INTO courses VALUES (?, ?, ?);'
            params = (row['code'], row['mark'], row['id'])
            c.execute(command, params)   

    # Table: students

    command = "CREATE TABLE students(name TEXT, age INTEGER, id INTEGER);"          # test SQL stmt in sqlite3 shell, save as string
    c.execute(command)    # run SQL statement

    with open('students.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:        
            command = 'INSERT INTO students VALUES (?, ?, ?);'
            params = (row['name'], row['age'], row['id'])
            c.execute(command, params)
    
    print("Done Making Database")

except:
    print("Database already exists")



#==========================================================

db.commit() #save changes
db.close()  #close database


