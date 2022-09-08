from core.utils import TheatreUtils

def test_valid_seat():
    seat = "A1"
    assert TheatreUtils.valid_seat(seat) == True

def test_valid_seat2():
    seat = "Z11"
    assert TheatreUtils.valid_seat(seat) == True

def test_invalid_seat():
    seat = "A0"
    assert TheatreUtils.valid_seat(seat) == False

def test_invalid_seat2():
    seat = "AA1"
    assert TheatreUtils.valid_seat(seat) == False

def test_invalid_seat3():
    seat = "Z-12"
    assert TheatreUtils.valid_seat(seat) == False

def test_row_to_index():
    row = "A"
    assert TheatreUtils.letter_to_index(row) == 0

def test_row_to_index2():
    row = "Z"
    assert TheatreUtils.letter_to_index(row) == 25

def test_row_to_index3():
    row = "AA"
    assert TheatreUtils.letter_to_index(row) == 26

def test_row_to_index4():
    row = "AZ"
    assert TheatreUtils.letter_to_index(row) == 51

def test_index_to_row():
    index = 0
    assert TheatreUtils.index_to_letter(index) == "A"

def test_index_to_row2():
    index = 25
    assert TheatreUtils.index_to_letter(index) == "Z"

def test_index_to_row3():
    index = 26
    assert TheatreUtils.index_to_letter(index) == "AA"

def test_index_to_row4():
    index = 51
    assert TheatreUtils.index_to_letter(index) == "AZ"
