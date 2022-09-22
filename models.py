from utils import Id


class CarParsing:
    def __init__(self, 
    mark: str,
    model: str, 
    issue: int, 
    body_type,
    eng_volume,
    color: str, 
    price):
        self.id = Id().id_
        self.mark = mark
        self.model = model
        self.issue = issue
        self.eng_volume = eng_volume
        self.color = color
        self.body_type = body_type
        self.price = price
           
    @property
    def as_dict(self):
        self.__dict__
        return self.__dict__

class Car(CarParsing):
    def __init__(self, mark: str, model: str, issue: int, body_type, milage, eng_volume, color: str, price):
        super().__init__(mark, model, issue, body_type, eng_volume, color, price)
        self.milage=milage
        


# a = Car()


    # def __init__(
    # self, 
    # mark: str,
    # model: str, 
    # b_data: int, 
    # eng_volume, 
    # color: str, 
    # milage: int, 
    # price
    # ):
    #     self.id = Id().id_
    #     self.mark = mark
    #     self.model = model
    #     self.b_data = b_data
    #     self.eng_volume = eng_volume
    #     self.color = color
    #     self.body_type = BodyType().body()
    #     self.milage = milage
    #     self.price = price
        
        