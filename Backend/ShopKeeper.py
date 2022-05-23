class Item:
    def __init__(self):
        self.name = None
        self.description = None
        self.basePrice = None
        self.RlPrice = None

class Transaction:
    def __init__(self):
        self.date = None
        self.price = None
        self.item = None
        self.buyer = None
        

class Shop:
    def __init__(self):
        self.balance = None
        self.items = []
        self.transactions = []


class ShopKeeper:
    pass


