# Canada Foxes - Deven Maheshwari, Emma Buller, Lucas Lee, Naomi Naranjo
# SoftDev
# P01 - ArRESTed Development
# 2022-01-04

import requests
import os
from dotenv import load_dotenv
from flask import render_template, redirect, request, url_for, session, Flask

# load_dotenv()
# KEY = os.getenv('IMDB_KEY')

with open('app/keys/key_imdb.txt') as f:
        KEY = f.readline().strip() #accessing key

url = "https://imdb-api.com/en/API/" #universal url for all calls

def findMovie(title): #gets basic movie info (poster, id) for a list of potential movies from a title input
    try:
        response = requests.get(url+ 'SearchMovie/' + KEY + '/' + title,
        )
        r = response.json()
        return r
    except: #catching errors from api key usage running out
        reponse = ""
        r = response.json()
        return r

def findMovieYear(title, year): #same thing as findMovie but with year input as well
    try:
        response = requests.get(url + 'SearchMovie/' + KEY + '/' + title
        + " " + year)
        r= response.json()
        return r
    except:
        reponse = ""
        r = response.json()
        return r

def getMovieInfo(id): #get the information about a specific movie
    response = requests.get(url + 'Title/'  + KEY + '/' + id + '/FullActor,FullCast,Trailer,Ratings,'
    )
    r = response.json()
    return r

def plots(title): #acquire plot summary from the initial list of movies from the initial search
    movies = findMovie(title)
    l = []
    for m in range(len(movies["results"])):
        movie = getMovieInfo(movies["results"][m]["id"])
        l.append(movie["plot"])
    return l

def plotsYear(title, year): #same thing as plots but with year input
        movies = findMovieYear(title, year)
        l = []
        for m in range(len(movies["results"])):
            movie = getMovieInfo(movies["results"][m]["id"])
            l.append(movie["plot"])
        return l

def metacriticReviews(id): #get reviews for a specific movie
    response = requests.get(url + 'MetacriticReviews/' + KEY + '/' + id)
    r = response.json()
    return r['items']

# print(metacriticReviews("tt1375666"))
app = Flask(__name__) #initial testing for accessing movie info

@app.route('/')
def test():
    # m = findMovieYear("inception","2010")
    # p = plotsYear("inception","2010")
    # return render_template("moviesearch.html", length=len(m['results']), movies=m,plots=p)
    m = getMovieInfo("tt1825683")
    r = metacriticReviews("tt1825683")
    return render_template("movieinfo.html", movie=m, reviews = r)
if __name__ == '__main__':
    app.debug = True
    app.run()
