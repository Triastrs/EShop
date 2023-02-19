import poetry
import pytest
class item:
    price_discount = 0.85

    def __init__(self,item_name,item_price,item_amount):
        self.item_name = item_name
        self.item_price = item_price
        self.item_amount = item_amount


    def calculate_total_price(self):
        print(self.item_price * self.item_amount)


    def apply_discount(self):
        print(self.item_price * self.price_discount)


item1 = item("Смартфон", 10000, 20)
item2 = item("Ноутбук", 20000, 5)

item1.calculate_total_price()
item2.calculate_total_price()

item.price_discount = 0.8
item1.apply_discount()
print(item2.item_price)