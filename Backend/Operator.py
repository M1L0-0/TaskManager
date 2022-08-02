import json
from ShopKeeper import ShopKeeper
from TaskHandler import TaskHandler
from Logistician import Logistician


class Operator:
    def __init__(self, db, metadata, engine, session, base):
        self.db = db
        self.metadata = metadata
        self.engine = engine
        self.session = session
        self.base = base
        self.last_bou = ''
        self.calendar = None
        self.shop_keeper = None
        self.task_handler = None
        self.logistician = None

    def format_return(self, response):
        if type(response) is not dict:
            return response
        return json.dumps(response), {'Content-Type': 'text/json; charset=utf-8'}

    def initialize(self):
        self.shop_keeper = ShopKeeper(self)
        self.task_handler = TaskHandler(self)
        self.logistician = Logistician(self)

    def return_bou(self, name):
        return self.logistician.fetch_bou(name)

    def return_all_items(self, name):
        return self.shop_keeper.fetch_items()

    def add_item(self, request_json):
        mapped_item = self.shop_keeper.map_item(request_json)
        return self.shop_keeper.add_item(self.name, mapped_item)

    def update_task_list(self):
        return self.task_handler.fetch_task_list()

    def add_task(self, request_json):
        mapped_task = self.task_handler.map_task(request_json)
        return self.task_handler.add_task(mapped_task)
    
    def return_task_by_title(self, title):
        return self.task_handler.fetch_task_by_title(title)

    def update_shop_id(self, name):
        if name == self.last_bou:
            return
        self.shop_keeper.shop_id = Logistician.fetch_bou(name)
        self.last_bou == name
        return

    def get_task(self, task):
        if self.task_handler.is_id(task):
            self.task_handler.return_task_by_id(self.session, self.base, task)
        else:
            self.task_handler.return_task_by_title(self.session, self.base, task)