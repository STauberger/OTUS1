import pytest
from Rectangle import Rectangle


def test_Rectangle_init():
    r = Rectangle(4, 5)
    assert r.name == "Rectangle"
    assert r.width == 4
    assert r.height == 5
    assert r.area == 20
    assert r.perimeter == 18


def test_Rectangle_calculate_area():
    r = Rectangle(6, 7)
    assert r.area == 42


def test_Rectangle_calculate_perimeter():
    r = Rectangle(6, 7)
    assert r.perimeter == 26