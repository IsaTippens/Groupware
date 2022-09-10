from core.services.booking_service import BookingService
from core.repositories.test_booking_repository import TestBookingRepository
from core.viewmodels import Ticket, Movie

bookService = BookingService(TestBookingRepository())

def test_get_all():
    tickets = bookService.get_all()
    assert tickets[1].id == 2

def test_get():
    ticket = bookService.get(2)
    assert ticket.owner == "Rogers"

def test_get_id():
    ticket = bookService.get(1)
    assert ticket.id == 1

def test_update():
    import copy
    currentTicket = bookService.get(2)
    ticket = copy.deepcopy(currentTicket)
    ticket.seats = ["C1", "C2"]
    bookService.update(ticket)
    updatedTicket = bookService.get(2)
    assert updatedTicket.seats == ["C1", "C2"] and currentTicket.seats == ["A1", "A2"]

def test_register():
    movie = Movie("Avengers 5", "")
    ticket = Ticket()
    ticket.movie = movie
    ticket.seats = ["A1", "A2"]
    ticket.time = "2PM"
    ticket.owner = "Steve"
    ticket.id = -1
    bookService.register_ticket(ticket)
    assert ticket.id != -1
