# Canada Foxes - Deven Maheshwari, Emma Buller, Lucas Lee, Naomi Naranjo
# SoftDev
# P01 - ArRESTed Development
# 2022-01-04

from flask import render_template, redirect, request, url_for, session
from app import app, imdb, nyt_review, spotify
from datetime import datetime
import urllib.request
import json
import sqlite3
from app import db

DB_FILE = "MusicalMovies.db"

@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    if session.get('username') is not None:
        user_id = db.get_id(session["username"])
        user = session['username']
        return render_template("homepage.html", user=user)

    else:

        return render_template("homepage.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if "username" in session:
        return redirect(url_for("index"))

    # GET request: display the form
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":

        # POST request: handle the form response and redirect
        username = request.form.get("name", default="")
        password = request.form.get("password", default="")
        password2 = request.form.get("password2", default="")

        error = db.signup(username, password)
        if password != password2:
            error = "Error: Passwords Must Match"


        if error:
            return render_template("register.html", error=error)
        else:
            db.signup(username, password)
            return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if "username" in session:
        return redirect(url_for("index"))

    # GET request: display the form
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":

        # POST request: handle the form response and redirect
        username = request.form.get("name", default="")
        password = request.form.get("password", default="")

        error = db.login(username, password)
        if error:
            return render_template('login.html', error=error)
        else:
            session['username'] = username
            return redirect(url_for("index"))


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if "username" in session:
        del session["username"]
    return redirect(url_for("index"))


@app.route("/search", methods=["GET", "POST"])
def search():
    if "username" not in session:
        return redirect(url_for("index"))


    # GET request: display the form
    if request.method == "GET":
        return render_template("search.html")

    # POST request: handle the form response and redirect
    if request.method == "POST":
        movie_title = request.form.get("title", default="")
        movie_year = request.form.get("year", default="")

        try:
            if movie_year != "":
                m = imdb.findMovieYear(movie_title, movie_year)
                p = imdb.plotsYear(movie_title, movie_year)
            else:
                m = imdb.findMovie(movie_title)
                p = imdb.plots(movie_title)
            if (len(m['results']) == 0):
                return render_template("Error.html", message="Movie Does Not Exist")

        except(Exception):
            return render_template("Error.html", message="API error")


        return render_template("moviesearch.html", length=len(m['results']), movies=m, plots=p)


@app.route("/results/<id>", methods=["GET"])
def results(id):
    if "username" not in session:
        return redirect(url_for("index"))

    username = session['username']
    user_id = db.get_id(username)

    # GET request: display the form
    if request.method == "GET":
        try:
            m = imdb.getMovieInfo(id)
            r = imdb.metacriticReviews(id)


            nyt = nyt_review.search_movie_review(m['title'])
            nyt_text = nyt_review.get_review_text(nyt['link']['url'])

            soundtrack, albums, related_artists, recs = spotify.return_all_spotify(m['title'])

        except(Exception):
            return render_template("Error.html", message="API error")

        finally:

            db.new_search(m['title'], user_id, id)

            return render_template("movieinfo.html", movie=m, reviews=r, soundtrack=soundtrack, albums=albums, related_artists=related_artists, recs=recs, nyt=nyt, nyt_text=nyt_text[:3])


@app.route("/profile", methods=["GET"])
def profile():
    if "username" not in session:
        return redirect(url_for("index"))

    username = session['username']
    user_id = db.get_id(username)

    # GET request: display the form
    if request.method == "GET":
        searches = db.get_user_searches(user_id)

        return render_template("profile.html", searches=searches)


@app.errorhandler(404)
def error_handler(e):
    return render_template('404.html'), 404

@app.errorhandler(503)
def error_handler(e):
    return render_template('503.html'), 503


if __name__ == "__main__":
    app.debug = True
    app.run()
