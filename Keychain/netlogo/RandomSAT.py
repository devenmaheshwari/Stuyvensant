#! /usr/bin/python
print('Content-type: text/html\n')

import random 

def RandomSchool(file):
    openn=open(file, 'r')
    read=openn.read()
    openn.close()
    data=read.split('\n')
    return random.choice(data[1:])

def TotalScore(line):
    filenew=line.split(',')
    result=0
    try:
        for i in filenew[-3:]:
            result+=int(i)
        filenew.append(str(result))
    except:
        filenew.append('s')
    answer='<tr><td>'+filenew[0] +'</td><td>'+filenew[1] +'</td><td>'+filenew[2] +'</td><td>'+filenew[3] +'</td><td>'+filenew[4] +'</td><td>'+filenew[5] +'</td><td>'+filenew[6] +'</td></tr>'  
    htmlstart='<html>\n<body>\n<center>\n<h3><b>Random School SAT Scores</b></h3>\n'
    htmlend='\n</table>\n</center>\n</body>\n</html>'
    tablehead='\n<table border="1">\n<tr><td>DBN </td><td>School </td><td>Number of Tests </td><td>Reading </td><td>Math </td><td>Writing </td><td>Total </td></tr>'
#     writing=open('SAT.html', 'w')
#     writing.write(htmlstart+tablehead+answer+htmlend)
    print(htmlstart+tablehead+answer+htmlend)

TotalScore(RandomSchool('SAT-2010.csv'))