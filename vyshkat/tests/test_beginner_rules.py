import pytest

from vyshkat.domain.vehicles import Bicycle
from vyshkat.services.beginner_rules import MinScoreRule


@pytest.mark.parametrize("score, expected", [(5, False), (6, True), (10, True)])
def test_min_score_rule_boundary(score, expected):
    rule = MinScoreRule(threshold=6)
    assert rule.is_suitable(Bicycle("VK-1", "Stels", score)) is expected