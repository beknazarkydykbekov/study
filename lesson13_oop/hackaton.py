# задание 2
# Напишите программу Logger.
# Это может быть либо функцией либо методом класса.
# Функция должна делать следующее:
# 1. Принимать Логин, Пароль1 и Пароль2.
# 2. Проверять если Логин меньше 5 символов возвращать пользователю что Логин слишком короткий.
# 3. Если Логин указан верно запустить бесконечный цикл для запроса пароля. 
# Пока пользователь не введёт верный пароль спрашивать снова и снова.
# 4. Проверять если Пароль меньше 8 символов выводить на экран пользователю что Пароль слишком короткий.
# 5. Проверять если Пароль1 НЕ равен Пароль2 выводить на экран пользователю что пароли не совпадают.
# 6. Если все данные верны создайте файл users.txt и запишите туда Логин и Пароль пользователя в формате: 
# Логин: <Логин Пользователя> - Пароль: <Пароль Пользователя>
# 7. Информацию о Всех Успешно Зарегистрированных Пользователей вносите в другой файл log.txt в формате: 
# "Пользователь успешно зарегистрирован <ВРЕМЯ>"
# Время должно быть в формате: <ЧАС>:<МИНУТЫ>:<СЕКУНДЫ>.<ТЫСЯЧНЫЕ СЕКУНДЫ>
# from datetime import datetime
# class Logger:
#     def autorization(self):
#         while True:
#             self.login = input('Ваш логин: ')
#             self.password_1 = input('Ваш пароль: ')
#             self.password_2 = input('Подтвердите пароль.')          
#             a = True
#             if len(self.login) < 5:
#                 a = False
#                 print('Логин слишком короткий!')
#             if len(self.password_1) < 8:
#                 a = False
#                 print('Ваш пароль слишком короткий!')
#             try:
#                 current_datetime = datetime.now()
#                 date = str(current_datetime.hour)+'-'+str(current_datetime.minute)+'-'+str(current_datetime.second)+'-'+str(current_datetime.microsecond)  
#                 if self.password_2 == self.password_1 and len(self.login) >= 5 and len(self.password_1) >=8:
#                     with open('users.txt', 'a') as file:
#                         file.writelines(f'Логин пользователя: {self.login}. Пароль пользователя: {self.password_1} Пользователь успешно зарегистрирован: {date}\n')
#                     print('Вы успешно зарегистрировались!')
#                 elif self.password_1 != self.password_2:
#                     a = False
#                     print('Пароли не совпадают!')
#             except:
#                 print('Error')
#             if a:
#                 break

# start = Logger()
# start.autorization()



# Задание 3:
# Перейдите по ссылке в Google Colab и используйте набор данных под кодовым названием - user_data.
# Создайте класс который будет принимать эти данные как аргумент.
# 1.Создайте метод genders() который вернёт всё разнообразие полов в типе данных Tuple.
# Example: ("Male", "Female",...)
# 2. Создайте метод get_domain() который возвращает Tuple ДОМЕННЫХ имён электронной почты ВСЕХ пользователей.
# Что такое доменное имя:
# python.itc@gmail.com
# 1. ИМЯ ПОЧТЫ - python.itc
# 2. РАЗДЕЛИТЕЛЬНЫЙ СИМВОЛ - @
# 3. ДОМЕННОЕ ИМЯ - gmail.com




# class GetCertainValue:
#     def __init__(self):
#         self.user_data = [{
#         "id": 1,
#         "first_name": "Humphrey",
#         "last_name": "Wilcox",
#         "email": "hwilcox0@odnoklassniki.ru",
#         "gender": "Male",
#         "ip_address": "80.232.175.95"
#         }, {
#         "id": 2,
#         "first_name": "Erhard",
#         "last_name": "Byart",
#         "email": "ebyart1@addthis.com",
#         "gender": "Male",
#         "ip_address": "125.7.237.155"
#         }, {
#         "id": 3,
#         "first_name": "Brok",
#         "last_name": "Leiden",
#         "email": "bleiden2@usnews.com",
#         "gender": "Male",
#         "ip_address": "108.201.248.102"
#         }, {
#         "id": 4,
#         "first_name": "Gradeigh",
#         "last_name": "Spreckley",
#         "email": "gspreckley3@marriott.com",
#         "gender": "Male",
#         "ip_address": "90.169.195.245"
#         }, {
#         "id": 5,
#         "first_name": "Trueman",
#         "last_name": "McArd",
#         "email": "tmcard4@cargocollective.com",
#         "gender": "Male",
#         "ip_address": "249.26.239.198"
#         }, {
#         "id": 6,
#         "first_name": "Giacobo",
#         "last_name": "Rishworth",
#         "email": "grishworth5@merriam-webster.com",
#         "gender": "Male",
#         "ip_address": "156.104.68.219"
#         }, {
#         "id": 7,
#         "first_name": "Marcia",
#         "last_name": "Burney",
#         "email": "mburney6@gmpg.org",
#         "gender": "Female",
#         "ip_address": "52.104.185.232"
#         }, {
#         "id": 8,
#         "first_name": "Court",
#         "last_name": "Haysar",
#         "email": "chaysar7@eepurl.com",
#         "gender": "Hidden",
#         "ip_address": "60.138.180.175"
#         }, {
#         "id": 9,
#         "first_name": "Penn",
#         "last_name": "Slatten",
#         "email": "pslatten8@narod.ru",
#         "gender": "Male",
#         "ip_address": "216.91.212.228"
#         }, {
#         "id": 10,
#         "first_name": "Rayna",
#         "last_name": "Jacobsson",
#         "email": "rjacobsson9@4shared.com",
#         "gender": "Female",
#         "ip_address": "158.81.126.17"
#         }, {
#         "id": 11,
#         "first_name": "Elissa",
#         "last_name": "Milch",
#         "email": "emilcha@ucoz.ru",
#         "gender": "Female",
#         "ip_address": "160.46.17.104"
#         }, {
#         "id": 12,
#         "first_name": "Cissiee",
#         "last_name": "Dever",
#         "email": "cdeverb@dailymail.co.uk",
#         "gender": "Hidden",
#         "ip_address": "198.12.171.92"
#         }, {
#         "id": 13,
#         "first_name": "Lorie",
#         "last_name": "Cavozzi",
#         "email": "lcavozzic@apache.org",
#         "gender": "Female",
#         "ip_address": "252.228.114.151"
#         }, {
#         "id": 14,
#         "first_name": "Shelton",
#         "last_name": "Pipe",
#         "email": "spiped@opera.com",
#         "gender": "Male",
#         "ip_address": "217.193.203.141"
#         }, {
#         "id": 15,
#         "first_name": "Cordell",
#         "last_name": "Hrinchenko",
#         "email": "chrinchenkoe@ovh.net",
#         "gender": "Transgender",
#         "ip_address": "147.76.167.191"
#         }, {
#         "id": 16,
#         "first_name": "Dyanna",
#         "last_name": "Sizzey",
#         "email": "dsizzeyf@xing.com",
#         "gender": "Female",
#         "ip_address": "8.177.20.12"
#         }, {
#         "id": 17,
#         "first_name": "Felice",
#         "last_name": "Floyed",
#         "email": "ffloyedg@instagram.com",
#         "gender": "Male",
#         "ip_address": "4.150.254.58"
#         }, {
#         "id": 18,
#         "first_name": "Arel",
#         "last_name": "Donoher",
#         "email": "adonoherh@youtu.be",
#         "gender": "Male",
#         "ip_address": "186.214.243.230"
#         }, {
#         "id": 19,
#         "first_name": "Kristoffer",
#         "last_name": "Carvill",
#         "email": "kcarvilli@xinhuanet.com",
#         "gender": "Male",
#         "ip_address": "58.204.72.103"
#         }, {
#         "id": 20,
#         "first_name": "Norbie",
#         "last_name": "Oleksinski",
#         "email": "noleksinskij@free.fr",
#         "gender": "Male",
#         "ip_address": "242.192.49.216"
#         }]
#     def genders(self):
#         self.results = [ item['gender'] for item in self.user_data ]
#         print(self.results)
    
#     def get_domein(self):
#         self.domein_result = [item ['email'] for item in self.user_data ]
#         self.res = str(self.domein_result).split('@')
#         self.s = []
#         self.s.append(self.res)
#         print(tuple(self.s))
# Start = GetCertainValue()
# Start.genders()
# Start.get_domein()


# # Задание 7:
# Создайте функцию которая возвращает список 10 любых Linux команд.
# Вызовите вашу функцию и сохраните её в переменную.
# Затем удалите ТОЛЬКО функцию так ЧТОБЫ при втором запуске вашего файла не было ошибок NameError.
# Переменную не удаляйте!

try:
    # def linux_commands():
    commands = ['mkdir', 'rmdir', 'pwd', 'touch', 'ls', 'cat', 'cd', 'rm', 'sudo', 'find']
    # print(commands)

    a = linux_commands()
except NameError:
    print(commands)
