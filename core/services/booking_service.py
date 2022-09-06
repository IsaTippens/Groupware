from core.services.service import Service
from core.models import Booking
from core.viewmodels import Ticket as TicketView
from core.repositories import BookingRepository

class BookingService(Service):
    def __init__(self, repository: BookingRepository):
        self.repository = repository
        pass

    def _to_viewmodel(self, booking: Booking) -> TicketView:
        bookingView = TicketView()
        bookingView.id = booking.id
        bookingView.movie = booking.movie
        bookingView.seats = booking.seats
        bookingView.time = booking.time
        bookingView.owner = booking.owner
        return bookingView
    
    def _to_model(self, bookingView: TicketView) -> Booking:
        booking = Booking()
        booking.id = bookingView.id
        booking.movie = bookingView.movie
        booking.seats = bookingView.seats
        booking.time = bookingView.time
        booking.owner = bookingView.owner
        return booking

    def get_all(self) -> list[TicketView]:
        tickets = self.repository.get_all()
        return [self._to_viewmodel(x) for x in tickets]

    def get(self, id: int) -> TicketView:
        booking = self.repository.get(id)
        if booking is not None:
            return self._to_viewmodel(booking)
        return TicketView()

    def add(self,value: TicketView):
        booking = self._to_model(value)
        self.repository.add(booking)
        pass

    def update(self, value: TicketView):
        booking = self._to_model(value)
        self.repository.update(booking)
        pass

    def delete(self, value: TicketView):
        booking = self._to_model(value)
        self.repository.delete(booking)
        pass

