from models import Car
from mixins import JsonMixin, CreateMixin, ListingMixin, UpdateMixin, DeleteMixin
from parsing import ModelParse

class Crud(JsonMixin, CreateMixin, ListingMixin, UpdateMixin, DeleteMixin, ModelParse):
    _model = Car


    def help(self):
        print(
            """
            parsing - парсинг
            create - создание записи
            list - список записей
            details - получение одной записи
            update - обновление записи
            delete - удаление записи
            help - список команд
            quit - выход
            """

        )

    def start(self):
        commands = {
            'parsing': self.parse_model_from_cards,
            'create': self.create,
            'list': self.get_cars_list,
            'details': self.get_car_by_id,
            'update': self.update,
            'delete': self.delete,
            'help': self.help
        }
        while True:
            try:
                command = input('Введите команду или help для списка команд: ').lower().strip()
                if command in commands:
                    if command == 'parsing':
                        print("""
                        ----------------------------
                        Подождите окончания парсинга
                        ----------------------------
                        """)
                    commands[command]()
                elif command == 'quit':
                    print('Выход')
                    break
                else:
                    print('Такой команды нет')
            except ValueError:
                print('Произошла ошибка')

car = Crud()
car.start()