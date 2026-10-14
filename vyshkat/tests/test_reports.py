import pytest

from vyshkat.domain.things import Helmet, DockStation
from vyshkat.domain.vehicles import Scooter, Bicycle, ElectricBicycle
from vyshkat.services.beginner_rules import MinScoreRule
from vyshkat.services.fleet import Fleet
from vyshkat.services.reports import ReportService


@pytest.fixture
def fleet():
    f = Fleet()
    f.add_vehicle(Scooter("VK-1", "M365", 8, 0.5))
    f.add_vehicle(Bicycle("VK-2", "Stels", 9))
    f.add_vehicle(ElectricBicycle("VK-3", "Eltreco", 5, 0.3))
    f.add_thing(Helmet("VK-4", "M"))
    f.add_thing(DockStation("VK-5", "Корпус", 1.2))
    return f


@pytest.fixture
def reports(fleet):
    return ReportService(fleet, MinScoreRule(6))


def test_total_energy_sums_only_consumers(reports):
    assert reports.total_energy_kwh() == pytest.approx(2.0)


def test_counts_by_kind(reports):
    counts = reports.counts_by_kind()
    assert counts["Самокат"] == 1
    assert counts["Шлем"] == 1


def test_beginner_vehicles_follow_rule(reports):
    names = [v.inventory_number for v in reports.beginner_vehicles()]
    assert names == ["VK-1", "VK-2"]


def test_inventory_list_contains_vehicles_and_things(reports):
    numbers = [number for number, _ in reports.inventory_list()]
    assert numbers == ["VK-1", "VK-2", "VK-3", "VK-4", "VK-5"]


def test_empty_fleet_reports():
    empty = ReportService(Fleet(), MinScoreRule(6))
    assert empty.total_energy_kwh() == 0
    assert empty.counts_by_kind() == {}