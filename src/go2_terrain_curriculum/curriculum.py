"""Terrain curriculum scheduling."""

from __future__ import annotations

from dataclasses import dataclass, field

from .config import TerrainBand


@dataclass
class CurriculumEvent:
    from_band: str
    to_band: str
    reason: str
    success_rate: float


@dataclass
class TerrainCurriculumScheduler:
    bands: list[TerrainBand]
    promotion_threshold: float
    demotion_threshold: float
    min_episodes_per_band: int
    current_index: int = 0
    history: list[CurriculumEvent] = field(default_factory=list)

    @property
    def current_band(self) -> TerrainBand:
        return self.bands[self.current_index]

    def update(self, success_rate: float, episodes_seen: int) -> TerrainBand:
        if episodes_seen < self.min_episodes_per_band:
            return self.current_band

        if success_rate >= self.promotion_threshold and self.current_index < len(self.bands) - 1:
            previous = self.current_band
            self.current_index += 1
            self.history.append(
                CurriculumEvent(
                    from_band=previous.name,
                    to_band=self.current_band.name,
                    reason="promotion",
                    success_rate=success_rate,
                )
            )
        elif success_rate <= self.demotion_threshold and self.current_index > 0:
            previous = self.current_band
            self.current_index -= 1
            self.history.append(
                CurriculumEvent(
                    from_band=previous.name,
                    to_band=self.current_band.name,
                    reason="demotion",
                    success_rate=success_rate,
                )
            )
        return self.current_band

