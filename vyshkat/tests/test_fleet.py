from unittest.mock import Mock

import pytest

from vyshkat.domain.things import Helmet
from vyshkat.domain.vehicles import Bicycle
from vyshkat.container import build_container
from vyshkat.services.fleet import Fleet, FleetService
from vyshkat.services.inspection import ServiceCenter, InspectionResult


def make_service(passed: bool):
    center = Mock(spec=ServiceCenter)
    center.inspect.return_value = InspectionResult(passed, "" if passed else "брак")
    fleet = Fleet()
    return FleetService(fleet, center), fleet, center


def test_vehicle_added_when_inspection_passed():
    service, fleet, center = make_service(passed=True)
    vehicle = Bicycle("VK-1", "Stels", 9)

    result = service.accept_vehicle(vehicle)

    assert result.passed
    assert vehicle in fleet.vehicles
    center.inspect.assert_called_once_with(vehicle)


def test_vehicle_not_added_when_inspection_failed():
    service, fleet, _ = make_service(passed=False)

    result = service.accept_vehicle(Bicycle("VK-1", "Stels", 9))

    assert not result.passed
    assert result.reason == "брак"
    assert fleet.vehicles == ()


def test_duplicate_inventory_number_rejected():
    service, _, _ = make_service(passed=True)
    service.accept_vehicle(Bicycle("VK-1", "Stels", 9))

    with pytest.raises(ValueError):
        service.add_thing(Helmet("VK-1", "M"))


def test_container_uses_substituted_service_center():
    fake_center = Mock(spec=ServiceCenter)
    fake_center.inspect.return_value = InspectionResult(False, "fake")

    service = build_container(service_center=fake_center).resolve(FleetService)
    result = service.accept_vehicle(Bicycle("VK-1", "Stels", 9))

    assert result.reason == "fake"