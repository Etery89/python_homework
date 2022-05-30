"""Инкапсулировать оба параметра (название и цену) товара родительского класса. 
Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения. 
Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным. 
"""

class ItemDiscount:
    __name = "item"
    __price = 1000

    def get_parent_data(self):
        print(f"{self.__name} {self.__price}")


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        super().get_parent_data()


if __name__ == "__main__":
    item = ItemDiscount()
    item_report = ItemDiscountReport()
    item_report.get_parent_data()