from go2_terrain_curriculum.config import RewardWeights
from go2_terrain_curriculum.reward import locomotion_reward


def test_reward_total_matches_components() -> None:
    weights = RewardWeights(
        command_tracking=1.0,
        upright=1.0,
        foot_clearance=0.2,
        torque_penalty=0.1,
        slip_penalty=0.2,
    )
    components = locomotion_reward(
        commanded_speed=1.0,
        actual_speed=0.9,
        upright_score=0.95,
        foot_clearance_score=0.6,
        torque_cost=0.5,
        slip_cost=0.1,
        weights=weights,
    )
    subtotal = sum(value for key, value in components.items() if key != "total")
    assert abs(subtotal - components["total"]) < 1e-8

