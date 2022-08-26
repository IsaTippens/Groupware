from app.screen.titled_screen import TitledScreen
from app.Test import Test
from app.globals import MovieService

class MovieScreen(TitledScreen):
    def __init__(self):
        super().__init__("Movies")
    def start(self):
        super().start()
        print("Movies available:")
        for movie in MovieService.get_all():
            print(movie.name)
            print(movie.description, "\n")
        print("Press enter to exit")
        num = input()

