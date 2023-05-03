from src.circle import Circle
import pytest

@pytest.mark.parametrize('radius, area, perimeter',
                           [
                               (10, 314, 63),
                               (53, 8820, 333)
                           ])
def test_circle_positive(radius, area, perimeter):
    r = Circle(radius)
    assert r.name == 'Circle'
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter

@pytest.mark.parametrize ('radius', [ -8, 0])
def test_circle_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)