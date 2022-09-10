
from core.viewmodels import Movie
from collections import Counter


class Ticket:
    def __init__(self):
        self.id:int = 0
        self.seats: list[str] = []
        self.movie: Movie = None
        self.snacks: list[str] = []
        self.time: str = ""
        self.date: str = ""
        self.owner: str = ""
    
    def __str__(self):
        seats = ""
        for idx, seat in enumerate(self.seats):
            seats += seat
            if idx < len(self.seats) - 1:
                seats += ", "
        snacks = "\nSnacks:"
        counter = Counter(self.snacks)
        snack_k = list(counter.keys())
        for key in snack_k:
            amount = counter[key]
            snacks += f"\n{amount}x {key}"
        return f"\n-----\nTicket #{self.id} for {self.movie.name} on {self.date} at {self.time}.\nSitting in {seats}.\nCustomer: {self.owner}{snacks}\n-----\n"