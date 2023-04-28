from main import Car

def add_car():
    brand = input("Введите марку машины: ")
    model = input('Введите модель машины')
    car_number = input('Введите гос номер машины')
    car = Car(brand, model, car_number)
    return car

while True:
    print('Вы звехали на парковку, возьмите талон')
    print(f'Ваш талон{}')



