from abc import ABC, abstractmethod
from dataclasses import dataclass

from vyshkat.domain.vehicles import Vehicle


@dataclass(frozen=True)
class InspectionResult:
    passed: bool
    reason: str = ""


class ServiceCenter(ABC):
    @abstractmethod
    def inspect(self, vehicle: Vehicle) -> InspectionResult: ...


class BasicServiceCenter(ServiceCenter):
    def __init__(self, min_condition: int = 70):
        self._min_condition = min_condition

    def inspect(self, vehicle: Vehicle) -> InspectionResult:
        if vehicle.condition < self._min_condition:
            return InspectionResult(
                False,
                f"состояние {vehicle.condition} ниже порога {self._min_condition}",
            )
        return InspectionResult(True)
