from pythonProject3.src. square import Square
import pytest


@pytest.mark.parametrize('side_a, area, perimeter',
                         [
                             (10, 100, 40),
                             (2, 4, 8),

                            ])

def test_rectangle_positive(side_a, area, perimeter):
    r = Square(side_a)
    assert r.name == 'Square'
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter

@pytest.mark.parametrize('side_a', [-10, 0])
def test_rectangle_negative(side_a):
    with pytest.raises(ValueError):
        Square(side_a)



