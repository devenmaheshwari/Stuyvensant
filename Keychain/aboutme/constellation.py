#! /usr/bin/python3
print('Content-type: text/html\n')

import cgi

import cgitb
cgitb.enable()


Top='''
<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=windows-1252">
    <title>Constellation</title>
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
  width: 50%
}
</style> </head>
  <body style="                                    background-color: rgba(255, 9, 39, 0.46);"><span
      style="font-family: Chalkduster;">
    </span>
      <div class="topnav" style="background-color: #34343a;"><span style="font-family: Chalkduster;"><span
            style="color: #4600ff;"><a
              href="ec.html"
              style="color: #fff7fd;">Home<span
                style="color: #e6e6e6;"></span></a><a
              href="zodiac.html">Zodiac</a><a
              href="horoscope.html">Horoscope</a><a
              href="constellation.html">Constellation</a>
          </span></span></div>
      <span style="font-family: Chalkduster;"> </span>
      <h1 style="background-color: rgba(255, 9, 39, 0); text-align: center;"><b><u><span
              style="font-family: Chalkduster;">Can
              You Identify these Major Constellations and Asterisms? <br>
            </span></u></b></h1>
      <h2 style="text-align: center;"><span
              style="font-family: Chalkduster;"><span style="color: white;">Your Score is ??score?? %</span></h2></span>
      <br>
      <h3 style=" text-align: center;">
      <img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhUTExMWFRUXFxcaGBcYGBodFxodGhgYGB0eFxobHyggGh0lHRoYITEiJSkrLi4uFx8zODMtNygtLisBCgoKDg0OGhAQGi0fHSUtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSstLS0tLS0tLS0tLS0tLS0tLf/AABEIAJ8BPgMBIgACEQEDEQH/xAAbAAACAwEBAQAAAAAAAAAAAAABAgADBAUGB//EAD0QAAEDAQUFBgUDAwMEAwAAAAEAAhEDBBIhMfAFQVFhcQYigZGhsRMywdHhFELxFVJiFkNTM3KCkgcjJP/EABgBAQEBAQEAAAAAAAAAAAAAAAABAgME/8QAKBEBAQACAQQCAQMFAQAAAAAAAAECERIDEyFBMVEEFCJhMlJxgfBC/9oADAMBAAIRAxEAPwD4uEWa8UziMcMNyjhGt69zBUxdzPPmkbgnAVktAAOGB+nFBohO3XqgRP18lfE/kHLLj9PPkk3pgzHjw5wmIwOuCtl9hIHM6/hWsaLkzjyzzj6yq3QPNB7z0U2UdR9lAPL15RjxQB1rNNOvsk0CCMZj878tyhd+fylJ14J6FK9vyWuf0l8fJb3VMTh9UQ3Ezz9JzSubjGvHwWploQHPxnW5JeTPO/XskH016qZ5aWRZfwhKRrclamJy1repM9zRot7DnxRDkrso14KDJc937BDt860c0XO+yUoyFeVEwKgMz+EHa4qOKm6ooDWeKLlJ9NePRNgSmc5Ii09daCIh3KNUlQooymjfzSA4IifHBamWvlByRAwUDvqnew+G7xXWaqFJzOvNVlNCJ1/CxcVKXHf4Tu3qEeKM6ySOnisaDROgiOKYNjEazSwNcFrUgJ1moVBuz8ufLP8ABR4Kyb+RbZaYJxkwMhvUrgAkD7xr6qmcUqzy1fAenVLcRh5wlqOJzjmlaUwbrcs7tAlTQ9deKMIXk8QMc1A7U+yUlTXqlqpIRbM+59N3NAjWvBGc41r6pEOXJXH6ay5JUWDWuqsvnyA9ADmi/ehKlvkMXdB0QOsvVSNeCgbzUUS0xKEa6K5pEZ7lSVaJ7/hLiEwapGjrFQTXRQHPWvFExunXso6eJ++f3QKVBr8qRx4KXUATmemt3iljLf5o8NSgBCjlAPFH8bkDhvilJElRrjCBH5VQMk5eYSx7otagdruW6ErhMoYjDWKAXSZ+qI1CTx14pwoVLPcEcdc0Wjjh5Ia6+aE4fzrml8fIId4a98kAMEoTEa1rBTzQD7IJncxr+UCSlx18gtHBEtjX0Qa4jWsVKj1kCeaE9FHD2QUUW9ES7gEcN51r3Sxr+UElEY4ApZRVATR7oEIiE0gFAKSmlFCOKAzTPclU8AgmcFfRpCJJCzSnDlZUsWOYAcCqwYz8ECVDnwxUEnnhrWKkdZU3Jhrx4IqRrW5LKhdJUB5IIUWwgida3oBKngoTwQQMWoFEZfZTXNWgA61rBNe4+f2SzwCI+2CiCXBDJTWtb0SJV+QAheRu+k7uqkdEl0CTy3ayQvIDWtb0Sctfwn+QBnr1TjXmklFWZaDSleg461rFHdOvyluxJ666dFPD8INRnUeyl/kTwQKl5AJ4UR47k14bgEvgoCm0EmeKUozhGtfZA81FEckZ5IRr7qIASgoCogkogqFBQGEdawSkqAIHBVgjWapUKsQzkBxUMa+iMR4cFFKiSoiGH7KoDt4z/lNHH139PRL560VNYIok8kCUCoUEHijKhRJQGcErs81B5a3a3IhAGhNIUE7kB1xQGeHollQYa90QeA9EE9VIg6kpqb4cCpWfJlXSEhGEMdfVSE8CAa10Rdhy/lA8skSU2qDyw+impQARwhRBMeSUwjKhCAShCYBFw80CQpxTwhdVNgQi1qIamYU0lpXMSAK958UrAibVQjCscEW5KaXakhGU11QNTS7LdTXcFCFAhssa1zRDU13WvHyR5q6Nlpt6b091IQictdft5IhDj0QiUx1riooo4fnDww+iWI9EQVEAUhQBFAIw1reoRGKh6qE4oqI3NHJABTWCAgIE+/BFvPPogcdH6IJKUK9lMET9lXr1VTYSoSoCmBUCqQmnXmgRrW5UQqFQBPuRC3SpCeFI8ldJsoHFQDkrA3zRDVrim1YajCuDEwYrxTkoDVLq0immFNXinJk+GiGLV8NQUU4pyZbilxa/glH4avA5Mfw00b1qNJAU1OByZC3FH4R4LUaRRa2E4ryZC3rzSuC0vpoBinE5M0ShdWhzErmqcV5KY1rkPRHlEa4prsKXSpcWpVRahdVkBAqaXZCoUzUFFAhKrJlAt4Y8sVABnz9PVKCmPqpz1nryQBuY3alD3T8OiS9unWP3RRnmoESEQ3yVQBKJEZqINTQPijCIaiAtSM2g1qcNjqi1qubSW5ixclIb5KwMWhtJXMoLcwYuTK2irG0l0KNllaRYluYMXNyRRVjbOuvTsStFj5LcwYvUcf8ATI/p1222FWssHJXgnccIWZX0LLhku0Nn8lYywlXgnccOrZeSp/Sr0n6AlH+nHgnBO480bKVP0vJek/Qckv8AT+ScDuPOGzJDZtb16U7P5Kt9g5JwXuPNPsyU2cr0TrDyVLrCpcGp1HnzSSGmu4+xKh9kWeDUzcZ9LxSPprrPs6ofZuKxcG5m5bglcFvdQ1rNUupwsXBuZMpYmc1Nc190p6rncWtqXJ6boRc1VuwWdN/IuzS9UfxkoBoLKlJ1yUcjG/7IXoylFQFOMld8PXBU3cVqRjZAFa0JmtVzKS6TC1m5KmtVrKS00rMSttCxrtj0nLLqMNKgtdKzLp0LFyXQobP5LtOk45dVx6VjW2nYV6KxbDqP+Wm53QL0Fj7GVzmwN/7iArbhj81z55X4eLoWDktjLDyXv7P2LA+eswdJJW6l2csjfmqOd0gLnev0/XlOOb5yywclczZq+kMsthZ+yepWilb7K3AU2DqB9Vm/kfWNO395R85pbKO5p8itVLYdQ5U3eRX0hu3LM0fMwchH0SntPS3YrH6jqX4wb7WHvJ4Sl2ZrH/ad5LS3slW/4yvYf6kByCH+ows97r/2xe10vuvK0+yNf/j9k/8ApCv/AGeoXoqvaWOC0WDaz6mIgDn9lL1evJuyE6fSviWvJnsfX/s9QkPZGv8A8fsvfUbYZIOPhA896sqWsASXQBvMBc/1XV+o6fpsPuvm7+ylcf7RWep2brDOk7yX0QbZZMXh1OCZ21gPwQfZdJ+R1f7WOx0/t8tq7EeM2O8lkq7LI3ei+vf1Vp4JHW2kfma09QPstT8rP3iz2cfWT41U2dyWWrs5faH07K/Okw9PwslXYVif+270ctz8qe8anay9WPi1XZ/JZKthX2av2Ls7vlqOb1AK5Vr/APj9/wCyox3otz8jpX3o49SenyKpY1kq2Tkvpdv7E2lv+0XD/HH2XnbXsd7DDmOHUFdJMMvi7Odny8W+zFUuoL0tosZG5YqllzWMuk649RwHshVVGa1rFde0WYrJUoQPD6/wuOXTrtjmwgKOIV7mqssOtcguOWNjrKq91WdZq8Mk4qGlwWNNbWNlWMpK6nSXW2fsirU+VhjicB5nBevHpvNl1NOZQsy3ULIvR2XYFNuNWqB/izE+ZgD1XTpWuyUfkphx4v73pl6LtJJ8Tbz3qWuHs7Y1SoYYxzug916SxdjX51HMpjmZPkJVb+1L3CGZDcMAPos/9RqOxc6B1Hut/u/w527els2xLHT+eo6oeUNH1XUstrszcKVFnU4+6+a2zbTASxkvOV4OJb4RmrbFUqkgn4tzMlrYDhP9zsIn7rN6W5+6rqx9Mr9oi0ReA5CB5D8LibQ7WOabpvA88FkswoucLoE5d98AOwxJLhMdMVydsPpzcNVji4jBjgXeG85HIrnhjhvWlu22r2pcd6yVO0jjvXL2d2etFpM0m02MGF51QEYcYvQV3tl9lLPTl1ptNOpA+RriB4kEGF2y6nSwJ0rXPO3XHKT0SnaFU/td44e/Q+S9Hb6lla1rqdMmO6DSpEAf+RhuQ5rC91J92nRpOl2EVCQZykXe67jxWZ15f/Jenpz7PbXjvOiIG8TjOQ8Ctb9qw2bw5tAdMccQPdYtqUX0nBrntMEhwaCLro3uIEnLecVmZaSWuJeHXQ0n/wCz5v24AxejKRJw3rXLl5Z46dRm2yMRJ9sOK2O229sOq0oaciTHXquD/Ue6Gup3pEggbhhnmBn6qmzWmmTF2DmTTF52WUOLcBBxnop4+jT1g7WXSQ2mCOvDlAhaf9VWgi8GANPI4dcV4ptqZumYmMJJmRm4xj1+q3Ne65gKYGc3oOPB2Ib0JGfgsXHH6a3l9vWN7Y1WtktY7gccRygDHkstftZXrAsa0m9hdY2TB4HH79Fw7PWsoN+pUqF2BMA4cMTBccoHI5rHUttO8X/Gc4mZD24tyggtfePlGBWZMN+MWrz+3Yqbbe3B7XAjMEY+IOSLu0ZGEjz/ABgvLWvaDZkknfiwAHEieQzyOeGOaw/rL8w8CcTBIHljvO6V6JJfmONwvp7Y9pDh3o661CZvaFzgRfzE5n6T9F4KvUhxEnfjjjzxGPoiXmYvGZ4TJmMMTP53rfDE417qh2kcDBk9Dkt1LtCMw8T19182bekSf54Hx3q6zV3ucGgtk4AOMDpjgB1UvTxNX0+pUu0MR3gVso9pG/3e6+S16j2GJblPde14xxwLSUGbSqbjPhJjE/ZYvQwpvOPtVn22TiHDpIWh+1wRFQA8nAEeq+L0NskCSXRhGJieu7+Vup9pHDAnDR3Zlcr+JPTXdyj6Xa7DYqvzUWg8WS30GHouJauxNmdPwqrmcnAH1Eey81Q2zeIAIB5GPOei10u0jhz5CDO/zVnRzx/pqdye4p2l2DtDRLQ2oP8AE4+Rg+i8ltDZD6Zh7HMPBwIPqvodm7SgwZLeQIPmuoNtte268Ne3g4AjyMp++f1TazOeq+J1rJwWZ1CF9ituwbFXEhhpk72ER/6kkeS8ztHsNUEmjUbUHA9x/kcPVYvG/wAO2PVfO6jIPuqahXb2nsypSJbVpuYf8hE9Dv8ABcp9Jcsum745yu/Z7VRp5NDjxdifLJWWntA4j5l5M1SheXeWM9r7dqptdx3qhu0Me9J5BcyUZXTmvbjsu20boaxobxJxJ4Z/lUfri/8A6lR0cAM9/Ie65wWqyW91MODQ3vZkjHfkZ5+gTmcJ6dCz2yo0Sym/AYOJcYE7roEecLoU32hwJfVfkLuAmDPLcG8cM5zWGwbYBfdfSbDoDS29g44AmXYjiu9b2EOIDWtu93NzgO6ZEuJMAAzE5GNynKWueU16YRQENNV1Srm2HvIb3QMsZIExGC9Ds19hp3S+iWmCHBr2tLjie9e70QOQHVedouvteWktgAuaP3QQO8ZA9Dn4oWSvjFQv+G4C8GOghoJ7wGDZwyjj4spLNM6r0G2NuUHOIog02NN26SS8xwnPoY5b451djnm8GNblEENJmADcvfLjEwQY6xbsNlGpUbfFQklg7ru81oHeJeS0jBt7ugngujaNt2WXmlQxYXQyGmmRkCS4AwCG4XcZM8Vnnx8Yw4e2mwWioaLWuqupU6ZkVA7ATAJDi4NMY4zG7FNtHa9IvhloDLpIJDHfGqGP+QDiM2k8oWTZlrZa67m1aj2MY2TdbwdHdgwDLsyDgYxxXQp7Z2fYzIptc4gup/Fa5wdMDB/eLMMPlE8MMeGVkvmeXSY/TjWrblRzWkPe+HYMLBdA3mcyXRhlhwwWez217Q2pcESQCWCHEhsiZaTgOgJ5r2Vl29QqNvVNnMax0i8wU3AhoOYNxwEDnluWq2doLHZnsaGNpucDcL6UtFwE/tLjv3R9FO96mP8A3+jt+9vAXbQ9zrtB795Aa47jJEfL/dA5RhM4qbazrwAaSGi+Ll94AwMhzSRhn/K6Hb217SvuqurP/TSPhmnUutgwG90XXTgMCMDK89au076jrz2tMgAyCct7cZZAmA3jjOEdcepbPS9p39nWSqBfYZLYLm3REHI3mjAY5ECJHHC207Vql14/DH/g2Jb/AGlowEgTBylcqy2muaf/AOergGi9cLmXcgbwwvYGI72M4wsj6r2/9RgDjEPJnMh0mDLsCMDhBPhqXzusXGO8y2Uy5pq03vAaTg64XRMQQXH5hBjrhAip9JpF5tMhuYvY5uyExew5bjhmFldbrlMuiQ8hrXCMwRIcCAcIBGBzOImV09l7SpPxfReaYm6WlgqScgXECADycMZAU7mvJwYX1rjbzhEZOjARJADcBv3GBeOGQPOqWljyAQIPKJmP3NmMeA6rr7fpNaxxpl4+G68WOdN2+YEiLpwuzdK49iaWHMk4FzQQ1pAIa0nDHvEiI4lbnUl8xJh9nr2J7Q6DgCDGBbl/kZJAnnngIKShUEtaRj/dgPmyBBMT80HoeaLaYIul5cCZAJdeByIJiJPEGMug6Fmo2epDHvNNpcbry0F2LcLxDHOIF4ZR82AEYXnYuozVu5k6CBeETePTpB4RB4QsLWmCcMDBxF7ymT5blp+DdJpgh/zd4ziGgjuy0ECBv9MVRVpfMQwhoZe+YHIdBgc4iVuZscCVH8Rd6g4fXci5/WcsPlIAHDPAesrG3atRhlkNkGJAdAPC9IyPDesot1QT33QfmEmDvx444p3I3OlXbP7ThDwYBcXOGMYhokb8DOAOeC0/FdTZk1zXYFxDxdIMgd4AB0AYQcIXDpWj4hghsnMAAZcMIHgrnAtJnEjCDnhGs9ym9+y46+WynaajjgXG7lLojfmPTnkpVtLxi+QTvznjPA+q4zbXBy8jByPLmukdvVKjwXOdkMzJJHA3cJ3cOancsvgvS/hb/USN5Wmltl0RPnjl7KhnwjSdeDr2Dmw1sRJb3nBwnfIDQThjgue+AYwHnh1zlbnV253o4vT2Lbbjk4DDeTGXkPFdOydpLsSfDBeHpuEy4mA4Yg4xynxz9EalUXjdcSNxIieoE/ZOUvzGb0fp9Pbt5lRsOuuBzacR4giFyLdsOxVTeE0jvuEQfAyB4LxItDgc8lqZtd4ESs8Mb8M8c58P/9k=" width="700" height="500">
      </span></h3><br>
      <center><h4 style="text-align: center;"><span
              style="font-family: Chalkduster;"><span style="color: white;">Correct Answers</span></h4></span>
            <span style="font-family: Chalkduster;"><span style="color: black;">1. Ursa Major, Asterism </span></span><span style="font-family: Chalkduster;"><span style="color: red;">You Put ??answer1??</span></span><br>
            <span style="font-family: Chalkduster;"><span style="color: black;">2. Hercules or Hercules Constellation </span></span><span style="font-family: Chalkduster;"><span style="color: red;">You Put ??answer2??</span></span><br>
            <span style="font-family: Chalkduster;"><span style="color: black;">3. Polaris </span></span><span style="font-family: Chalkduster;"><span style="color: red;">You Put ??answer3??</span></span><br>
            <span style="font-family: Chalkduster;"><span style="color: black;">4. Square of Pegasus</span></span><span style="font-family: Chalkduster;"><span style="color: red;">You Put ??answer4??</span></span><br>
            <span style="font-family: Chalkduster;"><span style="color: black;">5. The Milky Way or Milky Way </span></span><span style="font-family: Chalkduster;"><span style="color: red;">You Put ??answer5??</span></span><br>
            <span style="font-family: Chalkduster;"><span style="color: black;">6. Set with stars </span></span><span style="font-family: Chalkduster;"><span style="color: red;">You Put ??answer6??</span></span><br>
            <span style="font-family: Chalkduster;"><span style="color: black;">7. Doofus </span></span><span style="font-family: Chalkduster;"><span style="color: red;">You Put ??answer7??</span></span><br>
            <span style="font-family: Chalkduster;"><span style="color: black;">8. Babylon </span></span><span style="font-family: Chalkduster;"><span style="color: red;">You Put ??answer8??</span></span><br>
</center>
</body>
</html>
'''

def constellation():
    form=cgi.FieldStorage()
    HTML=Top
    points=0
    total=8
    #Question 1
    if form.getvalue("dipper")=="yes":
        points+=1
        HTML=HTML.replace("You Put ??answer1??", "")
    else:
        HTML=HTML.replace("??answer1??", str(form.getvalue("dipper")))
    #Question 2
    two=form.getvalue("hercules")
    try:
        if two.lower()=="hercules" or two.lower()=="hercules constellation":
            points+=1
            HTML=HTML.replace("You Put ??answer2??", "")
        else:
            HTML=HTML.replace("??answer2??", two)
    except:
        HTML=HTML.replace("You Put ??answer2??", "You Put None")
    #Question 3
    if form.getvalue("star")=="yes":
        points+=1
        HTML=HTML.replace("You Put ??answer3??", "")
    else:
        HTML=HTML.replace("??answer3??", str(form.getvalue("star")))
    #Question 4
    if form.getvalue("aster")=="yes":
        points+=1
        HTML=HTML.replace("You Put ??answer4??", "")
    else:
        HTML=HTML.replace("??answer4??", str(form.getvalue("aster")))
    #Question 5
    five=form.getvalue("galaxy")
    try:
        if five.lower()=="milky way" or five.lower()=="the milky way":
            points+=1
            HTML=HTML.replace("You Put ??answer5??", "")
        else:
            HTML=HTML.replace("??answer5??", five)
    except:
        HTML=HTML.replace("You Put ??answer5??", "You Put None")
    #Question 6
    if form.getvalue("latin")=="yes":
        points+=1
        HTML=HTML.replace("You Put ??answer6??", "")
    else:
        HTML=HTML.replace("??answer6??", str(form.getvalue("latin")))
    #Question 7
    if form.getvalue("fit", "")=="Doofus":
        points+=1
        HTML=HTML.replace("You Put ??answer7??", "")
    else:
        HTML=HTML.replace("??answer7??", str(form.getvalue("fit")))
    #Question 8
    if form.getvalue("ancient")=="yes":
        points+=1
        HTML=HTML.replace("You Put ??answer8??", "")
    else:
        HTML=HTML.replace("??answer8??", str(form.getvalue("ancient")))
    #Python
    answer=(points/total)*100
    HTML=HTML.replace("??score??", str(answer))
    if form.getvalue("done")=="Done":
        print(HTML)

constellation()
    