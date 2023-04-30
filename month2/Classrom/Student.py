# Создайте класс Student, конструктор которого имеет параметры name, lastname,
# department, year_of_entrance. Добавьте метод get_student_info, который
# возвращает имя, фамилию, год поступления и факультет в
# отформатированном виде: “Вася Иванов поступил в 2017 г. на факультет:

class Student:
    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance


    def get_student_info(self):
        return f'{self.name} {self.lastname} поступила в {self.year_of_entrance} г. на факультет {self.department}'


# student = Student('Чолпон', 'Ажыбаева', '"Инженерия и технология"', 2012)
# print(student.get_student_info())


