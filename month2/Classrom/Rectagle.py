# Построить
# класс для описания плоской геометрической фигуры: Rectangle (Прямоугольник.).
# Класс
# должен содержать:
# Данные:
# длина и ширина прямоугольника
# Методы для операций с данными:

class Ractagle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def square(self):
        a = self.length * self.width
        return a

    def perimeter(self):
        p = 2*(self.length+self.width)
        return p



b = Ractagle(5, 2)
print(b.square())
print(b.perimeter())