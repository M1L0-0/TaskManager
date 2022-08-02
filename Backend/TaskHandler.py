import json
import uuid
from TaskDto import Task
from uuid import UUID


class TaskHandler (object):
    def __init__(self, operator) -> None:
        self.operator = operator
        self.task_list = []

    def fetch_task_list(self):
        session = self.operator.session
        c = self.operator.base.classes
        results = session.query(c.tasks).join(c.responsibilities).join(c.bous).join(c.categories).join(c.priorities).filter()
        recursive_ids = []
        self.task_list = []
        for row in results:
            alarms_result = session.query(c.alarms).join(c.alarms_o_tasks, c.alarms.id==c.alarms_o_tasks.id_alarm).filter(c.alarms_o_tasks.id_task==row.id)
            alarms = []
            results_recursive = session.query(c.tasks).filter(c.tasks.id==row.id).cte('cte', recursive=True)
            results_rec = session.query(results_recursive.union(session.query(c.tasks).join(results_recursive, c.tasks.id_parent_task==results_recursive.c.id)))
            for alarm in alarms_result:
                alarms.append([alarm.time, alarm.snooze])
            for res in results_rec:
                recursive_ids.append(res.id)
            new_task = Task(row.title,
                            row.slack,
                            row.due,
                            row.categories.name,
                            row.dailygoal,
                            row.responsibilities.bous.name,
                            row.priorities.severity,
                            row.priorities.difficulty,
                            row.priorities.prioretized,
                            row.priorities.progressive,
                            row.responsibilities.penalty,
                            row.responsibilities.reward,
                            alarms,
                            [row.frequencies.scope, row.frequencies.placements, row.frequencies.hour],
                            milestones=recursive_ids)
            self.task_list.append(new_task)
        return {'task_list': [task.get_dict() for task in self.task_list]}

    def get_category(self, category):
        session = self.operator.session
        c = self.operator.base.classes
        result = None
        if self.is_id(category):
            result = session.query(c.categories).where(c.categories.id == category).all()
        else: 
            result = result = session.query(c.categories).where(c.categories.name == category).all()

        for row in result:
            return row.name
        else:
            return 0

    def get_bou(self, bou):
        session = self.operator.session
        c = self.operator.base.classes
        result = None
        if self.is_id(bou):
            result = session.query(c.bous).where(c.bous.id == bou).all()
        else: 
            result = result = session.query(c.bous).where(c.bous.name == bou).all()

        for row in result:
            return row.name
        else:
                return 0

    def add_task(self, title, slack, due, categories, dailygoal, bou, severity, difficulty, prioretized, progressive, penalty, reward, alarm_time, alarm_snooze, frequency_scope, frequency_placements, frequency_hour, finished):
        session = self.operator.session
        c = self.operator.base.classes
        new_priority = c.priorities(id=uuid.uuid4(), severity=severity, difficulty=difficulty, prioretized=prioretized, progressive=progressive)
        new_responsibility = c.responsibilities(penalty=penalty, reward=reward, bou=self.get_bou(bou))
        new_alarm = c.alarms(id=uuid.uuid4(), time=alarm_time, snooze=alarm_snooze)
        new_frequency = c.frequencies(id=uuid.uuid4(), scope=frequency_scope, hour=frequency_hour, placements=frequency_placements)
        category = self.get_category(categories)
        new_task = c.tasks(title=title, slack=slack, due=due, dailygoal=dailygoal, id_priorities=new_priority, id_responsibility=new_responsibility, id_alarm=new_alarm, id_frequency=new_frequency, category=category)
        session.add(new_task)
        session.commit()
 
    def is_id(self, task):
        try:
            uuid = UUID(task)
        except ValueError:
            return False
        return True

    def return_task_by_id(self, id):
        session = self.operator.session
        c = self.operator.base.classes
        results = session.query(c.tasks).join(c.responsibilities).join(c.bous).join(c.categories).join(c.priorities).where(c.tasks.id == id).all()
        task = None
        for row in results:
            task = Task(row.title,
                            row.slack,
                            row.due,
                            row.categories.name,
                            row.dailygoal,
                            row.bous.name,
                            row.priorities.severity,
                            row.priorities.difficulty,
                            row.priorities.prioretized,
                            row.priorities.progressive,
                            row.responsibilites.penalty,
                            row.responsibilities.reward,
                            [row.alarms.time, row.alarms.snooze],
                            [row.frequencies.scope, row.frequencies.placements, row.frequencies.hour])
            break
        else:
            return -1
        return task

    def return_task_by_title(self, title):
        session = self.operator.session
        c = self.operator.base.classes
        results = session.query(c.tasks).join(c.responsibilities).join(c.bous).join(c.categories).join(c.priorities).where(c.tasks.title == title).all()
        task = None
        for row in results:
            task = Task(row.title,
                            row.slack,
                            row.due,
                            row.categories.name,
                            row.dailygoal,
                            row.bous.name,
                            row.priorities.severity,
                            row.priorities.difficulty,
                            row.priorities.prioretized,
                            row.priorities.progressive,
                            row.responsibilites.penalty,
                            row.responsibilities.reward,
                            [row.alarms.time, row.alarms.snooze],
                            [row.frequencies.scope, row.frequencies.placements, row.frequencies.hour])
            break
        else:
            return -1
        return task

