import math
import pytest
from Circle import Circle


def test_Circle_init():
    c = Circle(5)
    assert c.name == "Circle"
    assert c.radius == 5
    assert math.isclose(c.area, 78.53981633974483)
    assert math.isclose(c.perimeter, 31.41592653589793)


def test_Circle_calculate_area():
    c = Circle(8)
    assert math.isclose(c.area, 201.06192982974676)


def test_Circle_calculate_perimeter():
    c = Circle(8)
    assert math.isclose(c.perimeter, 50.26548245743669)