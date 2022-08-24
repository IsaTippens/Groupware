from app.screen.titled_screen import TitledScreen
from app.Test import Test

class Home(TitledScreen):
    def __init__(self):
        super().__init__("Home")
    def start(self):
        super().start()
        print("Enter 1 to navigate to the next screen")
        num = input("Enter a number: ")
        if num == "1":
            return self.navigate(Test())

