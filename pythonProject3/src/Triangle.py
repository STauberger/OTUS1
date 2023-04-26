from Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c
        self.calculate_area()
        self.calculate_perimeter()

    def calculate_area(self):
        # Heron's formula for the area of a triangle given its three sides
        p = (self.a + self.b + self.c) / 2
        self.area = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def calculate_perimeter(self):
        self.perimeter = self.a + self.b + self.c