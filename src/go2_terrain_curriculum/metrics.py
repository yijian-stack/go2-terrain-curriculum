"""Benchmark-style episode metrics."""

from __future__ import annotations


def stability_score(roll_radians: float, pitch_radians: float) -> float:
    tilt = abs(roll_radians) + abs(pitch_radians)
    return max(0.0, 1.0 - tilt)


def summarize_episode(
    *,
    success: bool,
    time_to_goal: float,
    mean_velocity_error: float,
    roll_radians: float,
    pitch_radians: float,
) -> dict[str, float]:
    stability = stability_score(roll_radians, pitch_radians)
    speed_score = max(0.0, 1.0 - time_to_goal / 30.0)
    tracking_score = max(0.0, 1.0 - mean_velocity_error)
    total = 0.45 * float(success) + 0.3 * speed_score + 0.25 * stability * tracking_score
    return {
        "success": float(success),
        "speed_score": speed_score,
        "stability_score": stability,
        "tracking_score": tracking_score,
        "benchmark_score": total,
    }

