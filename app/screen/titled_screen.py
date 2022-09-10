from app.screen.screen import Screen

class TitledScreen(Screen):
    def __init__(self, title: str = "Default", extra: str = "Page"):
        super().__init__()
        self.title = title
        self.extra = extra

    def print_border(self):
        print("-" * 25)

    def start(self):
        print("\n")
        self.print_border()
        print(self.title, self.extra)
        self.print_border()