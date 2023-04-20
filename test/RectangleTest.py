import sys
import unittest

# esto se hace para poder acceder a los módulos dentro de la carpeta src
sys.path.append('./')

from src.classes import Rectangle, Point


# clase para los tests correspondientes a la clase Rectangle
class RectangleTest(unittest.TestCase):

    def test_create_rectangle_with_parameters(self):
        rectangle = Rectangle.builder(1, 2, 4, 4)

        correct_point_one = rectangle.point_one == Point(1, 2)
        correct_point_two = rectangle.point_two == Point(4, 4)

        are_correct = bool(rectangle.point_one and rectangle.point_two)
        self.assertTrue(are_correct)

    def test_create_rectangle_no_parameters(self):
        rectangle = Rectangle.builder()

        correct_point_one = rectangle.point_one == Point(0, 0)
        correct_point_two = rectangle.point_two == Point(0, 0)

        are_correct = bool(rectangle.point_one and rectangle.point_two)
        self.assertTrue(are_correct)

    def test_base(self):
        rectangle = Rectangle(Point(1, 1), Point(4, 3))
        correct_base = 4 - 1
        self.assertEqual(rectangle.base(), correct_base, "Debe ser 3")

    def test_height(self):
        rectangle = Rectangle(Point(1, 7), Point(4, 1))
        correct_height = 7 - 1
        self.assertEqual(rectangle.height(), correct_height, "Debe ser 6")

    def test_area(self):
        rectangle = Rectangle(Point(-1, 2), Point(3, 8))
        correct_area = (3 - (-1)) * (8 - 2)
        self.assertEqual(rectangle.area(), correct_area, "Debe ser 12")


if __name__ == '__main__':
    unittest.main()
