import pytest
from bucketsort import bucketsort

@pytest.fixture()
def sorted_arr():
    return [0, 1, 2, 3, 4, 5]

@pytest.fixture()
def unsorted_arr():
    return [5, 2, 4, 1, 0, 3]

@pytest.fixture(params=[10, 100, 1000])
def random_arr(request):
    import random
    return [random.randint(0, request.param) for _ in range(request.param)]

def test_bucketsort_sorted(sorted_arr):
    assert bucketsort(sorted_arr, len(sorted_arr)) == sorted_arr

def test_bucketsort_unsorted(unsorted_arr):
    assert bucketsort(unsorted_arr, len(unsorted_arr)) == sorted(unsorted_arr)

def test_bucketsort_random(random_arr):
    assert bucketsort(random_arr, max(random_arr)+1) == sorted(random_arr)