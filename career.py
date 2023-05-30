from task import Task
from task_manager import TaskManager
from rewards import grant_reward


class Career:
    def __init__(self, sim_instance, tasks, rewards):
        self.sim = sim_instance
        self.tasks = tasks
        self.rewards = rewards
        self.task_manager = TaskManager(self, tasks)

    def is_sim_qualified(self):
        # Check if the sim has the necessary qualifications to join the IT career
        pass

    def on_task_completed(self, task: Task, successful: bool):
        if successful:
            reward = self.rewards.get(task.name)
            grant_reward(self.sim, reward)

    def create_it_task(self, task_name: str, task_difficulty: float) -> Task:
        required_skills = {'programming': int(task_difficulty)}
        it_task = Task(self.sim, task_name, task_difficulty, required_skills)
        return it_task


def init():
    # Create a Sim instance with relationships
    sim_instance = create_sim()

    # Create IT career task instances
    tasks = [
        Task(sim_instance, "Solve Algorithm Challenge", 1.0),
        Task(sim_instance, "Write Python Script", 2.0),
        Task(sim_instance, "Configure Router", 3.0)
    ]

    # Define rewards for each task
    rewards = {
        "Solve Algorithm Challenge": "bonus_simoleons",
        "Write Python Script": "skill_boost",
        "Configure Router": "mood_buff",
    }

    # Create an IT career instance
    it_career = ITCareer(sim_instance, tasks, rewards)

    # ... (Start/initiate the career, enqueue tasks, and progress through career)