import webbrowser
import fresh_tomatoes


class Movie():
    """ This is class documentation string..
    class instantiation calls init() and contructs the object.
    """
    VALID_RATINGS = ["P", "PG"]  # class variables

    def __init__(self, movie_title, movie_storyline, poster_img, youtube_url):
        """This is a class constructor.
        Assigns the data associated to the instance variables"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_img
        self.trailer_youtube_url = youtube_url
    """ show_trailer() docstring..
    This is an instance method associated to the instance created."""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
