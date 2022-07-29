# Umlauts - Yusuf Elsharawy & Bill, Alejandro Alonso & Señor Juan, Deven Maheshwari & Batman Pd. 1
# SoftDev
# K10 -- Putting Little Pieces Together/Flask/Creating a flask app to print a random occupation from the already created file occupation.py
# 2021-09-28

import occupation
from flask import Flask
app = Flask(__name__)

header = """\
Yusuf Elsharawy & Bill, Alejandro Alonso & Señor Juan, Deven Maheshwari & Batman
SoftDev
K10 -- Putting Little Pieces Together / Flask Intro / Displaying a occupation to a webpage.
2021-10-04
"""

@app.route("/")
def hello_world():
    response = header + "\n"
    for k in occupation.jobPercentages:
        response += k + "\n"
    chosenJob = occupation.chooseRandom()
    response += "\nRandom occupation: " + chosenJob
    return response.replace("\n", "<br>")

if __name__ == '__main__':
    occupation.init()
    app.run(debug=True)
