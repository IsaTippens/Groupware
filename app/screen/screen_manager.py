from app.screen.screen import Screen
class ScreenManager():
    def __init__(self):
        self.screens: list[Screen] = []
        pass

    def addScreen(self, screen: Screen):
        self.screens.append(screen)
        pass

    def start(self):
        """
            Magic starts here

            We start with the first screen in the stack, if any

            Once a screen's start function ends, we arrive back here.
            We check for any properties that have been set by the screen and act accordingly

            If there is a new screen in the next attribute, add it to the screens stack and start it

            If the current screen requests to go to the root screen, we set the screens stack to just the first screen

            Otherwise pop the current screen and loop again
        
        """
        while len(self.screens) > 0:
            current = self.screens[-1]
            current.next = None
            current.start()
            
            if current.pop:
                if (current.previous_screen != None):
                    current.previous_screen.next = None

            if current.next is not None:
                self.addScreen(current.next)
                continue

            if current.goToRoot == True:
                self.screens = [self.screens[0]]
                continue

            self.screens.pop()
        print("Exiting")