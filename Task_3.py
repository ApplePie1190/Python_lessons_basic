class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'полное имя сотрудника: {self.surname} {self.name}'

    def get_total_income(self):
        return f'доход с учетом премии: {sum(self._income.values())}'


worker_1 = Position('Андрей', 'Новиков', 'разработчик', 80000, 10000)
print(worker_1.get_full_name())
print(worker_1.get_total_income())
print(worker_1.position)
