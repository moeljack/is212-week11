class Product:
    def __init__(self, name, price, discount, tax_rate):
        self.name = name
        self.price = price
        self.discount = discount
        self.tax_rate = tax_rate

    def apply_discount(self):
        discounted_price = self.price - (self.price * self.discount)
        print(f"Discounted price for {self.name}: {discounted_price}")
        return discounted_price

    def calculate_tax(self):
        tax = self.price * self.tax_rate
        print(f"Tax for {self.name}: {tax}")
        return tax

class Electronics(Product):
    def __init__(self, name, price):
        super().__init__(name, price, discount=0.10, tax_rate=0.15)

class Clothing(Product):
    def __init__(self, name, price):
        super().__init__(name, price, discount=0.20, tax_rate=0.08)

class Grocery(Product):
    def __init__(self, name, price):
        super().__init__(name, price, discount=0.05, tax_rate=0.02)
