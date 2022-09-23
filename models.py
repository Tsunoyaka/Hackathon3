from utils import Id


class Car:
    def __init__(self, 
    mark: str,
    model: str, 
    issue: int, 
    body_type: int,
    eng_volume: float,
    color: str, 
    milage: int,
    price: float,
    comment = 'Комментарий отсутствует'
    ):
        self.id = Id().id_
        self.mark = mark
        self.model = model
        self.issue = issue
        self.eng_volume = eng_volume
        self.color = color
        self.body_type = body_type
        self.milage = milage
        self.price = price
        self.comment = comment
           
    @property
    def as_dict(self):
        self.__dict__
        return self.__dict__
