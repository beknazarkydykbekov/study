from bs4 import BeautifulSoup
import requests

def save():
    with open('sulpak_nout.txt', 'a') as file:
        file.writelines(f"Название: {comp['title']}, Цена: {comp['price']}\n, Ссылки: {comp['link']}")

def parce():
    URL = 'https://www.sulpak.kg/f/noutbuki'
    HEADERS = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'
    }
    response = requests.get(URL, headers=HEADERS, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_="goods-tiles")
    comps = []
    print(items)

    for item in items:
        try:
            comps.append({
                'title': item.find('h3', class_='title').get_text(strip=True),
                'price': item.find('div', class_='price-block').get_text(strip=True),
                'link': URL+item.find('div', class_='product-container-right-side').find('a').get('href')
            })
        except:
            pass

    global comp
    for comp in comps:
        print(f"Название: {comp['title']}, Цена: {comp['price']}, Ссылки: {comp['link']}")
        save()

parce()