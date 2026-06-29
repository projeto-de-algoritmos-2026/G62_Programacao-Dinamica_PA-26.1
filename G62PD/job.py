from datetime import datetime

class Job:
    def __init__(self, start: datetime, finish: datetime, weight: float):
        self.start = start
        self.finish = finish
        self.weight = weight

    def getLength(self):
        return self.finish - self.start