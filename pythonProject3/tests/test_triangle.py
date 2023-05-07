import unittest
from pythonProject3.src.triangle import Triangle


class TriangleTest(unittest.TestCase):
    def test_triangle_creation_positive(self):
        test_cases = [
            (10, 10, 10, 30, 43.3),
            (2, 2, 3, 7, 1.98),
            (5, 6, 8, 19, 14.98),
        ]
        for side_a, side_b, side_c, expected_perimeter, expected_area in test_cases:
            with self.subTest(side_a=side_a, side_b=side_b, side_c=side_c):
                triangle = Triangle(side_a, side_b, side_c)
                self.assertEqual(triangle.name, 'Triangle')
                self.assertEqual(triangle.get_perimeter(), expected_perimeter)
                self.assertAlmostEqual(triangle.get_area(), expected_area, places=2)

    def test_triangle_creation_negative(self):
        test_cases = [
            (0, 10, 10),
            (-2, 2, 3),
            (10, 10, 30),
        ]
        expected_error_msg = "Can not create a triangle with sides: ({}, {}, {})"
        for side_a, side_b, side_c in test_cases:
            with self.subTest(side_a=side_a, side_b=side_b, side_c=side_c):
                with self.assertRaises(ValueError) as context:
                    Triangle(side_a, side_b, side_c)
                expected_msg = expected_error_msg.format(side_a, side_b, side_c)
                self.assertEqual(str(context.exception), expected_msg)

    def test_two_triangle_areas_sum(self):
        expected_sum = 45.28
        triangle_1 = Triangle(10, 10, 10)
        triangle_2 = Triangle(2, 2, 3)
        self.assertEqual(triangle_1.add_area(triangle_2), expected_sum)

    def test_two_triangle_areas_sum_negative(self):
        triangle_1 = Triangle(10, 10, 10)
        with self.assertRaises(ValueError) as context:
            triangle_1.add_area('something')
        expected_msg = "Can only add areas of Triangles"
        self.assertEqual(str(context.exception), expected_msg)
