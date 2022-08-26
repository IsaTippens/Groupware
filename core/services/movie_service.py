from core.services.service import Service
from core.models import Movie
from core.enums import MovieType
from core.viewmodels import Movie as MovieView
from core.repositories import MovieRepository
class MovieService(Service):
    def __init__(self, repository: MovieRepository):
        self.repository = repository
        pass

    def get_all(self) -> list[MovieView]:
        movies = self.repository.get_all()
        result = []
        for movie in movies:
            movieType = MovieType(movie.type)
            movieName = movie.name
            movieDescription = movie.description
            mv = MovieView(movieName, movieDescription, movieType)
            result.append(mv)
        return result

    def get(self,name: str) -> MovieView:
        movie = self.repository.get(name)
        if movie is None:
            MovieView('nil', 'nil', MovieType.BASIC2D)
        movieType = MovieType(movie.type)
        movieName = movie.name
        movieDescription = movie.description
        return MovieView(movieName, movieDescription, movieType)

    def add(self,value: MovieView):
        movie = Movie(value.name, value.description, value.type.value)
        self.repository.add(movie)

    def update(self, value: MovieView):
        movie = Movie(value.name, value.description, value.type.value)
        self.repository.update(movie)
        pass

    def delete(self, value: MovieView):
        movie = Movie(value.name, value.description, value.type.value)
        self.repository.delete(movie)
        pass

