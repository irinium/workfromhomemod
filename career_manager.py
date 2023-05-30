from career import Career
from task import Task
from task_manager import TaskManager


class CareerManager:
    def __init__(self, sim):
        self.sim = sim
        self.it_career = None
        self.task = None
        self.task_manager = None

    def setup_career(self):
        # Acquire the IT career instance from the game
        self.it_career = Career.__init__(self, self.sim, )

        # Initialize ITCareer's TaskManager instance
        self.task_manager = TaskManager(self.it_career, [])

    def setup_task(self):
        # Create ITTask based on specific career requirements
        self.task = Task(sim, 'IT Task Name', task_difficulty=1.0, required_skills={'programming': 3})

        # Assign ITTask to the sim through TaskManager
        self.task_manager.assign_task(self.task)

    def create_relationship(self, other_sim):
        # Add relationship between the active sim and another sim
        self.sim.create_relationship_with(other_sim, relationship_type='friend')


def init() -> None:
    # Create a Sim instance (or acquire it through the game API)
    sim = Sim()  # Placeholder for Sim instance, replace it with a proper instance
    other_sim = Sim()  # Placeholder for Sim instance, replace it with a proper instance

    # Instantiate ITCareerManager
    it_career_manager = ITCareerManager(sim)

    # Set up IT career, tasks, and relationships
    it_career_manager.setup_it_career()
    it_career_manager.setup_it_task()
    it_career_manager.create_relationship(other_sim)