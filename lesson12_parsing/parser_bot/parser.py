import requests
from bs4 import BeautifulSoup

def parce():
    URL = 'https://www.mashina.kg/search/bmw/?currency=2&price_from=&price_to=',
    HEADERS = {
        'Accept': '*/*',
        'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'
    }
    response = requests.get(URL, headers=HEADERS, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_="list-item list-label new-line")
    cars = []

    for item in items:
        try:
            cars.append ({
                'name': item.find('h2', class_='name').get_text(strip=True),
                'title': item.find('div', class_="item-info-wrapper").get_text(strip=True),
                'price': item.find('p', class_='price').get_text(strip=True)
            })
        except:
            print('error')

    print(cars)

parce()