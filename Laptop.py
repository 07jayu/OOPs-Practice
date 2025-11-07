# Create a class Laptop with attributes brand and price. Print them.

class laptop:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    def laptop_info(self):
        print(f"laptop:{self.brand, self.price}")

l1 = laptop("Dell G3", 75000)
l1.laptop_info()