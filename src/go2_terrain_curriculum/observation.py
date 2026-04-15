"""Observation-profile benchmark helpers for locomotion experiments."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ObservationProfile:
    name: str
    modality: str
    observability: float
    terrain_precision: float
    latency_tolerance: float
    sim_to_real_readiness: float
    compute_cost: float
    benchmark_score: float


def default_profiles() -> list[ObservationProfile]:
    profiles = [
        ObservationProfile(
            name="proprio_only",
            modality="joint_state + imu",
            observability=0.58,
            terrain_precision=0.30,
            latency_tolerance=0.95,
            sim_to_real_readiness=0.64,
            compute_cost=0.10,
            benchmark_score=0.0,
        ),
        ObservationProfile(
            name="height_scan",
            modality="joint_state + local height scan",
            observability=0.76,
            terrain_precision=0.74,
            latency_tolerance=0.82,
            sim_to_real_readiness=0.78,
            compute_cost=0.34,
            benchmark_score=0.0,
        ),
        ObservationProfile(
            name="pointcloud_bev",
            modality="joint_state + pointcloud BEV raster",
            observability=0.88,
            terrain_precision=0.91,
            latency_tolerance=0.68,
            sim_to_real_readiness=0.86,
            compute_cost=0.46,
            benchmark_score=0.0,
        ),
        ObservationProfile(
            name="raw_pointcloud",
            modality="joint_state + raw pointcloud encoder",
            observability=0.93,
            terrain_precision=0.94,
            latency_tolerance=0.52,
            sim_to_real_readiness=0.81,
            compute_cost=0.74,
            benchmark_score=0.0,
        ),
    ]
    return [score_profile(profile) for profile in profiles]


def score_profile(profile: ObservationProfile) -> ObservationProfile:
    score = (
        0.26 * profile.observability
        + 0.29 * profile.terrain_precision
        + 0.18 * profile.latency_tolerance
        + 0.27 * profile.sim_to_real_readiness
        - 0.16 * profile.compute_cost
    )
    return ObservationProfile(
        name=profile.name,
        modality=profile.modality,
        observability=profile.observability,
        terrain_precision=profile.terrain_precision,
        latency_tolerance=profile.latency_tolerance,
        sim_to_real_readiness=profile.sim_to_real_readiness,
        compute_cost=profile.compute_cost,
        benchmark_score=score,
    )


def rank_profiles() -> list[ObservationProfile]:
    return sorted(default_profiles(), key=lambda profile: profile.benchmark_score, reverse=True)


def to_csv(profiles: list[ObservationProfile]) -> str:
    header = (
        "name,modality,observability,terrain_precision,latency_tolerance,"
        "sim_to_real_readiness,compute_cost,benchmark_score"
    )
    lines = [
        (
            f"{profile.name},{profile.modality},{profile.observability:.3f},{profile.terrain_precision:.3f},"
            f"{profile.latency_tolerance:.3f},{profile.sim_to_real_readiness:.3f},{profile.compute_cost:.3f},"
            f"{profile.benchmark_score:.4f}"
        )
        for profile in profiles
    ]
    return "\n".join([header, *lines]) + "\n"


def to_markdown(profiles: list[ObservationProfile]) -> str:
    best = profiles[0]
    lines = [
        "# Observation Profile Benchmark",
        "",
        "This benchmark compares locomotion observation stacks by balancing terrain information, latency tolerance, and sim-to-real readiness.",
        "It is a design benchmark rather than a simulator score table, and it exists to make observation choices explicit before a costly Isaac Lab sweep.",
        "",
        "| Rank | Profile | Modality | Observability | Terrain Precision | Latency Tolerance | Sim-to-Real | Cost | Score |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for idx, profile in enumerate(profiles, start=1):
        lines.append(
            f"| {idx} | {profile.name} | {profile.modality} | {profile.observability:.2%} | "
            f"{profile.terrain_precision:.2%} | {profile.latency_tolerance:.2%} | "
            f"{profile.sim_to_real_readiness:.2%} | {profile.compute_cost:.2f} | {profile.benchmark_score:.3f} |"
        )

    lines.extend(
        [
            "",
            "## Reading",
            "",
            f"- Best current tradeoff: `{best.name}`.",
            "- `pointcloud_bev` is the most balanced profile because it preserves terrain structure while avoiding the engineering cost of a raw point-cloud policy stack.",
            "- This profile is the natural place to plug in CUDA-accelerated pointcloud rasterization once the real training loop is online.",
        ]
    )
    return "\n".join(lines) + "\n"
