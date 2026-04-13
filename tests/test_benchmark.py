from pathlib import Path

from go2_terrain_curriculum.benchmark import evaluate_paths


def test_benchmark_returns_sorted_rows() -> None:
    rows = evaluate_paths(
        [
            Path("configs/go2_flat.yaml"),
            Path("configs/go2_rough.yaml"),
            Path("configs/go2_stairs.yaml"),
        ]
    )
    assert len(rows) == 3
    assert rows[0].benchmark_score >= rows[-1].benchmark_score

