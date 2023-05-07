import pytest

from pythonProject3.src.circle import Circle


def test_circle_area():
    circle = Circle(5)
    assert circle.get_area() == 78.54

def test_circle_perimeter():
    circle = Circle(5)
    assert circle.get_perimeter() == 31.42

def test_circle_name():
    circle = Circle(5)
    assert circle.name == 'Circle'