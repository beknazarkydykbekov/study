#1######
# values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
# true = []
# try:
#     true.append(set(values))
#     print(true)
# except  TypeError:
#     print("Ошибка типов данных") 


# # 2#####
# listochek = []
# while True:
#     a = int(input("vvedite chislo: "))
#     listochek.append(a)
#     if len(listochek) == 5:
#         break
# print(min(listochek))



# # 3#####
# listik = [12,12,23,4,55,56,666]
# print("Есть следующие данные", listik )
# guest = input("Есть следующие функции - all, max, min, any, reversed.  Выберите один ")
# if guest == "all": 
#     print(all(listik))
# elif guest == "max":
#     print(max(listik))
# elif guest == "min":
#     print(min(listik))
# elif guest == "any":
#     print(any(listik))
# elif guest == "reversed":
#     a = reversed(listik)
#     for i in a:
#         print(i)
# else:
#     print("hah")



# 4########
# su = int(input("Введите сумму займа: "))
# if su >=50000:
#     a =(su*3.47/100)
#     print(round(a, 2))

# else: 
#     print("Значение должно быть выше 50000!")




# 1########################################3
# # 1.1
# try:
#     a = "timosha"
#     b = 19
#     if a>b:
#         print(a)
# except TypeError:
#     print("Проблема в типах данных:( \nПопробуй снова:)")


# # 1.2
# try:
#     united = [1, 19, 6, 18, 11, 10, 7]
#     print(united[7])
# except IndexError:
#     print("Индекс больше диапазона.")



# 1.3
# try:
#     bruno = "fernandes"
#     fernandes = "bruno"
#     print(fernandez, bruno)
# except NameError:
#     print("Enter the right item!")




# 2
# try:
#     at = 10
#     i = 15
#     wo = 20

#     for e in range(-at, at):
#         print(wo / e)
#     if at > 5:
#         print(at > 5)
# except ZeroDivisionError:
#     print("delenie na 0 nevozmojno")


# # 3
# try:
#     lst = []
#     for i in range(10):
#         lst.append(i)

#     a = list(reversed(lst))
#     sls_obj = slice[0:8]
#     print(sls_obj)
# except TypeError:
#     print("Ошибка типов данных! ")

# 4
# a = 10
# b = 1
# numbers = []
# while b <= a:
#     numbers.append(b)
#     b += 1
# print(numbers)


# 1
# try:
#     dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}

#     for x in dict_.keys():
#         x + 'abc'
# except TypeError:
#     print("Ошибка в типах данных, попробуй их измненить. ")
