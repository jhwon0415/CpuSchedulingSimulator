class Task:
    name = str()
    group_id = int()
    is_periodical = bool
    execution_time = int()
    deadline = int()
    priority = int()
    start_time = int()
    remain_exe_time = int()
    end_time = int()

    def get_response_time(self):
        return self.end_time - self.start_time

class TaskList:
    list = []

class TaskQueue:
    list = []


class ExecutionRecord:
    list = []

class finishedTaskList:
    list = []

class Policy:
    current_policy = int

class TaskStatistics:
    list = []
