from app.screen.screen_manager import ScreenManager
from app.home import Home
class App():
    """
        Our terminal app

        Default screen is the Home screen

        ScreenManager handles a stack of the currently used screens and can navigate forwards and backwards
    """
    def __init__(self):
        self.screen = None
    
    def start(self):
        self.manager: ScreenManager = ScreenManager()
        self.manager.addScreen(Home())
        self.manager.start()
        pass