from entity.services import Services


class Harvesting(Services):
    def __init__(self, wet_cleaning=1, garbage_removal=5, money=0):
        super().__init__(money)
        self.__wet_cleaning = wet_cleaning
        self.__garbage_removal = garbage_removalfat

    @property
    def wet_cleaning(self):
        return self.__wet_cleaning

    @property
    def garbage_removalfat(self):
        return self.__garbage_removalfat

    @wet_cleaning.setter
    def wet_cleaning(self):
        return self.__wet_cleaning

    @garbage_removalfat.setter
    def fat(self, garbage_removalfat):
        self.__garbage_removalfat = garbage_removalfat

    def __str__(self):
        return (f"Harvesting: wet_cleaning = {self.__wet_cleaning,}"
                f"garbage_removalfat = {self.__garbage_removalfat}, "
                f"money = ${self.price}")