from core.enums import MovieType
class Movie:

    def __init__(self, id: int, name: str, description: str, movieType : MovieType = MovieType.BASIC2D):
        self.id = id
        self.name = name
        self.description = description
        self.type = movieType
        pass