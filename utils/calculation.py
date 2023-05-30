import random


def calculate_task_difficulty(base_difficulty: float) -> float:
    """Calculate task difficulty based on base difficulty and random modifier."""
    modifier = random.uniform(0.8, 1.2)
    return base_difficulty * modifier


def calculate_work_performance(task_difficulty: float) -> float:
    """Calculate work performance based on the task difficulty."""
    return task_difficulty * 10
