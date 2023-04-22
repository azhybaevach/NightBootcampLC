#problem1
#
#
# list_1 = ['name', 'age', '1', '19']
#
#
# def reverse_list():
#     my_list1 = list_1[0:len(list_1)//2]
#     my_list2 = list_1[len(list_1)//2:len(list_1)]
#     total = my_list1[::-1] + my_list2[::-1]
#     print(total)
#
# reverse_list()

#Problem_2 Создайте функцию которая генерирует 10 чисел Фибоначчи:
#
# 1,1,2,3,5,8,13,21,34,...

# def generate_fibonacci():
#     fib = [1, 1]
#     for i in range(2, 10):
#         fib.append(fib[i-1] + fib[i-2])
#     return fib
#
# numbers = generate_fibonacci()
# print(numbers)

#problem_3


# Создайте функцию сложения, затем функцию вычитания двух чисел...
# Создайте 3-ю функцию которая вызывает первые 2 внутри себя.

def summa(a, b):
    return a+b

def minus(a, b):
    return a-b

def total(a, b):
    result_1 = summa(a, b)
    result_2 = minus(a, b)
    return result_1, result_2
a = 10
b = 8
#print(summa(a, b))
#print(minus(a, b))
print(total(a, b))





















