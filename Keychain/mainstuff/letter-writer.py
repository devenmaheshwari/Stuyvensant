#! /usr/bin/python3 
print('Content-type: text/html\n')

import cgi

import cgitb
cgitb.enable()

Top='''
<html>
<head>
<title>Letter Writing</title>
</head>
<body>
??date??
</br></br>
Dear ??prefix?? ??text??
</br></br>
It is with great pleasure that we have decided to send you this ??choices?? as a small token of our esteem.
</br></br>
Unfortunately, returns are currently not possible. </br>
Sincerely, </br>
The Management
??number??
'''
Bottom='''
</body>
</html>
'''

def letter():
    form=cgi.FieldStorage()
    HTML=Top
    if form.getvalue("press", "yes")=="yes":
        date='Monday, 3rd month, 12 B.C.E'
    else:
        date=''
    HTML=HTML.replace('??date??', date)
    if form.getvalue("prefix")=="Mr":
        prefix='Mr.'
    elif form.getvalue("prefix")=="Ms":
        prefix='Ms.'
    else:
        prefix=''
    HTML=HTML.replace('??prefix??', prefix)
    surname=form.getvalue('surname')
    if form.getvalue("surname", "Appleseed")=="Appleseed":
        surname="Appleseed"
    HTML=HTML.replace('??text??', surname)
    choice=form.getvalue("choices", "")
    HTML=HTML.replace('??choices??', choice)
    HTML=HTML+Bottom
    if form.getvalue("button")=="Write It":
        print(HTML)
        print(form.getvalue("birth"))

letter()