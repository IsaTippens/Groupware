from __future__ import annotations
from abc import ABCMeta, abstractmethod
from app.screen.screen_interface import ScreenInterface


class Screen(ScreenInterface):
    def __init__(self):
        self.previous_screen: Screen = None
        self.next: Screen = None
        self.pop = False

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def navigate(self, to: Screen):
        self.next = to
        to.previous_screen = self

    @abstractmethod
    def goBack(self):
        self.pop = True
