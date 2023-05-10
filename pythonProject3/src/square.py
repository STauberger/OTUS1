from pythonProject3.src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <=0:
            raise ValueError(f'Expected side_a and side_b > 0, got{side_a}')
        super().__init__(side_a, side_a)
        self.name = 'Square'