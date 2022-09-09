from app.screen.titled_screen import TitledScreen
from app.Test import Test
from app.movies import MovieScreen

from app.globals import State

class Times(TitledScreen):
    def __init__(self):
        super().__init__("Times")
    def start(self):
        super().start()
        print("The state is: ", State.get("test", "Empty"))
        print()
        print("Select a time:")
        print("1\t2pm")
        print("2\t5pm")
        print("3\t7pm")
        print("4\tCancel")
        print()

        num = input("Enter a number: ")
        if num == "1":
            State["TICKET"].time = "2pm"
        if num == "2":
            State["TICKET"].time = "5pm"
        if num == "3":
            State["TICKET"].time = "7pm"
        if num == "4":
            return self.goBack()
        return self.navigate(Test()) #should go to seating selection

       

