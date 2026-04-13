"""Generate a first benchmark-style report from lightweight curriculum proxies."""

from __future__ import annotations

from pathlib import Path

from go2_terrain_curriculum.benchmark import evaluate_paths, to_csv, to_markdown


def main() -> None:
    config_paths = [
        Path("configs/go2_flat.yaml"),
        Path("configs/go2_rough.yaml"),
        Path("configs/go2_stairs.yaml"),
    ]
    rows = evaluate_paths(config_paths)
    results_dir = Path("results")
    results_dir.mkdir(parents=True, exist_ok=True)
    csv_path = results_dir / "proxy_benchmark.csv"
    md_path = results_dir / "initial_proxy_benchmark.md"
    csv_path.write_text(to_csv(rows), encoding="utf-8")
    md_path.write_text(to_markdown(rows), encoding="utf-8")
    print(to_markdown(rows))
    print(f"Saved {csv_path}")
    print(f"Saved {md_path}")


if __name__ == "__main__":
    main()

