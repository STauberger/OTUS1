import unittest

from src.square import square


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = square('MySquare', 5)

    def test_calculate_area(self):
        self.assertEqual(self.square.calculate_area(), 25)

    def test_calculate_perimeter(self):
        self.assertEqual(self.square.calculate_perimeter(), 20)

if __name__ == '__main__':
    unittest.main()