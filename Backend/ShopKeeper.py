from ShopDto import Item


class ShopKeeper(object):
    def __init__(self, operator) -> None:
        self.shop_id = None
        self.items = []
        self.balance = 0
        self.last_bou = ''
        self.operator = operator

    def fetch_items(self):
        session = self.operator.session
        c = self.operator.base.classes
        result = session.query(c.items).where(c.items.id_shop == self.shop_id).all()
        for row in result:
            self.items.append(Item(row.name, row.description, row.base_price, row.price))

        return self.items

    def add_item(self, item):
        db = self.operator.db
        db.session.add(item)
        db.commit()
        return item

    def map_item(self, request):
        item = request['item']
        name = item['name']
        description = item['description']
        base_price = item['base_price']
        price = self._determin_price(base_price)
        return self.operator.base.classes.items(name=name, description=description, base_price=base_price, price=price)


    def _determin_price(self, base_price):
        price = base_price
        if self.balance < base_price:
            price += int(base_price * 0.25)
        if self.balance > base_price * 2:
            price = int(base_price / 0.75)
        return price
