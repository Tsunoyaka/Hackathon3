import json
from pprint import pprint
from utils import BodyType, name


class JsonMixin:

    def get_db(self):
        try:
            with open(f'{name}', 'r') as file:
                return json.load(file)
        except json.decoder.JSONDecodeError:
            return {'Cars': [], 'cars_counter': 0}
    def write_to_db(self, data):
        with open(f'{name}', 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)



class CreateMixin:
            
    def create(self):
        mark = str(input('Марка: '))
        model = str(input('Модель: '))
        issue = int(input('Год выпуска: '))
        eng_volume = format(float(input('Объем двигателя: ')), '.1f')
        color = str(input('Цвет: '))
        milage = int(input('Пробег: '))
        price = format(float(input('Цена: ')), '.2f')
        car = self._model(mark=mark, model=model, issue=issue, eng_volume=float(eng_volume), 
        color=color, body_type=BodyType().body(), milage=milage, price=float(price))
        get_db = self.get_db()
        get_db['Cars'].append(car.as_dict)
        get_db.update(cars_counter=len(get_db['Cars']))
        self.write_to_db(get_db,)
        print('Успешно создано')


class ListingMixin:
    
    def get_cars_list(self):
        data = self.get_db()
        pprint(data, sort_dicts=False)

    def get_car_by_id(self):
        id = input('Введите id: ')
        data = self.get_db()
        car = data['Cars']
        for machine in car:
            if machine['id'] == id:
                pprint(machine, sort_dicts=False)
                return machine



class UpdateMixin:

    def update(self):
        cars = self._model
        data = self.get_db()
        car = self.get_car_by_id()
        if car is not None:
            data['Cars'].remove(car)
            mark = str(input('Марка: ')) or car['mark']
            model = str(input('Модель: ')) or car['model']
            issue = int(input('Год выпуска: ')) or car['issue']
            eng_volume = format(float(input('Объем двигателя: ')), '.1f') or car['eng_volume']
            color = str(input('Цвет: ')) or car['color']
            body_type = str(input('Тип кузова: ')) or car['body_type']
            milage = int(input('Пробег: ') or car['milage'])
            price = format(float(input('Цена: ')), '.2f') or car['price']
            new_car = cars(mark=mark, model=model, issue=issue, eng_volume=eng_volume, 
            color=color, body_type=body_type, milage=milage, price=float(price))
            new_car.__dict__['id'] = car['id']
            data['Cars'].append(new_car.as_dict)
            self.write_to_db(data)
            print('Данные машины обновлены!')
        else:
            print('Машины под таким id не существует')

class CommentMixin:
    def comment(self):
        cars = self._model
        data = self.get_db()
        car = self.get_car_by_id()
        a = input('Оставьте комментарий: ')
        if car is not None:
            data['Cars'].remove(car)
            mark = car['mark']
            model = car['model']
            issue = car['issue']
            eng_volume = car['eng_volume']
            color = car['color']
            body_type = car['body_type']
            milage = car['milage']
            price = car['price']
            new_car = cars(mark=mark, model=model, issue=issue, eng_volume=eng_volume, 
            color=color, body_type=body_type, milage=milage, price=float(price),comment=a)
            new_car.__dict__['id'] = car['id']
            data['Cars'].append(new_car.as_dict)
            self.write_to_db(data)
            print('Комментарий успешно добавлен')
        else:
            print('Машины под таким id не существует')


class DeleteMixin:

    def delete(self):
        data = self.get_db()
        car = self.get_car_by_id()
        if car is not None:
            data['Cars'].remove(car)
            data.update(cars_counter=len(data['Cars']))
            self.write_to_db(data)
            print('Успешно удалено')