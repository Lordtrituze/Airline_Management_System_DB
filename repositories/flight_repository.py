from typing import List
from models.flight import Flight

from repositories.base_repository import baserepsoitory


class FlightRepository(baserepsoitory):
    def __init__(self):
        super().__init__()
        self.db = baserepsoitory.db

    def create(self, flight: Flight):
        cursor = self.db.cursor()
        sql = "INSERT INTO flights(aircraft_id, takeoff_location, destination, takeoff_time, arrival_time, flight_no) " \
              "VALUES(%s, %s, %s, %s, %s, %s) "
        val = (flight.aircraft_id, flight.takeoff_location, flight.destination, flight.takeoff_time, flight.arrival_time, flight.flight_no)
        cursor.execute(sql, val)
        self.db.commit()
        flight.id = cursor.lastrowid

    def find(self, flight_no: str):
        cursor = self.db.cursor()
        sql = "SELECT * FROM flights WHERE flight_no = %s"
        adr = (flight_no,)
        cursor.execute(sql, adr)
        record = cursor.fetchone()
        flight = FlightRepository.__map_selected_record_to_flight(record)
        if flight is None:
            flight = "Flight unavailable"
            return flight
        print(f"{'ID':<5}\t{'aircraft_id':<10}\t{'takeoff_location':<20}\t{'destination':<20}\t{'takeoff_time':<20}\t{'arrival_time':<20}\t{'flight_no':<10}\t{'Created_at'}")
        return flight

    def find_id(self, flight_no: str):
        cursor = self.db.cursor()
        sql = "SELECT * FROM flights WHERE flight_no = %s"
        adr = (flight_no,)
        cursor.execute(sql, adr)
        record = cursor.fetchone()
        flight = FlightRepository.__map_selected_record_to_flight(record)
        if flight is None:
            flight = "Flight Unavailable"
            return flight
        return flight.id

    def delete(self, id: int):
        cursor = self.db.cursor()
        sql = "DELETE FROM flights WHERE id = %s"
        adr = (id,)
        cursor.execute(sql, adr)
        self.db.commit()
        message = "Deleted"
        return message

    def update(self, id: int, flight: Flight):
        cursor = self.db.cursor()
        sql = "UPDATE flights SET aircraft_id = %s, takeoff_location = %s, destination = %s, takeoff_time = %s, arrival_time = %s, flight_no = %s WHERE id = %s"
        val = (flight.aircraft_id, flight.takeoff_location, flight.destination, flight.takeoff_time, flight.arrival_time, flight.flight_no, id)
        cursor.execute(sql, val)
        self.db.commit()

    def list(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM flights"
        cursor.execute(sql)
        result = cursor.fetchall()
        flights: List[Flight] = []
        for record in result:
            flight = FlightRepository.__map_selected_record_to_flight(record)
            flights.append(flight)
        print(f"{'ID':<5}\t{'aircraft_id':<10}\t{'takeoff_location':<20}\t{'destination':<20}\t{'takeoff_time':<20}\t{'arrival_time':<20}\t{'flight_no':<10}\t{'Created_at'}")
        return flights
    def showAll(self):
        flights = self.list()
        for flight in flights:
            print(flight)

    @staticmethod
    def __map_selected_record_to_flight(record):
        if record is None:
            return None
        else:
            id, aircraft_id, takeoff_location, destination, takeoff_time, arrival_time, flight_no, created_at = record
            flight = Flight(id, aircraft_id, takeoff_location, destination, takeoff_time, arrival_time, flight_no, created_at)
            return flight
