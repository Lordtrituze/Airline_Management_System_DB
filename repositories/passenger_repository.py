from typing import List
from models.passenger import Passenger
from repositories.base_repository import baserepsoitory


class PassengerRepository(baserepsoitory):
    def __init__(self):
        super().__init__()
        self.db = baserepsoitory.db

    def create(self, passenger: Passenger):
        cursor = self.db.cursor()
        sql = "INSERT INTO passengers(first_name, last_name, email, address, reg_no) VALUES(%s, %s, %s, %s, %s)"
        val = (passenger.first_name, passenger.last_name, passenger.email, passenger.address, passenger.reg_no)
        cursor.execute(sql, val)
        self.db.commit()
        passenger.id = cursor.lastrowid

    def find(self, reg_no: str):
        cursor = self.db.cursor()
        sql = "SELECT * FROM passengers WHERE reg_no = %s"
        adr = (reg_no,)
        cursor.execute(sql, adr)
        record = cursor.fetchone()
        passenger = PassengerRepository.__map_selected_record_to_passenger(record)
        if passenger is None:
            passenger = "Passenger unavailable"
            return passenger
        print(f"{'ID':<5}\t{'First Name':<20}\t{'Last Name':<20}\t{'Email':<25}\t{'Address':<25}\t{'Reg_no':<10}\t{'Created_at'}")
        return passenger

    def list(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM passengers"
        cursor.execute(sql)
        result = cursor.fetchall()
        passengers: List[Passenger] = []
        for record in result:
            passenger = PassengerRepository.__map_selected_record_to_passenger(record)
            passengers.append(passenger)
        print(f"{'ID':<5}\t{'First Name':<20}\t{'Last Name':<20}\t{'Email':<25}\t{'Address':<25}\t{'Reg_no':<10}\t{'Created_at'}")
        return passengers

    def showAll(self):
        passengers = self.list()
        for passenger in passengers:
            print(passenger)

    def update(self, id: int, passenger: Passenger):
        cursor = self.db.cursor()
        sql = "UPDATE passengers SET first_name = %s, last_name = %s, email = %s, address = %s, reg_no = %s WHERE id " \
              "= %s "
        val = (passenger.first_name, passenger.last_name, passenger.email, passenger.address, passenger.reg_no, id)
        cursor.execute(sql, val)
        self.db.commit()

    def find_id(self, regNo: str):
        cursor = self.db.cursor()
        sql = "SELECT * FROM passengers WHERE reg_no = %s"
        adr = (regNo,)
        cursor.execute(sql, adr)
        record = cursor.fetchone()
        passenger = PassengerRepository.__map_selected_record_to_passenger(record)
        if passenger is None:
            passenger = "Passenger Unavailable"
            return passenger
        return passenger.id

    def delete(self, id: int):
        cursor = self.db.cursor()
        sql = "DELETE FROM passengers WHERE id = %s"
        adr = (id,)
        cursor.execute(sql, adr)
        self.db.commit()
        message = "Deleted"
        return message

    @staticmethod
    def __map_selected_record_to_passenger(record):
        if record is None:
            return None
        else:
            id, first_name, last_name, email, address, reg_no, created_at = record
            passenger = Passenger(id, first_name, last_name, email, address, reg_no, created_at)
            return passenger