from models import Car
from mixins import JsonMixin, CreateMixin, ListingMixin, UpdateMixin, DeleteMixin


class Crud(JsonMixin, CreateMixin, ListingMixin, UpdateMixin, DeleteMixin):
    _model = Car


    def help(self):
        print(
            """
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