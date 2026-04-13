from pathlib import Path

from go2_terrain_curriculum.config import load_experiment_config


def test_load_experiment_config() -> None:
    config = load_experiment_config(Path("configs/go2_rough.yaml"))
    assert config.name == "go2-rough-curriculum"
    assert len(config.terrain_bands) == 3
    assert config.reward_weights.upright == 1.0

