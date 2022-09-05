from core.repositories import MovieRepository
from core.models import Movie


class TestMovieRepository(MovieRepository):
    def __init__(self):
        self.movies: list[dict] = []
        self._init()

    def _init(self):
        self.movies = [
            Movie('Avengers 5', 'Thanos returns'),
            Movie('Avengers 4','Thor returns')]

    def _save(self):
        pass
