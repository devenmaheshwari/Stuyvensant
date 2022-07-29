# Sports! - Sean Ging and Deven Maheshwari
# SoftDev
# K15 - Sessions Greetings/Cookies & Error Handling/App to handle bad inputs and tracking username
# Oct 19 2021 

from flask.globals import session           #facilitate form submission

#the conventional way:
from flask import Flask, render_template, request, redirect
import os

from flask.helpers import url_for

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32) # Generates random unsigned 32 bit integer
username = 'Sports!' 
password = 'Mykolyk'

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():  
    """
    Login Page

    """
    if 'username' in session: # Checks if username is defined in session dictonary
        return render_template( 'response.html', name = username, success = True )
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST'])
def authenticate(): 
    """
    Checks login info and changes success variable based on correct usage. 
    """

    #if (request.method == "GET"):
    try:
        if (request.args['username'] == username and request.args['password'] == password): # Check for hardcoded account
            session['username'] = username
            session['password'] = password
            return redirect(url_for("disp_loginpage")) # Routes url for logged in session to login_html url so that session stays logged in
    except:
        return render_template( 'response.html', name = request.args['username'], success = False )
    return render_template( 'response.html', name = request.args['username'], success = False )

@app.route("/logout")
def logout():
    """
    Logs out of account
    """

    if 'username' in session:
        session.pop('username')
        session.pop('password')
    return render_template( 'login.html' )

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
