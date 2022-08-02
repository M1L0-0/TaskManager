class Item(object):
    def __init__(self, name, description, base_price, price) -> None:
        self.name = name
        self.description = description
        self.base_price = base_price
        self.price_old = price
        

class Shop(object):
    def __init__(self, balance) -> None:
        self.items = []
        self.balance = balance