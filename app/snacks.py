from app.payment import Payment
from app.screen.titled_screen import TitledScreen

from app.globals import State

class Snacks(TitledScreen):
    def __init__(self):
        super().__init__("Snacks")
    def start(self):
        super().start()
        snacks = []
        while(True):
            print("Select snack:")
            print("1\tPopcorn")
            print("2\tCandy")
            print("3\tSlushie")
            print("4\tCancel")
            print()
            num = input("Enter a number: ")
            if num == "1":
                snacks.append("Popcorn")
            if num == "2":
                snacks.append("Candy")
            if num == "3":
                snacks.append("Slushie")
            if num == "4":
                State["TICKET"].snacks = snacks
                break
                
        return self.navigate(Payment()) 
