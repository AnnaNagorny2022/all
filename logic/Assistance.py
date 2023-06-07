from entity.services import Services
from container.list import List


class Assistance:
    @staticmethod
    def calculate_total_price(assistance):
        if isinstance(list, List) and list.size != 0:
            total = 0
            for i in range(list.size):
                services = list.get_services(i)

                if isinstance(services, Services):
                    total +=services.price

            return total
        else:
            return 0