# Squidcatman - Michelle Lo & Hellokitty, Angela Zhang & Inky, Deven Maheshwari & Batman
# SoftDev
# K13 - Template for Success/Using Flask/Creating flask app using the occupation python data 
# October 13 2021

from flask import Flask, render_template 
import csv
import random

app = Flask(__name__)



@app.route("/")
def hello_world():
    return "No hablo queso!"

@app.route("/occupyflaskst") 
def test_tmplt():
    """
    Creates occupyflaskst route on flask app. Uses a dictonary to take in occupation jobs and percentages and sends them to tablified.html. 

    Parameters:
        None
    
    Returns:
        None
    """

    jobp = {}
    with open('data/occupations.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            job = row["Job Class"]
            percentage = float(row["Percentage"])
            link = row["Link"]
            jobp[job] = [str(percentage), link]
        del jobp['Total']
    return render_template( 'tablified.html', foo = "K13", random = chooseRandom(jobp), response = jobp)

def chooseRandom(jobdict):  
    """
    Chooses random occupation based on weighted averages (from occupation.py)

    Parameters:
        None
    Returns:
        k - job name

    """
    randVal = random.uniform(0, 100) # randomly chooses a number from 0 to total percentage
    for k, v in jobdict.items():
        randVal -= float(v[0])
        if randVal <= 0:    # first cumulative percentage >= random value is the job chosen
            return k

if __name__ == "__main__":
    app.debug = True
    app.run()
