from typing import List
from models.booking import Booking

from repositories.base_repository import baserepsoitory


class BookingRepository(baserepsoitory):
    def __init__(self):
        super().__init__()
        self.db = baserepsoitory.db

    def create(self, booking: Booking):
        cursor = self.db.cursor()
        sql = "INSERT INTO bookings(passenger_id, flight_id, booking_type, flight_class, booking_no, booking_date, seat_no) " \
              "VALUES(%s, %s, %s, %s, %s, %s, %s) "
        val = (booking.passenger_id, booking.flight_id, booking.booking_type, booking.flight_class, booking.booking_no, booking.booking_date, booking.seat_no)
        cursor.execute(sql, val)
        self.db.commit()
        booking.id = cursor.lastrowid

    def find(self, booking_no: str):
        cursor = self.db.cursor()
        sql = "SELECT * FROM bookings WHERE booking_no = %s"
        adr = (booking_no,)
        cursor.execute(sql, adr)
        record = cursor.fetchone()
        booking = BookingRepository.__map_selected_record_to_booking(record)
        if booking is None:
            booking = "Booking unavailable"
            return booking
        print(f"{'ID':<5}\t{'Passenger ID':<10}\t{'Flight ID':<10}\t{'Booking Type':<10}\t{'Flight Class':<10}\t{'Booking No':<10}\t{'Booking Date':<20}\t{'Seat No':<10}\t{'Created_at'}")
        return booking

    def find_id(self, booking_no: str):
        cursor = self.db.cursor()
        sql = "SELECT * FROM bookings WHERE booking_no = %s"
        adr = (booking_no,)
        cursor.execute(sql, adr)
        record = cursor.fetchone()
        booking = BookingRepository.__map_selected_record_to_booking(record)
        if booking is None:
            booking = "Booking unavailable"
            return booking
        return booking.id

    def delete(self, id: int):
        cursor = self.db.cursor()
        sql = "DELETE FROM bookings WHERE id = %s"
        adr = (id,)
        cursor.execute(sql, adr)
        self.db.commit()
        message = "Deleted"
        return message

    def update(self, id: int, booking: Booking):
        cursor = self.db.cursor()
        sql = "UPDATE bookings SET passenger_id = %s, flight_id = %s, booking_type = %s, flight_class = %s, booking_no = %s, booking_date = %s, seat_no = %s WHERE id = %s"
        val = (booking.passenger_id, booking.flight_id, booking.booking_type, booking.flight_class, booking.booking_no, booking.booking_date, booking.seat_no, id)
        cursor.execute(sql, val)
        self.db.commit()

    def list(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM bookings"
        cursor.execute(sql)
        result = cursor.fetchall()
        bookings: List[Booking] = []
        for record in result:
            booking = BookingRepository.__map_selected_record_to_booking(record)
            bookings.append(booking)
        print(f"{'ID':<5}\t{'Passenger ID':<10}\t{'Flight ID':<10}\t{'Booking Type':<10}\t{'Flight Class':<10}\t{'Booking No':<10}\t{'Booking Date':<20}\t{'Seat No':<10}\t{'Created_at'}")
        return bookings
    def showAll(self):
        bookings = self.list()
        for booking in bookings:
            print(booking)

    @staticmethod
    def __map_selected_record_to_booking(record):
        if record is None:
            return None
        else:
            id, passenger_id, flight_id, booking_type, flight_class, booking_no, booking_date, seat_no, created_at = record
            booking = Booking(id, passenger_id, flight_id, booking_type, flight_class, booking_no, booking_date, seat_no, created_at)
            return booking
