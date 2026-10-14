from abc import ABC, abstractmethod

from vyshkat.domain.vehicles import Vehicle


class BeginnerRule(ABC):
    @abstractmethod
    def is_suitable(self, vehicle: Vehicle) -> bool: ...


class MinScoreRule(BeginnerRule):
    def __init__(self, threshold: int = 6):
        self._threshold = threshold

    def is_suitable(self, vehicle: Vehicle) -> bool:
        return vehicle.beginner_score >= self._threshold