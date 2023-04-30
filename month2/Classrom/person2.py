# Создайте класс Person с атрибутами: имя и возраст строки типа.
# Создайте метод display(), который отображает имя и возраст объекта, созданного с помощью класса Person.
# Создайте дочерний класс Student, который наследуется от класса Person и также имеет атрибут раздела.
# Создайте метод displayStudent(), который отображает имя, возраст и раздел объекта, созданного с помощью класса Student.
# Создайте объект Student через создание экземпляра в классе Student, а затем протестируйте метод displayStudent

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def display(self):
        print (f'Имя{self.name}, Возраст{self.age}')


class Student(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department


    def displayStudent(self):
        return f"Name: {self.name}\nAge: {self.age}\nDepartment: {self.department}\n"


student = Student('Cholpon', 28, "IT")
print(student.displayStudent())