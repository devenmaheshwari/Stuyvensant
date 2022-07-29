# FACts - Deven Maheshwari, Aaron Contreras, Oscar Wang, Owen Yaggy
# Softdev
# P04 - Le Fin
# 2022-06-10

from flask import Flask, render_template, request, redirect, url_for
from regex import P
from app import db, csvhandler
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import sys
sys.path.append("/var/www/FlaskApp/FlaskApp")

DB_FILE = "app/tmp/Facts.db"

# boilerplate code
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/about', methods=["GET"])
def about():
    return render_template('about.html')

@app.route('/performance', methods=["GET"])
def performance():
    pdata = [["BN", "SCHOOL NAME", "PROGRESS REPORT TYPE", "2012-2013 PROGRESS REPORT GRADE", "2011-2012 PROGRESS REPORT GRADE", "2010-11 PROGRESS REPORT GRADE", "2009-10 PROGRESS REPORT GRADE", "2008-09 PROGRESS REPORT GRADE", "2007-08 PROGRESS REPORT GRADE", "2006-07 PROGRESS REPORT GRADE"]]
    BN_test = db.getFields("BN")
    SN_test = db.getFields("[SCHOOL NAME]")
    PRT_test = db.getFields("[PROGRESS REPORT TYPE]")
    one_test = db.getFields('''[2012-2013 PROGRESS
REPORT GRADE]''')
    two_test = db.getFields("[2011-2012 PROGRESS REPORT GRADE]")
    three_test = db.getFields("[2010-11 PROGRESS REPORT GRADE]")
    four_test = db.getFields("[2009-10 PROGRESS REPORT GRADE]")
    five_test = db.getFields("[2008-09 PROGRESS REPORT GRADE]")
    six_test = db.getFields("[2008-09 PROGRESS REPORT GRADE]")
    seven_test = db.getFields("[2007-08 PROGRESS REPORT GRADE]")
    eight_test = db.getFields("[2006-07 PROGRESS REPORT GRADE]")

    for i in range(len(BN_test)):
        pdata.append([BN_test[i], SN_test[i], PRT_test[i], one_test[i], two_test[i], three_test[i], four_test[i], five_test[i], six_test[i], seven_test[i], eight_test[i]])

    return render_template('performance.html', pdata=pdata)

@app.route('/study', methods=["GET", "POST"])
def study():
    if request.method == "GET":
        return render_template('study.html')
    if request.method == "POST":
        fileholder = request.form.get("fileUpload", default="")
        pathname = "app/data/" + fileholder
        options = csvhandler.get_headers(pathname)
        performance = csvhandler.get_headers("app/data/Student_Performance.csv")

        return render_template('results.html', options=options, performance=performance, pathname = pathname)

@app.route('/final', methods=["GET", "POST"])
def final():
    first = request.form.get("one", default="")
    second = request.form.get("two", default="")
    pathname = request.form.get("csv", default="")

    df = csvhandler.get_fields(pathname, first)
    helper = pd.factorize(np.ravel(df))

    for item in helper:
        item = item[0]

    df2 = csvhandler.get_fields("app/data/Student_Performance.csv", second)
    helper2 = pd.factorize(np.ravel(df2))

    try:
        c = print(df.apply(lambda x: x.factorize()[0]).corr(df2.apply(lambda x: x.factorize()[0])))
    except:
        c = "Correlation not availble with chosen dataset"

    return render_template('final.html', first=first, second=second, pathname=pathname, d1=df, d2=df2, c=c)

def holymoly():
    helper = np.ndarray.flatten(helper)
    helper2 = np.ndarray.flatten(helper2)
    print(np.correlate(helper, helper2))

    for row in helper2:
        row = row[0]

    

    if len(helper) > len(helper2):
        helper = np.reshape(helper, (len(helper2), 1))
    else:
        helper2 = np.reshape(helper2, (len(helper), 1))

   
    

    #for row in helper2:
        # if row == "A":
        #     row = 100
        # elif row == "B":
        #     row = 90
        # elif row == "C":
        #     row = 80
        # elif row == "D":
        #     row = 70
        # elif row == "F":
        #     row = 60
        # else:
        #     row = 0
        #print(row)

    print(np.corrcoef(helper, helper2))

    #print(df.apply(lambda x: x.factorize()[0]).corr(df2.apply(lambda x: x.factorize()[0])))


    #print(df2)
    # for row in df.iterrows():
    #     if row == "A":
    #         row = 100
    #     elif row == "B":
    #         row = 90
    #     elif row == "C":
    #         row = 80
    #     elif row == "D":
    #         row = 70
    #     elif row == "F":
    #         row = 60
    #     else:
    #         row = 0
    #     print(row)

 
    #print(csvhandler.get_fields(pathname, first))
    #print(csvhandler.get_fields("app/data/Student_Performance.csv", second))

    
    





if __name__ == '__main__':
    app.run(debug=True)
