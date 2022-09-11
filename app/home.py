from app.screen.titled_screen import TitledScreen
from app.movies import MovieScreen
from app.staff import StaffScreen

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

        while True:
            num = input("Enter a number (Enter \"exit\" to exit): ")
            if num == "1":
                return self.navigate(MovieScreen())
            if num == "2":
                self.goBack()
            if num == "3":
                return self.navigate(StaffScreen())
            if num == "exit":
                return
            print("Invalid option")

