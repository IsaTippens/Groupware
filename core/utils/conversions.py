from core.models import Movie, Booking, Theatre
from core.viewmodels import Movie as MovieView, Ticket as TicketView, Theatre as TheatreView

def movie_view_to_model(movie: MovieView) -> Movie:
    return Movie(movie.name, movie.description, movie.type)

def movie_model_to_view(movie: Movie) -> MovieView:
    return MovieView(movie.name, movie.description, movie.type)

def booking_view_to_model(ticket: TicketView) -> Booking:
    booking = Booking()
    booking.id = ticket.id
    booking.movie = ticket.movie
    booking.date = ticket.date
    booking.time = ticket.time
    booking.date = ticket.date
    booking.owner = ticket.owner
    booking.seats = ticket.seats
    return booking

def booking_model_to_view(booking: Booking) -> TicketView:
    ticket = TicketView()
    ticket.id = booking.id
    ticket.movie = booking.movie
    ticket.date = booking.date
    ticket.time = booking.time
    ticket.date = booking.date
    ticket.owner = booking.owner
    ticket.seats = booking.seats
    return ticket

def theatre_view_to_model(theatre: TheatreView) -> Theatre:
    t = Theatre(theatre.movie, theatre.date, theatre.time)
    t.seats = theatre.seats
    return t

def theatre_model_to_view(theatre: Theatre) -> TheatreView:
    t = TheatreView(theatre.movie, theatre.date, theatre.time)
    t.seats = theatre.seats
    return t

