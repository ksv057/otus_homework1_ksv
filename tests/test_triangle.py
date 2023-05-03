from src.triangle import Triangle
import pytest


@pytest.mark.parametrize('a_side, b_side, c_side, perimeter, area',
                         [
                             (10, 15, 20, 45, 73),
                             (13, 5, 10, 28, 22)
                         ])
def test_triangle_positive(a_side, b_side, c_side, perimeter, area):
    r = Triangle(a_side, b_side, c_side)
    assert r.name == 'Triangle'
    assert r.get_perimeter() == perimeter
    assert r.get_area() == area


@pytest.mark.parametrize ('a_side, b_side, c_side',
                          [
                              (-10, 20, 25),
                              (10, 0, 20)
                          ])
def test_triangle_negative(a_side, b_side, c_side):
    with pytest.raises(ValueError):
        Triangle(a_side, b_side, c_side)