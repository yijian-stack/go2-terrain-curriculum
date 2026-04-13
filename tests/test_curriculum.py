from go2_terrain_curriculum.config import TerrainBand
from go2_terrain_curriculum.curriculum import TerrainCurriculumScheduler


def test_curriculum_promotes_and_demotes() -> None:
    bands = [
        TerrainBand(name="flat", difficulty=0.1, command_scale=0.5),
        TerrainBand(name="rough", difficulty=0.5, command_scale=0.8),
    ]
    scheduler = TerrainCurriculumScheduler(
        bands=bands,
        promotion_threshold=0.8,
        demotion_threshold=0.3,
        min_episodes_per_band=5,
    )
    scheduler.update(success_rate=0.9, episodes_seen=5)
    assert scheduler.current_band.name == "rough"
    scheduler.update(success_rate=0.2, episodes_seen=5)
    assert scheduler.current_band.name == "flat"
    assert len(scheduler.history) == 2

