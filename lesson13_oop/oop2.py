# 1
# class Factory:
#     def engine(self):
#         return 'Двигатель создан!'
#     def bridge(self):
#         return 'Ходовая часть создана!'

# # f = Factory()
# # print(f.engine(), f.bridge() )

# class Toyota(Factory):
#     def wheels(self):
#         return 'Колеса готовы!'
#     def windows(self):
#         return 'Стекла готовы!'

# t = Toyota()
# v =[t.engine(), t.bridge(), t.wheels(), t.windows()]
# print(v)


# 2

# class Zoo:
#     def __init__(self, ):
#         self.animal_1 = 'тигр'
#         self.animal_2 = 'бегемот'
#         self.animal_3 = 'жираф'
#         self.animal_4 = [self.animal_2, self.animal_3]



# zozo = Zoo()
# zozo.animal_1 = 'лев'
# zozo.animal_3 = 'змея'
# print(zozo.animal_1, zozo.animal_4, zozo.animal_3)


####################################################################################


# 1)Student
# Создайте класс Student, конструктор которого имеет параметры name, lastname,
# department, year_of_entrance. Добавьте метод get_student_info, который
# возвращает имя, фамилию, год поступления и факультет в
# отформатированном виде: “Вася Иванов поступил в 2017 г. на факультет:
# Программирование.”


# class Students():
#     def __init__(self):
#         self.name = "Вася"
#         self.lastname = "Иванов"
#         self.department = "Программирование"
#         self.year_of_entrance = 2017

# a = Students()
# print(a.name, a.lastname, 'Поступил в', a.year_of_entrance, 'на факультет:', a.department)



# 2)Airplane
# Создайте новый класс Airplane. Создайте следующие характеристики (полей)
# объекAта:
# ● make (марка)
# ● model
# ● year
# ● max_speed
# ● odometer
# ● is_flying
# и методы имитирующих поведение самолета take off (взлет), fly (летать), land
# приземление). Метод take off должен изменить is_flying на True, а land на False. По
# умолчанию поле is_flying = False. Метод fly должен принимать расстояние полета и
# изменять показания одометра (километраж). Создайте 1 объект класса и используйте
# все методы класса.

# class Airplane:

#     def __init__(self, make, model, year, max_speed):
#         self.make = make 
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#         self.odometr = 0 
#         self.is_flying = False
    
#     def take_off(self):
#         self.is_flying = True
#         msg_take = f"{self.make} {self.model} is taken off"
#         return msg_take

#     def fly(self, km):
#         self.odometr+=km
#         msg_fly = f'{self.make} flew {self.odometr} km at speed of {self.max_speed} km/h.'
#         return msg_fly

#     def land(self):
#         self.is_flying = False
#         self.odometr = self.odometr
#         msg_land = f"{self.make} has landed. odometer shows {self.odometr}km"
#         return msg_land

# fly = Airplane(input('Название самолета'), input('Модель'), input('год выпуска'), int(input('введите высоту')))
# print(fly.take_off())
# print(fly.fly(500))
# print(fly.land())


# 3)Car
# Создайте класс Car. Пропишите в конструкторе параметры make, model, year,
# odometer, fuel. Пусть у показателя odometer будет первоначальное значение 0,
# а у fuel 70. Добавьте метод drive, который будет принимать расстояние в км. В
# самом начале проверьте, хватит ли вам бензина из расчета того, что машина
# расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние,
# то пусть этот метод добавляет эти километры к значению одометра, но не
# напрямую, а с помощью приватного метода __add_distance. Помимо этого
# пусть метод drive также отнимет потраченное количество бензина с помощью
# приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s
# drive!”. Если же бензина не хватит, то распечатайте “Need more fuel, please, fill
# more!”

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make 
#         self.model = model
#         self.year =year 
#         self.odometer = 0
#         self.fuel = 70

#     def drive(self, distance):
#         fuel = distance / 10
#         if self.fuel >= fuel:
#             self.__add_distance(distance)
#             self.__substract_fuel(fuel)
#             print('Let’s drive!')
#         else:
#             print('Need more fuel, please, fill more!')

#     def __add_distance(self, distance):
#         self.odometer +=distance
#     def __substract_fuel(self, fuel):
#         self.fuel -= fuel

# d = Car('honda', 'accord', 2002)
# print(f"{d.make}, {d.model} {d.year} ", d.drive(300))





# 4)ContactList
# Создайте класс ContactList, который должен наследоваться от
# встроенного класса list. В нем должен быть реализован метод
# search_by_name, который должен принимать имя, и возвращать список
# всех совпадений. Замените all_contacts = [ ] на all_contacts =
# ContactList(). Создайте несколько контактов, используйте метод
# search_by_name.

#################


# 5)AK-47
# Soldier Ryan has an AK47
# Soldiers can fire ("tigi-tigitishh").
# Guns can fire bullets.
# Guns can fill bullets - increase the number of bullets(reloads)
# Create class Act_of_Shooting, which will inheritates from class Soldier, class Guns.
# Where soldier will fire from a gun and reload, and fire one more time.

class Soldier:
    def __init__(self, name):
      self.name = name

class Gun:
    def bullet(self):
        bullets = 35

    def AK47(self):
        print(f'soldier {self.name} is shooting!!!')
        if self.bullets:
            for i in range(self.bullets):
                print('tigitishh')
        else:
            print('No more bullets!')
    
    def reload(self):
        self.bullets = 45
        print('Reloaad!')
        print(f'Reload is ready! {self.bullets}')
    
class Act_of_Shooting(Soldier, Gun):
    def __init__(self):
        Soldier.__init__(self)
        Gun.__init__(self)

tah_tah = Act_of_Shooting('Ryan')
print(tah_tah.AK47)