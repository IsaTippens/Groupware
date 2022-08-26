from core.enums import MovieType
from core.viewmodels import Movie
from core.services import MovieService
from core.repositories.test_movie_repository import TestMovieRepository

movieService = MovieService(TestMovieRepository())

def test_get_all():
    movies = movieService.get_all()
    assert movies[0].name == 'Avengers 5'

def test_get():
    movie = movieService.get('Avengers 4')
    assert movie.name == 'Avengers 4' and movie.type == MovieType.BASIC2D

def test_update():
    movie = movieService.get('Avengers 5')
    old = movie.description
    movie.description = 'Iron man arrives'
    movieService.update(movie)
    movie = movieService.get('Avengers 5')
    assert movie.description == 'Iron man arrives' and old == 'Thanos returns'
