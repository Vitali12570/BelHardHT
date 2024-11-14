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
        if num_km <= 0:
            raise ValueError('Расстояние должно быть положительным числом')
        else:
            self.milage += num_km

a = Car('Volvo', 'xc40', 2020, 'Bronze', 'diesel')
a.move(1)
print(a.milage)

