# Создайте класс Factory и внутри создайте 2 метода:
# # Метод engine который возвращает строку "Двигатель создан"
# # Метод bridge который возвращает строку "Ходовая часть создана"
# # Создайте класс Toyota который будет НАСЛЕДОВАТЬ класс Factory. В классе
# # Toyota создайте методы wheels и windows.
# # Метод wheels возвращает строку "Колёса готовы"
# # Метод windows возвращает строку "Стёкла готовы"
# # Из класса Toyota вызовите все методы, методы вернут вам строки(объекты)
# # Результат каждого метода вставьте в лист

# class Factory:
#     def engine(self):
#         return "Двигатель создан"
#
#     def bridge(self):
#         return "Ходовая часть создана"
#
# class Toyota(Factory):
#
#     def wheels(self):
#         return "Колеса готовы"
#
#     def windows(self):
#         return "Стекла готовы"
#
# toyota = Toyota()
# print([toyota.engine(), toyota.bridge(), toyota.wheels(), toyota.windows()])

# Создайте Класс Zoo.
# Инициализируйте класс в объект.
# К объекту Zoo добавьте атрибут animal_1 и присвойте ему значение "Тигр"
# К объекту Zoo добавьте атрибут animal_2 и присвойте ему значение "Бегемот"
# К объекту Zoo добавьте атрибут animal_3 и присвойте ему значение "Жираф"
# В объекте Zoo измените значение атрибута animal_1 и присвойте ему
# значение "Лев".
# К объекту Zoo добавьте атрибут animal_4 и присвойте ему list состоящий из
# animal_2 и animal_3
# В объекте Zoo измените значение атрибута animal_3 и присвойте ему значение
# "Змея".

# class Zoo:
#     def __init__(self):
#         self.animal_1 = "Тигр"
#         self.animal_2 = "Бегемот"
#         self.animal_3 = "Жираф"
#
# zoo = Zoo()
# zoo.animal_1 = "Лев"
# zoo.animal_4 = [zoo.animal_2, zoo.animal_3]
# zoo.animal_3 = "Змея"
#
# print(zoo.animal_1, zoo.animal_2, zoo.animal_3, zoo.animal_4)



