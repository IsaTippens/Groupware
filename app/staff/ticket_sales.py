from ast import Tuple
from app.screen.titled_screen import TitledScreen
from app.globals import State, MovieService, TheatreService, BookingService
from core.viewmodels import Ticket
from core.utils import TheatreUtils
from datetime import date


class TicketSales(TitledScreen):
    def __init__(self):
        super().__init__("Ticket", "Sales")

    def get_tickets_for_movie(self, tickets, movie, movie_date):
        result = []
        for ticket in tickets:
            if ticket.movie.name == movie.name and ticket.date == movie_date:
                result.append(ticket)
        return result

    def start(self):
        super().start()
        dt = str(date.today())
        print(f"Summary of sales for {dt}\n")
        movies = MovieService.get_all()
        tickets = BookingService.get_all()
        for movie in movies:
            movie_tickets = self.get_tickets_for_movie(tickets, movie, dt)
            times = {}
            for t in movie_tickets:
                count = times.get(t.time, 0)
                times[t.time] = count + 1
            print(f"Sales for {movie.name}:")
            if (len(times.keys()) == 0):
                print("None\n")
            else:
                t_keys = sorted(list(times.keys()))
                for k in t_keys:
                    print(f"{k}: {times[k]} ticket{'s' if times[k] != 1 else ''} sold")
                print("")

                
        return self.goBack()

