from collections import Counter


class Checkout(object):
    def __init__(self, inventory):
        self.__inventory = inventory
        self.__order = []

    def scan(self, item):
        self.__order.append(item)

    def get_total(self):
        total = 0

        counted_order = Counter(self.__order)

        for key in counted_order.keys():
            quantity = counted_order[key]
            if "special_price" in self.__inventory[key]:
                count_special_price_group = \
                    quantity / self.__inventory[key]["special_price"]["quantity"]
                total += \
                    count_special_price_group * \
                    self.__inventory[key]["special_price"]["price"]

                quantity = \
                    quantity % self.__inventory[key]["special_price"]["quantity"]

            total += quantity * self.__inventory[key]["price"]

        return total