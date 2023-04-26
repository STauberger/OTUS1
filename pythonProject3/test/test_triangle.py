import pytest
from Triangle import Triangle


def test_Triangle_init():
    t = Triangle(3, 4, 5)
    assert t.name == "Triangle"
    assert t.a == 3
    assert t.b == 4
    assert t.c == 5
    assert t.area == 6
    assert t.perimeter == 12


def test_Triangle_init_with_invalid_sides():
    with pytest.raises(ValueError):
        t = Triangle(1, 2, 5)


def test_Triangle_calculate_area():
    t = Triangle(5, 12, 13)
    assert t.area == 30


def test_Triangle_calculate_perimeter():
    t = Triangle(5, 12, 13)
    assert t.perimeter == 30