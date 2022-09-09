
from core.viewmodels import Movie


class Ticket:
    def __init__(self):
        self.id:int = 0
        self.seats: list[str] = []
        self.movie: Movie = None
        self.time: str = ""
        self.date: str = ""
        self.owner: str = ""
    
    def __str__(self):
        return f"Ticket {self.id} for {self.movie} at {self.time} for {self.owner} with {self.seats}"