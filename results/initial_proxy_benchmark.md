# Initial Proxy Benchmark

This report is a lightweight proxy benchmark generated from the curriculum and reward configs in this repo.
It is not a simulator leaderboard. Its job is to make config tradeoffs explicit and reproducible while the full Isaac Lab training loop is being wired in.

| Rank | Config | Success Rate | Mean Time | Velocity Error | Score |
| --- | --- | ---: | ---: | ---: | ---: |
| 1 | go2-rough-curriculum | 84.99% | 14.30 | 0.108 | 0.851 |
| 2 | go2-stairs-curriculum | 83.10% | 16.03 | 0.139 | 0.806 |
| 3 | go2-flat-baseline | 96.25% | 11.40 | 0.062 | 0.777 |

## Reading

- Best current proxy config: `go2-rough-curriculum`.
- The score rewards both nominal control quality and curriculum breadth, so a rough-terrain setup can beat a flat-only baseline when it stays reasonably stable.
- This proxy layer should be replaced by true simulator results as soon as Isaac Lab training is available on the target machine.
