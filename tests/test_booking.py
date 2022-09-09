from core.models.booking import Booking

def dummyBooking():
    booking = Booking()
    booking.movie = None
    booking.seats = ["A4", "A5", "A6"]
    booking.time = "2pm"
    return booking


def test_booking_seat():
    booking = dummyBooking()
    assert booking.seats[0] == "A4"

def test_booking_seats():
    booking = dummyBooking()
    assert "A5" in booking.seats and "A6" in booking.seats

def test_booking_time():
    booking = dummyBooking()
    assert booking.time == "2pm"