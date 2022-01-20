# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         print('Основной метод')

# class American(Person):
#     def talk(self):
#         return 'Hello, do you speak English?'

# class Russian(Person):
#     def talk(self):
#         return 'Привет говоришь по русски?'

# tourist = [American('Beka'), Russian('Вова')]

# print(tourist(American), (Russian))

# class A:
#     def ogo(self):
#         print('im the main method')
#     def ss(self):
#         print('sassas')
# class B(A):
#     def ogo(self):
#         print('I redefine the method')
# s = B()
# s.ogo()
# s.ss()

# class Parrot:
#     def fly(self):
#         print('i can fly')
#     def swim(self):
#         print('i cant swim')
# class Penguin:
#     def fly(self):
#         print('i cant fly')
#     def swim(self):
#         print('i can swim')
# def fly_test(a):
#     a.fly()
# def swim_test(b):
#     b.swim()
# a = Parrot()
# b = Penguin()
# fly_test(a)
# fly_test(b)
# swim_test(a)
# swim_test(b)

# class Country:
#     def capital(self):
#         print('Я столица')
#     def language(self):
#         print('Я язык')
#     def types(self):
#         print('типы')

# class India(Country):
#     def capital(self):
#         print('Нью дели столица Индии')
#     def language(self):
#         print('Основной язык индусский')
#     def types(self):
#         print('Страна блогеров разработчиков')
# class USA(Country):
#     def capital(self):
#         print('Вашингтон столица США')
#     def language(self):
#         print('Основной языка англ')
#     def types(self):
#         print('Страна технологий')
# s = USA()
# s.capital()
# s.language()
# s.types()
# a = India()
# a.capital()
# a.language()
# a.types()

# class House:
#     def __init__(self, Household_type = 'Mansion', total_area = 200, furniture = []):
#         self.Household_type = 'Mansion'
#         self.total_area = 200
#         self.furniture = furniture 

# class Furniture(House):
#     def fur(self, bed = {'bed': 4}, wardrobe = {'wardrobe': 2}, table = {'table' : 1.5}):
#         self.furniture.append(bed)
#         self.furniture.append(wardrobe)
#         self.furniture.append(table)
#         self.total_area = 200

        if self.total_area:
            for i in self.furniture:
                for o in i.keys():
                    self.total_area -= i.get(o)
                    print(i.get(o))
            return self.total_area
        else:
            print('Error Occccurreed')

# h = House()
# f = Furniture()
# print(f"{h.Household_type} {h.total_area} we add to the house the following furnitures ")
# print(f.fur())


# Students room:
# Implement Students room using OOP:
# Copy
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>


# class Room:
#     def __init__(self):
#         self.Steve = ("Steven Schultz", 23, "English")
#         self.Jonhy = ("Jonathan Rosenberg", 24, "Biology")
#         self.Penny = ("Penelope Meramveliotakis", 21, "Physics")

# class Act(Room):
#     def SteveS(self):
#         print (f"name: {self.Steve[0]} age: {self.Steve[1]} major: {self.Steve[2]}")
#     def JonhyR(self):
#         print(f"name: {self.Jonhy[0]} age: {self.Jonhy[1]} major: {self.Jonhy[2]}")
#     def PennyM(self):
#         print(f"name: {self.Penny[0]} age: {self.Penny[1]} major: {self.Penny[2]}")

# a = Act()
# print(a.SteveS())
# print(a.JonhyR())
# print(a.PennyM())


#####################

# Deck of Cards:
# Create a deck of cards class. Internally, the deck of cards should use another class, a card class. 
# Your requirements are:

# The Deck class should have a deal method to deal a single card from the deck
# After a card is dealt, it is removed from the deck.
# # There should be a "mix" method which make sure the deck of cards has all 52 cards and then 
# rearrange them randomly.
# The card class must have a suit (hearts, diamonds, clubs, spades) and a value
# (A, 2,3,4,5,6,7,8,9,10, J, Q, K)
# Note: use random shuffle

from random import shuffle, choice, sample

class Deck_of_Cards:
    def __init__(self):
        self.cards = {
            'hearts': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'],
            'diamonds': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'],
            'clubs': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'],
            'spades': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        }
    
    def deal(self):
        self.player_1 = []
        for i in self.cards:
            for x in i.keys().get(x):
                self.player_1.append(sample(x, 6))
                if len(self.player_1) == 6:
                    break
                print(self.player_1)


class Cards(Deck_of_Cards):
    pass

d = Deck_of_Cards()
print(d.deal())