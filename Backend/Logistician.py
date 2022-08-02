class Logistician(object):
    def __init__(self, operator) -> None:
        self.operator = operator

    def fetch_bou(self, name):
        result = self.operator.session.query(self.operator.base.classes.bous).where(self.operator.base.classes.bous.name == name).all()
        for row in result:
            if row.id_shop:
                return {'id_bou': row.id_shop}

