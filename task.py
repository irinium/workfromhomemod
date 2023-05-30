from typing import Any, Dict
from datetime import datetime, timedelta


class Task:
    def __init__(self, sim, name: str, task_difficulty: float = 1.0, required_skills: Dict[str, int] = None,
                 deadline: timedelta = None, expires_in: timedelta = None, reward: str = None):
        self.sim = sim
        self.name = name
        self.difficulty = task_difficulty
        self.required_skills = required_skills or {'programming': 1}
        self.deadline = deadline
        self.start_time = datetime.now()

        self.expires_in = expires_in
        self.expiration_time = datetime.now() + self.expires_in if expires_in else None

        self.base_task_duration = timedelta(minutes=60) * self.difficulty
        self.task_duration = self.calculate_duration_based_on_skills()

        self.reward = reward

    def is_expired(self) -> bool:
        if not self.expiration_time:
            return False
        remaining_time = self.expiration_time - datetime.now()
        return remaining_time.total_seconds() < 0

    def progress_percentage(self) -> float:
        elapsed_time = datetime.now() - self.start_time
        progress = (elapsed_time.total_seconds() / self.task_duration.total_seconds()) * 100
        return min(progress, 100)

    def calculate_duration_based_on_skills(self) -> timedelta:
        total_required_level = sum(self.required_skills.values())
        total_sim_skills_level = sum([self.sim.get_skill_level(skill) for skill in self.required_skills])

        skill_adjustment_factor = (total_required_level / total_sim_skills_level)
        adjusted_duration = self.base_task_duration * skill_adjustment_factor
        return adjusted_duration

    def has_sim_met_skill_requirements(self, sim) -> bool:
        for skill, level in self.required_skills.items():
            if sim.get_skill_level(skill) < level:
                return False
        return True

    def is_deadline_met(self) -> bool:
        if not self.deadline:
            return True
        remaining_time = (self.start_time + self.deadline) - datetime.now()
        return remaining_time.total_seconds() >= 0
