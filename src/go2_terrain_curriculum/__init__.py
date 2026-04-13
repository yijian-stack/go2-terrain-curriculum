"""Go2 terrain curriculum utilities."""

from .config import ExperimentConfig, RewardWeights, TerrainBand, load_experiment_config
from .curriculum import TerrainCurriculumScheduler

__all__ = [
    "ExperimentConfig",
    "RewardWeights",
    "TerrainBand",
    "TerrainCurriculumScheduler",
    "load_experiment_config",
]

