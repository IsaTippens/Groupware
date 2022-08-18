from core.models.booking import Booking

def test_booking_seat():
    booking = Booking()
    booking.create(None, ["A4"], "10pm")
    assert booking.seats[0] == "A4"

def test_booking_seats():
    booking = Booking()
    booking.create(None, ["A4", "A5", "A6"], "10pm")
    assert "A5" in booking.seats and "A6" in booking.seats

def test_booking_time():
    booking = Booking()
    booking.create(None, ["A4", "A5", "A6"], "2pm")
    assert booking.time == "2pm"