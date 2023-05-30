from S4CL.sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils


def add_skill_points(skill, points):
    try:
        sim_id = CommonSimUtils.get_active_sim_id()
        sim_info = CommonSimUtils.get_active_sim_info()

        # Check if the Sim exists
        if sim_info is None:
            raise Exception(f"Sim with ID {sim_id} not found.")

        # Check if the skill exists
        skill_entry = sim_info.skill_tracker.get_skill(skill)
        if skill_entry is None:
            raise Exception(f"Skill {skill} not found for Sim {sim_info.first_name}.")

        # Add skill points
        skill_entry.add_skill_points(points)
    except Exception as e:
        print(e.__cause__)


def grant_reward(self) -> None:
    if not self.reward:
        return

    if self.reward == 'bonus_simoleons':
        self.sim.add_simoleon_amount(5000)
    elif self.reward == 'skill_boost':
        for skill, level in self.required_skills.items():
            self.sim.skills.add_skill_points(skill, points=3)  # Assumed in-game API method
        pass
