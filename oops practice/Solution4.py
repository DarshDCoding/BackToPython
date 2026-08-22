# 4. E-Commerce Product Catalog & Cart System
# Key Concepts: Class Inheritance (`Product` -> `ElectronicsProduct`, `ClothingProduct`), Private attributes (`__price`), Getters/Setters with `@property`.
# Goal: Create a base class `Product` with encapsulated prices. Extend it into specific sub-classes that add unique attributes (e.g., warranty length or clothing size).
#       Build a `ShoppingCart` class that accepts `Product` instances and calculates total tax.

class Product:
    def __init__(self, name:str,price: float, tax:int):
        self.__name = name
        self.__price = price
        self.__tax = tax

    @property
    def price(self):
        return self.__price

    @property
    def taxed_price(self):
        return self.__price + (self.__price*(self.__tax/100))


class ElectronicProduct (Product):
    def __init__(self,name, price, tax, warranty_period:str):
        super().__init__(name, price, tax)
        self.warranty_period = warranty_period

class ClothingProduct (Product):
    def __init__(self,name, price, tax, clothing_size:str):
        super().__init__(name, price, tax)
        self.clothing_size = clothing_size


phone = ElectronicProduct("Phone", 200, 15, "10years")
