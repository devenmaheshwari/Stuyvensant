#! /usr/bin/python3
print('Content-type: text/html\n')

import cgi

import cgitb
cgitb.enable()

Top='''
<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=windows-1252">
    <title>Zodiac</title>
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
<body style="            background-color: rgba(255, 9, 39, 0.46);"><span style="font-family: Chalkduster;">
    </span>
    <form method="get" action="second.py">
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
              style="font-family: Chalkduster;">
              ??sign?? 2020 Horoscope</span></u></b></h1><br>
      <center><img src="https://static.toiimg.com/photo/74064747.cms" width="500" height="500">
      <h2><span style="font-family: Chalkduster;">Horoscopes Courtesy of <a href="https://www.horoscope.com/us/index.aspx">horoscope.com</a></span></h2><br>

     <h3><span style="font-family: Chalkduster;">Personal</span></h3>
     <h4><span style="font-family: Chalkduster;">??personal??</span></h4><br>
     <h3><span style="font-family: Chalkduster;">Career</span></h3>
     <h4><span style="font-family: Chalkduster;">??career??</span></h4><br>
</center>               
</body>
</html>
'''

def horoscope():
    form=cgi.FieldStorage()
    HTML=Top
    if form.getvalue("sign")=="aries":
        sign="Aries"
        personal="You feed off the fast-paced energy from your dynamic power planet Mars and 2020 starts with this aggressive <br>planet in Sagittarius, the sign of adventure and knowledge. World travel now is an amazingly eye-opening<br> experience now, rich with valuable learning experiences. It will take another several months, until the end of <br>June, until Mars reaches its most dominant placement in your sign, where it will stay for the next two months.<br> Winning is your main objective and yes, you can be a sore loser!"
        second="Moneymaking Venus moves into Taurus, the sign that loves money the most, at the start of March, which all <br>but gives you permission to start printing your own cash. Grab hold of all financial opportunities now, and <br>don't be afraid to work hard when the right chance comes along. Though Saturn moves into eccentric Aquarius <br>at the end of the month, calling on you to change things that aren't effective. Don't be afraid to walk into a <br>meeting and announce your ideas loudly and proudly. Your unique perspective deserves to be heard, and it's <br>that very same unique take on things that can earn you a raise, promotion, or brand new career opportunity."
    if form.getvalue("sign")=="taurus":
        sign="Taurus"
        personal="Your mind opens to new ideas in both areas. You're more comfortable, though, when she enters your sign in <br>early March until early April and then again in Libra for about three weeks at the end of October. Pleasure <br>and passion combien now to help you enjoy the finer things in life. The one retrograde period your ruler <br>experiences is from mid May to end of June, during her trip through curious Gemini, causing you to ponder <br>the dualities of love and money. While you can't imagine living life without a lot of either, it's interesting to <br>consider the alternatives."
        second="You're all about that money, but will your career goals and financial results meet your high expectations this <br>year? Saturn turns retrograde in early May, causing you to reconsider a career related opportunity, and then <br>goes direct again in Capricorn in late September. All this movement in this ambitious planet reminds you not <br>to give up. Keep working toward your goals, Taurus. You will get there."
    if form.getvalue("sign")=="gemini":
        sign="Gemini"
        personal="Not that you are going to let them slow you down too much, but this year the three periods between February <br>6 and March 9, June 17 and July 11, and October 13 and November 2 are all dates to be aware of. It's also <br>important to note that all three retrogrades pass through emotional water signs, which advise you to slow <br>down when dealing with the obstacles like miscommunications, misunderstandings, and commuting mishaps.<br> This will be challenging for you, Gemini, but you can do it."              
        second="Getting serious about career and finances this year literally pays off. Taking responsibility for youself and <br>your career and thinking about making changes will improve your long term life bottom line. Moderation <br>and caution are always linked to Saturn transits, so keep a cautious eye towards making any major <br>adjustments."
    if form.getvalue("sign")=="cancer":
        sign="Cancer"
        personal="Your sign is linked with your roller coaster emotions, so it makes sense that your ruler is the emotional <br>moon. You may feel lasting effects of this lunation as it is closely tied to family relationships, especially <br>parent child. Reunions and healing can take place now but be careful not to fall back into the same old <br>unhealthy dynamics you have been trying to escape once the happiness subsides."
        second="Keep putting in the work for maximum rewards. Besides ruling love, Venus also watches over financial <br>situations, so when she enters money focused Taurus at the start of March, it is a perfect match. You have a <br>real feel for money now, and any investments you make should be geared towards the long term. Keep in <br>mind that Uranus, the planet of change, is also riding with fiscally savvy Taurus this year, so be open to new <br>opportunities!"
    if form.getvalue("sign")=="leo":
        sign="Leo"
        personal="You love basking in attention so it's only fitting that your ruler is the ego boosting sun. When 2020 begins the <br>sun is in earthy, responsible Capricorn, so you will find yourself doing things for the sense of <br>accomplishment more that the glory. That all changes by the end of July, however, when the sun moves into <br>your flashy sign and welcomes in your birthday month. Happy birthday expressive, creative Leo! Your mood is <br>outgoing and playful, and you crave strong reactions to your antics. For the next four weeks you are the life <br>of the party, and you add the color and drama that had been missing from your loved ones lives."     
        second="You have got the tools to build success in 2020. Mars, the planet of action, enters ambitious Capricorn mid<br>-February, so working overitme might become the norm as you move towards your career goals. This energy <br>drives you to succeed, and you will see a lot of progress if you can stay focused. This is the time to think <br>big, Leo. Show your boss or clients why they can count on you to deliver when it really counts. When you<br> make your job top priority, success is all but guaranteed."
    if form.getvalue("sign")=="virgo":
        sign="Virgo"
        personal="Take care of your mind and body this year! Your ruler, Mercury, is one of the fastest moving planets, so your <br>mind is naturally quick and alert. This year Mercury begins in practical, kindred earth sign Capricorn and <br>quickly forms a conjunction with mind-expanding Jupiter, setting an optimistic tone for the year. Feeling <br>broad-minded and sociable is a great way to start 2020."
        second="Work hard for what you want in 2020. Hardworking Saturn is in ambitious Capricorn, a kindred earth sign and <br>sign it rules, at the beginning of the year and forms a serious conjunction with Pluto in mid-January.<br> Getting the year off to a productive start is what this transit is about, especially if you remain patient and <br>disciplined. You might be given extra responsibilities that could lead to an increase in salary but be prepared <br>to really work for it. There are no free rides now."
    if form.getvalue("sign")=="libra":
        sign="Libra"
        personal="Your sense of fairness drives you to success. This comfortable paring creates a romantic, dreamy flow of love <br>that will help you be more understanding, forgiving, and affectionate. Venus travels through your sign <br>starting at the end of October, putting close relationships in the spotlight. Do not let your willingness to <br>negotiate with people lead to crippling indecisiveness."   
        second="You get what you want when you work hard for it! Most people want to get lucky when it comes to money,<br> and you are no different. Looking for Jupiter, the planet of luck, combinations in the yearly planetary <br>movements yields a Venus Jupiter square at the end of February that makes you want to overspend. If you <br>have got money to burn, go for it. But if you are on a budget, do not give in to materialistic tempations. A <br>sun Jupiter trine at the start of September is one of the best solar transits and can bring big money <br>opportunities your way. it is relatively easy to improve your overall net worth now, so grab onto those high <br>dollar chances when they cross your path."
    if form.getvalue("sign")=="scorpio":
        sign="Scorpio"
        personal="Nothing shakes your confidence this year! You have got that infamous Scorpio swagger already, but you will <br>really be feeling yourself when your power planet, Mars, spends time in your sign at the very beginning of the <br>year. A couple days later, Mars moves on to adventurous, knowledge seeking Sagittarius, but for those first <br>two days you are untouchable! Mars in Aries, the other sign in rules, packs another great punch when they <br>team up at the end of June, but it could also cause you to be impatient and self centered, which are not two <br>inherent Scorpio qualities."
        second="Ambition takes you far. Hardworking Saturn is comfortable traveling with serious Capricorn, the sign it rules,<br> at the start of the year, and this is good news for ambitious Scorpios who have career goals they want to<br> reach by 2021. The actions you already put into play should be coming along well, and anything new you start<br> now will have a good chance of success."
    if form.getvalue("sign")=="sag":
        sign="Sagittarius"
        personal="As the fiery archer, your outgoing, adventerous nature is backed by your power planet, optimistic Jupiter. This <br>year, Jupiter is paired up with serious Capricorn again, so the modd still is not that light. Your good luck is <br>directly tied to your actions this year, essentially ensuring that you make your own luck by working hard and <br>actively shaping your own future. A retrograde period from the middle of May to September gives you a <br>chance to review your goals, and reconsider some of your opnions or ideals."
        second="Getting a jump on financial issues now can save you time and money in the future. The Saturn Capricorn<br> pairing was made at the end of 2017, so you have likely spent the past couple years working steadily towards <br>your goals. Yes, there will have been setbacks, but you should be on track to getting rewarded for the work <br>you have put in lately."
    if form.getvalue("sign")=="cap":
        sign="Capricorn"
        personal="Combine the old with the new to be more successful this year. Your home planet Saturn arrived in your <br>practical sign back in December of 2017, and countinues that trip for part of this year as well. You should be <br>especially focused on your goals now and may be particularly in tune with your ultimate purpose in life. You <br>must be willing to make changes to meet your full potential, but a hardworking Goat is never afraid to do <br>whatever it takes to climb to the top."
        second="Your home planet Saturn rules your drive and motivation, and because it is traveling in your steady sign for <br>the first three months of the year, you have ambitious galore. In other words, work your butt off now and you <br>will see the rewards eventually. There is little question about your dedication, and it would be a huge suprise <br>if you were not financially rewarded for your efforts at work."
    if form.getvalue("sign")=="aqua":
        sign="Aquarius"
        personal="This new year is full of changes and challenges! Your home planet, Uranus, made a big move into steady <br>Taurus last year, and these two very different energies are not the best of friends. Uranus is experimental <br>and Taurus likes to take a conservative approach, so there will be some mismatched energy to deal with now.<br> The retrograde period for your power planet this year is from mid August until the end of the year, which <br>should give you a slight break from the need for outward rebellion. Turning that rebellious streak inward,<br> however, can create its own set of issues, so be prepared for inner battles that can lead you down the path to <br>self destrucition and redemption this year."   
        second="Be true to yourself and the money will follow. Responsible Saturn is in hardworking Capricorn for the first <br>three months of the year, creating a good environment for you to work hard earning money and gaining <br>recognition that could lead up to future promotions and career opportunities. When Saturn makes a big move <br>into your humanitarian sign towards the end of March, however, you want to break free from traditional <br>career restrictions. A normal 9 to 5 job is about the last thing that appeals to you, so if that is what you are <br>stuck in you will aim to break free into a career that will let you do more of your own thing."
    if form.getvalue("sign")=="pisces":
        sign="Pisces"
        personal="A mix of illusion and reality shapes your year. Your home planet Neptune supports your idealistic approach to <br>life, and because it is traveling in your escapist sign all year, this is the time to really dream big. Pay <br>attention to intuition and visions, your subconcious is an accurate window into your soul and what you truly <br>want this year."
        second="Take advantage of every opportunity that comes your way. Venus guides your love life but she also rules over <br>money, and because she enters steady Taurus, the sign that knows how to make that dough more that almost <br>any other sign, at the beginning of March, this is a good time to pay attention to your finances. If you have <br>been lucky enough to save up a little nest egg, this is the perfect time for investing in a big ticket luxury<br> item. The Bull is an excellent saver but this energy also tells you to reward yourself when you deserve it."
    try:
        HTML=HTML.replace("??sign??", sign)
        HTML=HTML.replace("??personal??", personal)
        HTML=HTML.replace("??career??", second)
    except:
        pass
    if form.getvalue("done")=="Find Out":
        print(HTML)

horoscope()
    
    
