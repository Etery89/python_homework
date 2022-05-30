"""Реализовать возможность переустановки значения цены товара в родительском классе.
Проверить, распечатать информацию о товаре.
"""

class ItemDiscount:
    __name = "item"
    __price = 1000

    def get_parent_data(self):
        print(f"{self.__name} {self.price}")

    def get_price(self):
        return self.__price

    def set_price(self, value):
        self.__price = value

    price = property(fget=get_price, fset=set_price)



class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        super().get_parent_data()


if __name__ == "__main__":
    ItemDiscount.price = 2000
    print(ItemDiscount.price)
    print(ItemDiscount.__dict__)
    item_report = ItemDiscountReport()
    print(ItemDiscountReport.__dict__)
    print(item_report.__dict__)
    print(item_report.price)
    item_report.get_parent_data()