from core.utils import conversions
from core.enums import MovieType
from core.models import Movie, Booking, Theatre, theatre
from core.viewmodels import Movie as MovieView, Ticket as TicketView, Theatre as TheatreView

movie = Movie("Avengers 5", "Thanos returns", 1)
movieView = MovieView("Avengers 5", "Thanos returns", MovieType.BASIC2D)

booking = Booking()
booking.id = 1
booking.movie = movie
booking.date = "2020-01-01"
booking.time = "10:00"
booking.owner = "John"
booking.seats = ["A1", "A2"]
booking.snacks = ["Popcorn", "Coke"]

ticketView = TicketView()
ticketView.id = 1
ticketView.movie = movieView
ticketView.date = "2020-01-01"
ticketView.time = "10:00"
ticketView.owner = "John"
ticketView.seats = ["A1", "A2"]
ticketView.snacks = ["Popcorn", "Coke"]

theatre = Theatre()
theatre.movie = "Avengers 5"
theatre.date = "2020-01-01"
theatre.time = "10:00"
theatre.seats = ["A1", "A2"]
theatreView = TheatreView()
theatreView.movie = "Avengers 5"
theatreView.date = "2020-01-01"
theatreView.time = "10:00"
theatreView.seats = ["A1", "A2"]

def test_movie_model_to_view():
    temp = conversions.movie_model_to_view(movie)
    assert temp.name == "Avengers 5" and temp.type == MovieType.BASIC2D and temp.description == "Thanos returns"

def test_movie_view_to_model():
    temp = conversions.movie_view_to_model(movieView)
    assert temp.name == "Avengers 5" and temp.type == 1 and temp.description == "Thanos returns"

def test_booking_model_to_view():
    temp = conversions.booking_model_to_view(booking)
    assert temp.id == 1 and temp.owner == "John" and temp.date == "2020-01-01" and temp.time == "10:00" and temp.seats == ["A1", "A2"] and temp.snacks == ["Popcorn", "Coke"]

def test_booking_view_to_model():
    temp = conversions.booking_view_to_model(ticketView)
    assert temp.id == 1 and temp.owner == "John" and temp.date == "2020-01-01" and temp.time == "10:00" and temp.seats == ["A1", "A2"] and temp.snacks == ["Popcorn", "Coke"]

def test_theatre_model_to_view():
    temp = conversions.theatre_model_to_view(theatre)
    assert temp.movie == "Avengers 5" and temp.date == "2020-01-01" and temp.time == "10:00" and temp.seats == ["A1", "A2"]

def test_theatre_view_to_model():
    temp = conversions.theatre_view_to_model(theatreView)
    assert temp.movie == "Avengers 5" and temp.date == "2020-01-01" and temp.time == "10:00" and temp.seats == ["A1", "A2"]