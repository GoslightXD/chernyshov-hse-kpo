from vyshkat.domain.abstractions import Inventoriable
from vyshkat.domain.things import Thing
from vyshkat.domain.vehicles import Vehicle
from vyshkat.services.inspection import ServiceCenter, InspectionResult


class Fleet:
    def __init__(self):
        self._vehicles: list[Vehicle] = []
        self._things: list[Thing] = []

    @property
    def vehicles(self) -> tuple[Vehicle, ...]:
        return tuple(self._vehicles)

    @property
    def things(self) -> tuple[Thing, ...]:
        return tuple(self._things)

    @property
    def items(self) -> list[Inventoriable]:
        return [*self._vehicles, *self._things]

    def add_vehicle(self, vehicle: Vehicle) -> None:
        self._check_unique(vehicle)
        self._vehicles.append(vehicle)

    def add_thing(self, thing: Thing) -> None:
        self._check_unique(thing)
        self._things.append(thing)

    def _check_unique(self, item: Inventoriable) -> None:
        if any(i.inventory_number == item.inventory_number for i in self.items):
            raise ValueError(f"Инвентарный номер {item.inventory_number} уже занят")


class FleetService:
    def __init__(self, fleet: Fleet, service_center: ServiceCenter):
        self._fleet = fleet
        self._service_center = service_center

    def accept_vehicle(self, vehicle: Vehicle) -> InspectionResult:
        result = self._service_center.inspect(vehicle)
        if result.passed:
            self._fleet.add_vehicle(vehicle)
        return result

    def add_thing(self, thing: Thing) -> None:
        self._fleet.add_thing(thing)