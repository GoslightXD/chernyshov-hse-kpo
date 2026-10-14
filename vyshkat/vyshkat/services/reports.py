from collections import Counter

from vyshkat.domain.abstractions import EnergyConsumer
from vyshkat.domain.vehicles import Vehicle
from vyshkat.services.beginner_rules import BeginnerRule
from vyshkat.services.fleet import Fleet


class ReportService:
    def __init__(self, fleet: Fleet, beginner_rule: BeginnerRule):
        self._fleet = fleet
        self._beginner_rule = beginner_rule

    def total_energy_kwh(self) -> float:
        return sum(
            item.daily_energy_kwh
            for item in self._fleet.items
            if isinstance(item, EnergyConsumer)
        )

    def counts_by_kind(self) -> dict[str, int]:
        return dict(Counter(item.kind for item in self._fleet.items))

    def beginner_vehicles(self) -> list[Vehicle]:
        return [v for v in self._fleet.vehicles if self._beginner_rule.is_suitable(v)]

    def inventory_list(self) -> list[tuple[str, str]]:
        return [(item.inventory_number, item.name) for item in self._fleet.items]