"""Реализовать расчет цены товара со скидкой.
Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса (метод __init__,
в который должна передаваться переменная — скидка), и перегрузку метода __str__ дочернего класса.
В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
(вторая и третья строка после объявления дочернего класса). 
"""

class ItemDiscount:
    __name = "item"
    __price = 1000

    def __init__(self):
        self.discount = None

    def get_parent_data(self):
        print(f"{self.__name} {self.price}")

    def get_price(self):
        return self.__price

    def set_price(self, value):
        self.__price = value

    price = property(fget=get_price, fset=set_price)



class ItemDiscountReport(ItemDiscount):

    def __init__(self, discount):
        super().__init__()
        self.discount = discount

    def get_parent_data(self):
        super().get_parent_data()

    def __str__(self):
        return f'{self.price - self.price * (self.discount / 100)}'


if __name__ == "__main__":
    item = ItemDiscount()
    item_report = ItemDiscountReport(15)
    print(item_report)