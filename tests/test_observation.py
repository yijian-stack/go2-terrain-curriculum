from go2_terrain_curriculum.observation import rank_profiles


def test_pointcloud_bev_is_best_tradeoff() -> None:
    profiles = rank_profiles()
    assert profiles[0].name == "pointcloud_bev"
    assert profiles[0].benchmark_score > profiles[-1].benchmark_score
