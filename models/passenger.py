from datetime import date


class Passenger:
    id: int
    first_name: str
    last_name: str
    email: str
    address: str
    reg_no: str
    created_at: date
    def __init__(self, id, first_name, last_name, email, address, reg_no, created_at):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.reg_no = reg_no
        self.created_at = created_at

    def __str__(self):
        description = f"{self.id:<5}\t{self.first_name:<20}\t{self.last_name:<20}\t{self.email:<25}\t{self.address:<25}\t{self.reg_no:<10}\t{self.created_at}"
        return description
