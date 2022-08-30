from app.screen.titled_screen import TitledScreen
from app.Test import Test
from app.movies import MovieScreen

class Home(TitledScreen):
    def __init__(self):
        super().__init__("Home")
    def start(self):
        super().start()
        print("Enter a number to select a screen")
        print("1\tMovies")
        print("2\tExit")

        num = input("Enter a number: ")
        if num == "1":
            return self.navigate(Test())
        if num == "2":
            return self.navigate(MovieScreen())

