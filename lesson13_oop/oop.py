
# class Person:
#     def __init__(self, name, lastname):
#         self.name= name
#         self.lastname = lastname

#     def get_info(self):
#         print('привет', self.name, self.lastname)

# person = Person('bruno', 'fernandes')
# person.get_info()


# class Person:
#     def __init__(self, name, phone, address):
#         self.name = name 
#         self.phone = phone 
#         self.address = address

# personal = Person("Ralf", +502011352, 'Manchester')
# print("Ralf.__dict__=", personal.__dict__)


#####################################################################################################


# class Nout:
#     def __init__(self, name, CPU, RAM, video_card, SSD, size):
#         self.name = name
#         self.CPU = CPU
#         self.RAM = RAM
#         self.video_card = video_card
#         self.SSD = SSD
#         self.size = size
#         print(self.name,  self.CPU, self.RAM, self.video_card, self.SSD, self.size)

# noutbuk = Nout('Acer-Aspire-A315-42G', '5,7', 'AMD® Athlon 300u', 'Radeon 540X Series', '240', '1920x1080' )
# print('Your Notebook: ', noutbuk.__dict__)


# colors = {
# "black": {
# "category": "hue",
# "type": "primary",
# "code": {
# "rgba": [255,255,255,1],
# "hex": "#000"
# }
# },
# "white": {
# "category": "value",
# "code": {
# "rgba": [0,0,0,1],
# "hex": "#FFF"
# }
# },
# "red": {
# "category": "hue",
# "type": "primary",
# "code": {
# "rgba": [255,0,0,1],
# "hex": "#FF0"
# }
# },
# "blue": {
# "category": "hue",
# "type": "primary",
# "code": {
# "rgba": [0,0,255,1],
# "hex": "#00F"
# }
# },
# "yellow": {
# "category": "hue",
# "type": "primary",
# "code": {
# "rgba": [255,255,0,1],
# "hex": "#FF0"
# }
# },
# colors ={
# "green": {
# "category": "hue",
# "type": "secondary",
# "code": {
# "rgba": [0,255,0,1],
# "hex": "#0F0"
# }
# }
# }
# class Dictionary():
#     def __init__(self, colors):
#         self.colors = colors

#     def get_keys_tuple(self):
#         return tuple(self.colors.keys())

#     def get_values_tuple(self):
#         ls = []
#         for i in self.colors.keys():
#             s = self.colors.get(i)
#             for v in s.values():
#                 l = self.colors.get(v)
#                 for h in l:
#                     ls.append(h)

#         return ls 

# color = Dictionary(colors)
# print(color.get_values_tuple())


# def get_tuple_keys(self):
#         keys = []
#         for i in self.colors.keys():
#             keys.append(i)
#             a = self.colors.get(i)
#             for j in a.keys():
#                 keys.append(j)
#                 try:
#                     d = a.get(j)
#                     for t in d.keys():
#                         keys.append(t)
#                 except AttributeError:
#                     pass


class Airplane():
    
    def init(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying = False

    def take_off(self):
        self.is_flying = True
        message_take = f"{self.make} {self.model} was take off."
        return message_take

    def fly(self, km):
        self.odometer += km
        message_fly = f"{self.make} flew {self.odometer}km at a speed of {self.max_speed}km/h."
        return message_fly

    def land(self):
        self.is_flying = False
        self.odometer = 0
        message_land = f"{self.make} has landed, it's odometer shows {self.odometer}km."
        return message_land

go = Airplane(input("Название самолета:"), input("Модель:"), input("Введите год выпуска:"), int(input('Укажите высоту')))
print(go.take_off())
print(go.fly(500))
print(go.fly(500))
print(go.land())



class Car:
    def __init__(self, make, model, year, odometer = 0, fuel = 70):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
        self.fuel = fuel
 
    def drive(self, distance):
        fuel = distance / 10
        if self.fuel >= fuel:
            self.__add_distance(distance)
            self.__subtract_fuel(fuel)
            print('Let’s drive!')
        else:
            print('Need more fuel, please, fill more!')
            
        
    def __add_distance(self, distance):
        self.odometer += distance
 
    def __subtract_fuel(self, fuel):
        self.fuel -= fuel