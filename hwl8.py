from abc import ABC,abstractmethod


class Transport(ABC):

    @abstractmethod
    def __init__(self, brand: str, model: str, issue_year: int, color: str, milage = 0):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.color = color
        self.milage = milage

    @abstractmethod
    def move(self, num_km: float):
        try:
            num_km <= 0
        except ValueError:
            print('Расстояние должно быть положительтным числом')
        else:
            self.milage += num_km

class Car(Transport):

    def __init__(self, brand: str, model: str, issue_year: int, color: str,engine_type: str, milage = 0):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.color = color
        self.engine_type = engine_type
        self.milage = milage

    def move(self, num_km: float):
        try:
            num_km <= 0
        except ValueError:
            print('Расстояние должно быть положительтным числом')
        else:
            self.milage += num_km
        print(f'{self.brand}{self.model}({self.color}-{self.issue_year}) проехала {self.milage} км')

class Airplane(Transport):

    def __init__(self, brand: str, model: str, issue_year: int,color: str, lifting_capacity: int, milage = 0):
        self.brand = brand
        self.model = model
        self.color = color
        self.issue_year = issue_year
        self.lifting_capacity = lifting_capacity
        self.milage = milage


    def move(self, num_km: float):
        try:
            num_km <= 0
        except ValueError:
            print('Расстояние должно быть положительтным числом')
        else:
            self.milage += num_km
        print(f'{self.brand} {self.model} ({self.color}-{self.issue_year})(грузоподъемность: {self.lifting_capacity} кг) пролетел {self.milage} км')

volvo1 = Car('Volvo', 'xc40', 2020, 'Bronze', 'diesel')
volvo1.move(1234)

jet1 =Airplane('Jet', 'qwe', 2024, 'White', 30000)
jet1.move(1000000)