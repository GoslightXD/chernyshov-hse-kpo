import punq

from vyshkat.console import ConsoleApp
from vyshkat.services.beginner_rules import BeginnerRule, MinScoreRule
from vyshkat.services.fleet import Fleet, FleetService
from vyshkat.services.inspection import ServiceCenter, BasicServiceCenter
from vyshkat.services.numbering import InventoryNumberGenerator
from vyshkat.services.reports import ReportService


def build_container(service_center: ServiceCenter | None = None) -> punq.Container:
    container = punq.Container()
    singleton = punq.Scope.singleton

    container.register(Fleet, scope=singleton)
    container.register(InventoryNumberGenerator, scope=singleton)
    container.register(ServiceCenter, instance=service_center or BasicServiceCenter(70))
    container.register(BeginnerRule, instance=MinScoreRule(6))
    container.register(FleetService, scope=singleton)
    container.register(ReportService)
    container.register(ConsoleApp)
    return container