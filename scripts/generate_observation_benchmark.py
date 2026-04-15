"""Generate observation-profile benchmark artifacts for Go2 locomotion."""

from __future__ import annotations

from pathlib import Path

from go2_terrain_curriculum.observation import rank_profiles, to_csv, to_markdown


def main() -> None:
    profiles = rank_profiles()
    results_dir = Path("results")
    results_dir.mkdir(parents=True, exist_ok=True)
    csv_path = results_dir / "observation_benchmark.csv"
    md_path = results_dir / "observation_benchmark.md"
    csv_path.write_text(to_csv(profiles), encoding="utf-8")
    md_path.write_text(to_markdown(profiles), encoding="utf-8")
    print(to_markdown(profiles))
    print(f"Saved {csv_path}")
    print(f"Saved {md_path}")


if __name__ == "__main__":
    main()
