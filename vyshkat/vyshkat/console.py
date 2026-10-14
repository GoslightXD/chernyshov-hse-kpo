from vyshkat.domain.things import Helmet, DockStation, ChargingCabinet
from vyshkat.domain.vehicles import Scooter, Bicycle, ElectricBicycle, Vehicle
from vyshkat.services.fleet import FleetService
from vyshkat.services.numbering import InventoryNumberGenerator
from vyshkat.services.reports import ReportService


class ConsoleApp:
    def __init__(self, fleet_service: FleetService, reports: ReportService,
                 numbers: InventoryNumberGenerator):
        self._fleet_service = fleet_service
        self._reports = reports
        self._numbers = numbers

    def run(self) -> None:
        self._section("1. Отчёты по пустому парку")
        self._print_reports()

        self._section("2. Приёмка транспорта (с техосмотром)")
        self._accept(Scooter(self._numbers.next(), "Xiaomi M365", 8, 0.6))
        self._accept(Bicycle(self._numbers.next(), "Stels Navigator", 9))
        self._accept(ElectricBicycle(self._numbers.next(), "Eltreco XT", 5, 0.9))
        self._accept(Scooter(self._numbers.next(), "Ninebot Max", 4, 0.8, condition=40))

        self._section("3. Постановка вещей на баланс")
        for thing in (
                Helmet(self._numbers.next(), "M"),
                DockStation(self._numbers.next(), "Корпус на Покровке", 1.5),
                ChargingCabinet(self._numbers.next(), "Склад А", 3.2),
        ):
            self._fleet_service.add_thing(thing)
            print(f"На балансе: {thing.inventory_number} {thing.name}")

        self._section("4. Отчёты по заполненному парку")
        self._print_reports()

    def _accept(self, vehicle: Vehicle) -> None:
        result = self._fleet_service.accept_vehicle(vehicle)
        if result.passed:
            print(f"Принят: {vehicle.inventory_number} {vehicle.name}")
        else:
            print(f"Отклонён: {vehicle.inventory_number} {vehicle.name} ({result.reason})")

    def _print_reports(self) -> None:
        print("Количество по типам:", self._reports.counts_by_kind() or "парк пуст")
        print(f"Суммарное потребление: {self._reports.total_energy_kwh():.2f} кВт·ч/сутки")
        beginners = self._reports.beginner_vehicles()
        print("Для новичков:", [v.name for v in beginners] or "нет подходящих")
        print("Инвентарные номера:")
        for number, name in self._reports.inventory_list():
            print(f"  {number}  {name}")

    @staticmethod
    def _section(title: str) -> None:
        print(f"\n=== {title} ===")
