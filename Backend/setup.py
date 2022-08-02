import datetime
import uuid

class Setup:
    def setup(self, db, base):
        Shops = base.classes.shops
        Looking_forwardables = base.classes.looking_forwardables
        Bous = base.classes.bous
        Alarms = base.classes.alarms
        Categories = base.classes.categories
        Frequency = base.classes.frequencies
        Priorities = base.classes.priorities
        Responsibilities = base.classes.responsibilities
        Items = base.classes['items']
        Transactions = base.classes.transactions
        Tasks = base.classes.tasks
        Alarms_o_tasks = base.classes.alarms_o_tasks
        Bous_o_looking_forwardables = base.classes.bous_o_looking_forwardables

        shop_uuid = uuid.uuid1().__str__()
        shop = Shops(id=shop_uuid, balance=0)
        looking_forwardables_uuid = uuid.uuid1().__str__()
        looking_forwardables = Looking_forwardables(id=looking_forwardables_uuid, name='name', description='description', date=datetime.date(2022, 12, 12))
        bous_uuid = uuid.uuid1().__str__()
        bous = Bous(id=bous_uuid, name='bou', id_shop=shop_uuid)
        alarms_uuid = uuid.uuid1().__str__()
        alarms = Alarms(id=alarms_uuid, time=datetime.datetime(2022, 12, 12, 12, 12, 12, 12), snooze=1)
        categories_uuid = uuid.uuid1().__str__()
        categories = Categories(id=categories_uuid, name='category')
        frequency_uuid = uuid.uuid1().__str__()
        frequency = Frequency(id=frequency_uuid, scope='month', placements=[31, 1], hour=1)
        priorities_uuid = uuid.uuid1().__str__()
        priorities = Priorities(id=priorities_uuid, severity=1, difficulty=1, prioretized=True, progressive=False)
        db.session.add(shop)
        db.session.commit()
        db.session.add(looking_forwardables)
        db.session.add(bous)
        db.session.add(alarms)
        db.session.add(categories)
        db.session.add(frequency)
        db.session.add(priorities)
        db.session.commit()

        responsibilities_uuid = uuid.uuid1().__str__()
        responsibilities = Responsibilities(id=responsibilities_uuid, id_bou=bous_uuid, reward=1, penalty=1, due=datetime.datetime(2022, 12, 12, 12, 12))
        items_uuid = uuid.uuid1().__str__()
        items = Items(id=items_uuid, id_shop=shop_uuid, name='item', description='description', base_price=1, price=2)
        transactions_uuid = uuid.uuid1().__str__()
        transactions = Transactions(id=transactions_uuid, id_item=items_uuid, id_buyer=bous_uuid, date=datetime.date(2022, 12, 12), price=1)
        tasks_uuid = uuid.uuid1().__str__()
        tasks2_uuid = uuid.uuid1().__str__()
        tasks = Tasks(id=tasks_uuid, id_responsibility=responsibilities_uuid, id_frequency=frequency_uuid, id_category=categories_uuid, id_priority=priorities_uuid, title='title', description='description', slack=1, dailygoal=False, due=datetime.date(2022, 12, 12), finished=False)
        tasks2 = Tasks(id=tasks2_uuid, id_responsibility=responsibilities_uuid, id_frequency=frequency_uuid, id_category=categories_uuid, id_priority=priorities_uuid, id_parent_task=tasks_uuid, title='subtask_title', description='description', slack=1, dailygoal=False, due=datetime.date(2022, 12, 12), finished=False)
        Alarms_o_tasks_uuid = uuid.uuid1().__str__()
        alarms_o_tasks = Alarms_o_tasks(id=Alarms_o_tasks_uuid, id_alarm=alarms_uuid, id_task=tasks_uuid)
        Bous_o_looking_forwardables_uuid = uuid.uuid1().__str__()
        bous_o_looking_forwardables = Bous_o_looking_forwardables(id=Bous_o_looking_forwardables_uuid, id_bou=bous_uuid, id_looking_forwardable=looking_forwardables_uuid)
        db.session.add(responsibilities)
        db.session.commit()
        db.session.add(items)
        db.session.commit()
        db.session.add(transactions)
        db.session.commit()
        db.session.add(tasks)
        db.session.add(tasks2)
        db.session.commit()
        db.session.add(alarms_o_tasks)
        db.session.add(bous_o_looking_forwardables)
        db.session.commit()




        