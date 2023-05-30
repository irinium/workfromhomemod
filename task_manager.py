from typing import List

from career import Career
from task import Task
from utils.calculation import calculate_work_performance
from utils.log import log_task_event


class TaskManager:
    def __init__(self, career: Career, tasks: List[Task]):
        self.career = career
        self.tasks = tasks

    def assign_task(self, task: Task) -> None:
        self.tasks.append(task)
        log_task_event(self.career.sim, f"{self.career.sim.name} was assigned a new task: {task.name}")

    def submit_task(self, task: Task) -> None:
        if task in self.tasks:
            career_gain = calculate_work_performance(task.difficulty)
            self.career.adjust_performance(career_gain)
            self.tasks.remove(task)
            log_task_event(self.career.sim, f"{self.career.sim.name} submitted the {task.name} task.")
        else:
            # log warning when task is not found
            log_task_event(self.career.sim, f"{self.career.sim.name} attempted to submit an unassigned task: {task.name}")
