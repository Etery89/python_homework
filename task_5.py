"""Проверить на практике возможности полиморфизма.
Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно.
Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены.
Далее реализовать вызов каждой из функции get_info.
"""

from unicodedata import name


class ItemDiscount:
    __name = "item"
    __price = 1000

    def get_parent_data(self):
        print(f"{self.name} {self.price}")

    def get_price(self):
        return self.__price

    def set_price(self, value):
        self.__price = value

    price = property(fget=get_price, fset=set_price)

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    name = property(fget=get_name, fset=set_name)



class ItemPriceReport(ItemDiscount):

    def get_parent_data(self):
        return super().get_parent_data()

    def get_info(self):
        print(f"{self.price}")


class ItemNameReport(ItemDiscount):

    def get_parent_data(self):
        return super().get_parent_data()

    def get_info(self):
        print(f"{self.name}")


if __name__ == "__main__":
    item_reports = [ItemNameReport(), ItemPriceReport()]
    for item_report in item_reports:
        item_report.get_info()
