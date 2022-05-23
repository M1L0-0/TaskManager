class Priority:
    def __init__(self, severity, difficulty, prioretized=False, progressive=False):
        self.severity = severity
        self.difficulty = difficulty
        self.prioretized = prioretized
        self.progressive = progressive

class Responsibility:
    def __init__(self, penalty=0, reward=0, assignee=None):
        self.assignee = assignee
        self.penalty = penalty
        self.reward = reward

class Alarm:
    def __init__(self, time, snoozeMax=0):
        self.time = time
        self.snoozeMax = snoozeMax

class Frequency:
    def __init__(self, scope, placements, hour=0):
        self.scope = scope
        self.placements = placements
        self.hour = hour

class Task:
    def __init__(self):
        self.id = None
        self.title = None
        self.description = None
        self.slack = None
        self.due = None
        self.dailyGoal = False
        self.priority = None
        self.responsibility = None
        self.alarms = []
        self.frequency = None
        

    def build(self, id, title, due, priority, responsibility, frequency, dailyGoal=False, slack=0, description='', alarms=[]):
        self.id = id
        self.title = title
        self.description = description
        self.slack = slack
        self.due = due
        self.dailyGoal = dailyGoal

        self.priority = priority
        self.responsibility = responsibility
        self.alarms = alarms
        self.frequency = frequency

class TaskHandler:
    pass

