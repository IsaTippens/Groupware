from app.screen.screen import Screen

class TitledScreen(Screen):
    def __init__(self, title: str = "Default"):
        super().__init__()
        self.title = title

    def print_border(self):
        print("-" * 25)

    def start(self):
        print("\n")
        self.print_border()
        print(self.title, "Page")
        self.print_border()