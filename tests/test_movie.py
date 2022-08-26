from core.models import Movie

def test_movie_id():
    movie = Movie(0, "Pacman")
    assert movie.id == 0

def test_movie_name():
    movie = Movie(0, "Pacman")
    assert movie.name == "Pacman"