import math
from pythonProject3.src.figure import Figure
import pytest

class Circle(Figure):
    def __init__(self, radius: int):
        self.name = 'Circle'
        self.radius = radius

    def get_area(self) -> float:
        return round(math.pi * self.radius ** 2, 2)

    def get_perimeter(self) -> float:
        return round(2 * math.pi * self.radius, 2)