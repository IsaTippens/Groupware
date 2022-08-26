from core.repositories import MovieRepository


class TestMovieRepository(MovieRepository):
    def __init__(self):
        self.movies: list[dict] = []
        self._init()

    def _init(self):
        self.movies = [
            {
                'name': 'Avengers 5',
                'type': 1,
                'description': 'Thanos returns',
            },
            {
                'name': 'Avengers 4',
                'type': 1,
                'description': 'Thor returns',
            }]

    def _save_movies(self):
        pass
