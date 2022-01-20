# 1
# lang = 'Rust'
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']

# for i in languages:
#     if i == lang:
#         print('this languages is in list') 

# print('No rust in this list')



# 2
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# p = "php"
# i=0
# while languages[i] != p:
#     print(languages[i])
#     i= i + 1 



# 3
# b = 7
# i = 0
# while i <6:
#     print(b*5)
#     i+=1




# 4
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i, item in enumerate(languages):
#     print (i+1, item)


# 5
# i = 0
# while i <=9:
#     print(i, end=' ')
#     i +=1
# while i !=0:
#     print(i, end=' ')
#     i-=1


# 6 

# a = ['Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан']
# b = [v for k,v in enumerate(a) if not k%2]
# print(b) 


# 7
# a = ['Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан']
# print(a[1::2])




# zx = 23
# if zx <=999 and zx >=100:
#     print("Eto chislo trexznachnoe!")
# elif zx <=99 and zx >=10:
#     print("Eto chislo ne trexznachnoe!")
# elif zx >=1:
#     print("Chislo polojitelnoe")
# elif zx <=0:
#     print("Chislo otricatelnoe")
# elif zx%2==0:
#     print("Chislo chetnoe")
# elif zx%2!=0:
#     print("Chislo ne chetnoe")
# else: 
#     print("Vashe chislo ne podlejit nashim usloviam!")


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b =[]
# for i in a:
#     if i <5:
#         print(i)
#         b.append(i)
# print(b)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# v = []
# for i in a:
#     for x in b:
#         if i==x:
#             v.append(i)
# print(v)


# import operator 
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# result = dict(sorted(d.items(), key=operator.itemgetter(1)))
# result2 = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
# print(result2)


# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# f = {12: 1, 22: 2, 3: 33}
# result = {**d, **f}
# print(result)
