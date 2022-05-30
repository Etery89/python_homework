"""Создать два класса. Первый — родительский (ItemDiscount), должен содержать статическую информацию о товаре: название и цену. 
Второй — дочерний (ItemDiscountReport), должен содержать функцию (get_parent_data), 
отвечающую за отображение информации о товаре в одной строке вида (“{название товара} {цена товара}”). 
Создать экземпляры родительского класса и дочернего. 
Распечатать информацию о товаре."""


class ItemDiscount:
    name = "item"
    price = 1000


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(f"{self.name} {self.price}")


if __name__ == "__main__":
    item = ItemDiscount()
    item_report = ItemDiscountReport()
    item_report.get_parent_data()