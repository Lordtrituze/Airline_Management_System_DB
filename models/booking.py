from datetime import date


class Booking:
    id: int
    passenger_id: str
    flight_id: int
    booking_type: str
    flight_class: str
    booking_no: str
    booking_date: date
    seat_no: int
    created_at: date

    def __init__(self, id, passenger_id, flight_id, booking_type, flight_class, booking_no, booking_date, seat_no, created_at):
        self.id = id
        self.passenger_id = passenger_id
        self.flight_id = flight_id
        self.booking_type = booking_type
        self.flight_class = flight_class
        self.booking_no = booking_no
        self.booking_date = booking_date
        self.seat_no = seat_no
        self.created_at = created_at

    def __str__(self):
        description = f"{self.id:<5}\t{self.passenger_id:<10}\t{self.flight_id:<10}\t{self.booking_type:<10}\t{self.flight_class:<10}\t{self.booking_no:<10}\t{self.booking_date:<20}\t{self.seat_no:<10}\t{self.created_at} "
        return description
