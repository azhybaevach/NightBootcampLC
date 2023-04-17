import random

try:
    start = 1
    number = int(input('Введите максимальное значение: '))
    correct = 0
    wrong = 0
    while start <= 1:
        num1 = random.randint(0, number)
        num2 = random.randint(0, number)
        result = num1 * num2
        answer = int(input('Сколько будет '+ str(num1) + ' * ' +str(num2) + '?: '))
        if answer == result:
            correct += 1
            print('Верно')
        else:
            wrong += 1
            print('неверно')
        start = int(input('Нажмите 1, чтобы продолжить: '))
        if start != 1:
            break
    print('Правильных ответов: ', correct)
    print( 'Неправильных ответов: ', wrong)
except:
    print('Введите числа')



