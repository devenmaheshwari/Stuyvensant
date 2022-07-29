# FACts - Deven Maheshwari, Aaron Contreras, Oscar Wang, Owen Yaggy
# Softdev
# P04 - Le Fin
# 2022-06-10

import sqlite3
import csv
import pandas as pd
from csvhandler import *

DB_FILE = "app/tmp/Facts.db"

def setup():
    db  = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("DROP TABLE IF EXISTS users")
    command = "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, password TEXT, timestamp TEXT)"
    c.execute(command)

    c.execute("DROP TABLE IF EXISTS performance")
    command = "CREATE TABLE statistics (initiative_id INTEGER PRIMARY KEY, grade TEXT, dataset_specific TEXT, num_students TEXT)"
    c.execute(command)

    c.execute("DROP TABLE IF EXISTS research")
    command = "CREATE TABLE research (initiative_id INTEGER PRIMARY KEY, research_study_summary TEXT)"

    db.commit()
    db.close()

# Performance Table (Imported through terminal sqlite commands)
def getFields(fieldname):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    field = None
    command = "SELECT " + fieldname + " FROM Performance" 
    c.execute(command)
    row = c.fetchall()

    return row

def getData(fieldname):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    field = None
    command = "SELECT " + fieldname + " FROM Performance" 
    c.execute(command)
    row = c.fetchall()

    return row