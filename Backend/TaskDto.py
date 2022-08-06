class Task(object):
    class _Frequency(object):
        def __init__(self, scope, placements, hour) -> None:
            self.scope = scope
            self.placements = placements
            self.hour = hour

    class _Alarm(object):
        def __init__(self, time, snoozeMax=0) -> None:
            self.time = time
            self.snoozeMax = snoozeMax

    def __init__(self, title, slack, due, category, daily_goal, assignee, severity, difficulty, prioretized, progressive, penalty, reward, alarms, frequency=None, milestones=None) -> None:
        self.title = title
        self.slack = slack
        self.due = due
        self.category = category
        self.daily_goal = daily_goal
        self.assignee = assignee
        self.severity = severity
        self.difficulty = difficulty
        self.prioretized = prioretized
        self.progressive = progressive
        self.penalty = penalty
        self.reward = reward
        self.alarms = []
        for alarm in alarms:
            self.alarms.append(self._Alarm(alarm[0], alarm[1]))
        self.milestones = []
        if milestones:
            self.milestones = milestones
        if frequency:
            self.frequency = self._Frequency(frequency[0], frequency[1], frequency[2])
    

class Calendar(object):
    class _LookingForwardables(object):
        def _init__(self, name, description, date) -> None:
            self.name = name
            self.description = description
            self.date = date

    def __init__(self, title=None, slack=None, due=None, category=None, daily_goal=None, assignee=None, severity=None, difficulty=None, prioretized=None, progressive=None, penalty=None, reward=None, frequency=None):
        self.tasks = []
        self.looking_forwardables = []
        if title is not None:
            self.tasks.append(super().__init__(title, slack, due, category, daily_goal, assignee, severity, difficulty, prioretized, progressive, penalty, reward, frequency))

    def create_looking_forwardable(self, name, description, date):
        return self._LookingForwardables(name, description, date)

