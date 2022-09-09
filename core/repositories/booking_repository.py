from core.repositories.repository import Repository
from core.models import Movie, Booking
from core.utils import load_json, save_json

class BookingRepository(Repository):
    def __init__(self, bookingsFile: str):
        """
            bookings.json:
            {
                1: {
                    "id": 1,
                    "movie": "The Matrix",
                    "movietype": 1
                    "date": "2021-01-01",
                    "time": "12:00",
                    "owner": "John Doe",
                    "seats": ["A1"],
                }
            }
        """
        self.bookingsFile = bookingsFile
        self.bookings: dict = {}
        self._init()

    def _init(self):
        with open(self.bookingsFile, 'r') as f:
            data = load_json(f)
            for booking in data.values():
                booking = self._convert_from_json(booking)
                self.bookings[booking.id] = booking
        
    def get_all(self) -> list[Booking]:
        return [x for x in self.bookings.values()]

    def get(self, id: int) -> Movie:
        return self.bookings.get(id, None)

    def get_next_id(self) -> int:
        keys = list(self.bookings.keys())
        if len(keys) == 0:
            return 1
        max_id = keys[0]
        for key in keys:
            if key > max_id:
                max_id = key
        return max_id + 1

    def add(self, value: Booking):
        t_id = self.get_next_id()
        value.id = t_id
        self.bookings[t_id] = value
        self._save()
    
    def _save(self):
        result = {}
        for booking in self.bookings.values():
            result[booking.id] = self._convert_to_json(booking)
        save_json(self.bookingsFile, result)
    
    def update(self, value: Booking):
        booking = self.bookings.get(value.id, None) 
        if booking is not None:
            self.bookings[value.id] = value
            self._save()
    
    def delete(self, value: Movie):
        self.bookings.pop(value.id, None)
        self._save()
    
    def _convert_from_json(self, booking: dict):
        movie = Movie()
        movie.name = booking["movie"]
        movie.type = booking["movietype"]
        booking = Booking()
        booking.id = booking["id"]
        booking.movie = movie
        booking.date = booking["date"]
        booking.time = booking["time"]
        booking.owner = booking["owner"]
        booking.seats = booking["seats"]
        return booking

    def _convert_to_json(self, booking: Booking):
        return {
            "id": booking.id,
            "movie": booking.movie.name,
            "movietype": booking.movie.type,
            "date": booking.date,
            "time": booking.time,
            "owner": booking.owner,
            "seats": booking.seats
        }