# a) поля fullName, age, place(address)
# б) метод talk(), в которых просто вывести на консоль сообщение -"Такой-то  Person говорит". Метод
#
# move()  будет менять его адрес
# в) Добавьте  конструктор  с тремя параметрами fullName, address, age = 18
# г) Настроить  метод __str__  (Сделать отображение всех полей объекта)


class Person:
    def __init__(self, full_name, adress, age=18):
        self.full_name = full_name
        self.adress = adress
        self.age = age

    def talk(self):
        print(f'{self.full_name} говорит')


    def move(self, new_adress):
        self.new_adress = new_adress
        print (f'переехала с {self.adress} на {new_adress}')


    def __str__(self):
        return f'имя: {self.full_name}, адресс: {self.adress}, возраст: {self.age}'



person = Person('Чолпон', 'ул. Коммунарская 91', 28)
person.talk()
print(person)
person.move('ул. Кок - жар 22')


