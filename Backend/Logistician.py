from uuid import UUID
import uuid
from CalendarDto import Calendar
from LookingForwardablesDto import LookingForwardables


class Logistician(object):
    def __init__(self, operator) -> None:
        self.operator = operator

    def fetch_bou(self, name):
        result = self.operator.session.query(self.operator.base.classes.bous).where(self.operator.base.classes.bous.name == name).all()
        for row in result:
            if row.id_shop:
                return {'id_bou': row.id_shop}

    def get_bou_id(self, name):
        result = self.operator.session.query(self.operator.base.classes.bous).where(self.operator.base.classes.bous.name == name).all()
        for row in result:
            if row.id_shop:
                return row.id

    def get_calendar(self, bou):
        bou_id = self.operator.return_bou_id(bou)
        task_list = self.operator.return_task_list()
        filtered_task_list = (task for task in task_list if task.assignee == bou_id)
        looking_forwardables = self.operator.return_looking_forwardables(bou_id)
        return Calendar(filtered_task_list, bou_id, looking_forwardables)

    def return_looking_forwardables(self, bou_id):
        c = self.operator.base.classes
        looking_forwardables = []
        result = self.operator.session.query(c.looking_forwardables).join(c.bous_o_looking_forwardables).where(c.bous_o_looking_forwardables.id_bou == bou_id).all()
        for row in result:
            looking_forwardables.append(LookingForwardables(row.name, row.description, row.date))
        return {'looking_forwardables': looking_forwardables}

    def add_looking_forwardable(self, bou_id, name, description, date):
        c = self.operator.base.classes
        id_looking_forwardable = uuid.uuid4()
        lf = c.looking_forwardables(id=id_looking_forwardable, name=name, description=description, date=date)
        lf_o = c.bous_o_looking_forwardables(id=uuid.uuid4(), id_bou=bou_id, id_looking_forwardable=id_looking_forwardable)
        self.operator.session.add(lf)
        self.operator.session.add(lf_o)
        self.operator.session.commit()

    def map_looking_forwardable(self, request):
        lf = request['looking_forwardable']
        return self.operator.base.classes.looking_forwardables(nmae=lf['name'], description=lf['description'], date=lf['date'])

