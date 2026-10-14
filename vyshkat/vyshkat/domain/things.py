from abc import ABC

from vyshkat.domain.abstractions import Inventoriable, EnergyConsumer


class Thing(Inventoriable, ABC):
    def __init__(self, inventory_number: str, title: str):
        self._inventory_number = inventory_number
        self._title = title

    @property
    def inventory_number(self) -> str:
        return self._inventory_number

    @property
    def name(self) -> str:
        return f"{self.kind} {self._title}"


class Helmet(Thing):
    @property
    def kind(self) -> str:
        return "Шлем"


class DockStation(Thing, EnergyConsumer):
    def __init__(self, inventory_number: str, title: str, daily_energy_kwh: float):
        super().__init__(inventory_number, title)
        self._daily_energy_kwh = daily_energy_kwh

    @property
    def kind(self) -> str:
        return "Док-станция"

    @property
    def daily_energy_kwh(self) -> float:
        return self._daily_energy_kwh


class ChargingCabinet(Thing, EnergyConsumer):
    def __init__(self, inventory_number: str, title: str, daily_energy_kwh: float):
        super().__init__(inventory_number, title)
        self._daily_energy_kwh = daily_energy_kwh

    @property
    def kind(self) -> str:
        return "Зарядный шкаф"

    @property
    def daily_energy_kwh(self) -> float:
        return self._daily_energy_kwh