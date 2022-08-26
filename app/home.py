from app.screen.titled_screen import TitledScreen
from app.Test import Test
from app.movies import MovieScreen

class Home(TitledScreen):
    def __init__(self):
        super().__init__("Home")
    def start(self):
        super().start()
        print("Enter 1 to navigate to the next screen")
        print("Enter 2 to navigate to the movie screen")
        num = input("Enter a number: ")
        if num == "1":
            return self.navigate(Test())
        if num == "2":
            return self.navigate(MovieScreen())

