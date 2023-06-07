from entity.services import Services


class Painting(Services):
    def __init__(self, color='black', price=0):
        super().__init__(price)
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def __str__(self):
        return (f"Bread: color = {self.__color}, "
                f"price = ${self.price}")