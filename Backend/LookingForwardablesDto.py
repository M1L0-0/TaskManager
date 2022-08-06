class LookingForwardables(object):
    def __init__(self, name, description, date) -> None:
        self.name = name
        self.description = description
        self.date = date

    def get_dict(self):
        return {'name': self.name, 'description': self.description, 'date': self.date.strftime("%m/%d/%Y, %H:%M")}