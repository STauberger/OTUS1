import pytest
from pythonProject3.src.triangle import Triangle


@pytest.mark.parametrize('side_a, side_b, side_c, expected_perimeter, expected_area',
                         [
                             (5, 6, 7, 18, 14.7),
                             (3, 4, 5, 12, 6),
                             (8, 10, 12, 30, 39.69),
                         ]
                         )
def test_triangle_creation_positive(side_a, side_b, side_c, expected_perimeter, expected_area):
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.name == 'Triangle', 'Expected name is Triangle'
    assert triangle.get_perimeter() == expected_perimeter, 'Expected correct perimeter'
    assert triangle.get_area() == expected_area, 'Expected correct area'


@pytest.mark.parametrize('side_a, side_b, side_c',
                         [
                             (0, 10, 10),
                             (-2, 2, 3),
                             (10, 10, 30),
                         ],
                         ids=[
                             'one side is zero',
                             'one side is negative',
                             'can not create rectangle with these sides'
                         ])
def test_triangle_creation_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


def test_two_triangle_areas_sum():
    expected_sum = 20.7
    triangle_1 = Triangle(5, 6, 7)
    triangle_2 = Triangle(3, 4, 5)
    assert triangle_1.add_area(triangle_2) == expected_sum, f'Expected sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [10, 10.1, 'something'], ids=['integer', 'float', 'str'])
def test_two_triangle_areas_sum_negative(some_other_class):
    triangle_1 = Triangle(5, 6, 7)
    with pytest.raises(ValueError):
        triangle_1.add_area(some_other_class)