import requests
from bs4 import BeautifulSoup
from bs4 import Tag, ResultSet

from utils import HOST, Categor, HEADERS



def get_html(url: str=HOST, category: str=Categor, headers: dict=HEADERS, params: str=''):
    """ Функция для получения html кода """
    html = requests.get(
        url + category,
        headers=headers,
        params=params,
        verify=False
    )
    return html.text


def get_card_from_html(html: str=get_html()):
    """ Функция для получения карточек из html кода """
    soup = BeautifulSoup(html, 'lxml')
    cards: ResultSet = soup.find_all('div', class_='list-item list-label')
    return cards
    


class ModelParse:
    def parse_model_from_cards(self, cards=get_card_from_html()):
        """ Фильтрация данных из карточек """
        model = self._model
        get_db = self.get_db()
        for card in cards:
            link: str = "https://www.mashina.kg" + card.find("a").get("href")
            html = requests.get(link).text
            soup = BeautifulSoup(html, 'lxml')
            try:
                milage = int(card.find('p', class_='volume').text.strip().split(',')[1].replace(' ', '')[:-2])
            except:
                milage = 'Не указано'
            obj = model(
            mark=card.find('h2', class_='name').text.strip().split()[0],
            model=card.find('h2', class_='name').text.strip(), 
            issue=int(card.find('p', class_='year-miles').find('span').text.replace(' г.', '')),
            eng_volume=float(card.find('p', class_='year-miles').text.split(',')[1].replace('л.', '')),
            color = soup.find('meta', itemprop='color').get('content').capitalize(),
            body_type=card.find('p', class_='body-type').text.strip().split(',')[0].capitalize(),
            milage = milage, 
            price=float(card.find('p', class_='price').find('strong').text.lstrip('$').replace(' ', ''))
            )
            get_db['Cars'].append(obj.as_dict)
            get_db.update(cars_counter=len(get_db['Cars']))
        print("""
                        ----------------------------
                        Парсинг прошел успешно!
                        ----------------------------
        """)
        return self.write_to_db(get_db)