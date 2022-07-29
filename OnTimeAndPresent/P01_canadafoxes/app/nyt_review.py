# Canada Foxes - Deven Maheshwari, Emma Buller, Lucas Lee, Naomi Naranjo
# SoftDev
# P01 - ArRESTed Development
# 2022-01-04

import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

from flask import render_template, redirect, request, url_for, session, Flask

# load_dotenv()
# KEY = os.getenv('NYT_KEY')

with open('app/keys/key_nyt.txt') as f:
        KEY = f.readline().strip()

URL = 'https://api.nytimes.com/svc/movies/v2'

# Gets the text paragraphs of a particular NYT Review page
def get_review_text(url):

    # In case there is an error with the API or the parsing
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser") # Library to parse html page
        review = soup.find_all("div", class_="StoryBodyCompanionColumn") # All content divs are tagged with this class

        # Concatenate all the paraagraphs into a list
        paragraphs = []
        for section in review:
            tags = section.find_all("p")
            paragraphs.extend([p.text for p in tags])

        return paragraphs # Array of paragraphs in the article
    except:
        paragraphs = []
        return paragraphs

# Make NYT Review query based on movie title
def search_movie_review(query):
    r = requests.get(url=f'{URL}/reviews/search.json',
        params={'api-key': KEY,'query': query}
    )

    json = r.json()
    return json['results'][0] # Only take first result

if __name__ == '__main__':
    review = search_movie_review('Black Panther')
    text = get_review_text(review['link']['url'])

    print(review)
