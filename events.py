from task import Task
from task_manager import TaskManager
from career import Career

from career_it_interactions import ITSubmitTaskInteraction


class ITTaskAssignedEvent:
    def __init__(self, sim, career: Career, task: Task):
        self.sim = sim
        self.career = career
        self.task = task

    def on_task_assigned(self):
        task_manager = TaskManager(self.career, [])

        # Display the assigned task notification
        self.sim.display_notification(f"New IT task assigned: {self.task.name}")

        # Create SubmitTaskInteraction and add it to the queue
        submit_task_interaction = ITSubmitTaskInteraction(self.sim, self.task)
        submit_task_interaction.enqueue()


def init() -> None:
    # Register event listeners
    pass
