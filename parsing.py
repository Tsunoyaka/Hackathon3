import requests
from bs4 import BeautifulSoup
from bs4 import Tag, ResultSet

from models import CarParsing
from mixins import JsonMixin
from utils import HOST, Categor, HEADERS
json_ = JsonMixin()


def get_html(url: str, category: str, headers: dict='', params: str=''):
    """ Функция для получения html кода """
    html = requests.get(
        url + category,
        headers=headers,
        params=params,
        verify=False
    )
    return html.text


def get_card_from_html(html: str):
    """ Функция для получения карточек из html кода """
    soup = BeautifulSoup(html, 'lxml')
    cards: ResultSet = soup.find_all('div', class_='list-item list-label')
    return cards
    


class ModelParse:
    def parse_model_from_cards(self, cards):
        """ Фильтрация данных из карточек """
        _model = CarParsing
        get_db = json_.get_db('parse_db.json')
        for card in cards:
            obj = _model(
            mark=card.find('h2', class_='name').text.strip().split()[0],
            model=card.find('h2', class_='name').text.strip(), 
            issue=int(card.find('p', class_='year-miles').find('span').text.replace(' г.', '')),
            eng_volume=float(card.find('p', class_='year-miles').text.split(',')[1].replace('л.', '')),
            color=None,
            body_type=card.find('p', class_='body-type').text.strip().split(',')[0].capitalize(),
            price=float(card.find('p', class_='price').find('strong').text.lstrip('$').replace(' ', ''))
            )
            get_db['Cars'].append(obj.as_dict)
            get_db.update(cars_counter=len(get_db['Cars']))
        print('Парсинг прошел успешно!')
        return json_.write_to_db(get_db, 'parse_db.json')

if __name__ == '__main__':
    html = get_html(HOST, Categor, HEADERS)
    cards= get_card_from_html(html)
    parsing = ModelParse()
    parsing.parse_model_from_cards(cards)