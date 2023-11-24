class Dish():
    def __init__(self, name, price):
        self.name = name
        if isinstance(price, (int, float)):
            self.price = price
        else:
            raise TypeError("Invalid price, must be a number!")