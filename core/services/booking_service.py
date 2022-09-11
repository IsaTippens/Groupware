from core.services.service import Service
from core.models import Booking
from core.viewmodels import Ticket as TicketView
from core.repositories import BookingRepository
from core.utils import conversions

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
        return [conversions.booking_model_to_view(x) for x in tickets]

    def get(self, id: int) -> TicketView:
        booking = self.repository.get(id)
        if booking is not None:
            return conversions.booking_model_to_view(booking)
        return TicketView()

    def add(self, value: TicketView):
        booking = conversions.booking_view_to_model(value)
        self.repository.add(booking)
        pass

    def update(self, value: TicketView):
        booking = conversions.booking_view_to_model(value)
        self.repository.update(booking)
        pass

    def register_ticket(self, ticket: TicketView):
        t_id = self.repository.get_next_id()
        ticket.id = t_id
        self.add(ticket)
        pass

    def deregister_ticket(self, ticket: TicketView):
        booking = self._to_model(ticket)
        self.delete(booking)
        pass

    def delete(self, value: Booking):
        self.repository.delete(value)
        pass

