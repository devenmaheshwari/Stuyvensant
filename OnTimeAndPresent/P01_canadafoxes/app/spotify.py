# Canada Foxes - Deven Maheshwari, Emma Buller, Lucas Lee, Naomi Naranjo
# SoftDev
# P01 - ArRESTed Development
# 2022-01-04

import sqlite3
import requests
import base64
import random
import os
from dotenv import load_dotenv

from flask import render_template, redirect, request, url_for, session, Flask

# load_dotenv()
# ID = os.getenv('SPOTIFY_ID')
# SECRET = os.getenv('SPOTIFY_SECRET')

with open('app/keys/key_spotify.txt') as f:
        ID = f.readline().strip()
        SECRET = f.readline().strip()


URL = 'https://api.spotify.com/v1'
TOKEN = ''


# Gets token based on a client id and secret
def get_token(client_id, client_secret):
    try:
        encoded = f'{client_id}:{client_secret}'
        encoded = base64.urlsafe_b64encode(encoded.encode()).decode()

        r = requests.post(url='https://accounts.spotify.com/api/token',
            headers={'Authorization' : f'Basic {encoded}', 'Content-Type': 'application/x-www-form-urlencoded'},
            data={'grant_type': 'client_credentials'}
        )

        json = r.json()
        token = json['access_token']

        return token
    except:
        pass

# Finds a soundtrack album based on a search
# Returns a python dictionary containing information on the album
def search_movie_soundtrack(query):

    r = requests.get(url=f'{URL}/search',
        headers={'Authorization' : f'Bearer {TOKEN}', 'Content-Type': 'application/json'},
        params={'q': query, 'type': 'album', 'limit': 2}
    )

    json = r.json()
    return json['albums']['items'][0] # Gets only first result


# Gets other albums by the same artist given their id
def get_artist_albums(id):
    r = requests.get(url=f'{URL}/artists/{id}/albums',
        headers={'Authorization' : f'Bearer {TOKEN}', 'Content-Type': 'application/json'},
    )

    json = r.json()
    return list({album['name']:album for album in json['items']}.values()) # Filters out repeat albums

# Gets artists related to some artist given thier id
def get_related_artists(id):
    r = requests.get(url=f'{URL}/artists/{id}/related-artists',
        headers={'Authorization' : f'Bearer {TOKEN}', 'Content-Type': 'application/json'},
    )

    json = r.json()
    return json['artists'] # Returns artist information dictionary

# Gets songs related to that of the songs in an album, given the album id
def get_related_tracks(id):

    r = requests.get(url=f'{URL}/albums/{id}/tracks',
        headers={'Authorization' : f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
    )

    json = r.json()
    tracks = json['items'] # Gets all the tracks in the album

    # Gets random songs to sample
    # Spotify has a limit of 5 songs to base reccomendations on
    sample = random.sample(tracks, 5)
    sample = [track['id'] for track in sample]
    sample = ','.join(sample) # Turns id list into a comma separated list

    r = requests.get(url=f'{URL}/recommendations',
        headers={'Authorization' : f'Bearer {TOKEN}', 'Content-Type': 'application/json'},
        params={'seed_tracks': sample}
    )

    json = r.json()
    ids = ','.join([track['id'] for track in json['tracks']]) #Gets all the track ids that the reccomendations request returned

    r = requests.get(url=f'{URL}/tracks',
        headers={'Authorization' : f'Bearer {TOKEN}', 'Content-Type': 'application/json'},
        params={'ids': ids}
    )

    json = r.json()
    return json['tracks'] # Returns array of track dictionaries


# Combines all the information needed to display spotify info
def return_all_spotify(search):
    try:
        soundtrack = search_movie_soundtrack(search)
        artist = soundtrack['artists'][0]

        recs = get_related_tracks(soundtrack['id'])
        albums = get_artist_albums(artist['id'])
        related_artists = get_related_artists(artist['id'])

        return (soundtrack, albums, related_artists, recs)
    except:
        pass

# Gets and sets token constant
TOKEN = get_token(ID, SECRET)


# app = Flask(__name__)
#
# @app.route('/')
# def test_spotify():
#
#     soundtrack, albums, related_artists, recs = return_all_spotify('Black Panther')
#     return render_template('spotify.html', soundtrack=soundtrack, albums=albums, related_artists=related_artists, recs=recs)


if __name__ == '__main__':

    app.debug = True
    app.run()
