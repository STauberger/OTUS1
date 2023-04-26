import math

from Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
        self.calculate_area()
        self.calculate_perimeter()

    def calculate_area(self):
        self.area = math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        self.perimeter = 2 * math.pi * self.radius