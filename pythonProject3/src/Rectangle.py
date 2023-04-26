from Figure import Figure


class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
        self.calculate_area()
        self.calculate_perimeter()

    def calculate_area(self):
        self.area = self.width * self.height

    def calculate_perimeter(self):
        self.perimeter = 2 * (self.width + self.height)