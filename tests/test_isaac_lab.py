from pathlib import Path

from go2_terrain_curriculum.isaac_lab import load_isaac_lab_config, render_train_command


def test_render_train_command_contains_env_id() -> None:
    config = load_isaac_lab_config(Path("configs/isaac_lab/go2_rough_rsl_rl.yaml"))
    command = render_train_command(config)
    assert "Isaac-Velocity-Rough-Unitree-Go2-v0" in command
    assert "--max_iterations 2500" in command
