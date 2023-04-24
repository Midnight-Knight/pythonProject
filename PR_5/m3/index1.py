import pytest
import triangle_type

def test_triangle_type():
    # равносторонний треугольник
    assert triangle_type(0, 0, 1, 0, 0.5, 0.866) == "равносторонний"
    # разносторонний треугольник
    assert triangle_type(0, 0, 1, 0, 0, 1) == "разносторонний"
    # равнобедренный треугольник
    assert triangle_type(0, 0, 1, 0, 0, 1) == "равнобедренный"