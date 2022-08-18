from enum import Enum

class MovieType(Enum):
    BASIC2D = 1
    BASIC3D = 2
    IMAX2D = 3
    IMAX3D = 4


class Movie:

    def __init__(self, id: int, name: str, movieType : MovieType = MovieType.BASIC2D):
        self.id = id
        self.name = name
        self.type = movieType
        pass