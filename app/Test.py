from app.screen.titled_screen import TitledScreen
from app.globals import State

class Test(TitledScreen):
    """
    Make sure to do
    ```
        return self.goBack()
        return self.navigate(Test())
    ```
    So that the function exits when navigating to the next screen.
    """
    def __init__(self):
        super().__init__("Test")

    def start(self):
        super().start()
        print("This is the test screen")
        print("Enter 1 to go back")
        print("Enter 2 to modify the state")
        num = input("Enter a number: ")
        if num == "1":
            return self.goBack()
        elif num == "2":
            State["test"] = input("Enter something: ")
            return self.goBack()