from app.screen.titled_screen import TitledScreen
from app.Test import Test
from app.globals import MovieService
from app.globals import State
class MovieScreen(TitledScreen):
    def __init__(self):
        super().__init__("Movies")
    def start(self):
        super().start()
        print("Movies available:")
        count = 1
        for movie in MovieService.get_all():
            print("Theatre"+ str(count))
            print(movie.name)
            print(movie.description, "\n")
            count= count+1
        print("Enter theater number for the movie selection or 0 to return home:")
        num = int(input())
        Selection = MovieService.get_all()[num-1].name
        State["MOVIE"].name = Selection
        State["TICKET"].movie = State["MOVIE"].name
