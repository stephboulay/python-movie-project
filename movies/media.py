import webbrowser


# create a new class called Movie with constructors init and show trailer
class Movie ():
    """
    Class object stores movie related information
    """
    def __init__(
                self, movie_title, movie_storyline, poster_image,
                trailer_youtube):
        """
        Initialize instance of class Movie

        :param movie_title:
        :param movie_storyline:
        :param poster_image:
        :param trailer_youtube:
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Initializing instance for opening the youtube video

        :return: webbrowser to play trailer
        """
        webbrowser.open(self.trailer_youtube_url)
