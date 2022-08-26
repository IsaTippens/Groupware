from core.enums import MovieType
class Movie:

    def __init__(self, id: int, name: str, movieType : MovieType = MovieType.BASIC2D):
        self.id = id
        self.name = name
        self.type = movieType
        pass