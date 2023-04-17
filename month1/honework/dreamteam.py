# Задание 3: #Cholpon
def compare(list_1, list_2):
    a = ''.join(list_1)
    b = ''.join(list_2)
    if a == b:
        return True
    else:
        return False

list_1 = ['a', 'bc', 'de']
list_2 = ['ab', 'c', 'de']
print(compare(list_1, list_2))
####################################### DONE ###########################################




##############################################################################################################
# Задание 11:#Cholpon
# Попросить пользователя ввести слова через пробел.
# Отсортировать слова по количеству символов и вывести на экран результат.

# Пример input: сон машина стол книга девочка
# Результат: сон стол книга машина девочка
def length():
    word = input('Введите слова через пробел ').split()
    word.sort(key = len)
    total = ' '.join(word)
    print (total)
length()
############### DONE     ##############################################




######################## Dreamteam2_2 ########################################################
# Задание 1: #Cholpon

import random as rd
random_number = rd.randint(0, 10)
#print(random_number)

def gues_number():
    tries = 0
    while True:
        my_number = int(input("Введите число от 0 до 10: "))
        tries += 1

        if my_number == random_number:
            print("Вы выиграли!")
            break
        elif tries == 1:
            print('Попробуйте еще раз, сталось 2 попытки')
        elif tries == 2 and tries < 3:
            print('Попробуйте еще раз, сталась 1 попытка')
        else:
            print('Вы проиграли')
            break

gues_number()
#  DONE  ############################################################################################################

