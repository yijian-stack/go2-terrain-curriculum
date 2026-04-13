"""Render practical Isaac Lab training commands from compact configs."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True)
class IsaacLabTrainConfig:
    project_name: str
    simulator: str
    env_id: str
    backend: str
    seed: int
    num_envs: int
    max_iterations: int
    experiment_name: str
    notes: str


def load_isaac_lab_config(path: str | Path) -> IsaacLabTrainConfig:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    return IsaacLabTrainConfig(**data)


def render_train_command(config: IsaacLabTrainConfig) -> str:
    return (
        "isaaclab.bat -p scripts\\reinforcement_learning\\rsl_rl\\train.py "
        f"--task {config.env_id} "
        "--headless "
        f"--num_envs {config.num_envs} "
        f"--max_iterations {config.max_iterations} "
        f"--seed {config.seed} "
        f"agent.experiment_name={config.experiment_name}"
    )


def render_play_command(config: IsaacLabTrainConfig) -> str:
    return (
        "isaaclab.bat -p scripts\\reinforcement_learning\\rsl_rl\\play.py "
        f"--task {config.env_id} "
        f"agent.experiment_name={config.experiment_name}"
    )


def render_bundle(config: IsaacLabTrainConfig) -> str:
    return "\n".join(
        [
            f"# {config.project_name}",
            f"# Notes: {config.notes}",
            render_train_command(config),
            render_play_command(config),
            "",
        ]
    )
