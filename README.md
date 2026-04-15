# Go2 Terrain Curriculum

A benchmark-oriented quadruped locomotion project built around one question:

**How do we train a command-conditioned Go2 policy that stays stable as terrain difficulty increases?**

This repo is designed to look good to interviewers for a simple reason: it does not stop at "train PPO on flat ground." It packages the parts that usually separate a toy locomotion experiment from an engineering-grade benchmark:

- terrain curriculum scheduling
- explicit reward decomposition
- observation-profile tradeoff analysis
- reproducible experiment configs
- benchmark-style episode metrics
- clear hooks for Isaac Lab or MuJoCo Playground integration
- exported benchmark artifacts and result tables

## Why this project

Quadruped locomotion is one of the most credible RL directions for robotics hiring because it touches control, reward design, robustness, evaluation, and sim-to-real thinking. This repo focuses on the benchmark layer rather than pretending the simulator itself is the contribution.

## What is inside

- `configs/`: flat, rough, and stairs curriculum presets
- `configs/isaac_lab/`: real training configs for Isaac Lab Go2 environments
- `src/go2_terrain_curriculum/config.py`: experiment dataclasses and YAML loader
- `src/go2_terrain_curriculum/curriculum.py`: terrain difficulty scheduler
- `src/go2_terrain_curriculum/isaac_lab.py`: Isaac Lab training command renderer
- `src/go2_terrain_curriculum/observation.py`: observation stack benchmark helpers
- `src/go2_terrain_curriculum/reward.py`: reusable locomotion reward decomposition
- `src/go2_terrain_curriculum/metrics.py`: success, speed, and stability summaries
- `scripts/simulate_curriculum.py`: local dry-run without a heavy simulator
- `scripts/render_isaac_lab_commands.py`: print real training and evaluation commands
- `scripts/generate_proxy_benchmark.py`: export a first benchmark report
- `scripts/generate_observation_benchmark.py`: compare observation profiles for sim-to-real value
- `results/`: generated markdown and csv artifacts
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
python scripts/render_isaac_lab_commands.py --config configs/isaac_lab/go2_rough_rsl_rl.yaml
python scripts/generate_proxy_benchmark.py
python scripts/generate_observation_benchmark.py
```

## What makes this interview-friendly

1. The repo frames locomotion as a measurable benchmark problem instead of a vague "RL demo."
2. Reward terms are explicit and testable instead of buried in a monolithic training script.
3. Curriculum promotion and demotion logic are documented and unit tested.
4. Observation choices are benchmarked instead of being buried in hand-wavy notes.
5. The code is easy to extend toward real experiments on Go2.

## Next milestones

1. Connect the config layer to Isaac Lab Go2 locomotion tasks.
2. Add PPO/SAC experiment runners and seed sweeps.
3. Add result tables for `flat -> rough -> stairs`.
4. Track energy, slip, and command-tracking tradeoffs.

## Current artifacts

- `results/initial_proxy_benchmark.md`: first benchmark-style report generated locally
- `results/proxy_benchmark.csv`: config-level score comparison
- `results/isaac_lab_commands.txt`: ready-to-run Isaac Lab command snippets
- `results/observation_benchmark.md`: observation stack tradeoff report
- `results/observation_benchmark.csv`: sortable observation profile table

## License

MIT
