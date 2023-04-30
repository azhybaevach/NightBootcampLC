# Создайте класс Car. Пропишите в конструкторе параметры make, model, year,
# odometer, fuel. Пусть у показателя odometer будет первоначальное значение 0,
# а у fuel 70. Добавьте метод drive, который будет принимать расстояние в км. В
# самом начале проверьте, хватит ли вам бензина из расчета того, что машина
# расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние,
# то пусть этот метод добавляет эти километры к значению одометра, но не
# напрямую, а с помощью приватного метода __add_distance. Помимо этого
# пусть метод drive также отнимет потраченное количество бензина с помощью
# приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s
# drive!”. Если же бензина не хватит, то распечатайте “Need more fuel, please, fill more!”
class Car:
    def __init__(self, make, model, year, odometer = 0, fuel = 70):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
        self.fuel = fuel


    def __add_distance(self, distance):
        self.odometer += distance


    def __subtract_fuel(self, total_fuel):
        self.fuel -= total_fuel

    def drive(self, distance):
        total_fuel = distance / 10
        if self.fuel < total_fuel:
            return 'Need more fuel, please, fill more'
        else:
            self.__subtract_fuel(distance)
            self.__add_distance(total_fuel)
            return "Let's drive"


my_car = Car('Toyota', 'Camry', 2010, fuel=100)
print(my_car.drive(5000)) # Let's drive!


#print(f"Odometer: {my_car.odometer} km, Fuel: {my_car.fuel} liters.") # Odometer: 50 km, Fuel: 25.0 liters.

my_car.drive(200) # Need more fuel, please, fill more!
#print(f"Odometer: {my_car.odometer} km, Fuel: {my_car.fuel} liters.") # Odometer: 50 km, Fuel: 25.0 liters.




