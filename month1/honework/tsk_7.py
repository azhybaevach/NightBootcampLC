# Напишите программу, где исходный список содержит положительные и отрицательные числа.
# Требуется положительные поместить в один список, а отрицательные - в другой.
def positive_negative(numbers):
    positive = []
    negative = []
    for i in numbers:
        if i >= 0:
            positive.append(i)
        else:
            negative.append(i)
    return positive, negative

numbers = [1, 5, 6, -2, 6, -7]
positive, negative = positive_negative(numbers)

print(positive)
print(negative)