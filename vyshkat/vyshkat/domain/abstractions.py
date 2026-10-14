from abc import ABC, abstractmethod


class Inventoriable(ABC):
    @property
    @abstractmethod
    def inventory_number(self) -> str: ...

    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def kind(self) -> str: ...


class EnergyConsumer(ABC):
    @property
    @abstractmethod
    def daily_energy_kwh(self) -> float: ...
