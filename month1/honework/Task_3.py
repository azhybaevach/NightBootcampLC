# Напишите функцию которая принимает два аргумента (числа), умножает их друг на друга,
# и возвращает функцию, которая также берет два аргумента (числа),
# и возвращает результат умножения аргументов внешней функции плюс результат деления
# аргументов внутренней функции.
# Подсказка: (outer_arg1 * outer_arg2) + (inner_arg1 / inner_arg2)

def outer(outer_arg1: int, outer_arg2: int):
    def inner(inner_arg1: int, inner_arg2: int):
        return (outer_arg1 * outer_arg2) + (inner_arg1 / inner_arg2)
    return inner

f = outer(2, 5)
print (f(6, 3))