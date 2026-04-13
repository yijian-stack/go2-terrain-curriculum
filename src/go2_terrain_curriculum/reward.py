"""Reward decomposition for command-conditioned quadruped locomotion."""

from __future__ import annotations

from typing import Mapping

from .config import RewardWeights


def locomotion_reward(
    *,
    commanded_speed: float,
    actual_speed: float,
    upright_score: float,
    foot_clearance_score: float,
    torque_cost: float,
    slip_cost: float,
    weights: RewardWeights,
) -> dict[str, float]:
    tracking_error = abs(commanded_speed - actual_speed)
    command_term = max(0.0, 1.0 - tracking_error)

    components = {
        "command_tracking": weights.command_tracking * command_term,
        "upright": weights.upright * max(0.0, upright_score),
        "foot_clearance": weights.foot_clearance * max(0.0, foot_clearance_score),
        "torque_penalty": -weights.torque_penalty * max(0.0, torque_cost),
        "slip_penalty": -weights.slip_penalty * max(0.0, slip_cost),
    }
    components["total"] = sum(components.values())
    return components


def total_reward(components: Mapping[str, float]) -> float:
    return float(components["total"])

