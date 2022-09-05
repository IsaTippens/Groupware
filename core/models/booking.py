from core.models import Movie

class Booking:
    def __init__(self):
        self.id = 0
        self.seats = []
        self.movie = None
        self.time = ""
        self.owner = ""
        self.date = ""