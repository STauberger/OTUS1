from Figure import Figure


class square(Figure):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def calculate_area(self):
        self.area = self.side ** 2
        return self.area

    def calculate_perimeter(self):
        self.perimeter = self.side * 4
        return self.perimeter
