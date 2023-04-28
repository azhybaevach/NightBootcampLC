# а) Создайте класс Phone, который содержит атрибуты number, model и weight.
# б) Создайте три экземпляра этого класса.
# в) Выведите на консоль значения их атрибутов.
# г) Добавить конструктор в класс Phone, который принимает на вход три параметра
# для инициализации переменных класса - number, model и weight.
# д) Создать метод sendMessage. Данный метод принимает на вход номера телефонов,
# которым будет отправлено сообщение. Метод выводит на консоль номера этих телефонов.

class Phone:

    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def num_model(self):
        return f'{self.model} - {self.number}'

    def sendMessage(self, *numbers):
        print(f'c номера {self.number} отправлено сообщение на номер {*numbers,}')

phone1 = Phone(996700055545, 'Nokia', 100)
phone2 = Phone(996700577545, 'Samsung', 200)
phone3 = Phone(996555055545, 'Iphone', 300)

print("Телефон 1:", phone1.number, phone1.model, phone1.weight)
print("Телефон 2:", phone2.number, phone2.model, phone2.weight)
print("Телефон 3:", phone3.number, phone3.model, phone3.weight)

phone1.sendMessage(phone2.number)
phone2.sendMessage(phone3.number)
phone3.sendMessage(phone1.number)









