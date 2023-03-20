class Task:
    def __init__(self,taskId, taskname):
        self.taskId = taskId
        self.taskname = taskname
        self.priority = priority

    def __repr__(self):
        return f"Id: {self.taskId}\nTaskname: {self.taskname}\nPriority: {self.priority}"