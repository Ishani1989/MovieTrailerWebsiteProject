import json
import display_movie_website
import media
from media import Movie


# Store the file containing source JSON data
file_directory = "D:\Ishani_study\Udacity\NanoDegree\PythonFiles\Project_Movie_Trailer_Website\movienames.json"  # NOQA 564


# load the JSON data into module
with open(file_directory) as data_file:
    data = json.load(data_file)
    print type(data)

# loop for each movie details in the JSON list.
    movies = [Movie(**movie) for movie in data]
    display_movie_website.open_movies_page(movies)
