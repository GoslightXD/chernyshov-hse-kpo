from abc import ABC

from vyshkat.domain.abstractions import Inventoriable, EnergyConsumer


class Vehicle(Inventoriable, ABC):
    def __init__(self, inventory_number: str, model: str,
                 beginner_score: int, condition: int = 100):
        if not 1 <= beginner_score <= 10:
            raise ValueError("Простота для новичка должна быть от 1 до 10")
        if not 0 <= condition <= 100:
            raise ValueError("Состояние должно быть от 0 до 100")
        self._inventory_number = inventory_number
        self.model = model
        self.beginner_score = beginner_score
        self.condition = condition

    @property
    def inventory_number(self) -> str:
        return self._inventory_number

    @property
    def name(self) -> str:
        return f"{self.kind} {self.model}"


class Bicycle(Vehicle):
    @property
    def kind(self) -> str:
        return "Велосипед"


class _ElectricMixin(EnergyConsumer):
    def _init_energy(self, daily_energy_kwh: float) -> None:
        if daily_energy_kwh < 0:
            raise ValueError("Расход энергии не может быть отрицательным")
        self._daily_energy_kwh = daily_energy_kwh

    @property
    def daily_energy_kwh(self) -> float:
        return self._daily_energy_kwh


class Scooter(Vehicle, _ElectricMixin):
    def __init__(self, inventory_number: str, model: str, beginner_score: int,
                 daily_energy_kwh: float, condition: int = 100):
        super().__init__(inventory_number, model, beginner_score, condition)
        self._init_energy(daily_energy_kwh)

    @property
    def kind(self) -> str:
        return "Самокат"


class ElectricBicycle(Vehicle, _ElectricMixin):
    def __init__(self, inventory_number: str, model: str, beginner_score: int,
                 daily_energy_kwh: float, condition: int = 100):
        super().__init__(inventory_number, model, beginner_score, condition)
        self._init_energy(daily_energy_kwh)

    @property
    def kind(self) -> str:
        return "Электровелосипед"
