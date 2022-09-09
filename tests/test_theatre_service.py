from core.enums import MovieType
from core.services import TheatreService
from core.repositories.test_theatre_repository import TestTheatreRepository
from core.viewmodels import Theatre, Movie, Ticket

repo = TestTheatreRepository()
service = TheatreService(repo)

def test_get():
    """
        Test getting a known theatre that does exist
    """
    movie = Movie("Avengers 5", "", MovieType.BASIC2D)

    theatre = service.get(movie, "2022-05-01", "2PM")
    assert theatre.seats[1][1] == True

def test_get_none():
    """
        Test getting a theatre that does not exist
    """
    movie = Movie("Avengers 5", "", MovieType.BASIC2D)
    theatre = service.get(movie, "2022-05-01", "3PM")
    assert theatre.seats[0][0] == False

def test_add():
    """
        Test adding a new theatre
    """
    movie = Movie("Avengers 5", "", MovieType.BASIC2D)
    theatre = Theatre("Avengers 5", "2022-08-01", "12PM")
    theatre.seats = [[True, False, True]]
    service.add(theatre)
    new_theatre = service.get(movie, "2022-08-01", "12PM")
    assert new_theatre.seats == [[True, False, True]]

def test_update():
    """
        Test updating a theatre
    """
    movie = Movie("Avengers 8", "", MovieType.BASIC2D)
    theatre = Theatre("Avengers 8", "2022-08-01", "12PM")
    theatre.seats = [[True, False, True]]
    service.add(theatre)
    theatre.seats = [[False, False, False]]
    service.update(theatre)
    new_theatre = service.get(movie, "2022-08-01", "12PM")
    assert new_theatre.seats == [[False, False, False]]

def test_register():
    movie = Movie("Avengers 9", "", MovieType.BASIC2D)
    ticket = Ticket()
    ticket.movie = movie
    ticket.date = "2022-08-01"
    ticket.time = "12PM"
    ticket.seats = ["C1", "C2", "C3"]
    service.register_ticket(ticket)
    theatre = service.get(movie, ticket.date, ticket.time)
    assert theatre.seats[2][0] == True

def test_update_theatre():
    """
        Test updates to a person's ticket

        A ticket must have the same movie but can have a new date, time or seats
    """
    movie = Movie("Avengers 10", "", MovieType.IMAX3D)
    ticket = Ticket()
    ticket.movie = movie
    ticket.date = "2022-08-01"
    ticket.time = "12PM"
    ticket.seats = ["C1", "C2", "C3"]
    service.register_ticket(ticket)
    new_ticket = Ticket()
    new_ticket.movie = movie
    new_ticket.date = "2022-08-02"
    new_ticket.time = "3PM"
    new_ticket.seats = ["A1", "A2", "A3"]
    service.update_theatre(new_ticket, ticket)
    old_theatre = service.get(movie, ticket.date, ticket.time)
    theatre = service.get(movie, new_ticket.date, new_ticket.time)
    assert theatre.seats[0][0] == True and old_theatre.seats[2][0] == False

