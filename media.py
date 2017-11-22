import webbrowser
#Construct the class Movie to store common details of each movie.
class Movie():
    '''Initialize a space to remember information of title, storyline, poster image, and trailor link.
    '''
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    '''Open the webbrowser and play the trailer whenever the user clicks on the movie.
    '''
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
