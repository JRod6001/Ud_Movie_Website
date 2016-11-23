import webbrowser


# class definition holds movie data, and opens trailer
class Movie():
    """ This is some documentation for Movie()"""
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trialer_youtube):
        # creates instance object containing movie information and content link
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trialer_youtube

    def show_trailer(self):
        # opens movie trailer URL in a window
        webbrowser.open(self.trailer_youtube_url)
