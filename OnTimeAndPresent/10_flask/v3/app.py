# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print thing...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()

# This enabled debug mode for the flask app, which will display more information to the terminal(?).
# It will also say that debug mode is on.
# It might also restart the server whenever you edit the python file for easier debugging.

# Notes after running:
# No extra information was printed besides that the debugger is active.
# It also displayed "Debugger PIN: 890-502-291" to the terminal.