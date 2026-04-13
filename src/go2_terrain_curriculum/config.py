"""Configuration helpers for curriculum-based quadruped experiments."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True)
class TerrainBand:
    name: str
    difficulty: float
    command_scale: float


@dataclass(frozen=True)
class RewardWeights:
    command_tracking: float
    upright: float
    foot_clearance: float
    torque_penalty: float
    slip_penalty: float


@dataclass(frozen=True)
class ExperimentConfig:
    name: str
    terrain_bands: list[TerrainBand]
    reward_weights: RewardWeights
    promotion_threshold: float
    demotion_threshold: float
    min_episodes_per_band: int


def load_experiment_config(path: str | Path) -> ExperimentConfig:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    terrain_bands = [TerrainBand(**band) for band in data["terrain_bands"]]
    reward_weights = RewardWeights(**data["reward_weights"])
    return ExperimentConfig(
        name=data["name"],
        terrain_bands=terrain_bands,
        reward_weights=reward_weights,
        promotion_threshold=float(data["promotion_threshold"]),
        demotion_threshold=float(data["demotion_threshold"]),
        min_episodes_per_band=int(data["min_episodes_per_band"]),
    )

