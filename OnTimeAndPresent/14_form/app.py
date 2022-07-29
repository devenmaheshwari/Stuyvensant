# Sports! - Sean Ging and Deven Maheshwari
# SoftDev
# K14 - Form and Function/Intro to Flask/App to echo input from user. 
# Oct 14 2021 

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. Can you predict which?
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests. Process results.
PROTIP: Insert your own in-line comments wherever they will help your future self and/or current teammates understand what is going on.
'''

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage(): # Display. Prediction: Will work, login.html is in templates directory. 
    print("\n\n\n") # New line. HTML uses <br> tags
    print("***DIAG: this Flask obj ***")
    print(app) # Prints line 13
    print("***DIAG: request obj ***")
    print(request) # From form submission
    print("***DIAG: request.args ***")
    print(request.args) # Inputs from user
    #print("***DIAG: request.args['username']  ***") # Test by uncommenting line by line and seeing outputs in terminal and app. Prediction: Will work, just printing to termianl.  
    #print(request.args['username']) # Test by uncommenting line by line and seeing outputs in terminal and app. # Prediction: Depends on user input
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( 'login.html' )


@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate(): # Manipulation of form data. Prediction: Will work - does not reference external files. 
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.args['username']  ***") # Test by uncommenting line by line and seeing outputs in terminal and app. Prediction: Will work, just printing to termianl.  
    #print(request.args['username']) # Test by uncommenting line by line and seeing outputs in terminal and app. Prediction: Depends on user input
    print("***DIAG: request.headers ***")
    print(request.headers) # Headers is attribute of request
    if (request.method == "GET"):
        return render_template( 'response.html', name = request.args['username'], url = request.args['sub1'] )
    return render_template( 'response.html' )  #response to a form submission


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
