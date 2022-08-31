from typing import Any
from core.repositories import MovieRepository as MR
from core.services import MovieService as MS

"""
    Global Singletons to be used by the screens

    'X'Service should be the class that you use to interact with the data
    see app/movies.py for an example of how to use this class

    There will be more services added to handle bookings, seats available, anything to make life hopefully easier :)
"""
MovieService = MS(MR("data/movies.json"))

State = dict[str, Any]()