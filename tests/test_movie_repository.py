from core.repositories.test_movie_repository import TestMovieRepository
from core.models import Movie
mov = TestMovieRepository()

def test_get_all():
    movies = mov.get_all()
    assert movies[0].name == 'Avengers 5'

def test_get():
    movie = mov.get('Avengers 5')
    assert movie.name == 'Avengers 5' and movie.type == 1

def test_update():
    movie = mov.get('Avengers 5')
    movie.description = 'Thanos wins'
    mov.update(movie)
    movie = mov.get('Avengers 5')
    assert movie.description == 'Thanos wins'

def test_delete():
    movie = mov.get('Avengers 5')
    mov.delete(movie)
    assert mov.get('Avengers 5') == None

def test_add():
    movie =Movie('Ratatouille 2', 'A new fast food restaurant')
    mov.add(movie)
    assert mov.get('Ratatouille 2').description == 'A new fast food restaurant'