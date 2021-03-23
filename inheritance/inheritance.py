from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self._name = name
        self._cart = []

    @abstractmethod
    def purchase(self, item, quantity):
        return

    def get_name(self):
        return self._name

    def show_cart_total(self):
        total = 0
        for item,quantity in self._cart:
            total += item.get_price()* quantity
        return f"{total:.2f}"


class Dealer(Person):
    def __init__(self, name, discount):
        super().__init__(name)
        self._discount = discount

    def purchase(self, item, quantity):
        item.discount(self._discount)
        self._cart.append([item, quantity])

class Retail_Customer(Person):
    def purchase(self, item, quantity):
        self._cart.append([item, quantity])
        #print(self._cart)

class Item():
    def __init__(self,name,price):
        self._name = name
        self._price = price

    def discount(self,percentage_off):
        self._price *= (100-percentage_off)/100
        self._price = round(self._price, 2)

    def get_price(self):
        return self._price

robbie = Retail_Customer('Robbie')
print(robbie.get_name())

jaren = Dealer('Jaren', 25)
print(jaren.get_name())

teddyBear = Item('Teddy Bear', 24.99)
teddyBear2 = Item('Teddy Bear', 24.99)
rose = Item('Rose', 1.99)
rose2 = Item('Rose', 1.99)

jaren.purchase(rose, 12)
jaren.purchase(teddyBear, 1)
print(jaren._cart)
print(jaren.show_cart_total())

robbie.purchase(teddyBear2, 1)
robbie.purchase(rose2, 12)
print(robbie._cart)
print(robbie.show_cart_total())
