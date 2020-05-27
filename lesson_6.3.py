class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income_wage =income['wage']
        self.income_bonus = income['bonus']


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname, self.position)

    def get_total_income(self):
        print(self.income_wage + self.income_bonus)

pos = Position('Maks', 'Petrov', 'senior', {"wage": 200000, "bonus": 50000})
pos.get_full_name()
pos.get_total_income()