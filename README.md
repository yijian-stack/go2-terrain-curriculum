# Go2 Terrain Curriculum

A benchmark-oriented quadruped locomotion project built around one question:

**How do we train a command-conditioned Go2 policy that stays stable as terrain difficulty increases?**

This repo is designed to look good to interviewers for a simple reason: it does not stop at "train PPO on flat ground." It packages the parts that usually separate a toy locomotion experiment from an engineering-grade benchmark:

- terrain curriculum scheduling
- explicit reward decomposition
- reproducible experiment configs
- benchmark-style episode metrics
- clear hooks for Isaac Lab or MuJoCo Playground integration

## Why this project

Quadruped locomotion is one of the most credible RL directions for robotics hiring because it touches control, reward design, robustness, evaluation, and sim-to-real thinking. This repo focuses on the benchmark layer rather than pretending the simulator itself is the contribution.

## What is inside

- `configs/`: flat, rough, and stairs curriculum presets
- `src/go2_terrain_curriculum/config.py`: experiment dataclasses and YAML loader
- `src/go2_terrain_curriculum/curriculum.py`: terrain difficulty scheduler
- `src/go2_terrain_curriculum/reward.py`: reusable locomotion reward decomposition
- `src/go2_terrain_curriculum/metrics.py`: success, speed, and stability summaries
- `scripts/simulate_curriculum.py`: local dry-run without a heavy simulator
- `tests/`: fast tests for configs, rewards, and promotion logic

## Positioning

Use this repo as the control and benchmarking layer on top of:

- Isaac Lab locomotion environments
- MuJoCo Playground quadruped tasks
- a private simulator stack if you already have one

## Quickstart

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .[dev]
pytest
python scripts/simulate_curriculum.py --config configs/go2_rough.yaml
```

## What makes this interview-friendly

1. The repo frames locomotion as a measurable benchmark problem instead of a vague "RL demo."
2. Reward terms are explicit and testable instead of buried in a monolithic training script.
3. Curriculum promotion and demotion logic are documented and unit tested.
4. The code is easy to extend toward real experiments on Go2.

## Next milestones

1. Connect the config layer to Isaac Lab Go2 locomotion tasks.
2. Add PPO/SAC experiment runners and seed sweeps.
3. Add result tables for `flat -> rough -> stairs`.
4. Track energy, slip, and command-tracking tradeoffs.

## License

MIT

