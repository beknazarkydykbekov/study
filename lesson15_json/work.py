# import json 
# with open('load.json', 'r') as json_file:
#     a = json.load(json_file)
# del a['data']['date_joined']
# a['people']=['aybek', {'email':'aybek@mail.ru'}]
# print(json.dumps(a, indent=4))

# with open('load.json', 'w') as json_file:
#     json.dump(a, json_file, indent=2)
 

# username = input('names:')
# filename = 'user.json'

# with open(filename, 'a', encoding='utf-8') as f:
#     json.dump(username, f)
#     print('hello'+ username+'!')


# import json
# login = input('login:')
# password = input('password:')

# file_name = 'authentication.json'
# n = [f"'login':{login}, 'password'{password}"]
# print(n)
# with open(file_name, 'w', encoding='utf-8') as f:
#     json.dump(n, f)

# with open(file_name, 'r', encoding='utf-8') as fl:
#     a = json.load(fl)
# print(a)
 
import json
c = [{'user':{'login': 'admin', 'email': 'admin@gmail.com', 'age': 19, 'phone': 3843939430, 'language': 'python'}}]
with open('joystick.json', 'w', encoding='utf-8') as file:
    data = json.dump(c, file, indent=4)

name = input('enter your name:' )
lastname = input('enter your lastname')
for item in data['user']:
    item['language'] = item['language'].replace(name, lastname)

# item['iscategorical'] = item['iscategorical'].replace('$home', item['id'])