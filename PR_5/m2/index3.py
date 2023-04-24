import pytest
from distance import distance


@pytest.mark.parametrize("x1, y1, x2, y2, expected", [
    (0, 0, 3, 4, 5),
    (1, 1, 1, 1, 0),
    (-1, -1, 2, 2, 5),
])
def test_distance(x1, y1, x2, y2, expected):
    assert distance(x1, y1, x2, y2) == expected


def test_distance_raises_exception():
    with pytest.raises(TypeError):
        distance("a", 1, 2, 3)