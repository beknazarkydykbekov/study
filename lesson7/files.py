# 1
# files = open("direction.txt", "w")
# b = files.write("books  cdrom  Desktop  Documents  Downloads  githubprofile  Music  Pictures  Public  snap  study  Templates  unitedgit  users.txt  Videos")
# print(b)
# files.close()



# 2
# file = open("users.txt", "a+") 
# name = input("username: ")
# p = input("password: ")
# a = file.write(f'username: {name} \npassword: {p}')
# file.close()




# 3
# with open ("users.txt", "r") as a:
#     if 'w' in a.read():
#         print('est w')
#     elif 'w' not in a.read():
#         print('net w')
#     else:
#         print('я ищу только w ')



# 4
t_words =[]
a = open("python.txt", "w")
b=a.write('''Python is a widely used high-level programming language for general-purpose
programming, created by Guido van Rossum and first released in 1991. An interpreted
language, Python has a design philosophy that emphasizes code readability (notably
using whitespace indentation to delimit code blocks rather than curly brackets or
keywords), and a syntax that allows programmers to express concepts in fewer lines of
code than might be used in languages such as C++ or Java.
''')



