"""Simulate curriculum updates from a handcrafted success-rate schedule."""

from __future__ import annotations

import argparse

from go2_terrain_curriculum import TerrainCurriculumScheduler, load_experiment_config


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=str, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = load_experiment_config(args.config)
    scheduler = TerrainCurriculumScheduler(
        bands=config.terrain_bands,
        promotion_threshold=config.promotion_threshold,
        demotion_threshold=config.demotion_threshold,
        min_episodes_per_band=config.min_episodes_per_band,
    )

    fake_success_rates = [0.82, 0.87, 0.79, 0.34, 0.91, 0.88]
    for round_idx, success_rate in enumerate(fake_success_rates, start=1):
        band = scheduler.update(
            success_rate=success_rate,
            episodes_seen=config.min_episodes_per_band,
        )
        print(
            f"Round {round_idx}: success_rate={success_rate:.2f}, "
            f"active_band={band.name}, difficulty={band.difficulty:.2f}"
        )

    if scheduler.history:
        print("\nCurriculum events:")
        for event in scheduler.history:
            print(
                f"- {event.reason}: {event.from_band} -> {event.to_band} "
                f"(success_rate={event.success_rate:.2f})"
            )


if __name__ == "__main__":
    main()

