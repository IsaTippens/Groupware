from core.enums import MovieType
class Movie:

    def __init__(self, name: str ="", description: str="", movieType : MovieType = MovieType.BASIC2D):
        self.name = name
        self.description = description
        self.type = movieType
        pass

    def __str__(self):
        return f'{self.name} {self.description} {self.type}'