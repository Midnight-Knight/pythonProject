import pytest

from binary_search import binary_search


@pytest.mark.parametrize(
    "arr, x, expected_index",
    [([1, 2, 3, 4, 5], 3, 2),
     ([1, 2, 3, 4, 5], 6, -1),
     ([], 1, -1),
     ([1], 1, 0),
     ([1], 2, -1),
     ([1, 3, 5, 7], 7, 3),
     ([1, 3, 5, 7], 1, 0),
     ([1, 3, 5, 7], 4, -1),
     ([1, 3, 5, 7], 0, -1),
     ([1, 3, 5, 7], 8, -1)]
)
def test_binary_search(arr, x, expected_index):
    assert binary_search(arr, x) == expected_index