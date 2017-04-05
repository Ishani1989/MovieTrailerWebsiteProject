import json
import display_movie_website
import media
from media import Movie
import os

file_directory = os.getcwd() + "/movienames.json"

# load the JSON data into module
with open(file_directory) as data_file:
    data = json.load(data_file)
    print type(data)

# loop for each movie details in the JSON list.
    movies = [Movie(**movie) for movie in data]
    display_movie_website.open_movies_page(movies)
