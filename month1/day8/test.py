# a = 'dastan 123  ilan 123  ulan 321'
# with open('database.txt', 'w') as f:
#     f.write(a)
#
# with open('database.txt', 'r') as f:
#     data = f.read()
#
# users = data.split('  ')
# print(users)
#
# login = input()
# password = input()
#
# for i in users:
#     if login == i.split(' ')[0]:
#         print('Пользователь сущ. пропиште пароль')
#         password1 = input()
#         while True:
#             if password1 == password and password1 == i.split(' ')[1]:
#                 print('Вы вошли')
#             else:
#                 print('Попробуй еще раз')
#
# with open('database.txt', 'a') as f:
#     f.write('  ' + login + ' ' + password)
#     print('Регистрация прошла успешна')
#


my_file = open('people.txt', 'w')

name = input("Введите имя - ")
my_file.write(name)
my_file.close()