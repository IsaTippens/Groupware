from core.repositories.repository import Repository
from core.models import Movie, Booking
from core.utils import load_json, save_json

class BookingRepository(Repository):
    def __init__(self, bookingsFile: str):
        self.bookingsFile = bookingsFile
        self.bookings: dict = {}
        self._init()

    def _init(self):
        with open(self.bookingsFile, 'r') as f:
            data = load_json(f)
            self.bookings = data
        
    def get_all(self) -> list[Booking]:
        return [x for x in self.bookings.values()]

    def get(self, id: int) -> Movie:
        return self.bookings.get(id, None)

    def add(self, value: Booking):
        self.movies.append(value)
        self._save()
    
    def _save(self):
        save_json(self.bookingsFile, self.bookings)
    
    def update(self, value: Booking):
        booking = self.bookings.get(value.id, None) 
        if booking is not None:
            self.bookings[value.id] = value
            self._save()
    
    def delete(self, value: Movie):
        self.bookings.pop(value.id, None)
        self._save()