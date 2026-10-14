import pytest

from vyshkat.domain.vehicles import Bicycle
from vyshkat.services.inspection import BasicServiceCenter


@pytest.mark.parametrize("condition, expected", [(69, False), (70, True), (100, True)])
def test_basic_service_center_threshold(condition, expected):
    center = BasicServiceCenter(min_condition=70)
    result = center.inspect(Bicycle("VK-1", "Stels", 9, condition=condition))
    assert result.passed is expected