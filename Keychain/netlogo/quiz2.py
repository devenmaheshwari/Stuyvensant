#! /usr/bin/python

print('Content-type: text/html\n')

HTML_Template = '''
<html>
<body>
<head>
<meta http-equiv="content-type" content="text/html; charset=windows-1252">
<title>Quiz 2</title>
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
</style> </head>
<body style="                                   background-color: #d2e2ff;">
<form method="get" action="quiz1.py">
  <div class="topnav" style="background-color: #353940;"><span style="color: #4600ff;">
      <a href="home.html" style="color: #fff7fd;">Home</a> <a href="quizzes.html">Quizzes</a>
      <a href="makeastory.html">Storyteller</a> <a href="aboutus.html">About
        </a></span> </div>
  <h1 style="text-align: center;"><span style="color: #FF7F50;"><u><b>
  Quiz Complete!</b></u></span></h1>
<br> <center>
You are ???result???!
<br> <br>
Thank you for completing our quiz.
<br> <br>
Feel free to return to the "Quizzes" page and try another quiz!
<br>
<br>
???image???
</body>
</html>
'''

import cgi, cgitb
cgitb.enable()

def buildpage():
    entries = cgi.FieldStorage()

    HTML=HTML_Template
    points = 0

# Question 1: Which social media platform do you use most?
    if entries.getvalue('socmed') == "ig":
        points += 1
    if entries.getvalue('socmed') == "snap":
        points += 2
    if entries.getvalue('socmed') == "tweet":
        points += 3
    if entries.getvalue('socmed') == "fb":
        points += 4
    if entries.getvalue('socmed') == "zoom":
        points += 5
    if entries.getvalue('socmed') == "other":
        points += 6

# Question 2: Which picture is your favorite?
    if entries.getvalue('pic') == "red":
        points += 1
    if entries.getvalue('pic') == "water":
        points += 2
    if entries.getvalue('pic') == "park":
        points += 3
    if entries.getvalue('pic') == "window":
        points += 4

# Question 3: How young are you?
    if int(entries.getvalue('youth')) == 0:
        points += 0
    if int(entries.getvalue('youth')) > 0 and int(entries.getvalue('youth')) <= 10:
        points += 1
    if int(entries.getvalue('youth')) > 10 and int(entries.getvalue('youth')) <= 20:
        points += 2
    if int(entries.getvalue('youth')) > 20 and int(entries.getvalue('youth')) <= 30:
        points += 3
    if int(entries.getvalue('youth')) > 30 and int(entries.getvalue('youth')) <= 40:
        points += 4
    if int(entries.getvalue('youth')) > 40 and int(entries.getvalue('youth')) <= 50:
        points += 5
    if int(entries.getvalue('youth')) > 50 and int(entries.getvalue('youth')) <= 60:
        points += 1
    if int(entries.getvalue('youth')) > 60 and int(entries.getvalue('youth')) <= 70:
        points += 2
    if int(entries.getvalue('youth')) > 70 and int(entries.getvalue('youth')) <= 80:
        points += 3
    if int(entries.getvalue('youth')) > 80 and int(entries.getvalue('youth')) <= 90:
        points += 4
    if int(entries.getvalue('youth')) > 90 and int(entries.getvalue('youth')) <= 100:
        points += 5

# Question 4: Which is the most trustworthy source?
    if entries.getvalue('news') == "onion":
        points += 1
    if entries.getvalue('news') == "yahoo":
        points += 2
    if entries.getvalue('news') == "wiki":
        points += 3
    if entries.getvalue('news') == "wolfram":
        points += 4

# Question 5: How long do you spend on a screen every day?
    if entries.getvalue('choices') == "Less Than One Hour":
        points += 1
    if entries.getvalue('choices') == "2-4 Hours":
        points += 2
    if entries.getvalue('choices') == "5 Hours 38 Minutes Exactly":
        points += 3
    if entries.getvalue('choices') == "Between 6-7 hours":
        points += 4
    if entries.getvalue('choices') == "More than 8 hours":
        points += 5
    if entries.getvalue('choices') == "24/7 Sleep is for the weak":
        points += 6


# Question 6: Best movie watching platform
    if entries.getvalue('movies') == "netflix":
        points += 1
    if entries.getvalue('movies') == "hulu":
        points += 2
    if entries.getvalue('movies') == "123":
        points += 3
    if entries.getvalue('movies') == "theatre":
        points += 4

# Question 7: Are you familiar with the platform by the name of "WUPHF"?
    if entries.getvalue('answer') == "Yes":
        points += 2
    if entries.getvalue('answer') == "No":
        points += 1

# Results
    if points <= 15:
        result_response = "a Snapchatter, now go get your snapscore up"
        image_response = "<img src=data:image/png;base64,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>"
        HTML=HTML.replace('???result???', result_response)
        HTML=HTML.replace('???image???', image_response)

    if points > 15:
        result_response = "an Instagrammer, now go grow your influencer page"
        image_response = "<img src=data:image/jpeg;base64,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>"
        HTML=HTML.replace('???result???', result_response)
        HTML=HTML.replace('???image???', image_response)
    if points >= 6 and points < 7:
        princess_response = "Aurora"
        image_response = "<img src=images/aurora.jpeg>"
        HTML=HTML.replace('???princess???', princess_response)
        HTML=HTML.replace('???image???', image_response)
    if 7 <= points < 8:
        princess_response = "Pocahontas"
        image_response = "<img src=images/pocahontas.jpeg>"
        HTML=HTML.replace('???princess???', princess_response)
        HTML=HTML.replace('???image???', image_response)



    print (HTML)

buildpage()