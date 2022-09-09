from core.models.theatre import Theatre
from core.repositories.test_theatre_repository import TestTheatreRepository

repo = TestTheatreRepository()

def test_get():
    """
        Test getting a known theatre that does exist
    """
    theatre = repo.get("Avengers 5", "2022-05-01", "2PM")
    assert theatre.seats != None

def test_get_none():
    """
        Test getting a theatre that does not exist
    """
    theatre = repo.get("Avengers 5", "2022-05-01", "3PM")
    assert theatre.seats == None

def test_add():
    """
        Test adding a new theatre
    """
    theatre = Theatre("Avengers 7", "2022-08-01", "12PM")
    theatre.seats = [[True, False, True]]
    repo.add(theatre)
    new_theatre = repo.get("Avengers 7", "2022-08-01", "12PM")
    assert new_theatre.seats == [[True, False, True]]

def test_update():
    """
        Test updating an existing theatre
    """
    theatre = repo.get("Avengers 5", "2022-05-01", "2PM")
    assert theatre.seats[1][1] == True

    theatre.seats[1][1] = False
    repo.update(theatre)
    new_theatre = repo.get("Avengers 5", "2022-05-01", "2PM")
    assert new_theatre.seats[1][1] == False

def test_update_add():
    """
        Test updating a non-existing theatre.

        The repository should add the theatre if it does not exist
    """
    theatre = repo.get("Avengers 1", "2022-05-01", "2PM")
    assert theatre.seats == None

    theatre.seats = [[False]]
    repo.update(theatre)
    new_theatre = repo.get("Avengers 1", "2022-05-01", "2PM")
    assert new_theatre.seats[0][0] == False

def test_delete():
    """
        Test deleting a theatre
    """
    theatre = repo.get("Avengers 5", "2022-05-01", "2PM")
    assert theatre.seats != None

    repo.delete(theatre)
    new_theatre = repo.get("Avengers 5", "2022-05-01", "2PM")
    assert new_theatre.seats == None