import webbrowser


# class Video():
#     
#     def __init__(self, title, duration):
#         self.title = title
#         self.duration = duration


class Movie():
    """ This is some bullshit documentation for Movie()"""
    VALID_RATINGS = ['G','PG','PG-13','R'] #each instance of this class has access to this constant
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trialer_youtube):
        # instance variables will be different across all classes 

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trialer_youtube
        
    def show_trailer(self): 
        webbrowser.open(self.trailer_youtube_url)
        
