from app.screen.screen_manager import ScreenManager
from app.home import Home
class App():
    def __init__(self):
        self.screen = None
    
    def start(self):
        self.manager: ScreenManager = ScreenManager()
        self.manager.addScreen(Home())
        self.manager.start()
        pass