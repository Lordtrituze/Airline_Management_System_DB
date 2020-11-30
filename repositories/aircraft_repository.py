from typing import List

from models.aircraft import Aircraft
from repositories.base_repository import baserepsoitory


class AircraftRepository(baserepsoitory):
    def __init__(self):
        super().__init__()
        self.db = baserepsoitory.db

    def create(self, aircraft: Aircraft):
        cursor = self.db.cursor()
        sql = "INSERT INTO aircrafts(name, model, capacity, reg_no) VALUES(%s, %s, %s, %s)"
        val = (aircraft.name, aircraft.model, aircraft.capacity, aircraft.reg_no)
        cursor.execute(sql, val)
        self.db.commit()
        aircraft.id = cursor.lastrowid

    def update(self, id: int, aircraft: Aircraft):
        cursor = self.db.cursor()
        sql = "UPDATE aircrafts SET name = %s, model = %s, capacity = %s, reg_no = %s WHERE id = %s"
        val = (aircraft.name, aircraft.model, aircraft.capacity, aircraft.reg_no, id)
        cursor.execute(sql, val)
        self.db.commit()

    def list(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM aircrafts"
        cursor.execute(sql)
        result = cursor.fetchall()
        aircrafts: List[Aircraft] = []
        for record in result:
            aircraft = AircraftRepository.__map_selected_record_to_aircraft(record)
            aircrafts.append(aircraft)
        print(f"{'ID':<5}\t{'Name':<10}\t{'Model':<10}\t{'Capacity':<10}\t{'Reg_no':<10}\t{'Created_at'}")
        return aircrafts
    def showAll(self):
        aircrafts = self.list()
        for aircraft in aircrafts:
            print(aircraft)

    def find(self, reg_no: str):
        cursor = self.db.cursor()
        sql = "SELECT * FROM aircrafts WHERE reg_no = %s"
        adr = (reg_no,)
        cursor.execute(sql, adr)
        record = cursor.fetchone()
        aircraft = AircraftRepository.__map_selected_record_to_aircraft(record)
        if aircraft is None:
            aircraft = "Aircraft unavailable"
            return aircraft
        print(f"{'ID':<5}\t{'Name':<10}\t{'Model':<10}\t{'Capacity':<10}\t{'Reg_no':<10}\t{'Created_at'}")
        return aircraft

    def find_id(self, regNo: str):
        cursor = self.db.cursor()
        sql = "SELECT * FROM aircrafts WHERE reg_no = %s"
        adr = (regNo,)
        cursor.execute(sql, adr)
        record = cursor.fetchone()
        aircraft = AircraftRepository.__map_selected_record_to_aircraft(record)
        if aircraft is None:
            aircraft = "Aircraft Unavailable"
            return aircraft
        return aircraft.id

    def delete(self, id: int):
        cursor = self.db.cursor()
        sql = "DELETE FROM aircrafts WHERE id = %s"
        adr = (id,)
        cursor.execute(sql, adr)
        self.db.commit()
        message = "Deleted"
        return message

    @staticmethod
    def __map_selected_record_to_aircraft(record):
        if record is None:
            return None
        else:
            id, name, model, capacity, reg_no, created_at = record
            aircraft = Aircraft(id, name, model, capacity, reg_no, created_at)
            return aircraft
