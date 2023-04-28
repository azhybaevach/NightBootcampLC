# Нужно создать класс который принимает Data #2 данные.
# И внутри класса создать несколько методов:
# 1/Метод который вернёт все имена отелей.
# 2/Метод который из собирает все name в один Tuple и locations
# в другой и возвращает dictionary c двумя ключами списками со всеми значениями.
# 3.Метод который добавит к каждому элементу в markers поле status_id:

# class Data:
#     def __init__(self, data):
#         self.data = data
#
#     def names(self):
#         all_names = []
#         for i in self.data["MARKERS"]:
#             if "NAME" in i:
#                 all_names.append(i["NAME"])
#         return all_names
# #
#     def names_location(self):
#         name = []
#         location = []
#         for i in self.data["MARKERS"]:
#             if "NAME" in i:
#                 name.append(i["NAME"])
#             if "LOCATION" in i:
#                 location.append(i["LOCATION"])
#             if "POSITION" in i:
#                 location.append(i["POSITION"])
#         return {'NAME': name, "LOCATION": location}
#
#
#     def status_id(self, status_id):
#         for i in self.data['MARKERS']:
#             i['status_id'] = status_id
#             status_id += 1
#             return status_id
#
#
# data = {"MARKERS": [
#     {"NAME": "RIXOS THE PALM DUBAI", "POSITION": [25.1212, 55.1535]},
#     {"NAME": "SHANGRI-LA HOTEL", "LOCATION": [25.2084, 55.2719]},
#     {"NAME": "GRAND HYATT", "LOCATION": [25.2285, 55.3273]}
# ]}
# hotel_data = Data(data)
# hotel_data.status_id(1)
# print(hotel_data.names())
# print(hotel_data.names_location())
# print(data)







