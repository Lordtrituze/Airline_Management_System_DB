from datetime import date


class Flight:
    id: int
    aircraft_id: int
    takeoff_location: str
    destination: str
    takeoff_time: str
    arrival_time: str
    flight_no: int
    created_at: date

    def __init__(self, id, aircraft_id, takeoff_location, destination, takeoff_time, arrival_time, flight_no, created_at):
        self.id = id
        self.aircraft_id = aircraft_id
        self.takeoff_location = takeoff_location
        self.destination = destination
        self.takeoff_time = takeoff_time
        self.arrival_time = arrival_time
        self.flight_no = flight_no
        self.created_at = created_at

    def __str__(self):
        description = f"{self.id:<5}\t{self.aircraft_id:<10}\t{self.takeoff_location:<20}\t{self.destination:<20}\t{self.takeoff_time:<20}\t{self.arrival_time:<20}\t{self.flight_no:<10}\t{self.created_at} "
        return  description