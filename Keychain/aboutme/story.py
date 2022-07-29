#! /usr/bin/python

print('Content-type: text/html\n')

HTML_Template = '''
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="content-type" content="text/html; charset=windows-1252">
    <title>Storyteller</title>
    <style>
body {
background-color: #262626;
color: black;
}
.topnav {
  background-color: #000000;
  overflow: hidden;
}
.topnav a {
  float: left;
  color: #e6e6e6;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 24px;
}
.center {
    margin: auto;
    width: 60%
}
</style> </head>
<form method="get" action="story.py">
  <body style="  background-color: #d2e2ff;">
    <div class="topnav" style="background-color: #353940;"><span style="color: #4600ff;">
        <a href="home.html" style="color: #fff7fd;">Home</a>
        <a href="quizzes.html">Quizzes</a>
        <a href="makeastory.html">Storyteller</a>
        <a href="aboutus.html">About</a></span>
    </div>

    <h1 style="text-align: center;"><span style="color: #FF7F50;"><u><b>Storyteller</b></u></span></h1>

    <div style="text-align: center;">
      <h3><span style="color: black;"> You Shakespearean mastermind! <br><br><div class="center"> Though the text may sometimes seem incoherent and delirious,
     you must look between the lines as it was made with love (and by a neural network).</h3> </div><br><br>
     <div class="center"><b>Disclaimer:</b> we are not responsible for the text that the API may print out. The GPT-2 model has been trained with
     random texts that we have no power over, and thus we cannot guarantee that it will always remain appropriate. This is actually part of a
     true debate on how to tame machine learning algorithms and make them more predictable.</span></div>
    </div>
    <br> <br> <br>
    <div class="center">
    ???text???
    </div>
    <br>
    <br>
    <br>
  </body>
</html>
'''

import cgi, cgitb
cgitb.enable()
import json

def buildpage():
    entries = cgi.FieldStorage()

    HTML=HTML_Template

    try:
        import requests
        r = requests.post(
            "https://api.deepai.org/api/text-generator",
            data={
                'text': entries.getvalue('phrase'),
                },
                headers={'api-key': 'ad0fc99f-1fd3-4177-9071-be6b86656a24'}
                )
        HTML=HTML.replace('???text???', r.json()['output'])

    except:
        HTML=HTML.replace('???text???', "<b>ERROR<b>: please enter a phrase. Return to the previous page.")

    print(HTML)

buildpage()