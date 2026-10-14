import pytest

from vyshkat.domain.abstractions import EnergyConsumer
from vyshkat.domain.vehicles import Scooter, Bicycle


def test_bicycle_is_not_energy_consumer():
    assert not isinstance(Bicycle("VK-1", "Stels", 9), EnergyConsumer)


def test_scooter_is_energy_consumer():
    assert isinstance(Scooter("VK-1", "M365", 8, 0.5), EnergyConsumer)


@pytest.mark.parametrize("score", [0, 11])
def test_invalid_beginner_score_rejected(score):
    with pytest.raises(ValueError):
        Bicycle("VK-1", "Stels", score)


def test_negative_energy_rejected():
    with pytest.raises(ValueError):
        Scooter("VK-1", "M365", 8, -1)