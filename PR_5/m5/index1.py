from hypothesis import given
import hypothesis.strategies as st
import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


@given(x1=st.floats(min_value=-1000, max_value=1000),
       y1=st.floats(min_value=-1000, max_value=1000),
       x2=st.floats(min_value=-1000, max_value=1000),
       y2=st.floats(min_value=-1000, max_value=1000))
def test_distance(x1, y1, x2, y2):
    assert distance(x1, y1, x2, y2) == distance(x2, y2, x1, y1)
    assert distance(x1, y1, x2, y2) >= 0