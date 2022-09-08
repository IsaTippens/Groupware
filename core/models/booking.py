from core.models import Movie

class Booking:
    def __init__(self):
        self.id = 0
        self.seats: list[str] = []
        self.movie: Movie = None
        self.time: str = ""
        self.owner: str = ""
        self.date: str = ""