#! /usr/bin/python3
print('Content-type: text/html\n')

import cgi

import cgitb
cgitb.enable()

Top='''
<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=windows-1252">
    <title>Quiz 3</title>
    <style>
body {
background-color: #262626;
color: white;
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
<body style="background-color: #d2e2ff;">
    <div style="text-align: center;">
    <div class="topnav" style="background-color: #353940;"><span style="color: #4600ff;">
            <a href="home.html" style="color: #fff7fd;">Home</a> <a
              href="quizzes.html">Quizzes</a>
            <a href="makeastory.html">Storyteller</a> <a href="aboutus.html">About
              </a></span> </div>
        <h1 style="text-align: center;"><span style="color: #FF7F50;"><u><b>Are
                You Smarter Than a 5th Grader??<br>
              </b></u></span></h1>
        <h2><span style="color: black;">You Got ??answer?? </span></h2> <br>
        <img src=" ??picture?? "  width="600" height="500">
        <br>
        <h2><span style="color: black;">Your Score Was ??percent??%</span> </h2>
        <h3><span style="color: black;">Correct Answers:</span><br>
            <span style="color: black;">1. 8/11 </span><span style="color: red;">You Put ??answer1??</span><br>
            <span style="color: black;">2. dog food or can of dog food </span><span style="color: red;">You Put ??answer2??</span><br>
            <span style="color: black;">3. Jumped </span><span style="color: red;">You Put ??answer3??</span><br>
            <span style="color: black;">4. Wall, great, king's, king's </span><span style="color: red;">You Put ??answer4??, ??answer5??, ??answer6??, ??answer7??</span><br>
            <span style="color: black;">5. Helsinki </span><span style="color: red;">You Put ??answer8??</span></h3>
'''
Bottom='''
</body>
</html>
'''

def quiz3quiz():
    form=cgi.FieldStorage()
    HTML=Top
    count=0
    total=8
    if form.getvalue("fractions")=="8/11":
        count+=1
        HTML=HTML.replace("You Put ??answer1??", "")
    else:
        HTML=HTML.replace("??answer1??", str(form.getvalue("fractions")))
    food=form.getvalue("song")
    try:
        if food.lower()=="can of dog food" or food.lower()=="dog food":
            count+=1
            HTML=HTML.replace("You Put ??answer2??", "")
        else:
            HTML=HTML.replace("??answer2??", food)
    except:
        HTML=HTML.replace("You Put ??answer2??", "You Put None")
    if form.getvalue("noun")=="Jumped":
        count+=1
        HTML=HTML.replace("You Put ??answer3??", "")
    else:
        HTML=HTML.replace("??answer3??", str(form.getvalue("noun")))
    if form.getvalue("humpty", "")=="Wall":
        count+=1
        HTML=HTML.replace("You Put ??answer4??", "")
    else:
        HTML=HTML.replace("??answer4??", str(form.getvalue("humpty")))
    if form.getvalue("humpty2", "")=="great":
        count+=1
        HTML=HTML.replace("You Put ??answer5??", "")
    else:
        HTML=HTML.replace("??answer5??", str(form.getvalue("humpty2")))
    if form.getvalue("humpty3", "")=="king's":
        count+=1
        HTML=HTML.replace("You Put ??answer6??", "")
    else:
        HTML=HTML.replace("??answer6??", str(form.getvalue("humpty3")))
    if form.getvalue("humpty4", "")=="king's":
        count+=1
        HTML=HTML.replace("You Put ??answer7??", "")
    else:
        HTML=HTML.replace("??answer7??", str(form.getvalue("humpty4")))
    if form.getvalue("capital")=="Helsinki":
        count+=1
        HTML=HTML.replace("You Put ??answer8??", "")
    else:
        HTML=HTML.replace("??answer8??", str(form.getvalue("capital")))
    if (count/total)<0.65:
        answer="No :("
        HTML=HTML.replace("??answer??", answer)
        image="https://media.tenor.com/images/4223f6e10588b21e2429a954c79a95b1/tenor.png"
        HTML=HTML.replace("??picture??", image)
        score=(count/total)*100
        HTML=HTML.replace("??percent??", str(score))
    else:
        answer="Yes!!!!!"
        HTML=HTML.replace("??answer??", answer)
        image="data:image/png;base64,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"
        HTML=HTML.replace("??picture??", image)
        score=(count/total)*100
        HTML=HTML.replace("??percent??", str(score))
    HTML=HTML+Bottom
    if form.getvalue("done")=="Find Out!":
        print(HTML)

quiz3quiz()
