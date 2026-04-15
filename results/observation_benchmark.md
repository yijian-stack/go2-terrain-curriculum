# Observation Profile Benchmark

This benchmark compares locomotion observation stacks by balancing terrain information, latency tolerance, and sim-to-real readiness.
It is a design benchmark rather than a simulator score table, and it exists to make observation choices explicit before a costly Isaac Lab sweep.

| Rank | Profile | Modality | Observability | Terrain Precision | Latency Tolerance | Sim-to-Real | Cost | Score |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | pointcloud_bev | joint_state + pointcloud BEV raster | 88.00% | 91.00% | 68.00% | 86.00% | 0.46 | 0.774 |
| 2 | height_scan | joint_state + local height scan | 76.00% | 74.00% | 82.00% | 78.00% | 0.34 | 0.716 |
| 3 | raw_pointcloud | joint_state + raw pointcloud encoder | 93.00% | 94.00% | 52.00% | 81.00% | 0.74 | 0.708 |
| 4 | proprio_only | joint_state + imu | 58.00% | 30.00% | 95.00% | 64.00% | 0.10 | 0.566 |

## Reading

- Best current tradeoff: `pointcloud_bev`.
- `pointcloud_bev` is the most balanced profile because it preserves terrain structure while avoiding the engineering cost of a raw point-cloud policy stack.
- This profile is the natural place to plug in CUDA-accelerated pointcloud rasterization once the real training loop is online.
