
class Phone:
    """Создаем класс Phone"""
    brand: str
    model: str
    issue_year: int
    name: str

    def __init__(self, brand, model, issue_year):
        """Создаем атрибуты brand, model, issue_year"""
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, name):
        """Входящий вызов"""
        self.name = name
        return print('Вам звонит', name)

    def get_info(self):
        """Информация о телефоне в виде кортежа"""
        print((self.brand, self.model, self.issue_year))

    def __str__(self):
        """Информация о телефоне в виде строки"""
        return print(f'Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}')

    def dict_info(self):
        """Информация о телефоне в виде словаря"""
        dict_info = {}
        dict_info['Бренд '] = self.brand
        dict_info['Модель '] = self.model
        dict_info['Год выпуска'] = self.issue_year
        print(dict_info)

phone1 = Phone('Xiaomi', 'Redmi13', 2022)
phone2 = Phone('iPhone', '15', 2024)

print(phone1.brand, phone1.model, phone1.issue_year)

phone1.receive_call('Виталий')

phone2.get_info()
phone1.get_info()

phone1.__str__()
phone2.__str__()

phone1.dict_info()
phone2.dict_info()