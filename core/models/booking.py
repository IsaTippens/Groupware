from core.models import Movie

class Booking:
    def __init__(self):
        self.seats = []
        self.movie = None
        self.time = ""
    
    def create(self, movie: Movie, seats: list[str], time: str):
        self.seats = seats
        self.movie = movie
        self.time = time