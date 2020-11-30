from datetime import date


class Aircraft:
    id:int
    name: str
    model: str
    capacity: int
    reg_no: str
    created_at: date

    def __init__(self, id, name, model, capacity, reg_no, created_at):
        self.id = id
        self.name = name
        self.model = model
        self.capacity = capacity
        self.reg_no = reg_no
        self.created_at = created_at

    def __str__(self):
        aircraft = f"{self.id:<5}\t{self.name:<10}\t{self.model:<10}\t{self.capacity:<10}\t{self.reg_no:<10}\t{self.created_at}"
        return aircraft
