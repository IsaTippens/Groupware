from app.screen.titled_screen import TitledScreen
from app.Test import Test
from app.movies import MovieScreen
from app.time import Times

from app.globals import State

class Home(TitledScreen):
    def __init__(self):
        super().__init__("Home")
    def start(self):
        super().start()
        print("The state is: ", State.get("test", "Empty"))
        print()
        print("Enter a number to select a screen")
        print("1\tMovies")
        print("2\tTest state stuff")

        num = input("Enter a number: ")
        if num == "1":
            return self.navigate(MovieScreen())
        if num == "2":
            return self.navigate(Times())

