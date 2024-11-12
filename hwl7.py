from encodings.punycode import selective_find
from sys import int_info


class Phone:
    brand: str
    model: str
    issue_year: int
    name: str

    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, name):
        self.name = name
        return print('Вам звонит', name)

    def get_info(self):
        print((self.brand, self.model, self.issue_year))

    def __str__(self):
        return print(f'Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}')





phone1 = Phone('Xiaomi', 'Redmi13', 2022)

print(phone1.brand, phone1.model, phone1.issue_year)

phone1.receive_call('Виталий')

phone1.get_info()

phone1.__str__()