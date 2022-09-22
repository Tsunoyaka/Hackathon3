from datetime import datetime

class Id:
    def __init__(self) -> None:
        self._id = self.generate_id()

    
    @staticmethod
    def generate_id():
        id = datetime.now().strftime('%M%S%f')[:-2]
        return id

    @property
    def id_(self):
        return self._id
    

class BodyType:

    type_ = ("""
        Выберите тип кузова:
        1 = Седан
        2 = Универсал
        3 = Купе
        4 = Хэтчбек
        5 = Минивен
        6 = Внедорожник
        7 = Пикап
        """)

    def body(self):
        print(self.type_)
        while True:
            num = input('Тип кузова: ')
            if num == '1':
                return 'Cедан'
            elif num == '2':
                return 'Универсал'
            elif num == '3':
                return 'Купе'
            elif num == '4':
                return 'Хэтчбек'
            elif num == '5':
                return 'Минивен'
            elif num == '6':
                return 'Внедорожник'
            elif num == '7':
                return 'Пикап'
            else:
                print('Выберите из вышеперечисленых вариантов')


HOST = 'https://www.mashina.kg/'
Categor = 'commercialsearch/all/?type=6'
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

name = 'db.json'