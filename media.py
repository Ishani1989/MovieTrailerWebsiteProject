import webbrowser


# class defining functions and attributes for movie website
class Movie():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

# attributes for movie info that will be fetched dynamically and used on our website
    def __init__(self, movie_title, movie_storyline, poster_image, movie_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = movie_url

# play the youtube video URL for the movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
