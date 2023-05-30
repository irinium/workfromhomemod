from S4CL.sims4communitylib.enums.icons_enum import CommonIconId

from career import Career
from task_manager import TaskManager


class WorkFromHomeInteraction(HashedTunedInstance):
    INSTANCE_TUNABLES = {
        'career': Career.TunableReference(description='Reference to the IT career this interaction belongs to.')
    }

    def __init__(self, *_, **__):
        super().__init__(*_, **__)
        self.it_career = self.career()  # Get IT career instance
        self.task_manager = TaskManager(self.it_career, [])

    def on_started(self, sim) -> None:
        """Triggered when the sims starts this interaction."""
        it_task = self.get_active_task()
        if it_task:
            sim.perform_task(it_task, self.on_task_completion)

    def on_task_completion(self, it_task: ITTask, success: bool) -> None:
        """Triggered when the task for the interaction is completed."""
        if success:
            self.task_manager.submit_task(it_task)
        sim.show_message(CommonLocalizationUtils.IT_TASK_COMPLETION,
                         f"{it_task.name} completed with {'success' if success else 'failure'}.",
                         icon_name=CommonIconId.NOTIFY_INFO)

    def get_active_task(self) -> ITTask:
        return self.it_career.get_active_work_from_home_task()


def init() -> None:
    # Register IT work-from-home interactions here
    pass
