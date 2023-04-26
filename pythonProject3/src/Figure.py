class Figure:
    def __init__(self, name):
        self.name = name
        self.area = None
        self.perimeter = None

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("The argument is not a geometric shape")
        return self.area + figure.area