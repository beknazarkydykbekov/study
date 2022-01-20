# import os 
# file  = input("How do you want to name the file? ")
# def create_file(file):
#     os.mknod(file)
# create_file(file)




# list = ['s','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s']
# def nel(list):
#     q =0
#     for i in list:
#         q+=1
#     return q

# s = nel(list)
# print(s)



# list_1 = ['name', 'age', '1', '19']
# def visa_versa(l):
#     c = l[:len(l) //2]
#     d =list(reversed(c))
#     s = l[len(l)//2:]
#     f  =list(reversed(s))
#     print(d+f)
# visa_versa(list_1)





# fibonaci#############################
# a = int(input('Give amount: '))

# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b

# print(list(fib(a)))


# a = int(input('Give amount: '))
# f1 = 1
# f2 = 1
# n =0
# while n <= a:
#     print(f1, f2, end=" ")
#     f1, f2 = f2, f1+f2
#     n += 1
#     print(f2)
################################################





# 3
# def plus():
#     a = int(input())
#     b = int(input())
#     result = a+b
#     print("the sum of the two numbers: ", result)
#     return result

# ## print(plus())


# def minus():
#     a = int(input())
#     b = int(input())
#     result = a-b
#     print("the result of subtraction: ", result)
#     return result

# # #print(minus())


# def plunus():
#     return plus(),  minus()

# print(plunus())




# SECOND PART#######################################################################################
# 1
# def add():
#     a = int(input("number: "))
#     v = int(input("number: "))
#     result = a+v
#     print(result)
#     return result 



# def substract():
#     c = int(input("number: "))
#     x = int(input("number: "))
#     result = c-x
#     return result


# def multiply():
#     w = int(input("number: "))
#     z = int(input("number: "))
#     result = w*z
#     return result

# def divide(num, number):
#     result = num/number
#     return result

# #print(divide(100, 5))




# 2
# def lenchik():
#     sentence = input("your sentence: ")
#     q = 0
#     for i in sentence:
#         if i == i:
#             q+=1
#     print(q)
#     return q
# lenchik()


# 3 Напишите функцию которая принимает 2 Dictionary и добавляет втрорую Dictionary к первой.
# def add_dic():
#     a = {input("key: " ): input("value: ")}
#     n = {input("key: " ): input("value: ")}
#     a.update(n)
#     print(a)
#     return a 
# add_dic()


# 4 Напишите функцию которая спрашивает у вас чтобы вы хотели заказать покушать и выпить.
# А затем записывает это всё в файл на рабочем столе menu.txt

# def havchik():
#     havka = input()
#     sush = input()
#     f = open("/home/beknazar/Desktop/menu.txt", "w")
#     v = f.write(f"{havka}, \n{sush}")
#     print("vash zakaz: ", havka, "i", sush)
#     return v

# havchik()



# 5 Создайте функцию которая принимает слово и создаёт файл с таким именем в той же директории, 
# где был запущен Ваш .py файл.

# def file():
#     import os
#     d = input("Name your file: ")
#     os.mknod(d)

# file()



# second slide
# 1 Создайте 2 функции где одна функция вложена в другую. Главная функция должна выводить на экран текст:
#"Я главная функция". А вложенная функция должна выводить на экран: "Я вложенная функция."

# def doublefun():
#     print("Я главная функция")
# def secondfun():
#     print("Я вложенная функция.")
# def fun():
#     doublefun()
#     secondfun()

# fun()

# 2 Создайте функцию которая принмает тип данных dictionary, но возвращает два Tuple в одном из них все 
# ключи, в другом только значения.

# def func():
#     dic = {"bruno": 18, "marcus": 10, "jadon": 25}
#     key = ()
#     values = ()
#     key = dict.keys(dic)
#     values = dict.values(dic)
#     return key, values
# print(func())




# 3

# def simple():
#     for num in range(2, 101):
#         prime =True
#         for i in range (2, num):
#             if num % i ==0:
#                 prime = False
#         if prime:
#             print(num)
# simple()



# 1 third slide 

# def relist(a, b):
#     list = []
#     list.append(f"{a}, {b}")
#     return list

# print(relist("aza", "uli"))





# 2 

# def chisla(number):
#     dic = {
#         "1": "one", 
#         "2": "two", 
#         "3": "three", 
#         "4": "four", 
#         "5": "five", 
#         "6": "six", 
#         "7": "seven", 
#         "8": "eight", 
#         "9": "nine", 
#         "10": "ten", 
#     }

#     word = " "
#     for i in str(number):
#         word += dic[i]
#     return word
    
# print(chisla(34))



# 3
# def work(name, zp = 5000):
#     print(f"{name}, vasha zarplata sostovlyaet {zp}")

# work("aza", 10000)



# 4 ___



# PART THREE ################################################################################


# 1 Написать lambda которая принимает 3 параметра и умножает все параметры между собой. 
# Функция должна вернуть строку: "Объём бассейна " и значение которое получилось.

# p = lambda v, c, z: v*c*z
# a = "Объём бассейна"
# print(a, p(2,4,6))



# 2 Написать lambda которая получает сколько дней ПРОШЛО с нового года как параметр и 
# говорит пользователю сколько дней ОСТАЛОСЬ до нового года.

# new_year = lambda v: 365-v
# a = "how many days left until the new year?"
# print(a, new_year(324))



# 3 Напишите программу которая выводит только нечётные числа с помощью рекурсии.

# def evens(a):
#     if a %2 !=0:
#         print(a)
#     if a == 995:
#         return a 
#     evens(a+1)    
  
# evens(1)


# 4 Напишите функцию которая принимает SET и рекурсивно удаляет оттуда по одному элементу при запуске.

# sets = {"aza", "uli", "maks", "bekjan", "bayish", 18, 19, True}
# def setpops(sets):
#     print(sets)
#     for i in sets:
#         sets.remove(i)
#         setpops(sets)
#         return sets

# setpops(sets)


# 2.1 (1)  Напишите функцию которая генерирует 100 рандомных чисел в диапазоне от 10 до 50 и возвращает 
# их в листе. Напишите ДЕКОРАТОР для этой функции которая удалит все дубликаты в первой функции и вернёт
# всё так же лист.


# import random 
# a = []
# def rando(a):
#     ran = 0
#     while ran !=100:
#         v = random.randrange(10, 50)
#         a.append(v)
#         ran +=1
#     return a
# print(rando(a))



# @rando(a)
# def delsimrando():
#     for i in a:
#         a.append(i)
#         if i in a:
#             continue
#     return a


# print(delsimrando())




# 2.2 Напишите функцию которая спрашивает у пользователя login и password. Напишите декоратор который 
# шифрует эти данные и возвращает вам зашифрованные данные. (Можете воспользоваться функцией ord и char, 
# можете загуглить...)




