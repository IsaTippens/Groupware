from app.screen.screen import Screen
class ScreenManager():
    def __init__(self):
        self.screens: list[Screen] = []
        pass

    def addScreen(self, screen: Screen):
        self.screens.append(screen)
        pass

    def start(self):
        super().start()
        while len(self.screens) > 0:
            current = self.screens[-1]
            current.next = None
            current.start()
            
            if current.pop:
                current.previous_screen.next = None

            if current.next is not None:
                print("Adding ", current.next)
                self.addScreen(current.next)
                continue
            self.screens.pop()
        print("Exiting")