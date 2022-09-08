from core.services.service import Service
from core.repositories import TheatreRepository
from core.models import Movie, Theatre, theatre
from core.enums import MovieType
from core.viewmodels import Movie as MovieView, Ticket as TicketView, Theatre as TheatreView
from core.utils import conversions, TheatreUtils
class TheatreService(Service):
    def __init__(self, repository: TheatreRepository):
        self.repository = repository
        pass

    def get_all(self):
        pass

    def get(self, movie: MovieView, date: str, time: str) -> TheatreView:
        theatre = self.repository.get(movie.name, date, time)
        if theatre.seats is None:
            theatre.seats = self.generate_seats_for_movie(conversions.movie_view_to_model(movie))
        return conversions.theatre_model_to_view(theatre)

    def add(self, theatre: Theatre):
        self.repository.add(theatre)

    def update(self, theatre: Theatre):
        self.repository.update(theatre)
        pass

    def update_theatre(self, value: TicketView, old: TicketView):
        self.deregister_ticket(old)
        self.register_ticket(value)

    def register_ticket(self, ticket: TicketView):
        movie = ticket.movie
        theatre = self.get(movie, ticket.date, ticket.time)
        for seat in ticket.seats:
            row, col = TheatreUtils.split_seat(seat)
            row_index = TheatreUtils.letter_to_index(row)
            col_index = col - 1
            theatre.seats[row_index][col_index] = True
        self.update(theatre)

    def deregister_ticket(self, ticket: TicketView):
        movie = ticket.movie
        theatre = self.get(movie, ticket.date, ticket.time)
        for seat in ticket.seats:
            row, col = TheatreUtils.split_seat(seat)
            row_index = TheatreUtils.letter_to_index(row) - 1
            col_index = col - 1
            theatre.seats[row_index][col_index] = False
        self.update(theatre)
        pass

    def delete(self, value: Theatre):
        self.repository.delete(value)
        pass

    def _type_to_rows(self, movietype: MovieType):
        if movietype in [MovieType.BASIC2D, MovieType.BASIC3D]:
            return 4
        elif movietype in [MovieType.IMAX2D, MovieType.IMAX3D]:
            return 6
        return 1

    def _type_to_cols(self, movietype: MovieType):
        if movietype in [MovieType.BASIC2D, MovieType.BASIC3D]:
            return 6
        elif movietype in [MovieType.IMAX2D, MovieType.IMAX3D]:
            return 10
        return 1

    def generate_seats_for_movie(self, movie: Movie) -> list[list[bool]]:
        rows = self._type_to_rows(movie.type)
        cols = self._type_to_cols(movie.type)
        seats = self.generate_seats(rows, cols)
        return seats

    def generate_seats(self, rows: int, cols: int) -> list[list[bool]]:
        seats: list[list[bool]] = []
        for i in range(1, rows):
            seats.append([False] * cols)
        return seats

