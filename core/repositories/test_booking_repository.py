from core.repositories import BookingRepository
from core.models import Booking, Movie


class TestBookingRepository(BookingRepository):
    def __init__(self):
        self.bookings: dict = []
        self._init()

    def faker(self):
        aMovie = Movie("Avengers 5", "")
        result = {}
        a = Booking()
        a.id = 1
        a.movie = aMovie
        a.seats = ["A1", "A2"]
        a.time = "2PM"
        a.owner = "Steve"
        a.date = "2022-04-01"
        result[a.id] = a

        bMovie = Movie("Avengers 4", "")
        a = Booking()
        a.id = 2
        a.movie = bMovie
        a.seats = ["A1", "A2"]
        a.time = "2PM"
        a.owner = "Rogers"
        a.date = "2022-02-02"
        result[a.id] = a

        return result

    def _init(self):
        self.bookings = self.faker()

    def _save(self):
        pass
    
TestBookingRepository.__test__ = False