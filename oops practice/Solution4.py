# 4. E-Commerce Product Catalog & Cart System
# Key Concepts: Class Inheritance (`Product` -> `ElectronicsProduct`, `ClothingProduct`), Private attributes (`__price`), Getters/Setters with `@property`.
# Goal: Create a base class `Product` with encapsulated prices. Extend it into specific sub-classes that add unique attributes (e.g., warranty length or clothing size).
#       Build a `ShoppingCart` class that accepts `Product` instances and calculates total tax.


class Product:
    def __init__(self, name:str,price: float, tax:int):
        self._name = name
        self.__price = price
        self._tax = tax

    @property
    def price(self) -> float:
        return self.__price

    @property
    def calculate_tax(self) -> float:
        return self.__price*(self._tax/100)

    def __repr__(self):
        return f"\nProduct: {self._name!r} Price:{self._price:.2f} Tax: {self._tax}%"



class ElectronicProduct (Product):
    def __init__(self,name, price, tax, warranty_period:str):
        super().__init__(name, price, tax)
        self.warranty_period = warranty_period
        self.__price = price

    def __repr__(self):
        return f"\nProduct:{self._name!r} Price:{self.__price:.2f} Tax: {self._tax}% Warranty_period: {self.warranty_period}"

class ClothingProduct (Product):
    def __init__(self,name, price, tax, clothing_size:str):
        super().__init__(name, price, tax)
        self.clothing_size = clothing_size
        self.__price = price

    def __repr__(self):
        return f"\nProduct:{self._name!r} Price:{self.__price} Tax: {self._tax}% Size: {self.clothing_size!r} "

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product:Product) -> None:
        self.items.append(product)

    def calculate_tax(self) -> float:
        total_base_price = 0
        total_tax_amount = 0

        #calculating all prices
        for product in self.items:
            total_base_price += product.price
            total_tax_amount += product.calculate_tax
        total_price = total_base_price + total_tax_amount

        #rendering bill
        heading = f"{'Product':<20} {'Price':<10} {'Tax':<10} {'Total':<10}" #this shit is completely new for me
        print("\n")
        print("-"*len(heading))
        print(heading)
        print("-"*len(heading))

        for product in self.items:
            name = product._name+" "+product.clothing_size if isinstance(product, ClothingProduct) else product._name
            base_price = str(product.price)
            tax = str(product.calculate_tax)
            taxed_price = str(product.price + product.calculate_tax)

            print(f"{name:<20} {base_price:<10} {tax:<10} {taxed_price:<10}")

        print("-"*len(heading))
        print(f"{'Total':<20} {str(total_base_price):<10} {str(total_tax_amount):<10} {str(total_price):<10}")
        print("-"*len(heading))

        return total_price

phone = ElectronicProduct("Phone",50000,25,"1yr")
shirt = ClothingProduct("Shirt", 250, 15, "Xl")

my_shoppingCart = ShoppingCart()
my_shoppingCart.add_item(phone)
my_shoppingCart.add_item(shirt)


my_shoppingCart.calculate_tax()
