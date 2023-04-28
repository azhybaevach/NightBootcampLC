import random
import datetime
# Класс который называется парковка
# С конструктором инит
# Принимает аттрибуты(макс кол-во мест, )
# аттрибуты- кол-во мест, список машин[пустой] который принимает в себе объекты экземпляра класса car,
#  записи - dictinary {в котором будут все таллоны и информация о том какая машина заехала и когда уехала,
#  булиан которая обозначает находится на парковке машина или нет },
#  талоны должны быть сгенерированны рандомно и должны быть уникальны
# методы - 1. Вызывается addCar принимает в себя аргумент класса Car,
#  метод должен добавить в наш аттрибут 'Машины' и добавляет новый элемент в записи
#  талон и если машина не уехала, то поле когда уехала машина возвращает  none
# метод - 2 Вызывается out_car(«talon») вы ищите талон и в записях добавляете
# время выхода машины а также булиан ставите фалс о том что машины нет в парковке,
# а также удилите машину из списка Машины
# Добавьте также разные методы чтобы просмотреть детально запись о машине итд
class Car:
    def __init__(self, brand, model, car_number):
        self.brand = brand
        self.model = model
        self.car_number = car_number
        self.created_date = datetime.datetime.now()
        self.end_date = None

class Parking:
    def __init__(self, max_place = 100):
        self.max_place = max_place
        self.cars_list = []
        self.notes = {}
        self.id = random.randint(1, 100)

    def new_talon(self):
        talon = self.id
        while talon in self.notes:
            talon = self.id
        return talon

    def get_parking_cars(self):
        return len([i for i in self.cars_list if not i.end_date])

    def get_unparking_cars(self):
        return len([i for i in self.cars_list if i.end_date])

    def add_Car(self, car: Car):
        if len(self.cars_list) < self.max_capacity:

            self.cars_list.append(car)
        self.cars_list.append(car)

    def remain(self, talon):
        for i in range(len(self.cars_list)):
            if self.cars_list[i].id == talon:
                return i * 10
        return 'Вашего талона здесь нет'













