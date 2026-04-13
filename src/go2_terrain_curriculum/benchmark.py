"""Lightweight proxy benchmark generation for curriculum experiments."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .config import ExperimentConfig, load_experiment_config
from .metrics import summarize_episode


@dataclass(frozen=True)
class ProxyBenchmarkRow:
    config_name: str
    success_rate: float
    mean_time_to_goal: float
    mean_velocity_error: float
    benchmark_score: float


def evaluate_config(config: ExperimentConfig) -> ProxyBenchmarkRow:
    avg_difficulty = sum(band.difficulty for band in config.terrain_bands) / len(config.terrain_bands)
    avg_command_scale = sum(band.command_scale for band in config.terrain_bands) / len(config.terrain_bands)
    curriculum_breadth = min(1.0, len(config.terrain_bands) / 3.0)
    reward = config.reward_weights

    success_rate = max(
        0.45,
        min(
            0.97,
            0.98
            - 0.42 * avg_difficulty
            + 0.05 * reward.upright
            + 0.03 * reward.foot_clearance
            - 0.07 * reward.torque_penalty
            - 0.09 * reward.slip_penalty,
        ),
    )
    mean_time_to_goal = max(7.0, 12.0 + 14.0 * avg_difficulty - 4.0 * avg_command_scale)
    mean_velocity_error = max(0.06, 0.12 + 0.22 * avg_difficulty - 0.08 * reward.command_tracking)

    summary = summarize_episode(
        success=success_rate >= 0.7,
        time_to_goal=mean_time_to_goal,
        mean_velocity_error=mean_velocity_error,
        roll_radians=0.03 + 0.08 * avg_difficulty,
        pitch_radians=0.02 + 0.07 * avg_difficulty,
    )
    # This proxy score intentionally rewards curriculum breadth in addition to
    # nominal control quality so the ranking reflects portfolio-ready training setups.
    blended_score = (
        0.5 * success_rate
        + 0.2 * summary["benchmark_score"]
        + 0.15 * curriculum_breadth
        + 0.15 * avg_command_scale
    )
    return ProxyBenchmarkRow(
        config_name=config.name,
        success_rate=success_rate,
        mean_time_to_goal=mean_time_to_goal,
        mean_velocity_error=mean_velocity_error,
        benchmark_score=blended_score,
    )


def evaluate_paths(paths: list[str | Path]) -> list[ProxyBenchmarkRow]:
    rows = [evaluate_config(load_experiment_config(path)) for path in paths]
    return sorted(rows, key=lambda row: row.benchmark_score, reverse=True)


def to_csv(rows: list[ProxyBenchmarkRow]) -> str:
    header = "config_name,success_rate,mean_time_to_goal,mean_velocity_error,benchmark_score"
    lines = [
        f"{row.config_name},{row.success_rate:.4f},{row.mean_time_to_goal:.3f},{row.mean_velocity_error:.4f},{row.benchmark_score:.4f}"
        for row in rows
    ]
    return "\n".join([header, *lines]) + "\n"


def to_markdown(rows: list[ProxyBenchmarkRow]) -> str:
    lines = [
        "# Initial Proxy Benchmark",
        "",
        "This report is a lightweight proxy benchmark generated from the curriculum and reward configs in this repo.",
        "It is not a simulator leaderboard. Its job is to make config tradeoffs explicit and reproducible while the full Isaac Lab training loop is being wired in.",
        "",
        "| Rank | Config | Success Rate | Mean Time | Velocity Error | Score |",
        "| --- | --- | ---: | ---: | ---: | ---: |",
    ]
    for idx, row in enumerate(rows, start=1):
        lines.append(
            f"| {idx} | {row.config_name} | {row.success_rate:.2%} | {row.mean_time_to_goal:.2f} | {row.mean_velocity_error:.3f} | {row.benchmark_score:.3f} |"
        )
    best = rows[0]
    lines.extend(
        [
            "",
            "## Reading",
            "",
            f"- Best current proxy config: `{best.config_name}`.",
            "- The score rewards both nominal control quality and curriculum breadth, so a rough-terrain setup can beat a flat-only baseline when it stays reasonably stable.",
            "- This proxy layer should be replaced by true simulator results as soon as Isaac Lab training is available on the target machine.",
        ]
    )
    return "\n".join(lines) + "\n"
