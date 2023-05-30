from datetime import datetime
from sims4communitylib.utils.common_log_registry import CommonLogRegistry
from workfromhomemod import mod_identity

# Create dedicated loggers for careers and tasks
task_log = CommonLogRegistry.get().register_log(mod_identity, "tasks.log")
career_log = CommonLogRegistry.get().register_log(mod_identity, "careers.log")


def _format_log_message(sim, message: str) -> str:
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sim_name = sim.name
    return f"[{date_time}] {sim_name}: {message}"


def log_task_event(sim, message: str) -> None:
    log_message = _format_log_message(sim, message)
    task_log.debug(log_message)


def log_career_event(sim, message: str) -> None:
    log_message = _format_log_message(sim, message)
    career_log.debug(log_message)
