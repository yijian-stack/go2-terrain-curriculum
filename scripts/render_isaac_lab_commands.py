"""Render Isaac Lab commands for Go2 locomotion experiments."""

from __future__ import annotations

import argparse
from pathlib import Path

from go2_terrain_curriculum import load_isaac_lab_config, render_bundle


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("results/isaac_lab_commands.txt"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = load_isaac_lab_config(args.config)
    content = render_bundle(config)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(content, encoding="utf-8")
    print(content)
    print(f"Saved command bundle to {args.output}")


if __name__ == "__main__":
    main()

