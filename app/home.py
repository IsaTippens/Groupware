from app.screen.titled_screen import TitledScreen
from app.Test import Test
from app.movies import MovieScreen

from app.globals import State

class Home(TitledScreen):
    def __init__(self):
        super().__init__("Home")
    def start(self):
        super().start()
        
        print("Welcome to GO MOVIES.")
        print("Where you find Entertainment4Everyone")
        print("Enter a number to select a option number:")
        print("1\tMovies")
        print("2\tTicket Query")
        print("3\tStaff Page")

        num = input("Enter a number: ")
        if num == "1":
            return self.navigate(MovieScreen())
        if num == "2":
            return self.navigate()
        if num == "3":
            return self.navigate()

