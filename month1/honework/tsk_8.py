# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
def season(month):
    if month in (12, 1, 2):
        return ("зима")
    elif month in (3, 4, 5):
        return ("весна")
    elif month in (6, 7, 8):
        return ("лето")
    elif month in (9, 10, 11):
        return ("осень")
    else:
        return False

month = 5
print(month)
