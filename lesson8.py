class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def voice(self):
        return print('Что-то гавкает')

class Dog(Animal):
    pass

bobik = Dog('Bobik', 3)



class Bird(Animal):
    def voice(self):
        return print('Что-то чирикает')

    def fly(self):
        return print('Я на ЮГ')

sowa = Bird('Sowa', 1)



class Insect(Dog, Bird):
    def voice(self):
        return print('Что-то пищит')
    pass

komar = Insect('Komar', 0.1)

komar.voice()
bobik.voice()
sowa.voice()


