from core.models import Movie

def test_movie_name():
    movie = Movie("Pacman", "waka")
    assert movie.name == "Pacman"