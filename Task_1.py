class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_number(cls, data):
        day_month_year = [int(num) for num in data.split('-')]
        return day_month_year

    @staticmethod
    def check_date(date):
        day = Date.get_number(date)[0]
        month = Date.get_number(date)[1]
        year = Date.get_number(date)[2]
        if day in range(1, 32) and month in range(1, 13) and year > 0:
            return 'дата корректная'
        else:
            return 'вы задали некорректную дату'


date_1 = Date('31-02-2022')
print(date_1.get_number(date_1.date))
print(date_1.date)
print(date_1.check_date(date_1.date))
