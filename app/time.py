from app.screen.titled_screen import TitledScreen
from app.Select_seats import SelectSeatsScreen
from datetime import date 

from app.globals import State

class Times(TitledScreen):
    def __init__(self):
        super().__init__("Times")
    def start(self):
        super().start()
        print("Select a time:")
        print("1\t2pm")
        print("2\t5pm")
        print("3\t8pm")
        print("4\tCancel")
        print()

        State["TICKET"].date = str(date.today())
        num = input("Enter a number: ")
        if num == "1":
            State["TICKET"].time = "2PM"
        if num == "2":
            State["TICKET"].time = "5PM"
        if num == "3":
            State["TICKET"].time = "8PM"
        if num == "4":
            return self.goBack()
        return self.navigate(SelectSeatsScreen()) #should go to seating selection

       

