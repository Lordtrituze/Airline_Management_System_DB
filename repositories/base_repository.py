import mysql.connector

class baserepsoitory:
    db =None

    def __init__(self):
        if baserepsoitory.db is None:
            baserepsoitory.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Olalekan100%",
                database="airline"
            )