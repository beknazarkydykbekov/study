from bs4 import BeautifulSoup
import requests

def save():
    with open('macs.txt', 'a') as file:
        file.writelines(f"{macbook}\n {macbook}\n {macbook}")

def parce():
    URL = 'https://softech.kg/noutbuki/apple-macbook/'
    HEADERS = {
        'Accept': '*/*', 
        'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'
    }
    responce = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(responce.content, 'html.parser')
    macs = soup.findAll('div', class_="product-thumb transition")
    macbooks = []

    for mac in macs:
        try:
            macbooks.append({
                'title': mac.find('div', class_="name").get_text(strip=True),
                'price': mac.find('div', class_='price').get_text(strip=True),
                'link': URL+mac.find('div', class_='name').find('a').get('href')
            })
        except: 
            pass

    global macbook 
    for macbook in macbooks:
        print(f"Name: {macbook}, Price: {macbook}, Link: {macbook}")
        save()

parce()