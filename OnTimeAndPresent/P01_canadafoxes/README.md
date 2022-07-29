# Musical Movies by Canada Foxes
Canada Foxes - Emma Buller, Lucas Lee, Naomi Naranjo, Deven Maheshwari Pd. 1 <br>
SoftDev <br>
P01: ArRESTed Development <br>

## Roster and Roles
Deven - PM; Backend routing, python <br>
Emma - IMDB and Movie Review API Backend, Frontend HTML <br>
Lucas - Spotify API Backend, Frontend CSS <br>
Naomi - Database management <br>

## Description
A website where users can enter and store searches on a movie title, showing information about the movie’s production/cast and critic reviews about the movie, based on Imdb and New York Times reviews). Generates 5 recommendations for songs based on the soundtrack album/artist using Spotify. Stores each movie search and subsequent suggestions for each user profile.  

## API KB
[1. Spotify API](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_Spotify.md)  
[2. MovieReviews API](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_MovieReviews.md)  
[3. Imdb API](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_imdb.md)

## Launch Codes
Be sure to have python3 and pip3 installed. 

1. Clone this repository.
```
$ git clone https://github.com/devenmaheshwari/canadafoxes.git
$ cd canadafoxes
```

2. Create a new virtual environment.
```
$ python3 -m venv env
$ . path/to/venv/bin/activate
```

3. Install project dependencies.
```
(env) $ pip3 install -r requirements.txt
```

4. Run the app.
```
(env) $ python canadafoxes.py
```

Access the web app by going to http://127.0.0.1:5000/
