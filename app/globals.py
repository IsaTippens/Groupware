from typing import Any
from core.repositories import MovieRepository as MR, BookingRepository as BR, TheatreRepository as TR
from core.services import MovieService as MS, BookingService as BS, TheatreService as TS


from core.viewmodels import Movie, Ticket

"""
    Global Singletons to be used by the screens

    'X'Service should be the class that you use to interact with the data
    see app/movies.py for an example of how to use this class

    There will be more services added to handle bookings, seats available, anything to make life hopefully easier :)
"""
MovieRepository = MR("data/movies.json")
MovieService = MS(MovieRepository)

BookingRepository = BR("data/bookings.json")
BookingService = BS(BookingRepository)

TheatreRepository = TR("data/theatres.json")
TheatreService = TS(TheatreRepository)

State = dict[str, Any]()
State["MOVIE"] = Movie()
State["TICKET"] = Ticket()
State["SECRET"] = "@BC321"
