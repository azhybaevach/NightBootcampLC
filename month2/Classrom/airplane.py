# Создайте новый класс Airplane. Создайте следующие характеристики (полей)
# объекта
# ● make (марка)● model● year● max_speed ● odometer● is_flying
# ﻿
# и методы имитирующих поведение самолета take off (взлет), fly (летать), land
# приземление). Метод take off должен изменить is_flying на True, а land на False. По
# умолчанию поле is_flying = False. Метод fly должен принимать расстояние полета и
# изменять показания одометра (километраж). Создайте 1 объект класса и используйте
# все методы класса.


class Airplane:
    def __init__(self, make, model, year, max_speed, odometer = 0, is_flying = False):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.is_flying = is_flying

    def __init__(self, make, model, year, max_speed, odometer=0):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.is_flying = False

    def take_off(self):
        self.is_flying = True
        return f'{self.make}{self.model} взлетел'

    def fly(self, km):
        self.odometer += km
        return f'самолет летел {km} км на скорости {self.max_speed} км/ч.'

    def land(self):
        self.is_flying = False
        return f'Самолет удачно приземлился'


airplane = Airplane('SU' ,'125', 2010, 500)

print(airplane.take_off())
print(airplane.fly(1500))
print(airplane.land())