from entity.services import Services


class List:
    def __init__(self, services=None):
        if products:
            self.__services = services
        else:
            self.__services = []

    @property
    def size(self):
        return len(self.__services)

    def get_services(self, index):
        if (isinstance(index, int)
                and index >= 0 and index < self.size):
            return self.__services[index]

    def add(self, services):
        if isinstance(services, Services):
            self.__services.append(services)

    def __str__(self):
        msg = "List of services:"

        for i in range(self.size):
            msg += f"\n{i + 1}) " + str(self.__services[i])

        return msg